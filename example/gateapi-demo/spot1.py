import logging
import time
import sys
import csv
from decimal import Decimal as D

from gate_api import ApiClient, Configuration, Order, SpotApi

from config import RunConfig

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Глобальные переменные для хранения статистики
fb_sold_total = D('0')
usdt_received_total = D('0')
trade_count = 0

# Инициализируем файл для сохранения статистики
stats_file = 'trade_statistics.csv'
with open(stats_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Timestamp', 'FB Sold', 'USDT Received', 'Average Price'])

def check_and_place_order(run_config):
    global fb_sold_total, usdt_received_total, trade_count

    # Initialize API client
    config = Configuration(key=run_config.api_key, secret=run_config.api_secret, host=run_config.host_used)
    spot_api = SpotApi(ApiClient(config))
    
    currency_pair = "FB_USDT"
    currency = currency_pair.split("_")[0]

    try:
        # Проверяем баланс аккаунта
        accounts = spot_api.list_spot_accounts(currency=currency)
        if not accounts or len(accounts) != 1:
            logger.error("Не удалось получить информацию об аккаунте")
            return

        available = D(accounts[0].available)
        logger.info("Доступный баланс: %s %s", str(available), currency)

        # Минимальная сумма для создания ордера
        min_order_amount_usdt = D('3')  # в USDT

        # Получаем текущую цену FB/USDT
        ticker = spot_api.list_tickers(currency_pair=currency_pair)[0]
        current_price = D(ticker.last)

        # Если баланс больше минимальной суммы, создаем маркет ордер на продажу
        if available > 0 and available * current_price >= min_order_amount_usdt:
            order = Order(amount=str(available), price="0", side='sell', currency_pair=currency_pair, 
                         type='market', time_in_force='ioc')
            logger.info("Создаем маркет ордер: %s в %s на сумму %s", order.side, order.currency_pair, order.amount)
            
            created_order = spot_api.create_order(order)
            logger.info("Ордер создан с id %s, статус: %s", created_order.id, created_order.status)

            # Получаем результат исполнения ордера
            if created_order.status in ['closed', 'filled']:
                trades = spot_api.list_my_trades(currency_pair, order_id=created_order.id)
                if trades:
                    for trade in trades:
                        fb_sold_total += D(trade.amount)
                        usdt_received_total += D(trade.amount) * D(trade.price)
                        trade_count += 1
                        logger.info("Ордер %s исполнен: количество %s, цена %s", trade.order_id, trade.amount, trade.price)
            else:
                logger.info("Ордер %s еще открыт или не полностью исполнен", created_order.id)
        else:
            logger.info("Баланс недостаточен для создания ордера, минимальная сумма: %s USDT", min_order_amount_usdt)
    except Exception as e:
        logger.error("Произошла ошибка: %s", str(e))

    # Выводим статистику и сохраняем в файл
    if trade_count > 0:
        average_price = usdt_received_total / fb_sold_total
        logger.info("Всего продано FB: %s, всего получено USDT: %s, средняя цена: %s", fb_sold_total, usdt_received_total, average_price)
        with open(stats_file, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), fb_sold_total, usdt_received_total, average_price])
    else:
        logger.info("Пока нет завершенных сделок для подсчета статистики")

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Run Gate APIv4 spot1 script")
    parser.add_argument("-k", "--key", required=True, help="Gate APIv4 Key")
    parser.add_argument("-s", "--secret", required=True, help="Gate APIv4 Secret")
    parser.add_argument("-u", "--url", required=False, help="API base URL used to test")
    options = parser.parse_args()

    host_used = options.url if options.url else "https://api.gateio.ws/api/v4"
    if host_used:
        host_used = host_used.rstrip("/")
    if not host_used.endswith("/api/v4"):
        host_used += '/api/v4'

    run_config = RunConfig(options.key, options.secret, host_used)
    while True:
        check_and_place_order(run_config)
        # Обратный отсчет перед следующим запуском
        for remaining in range(600, 0, -10):
            sys.stdout.write(f"\rОжидание {remaining} секунд до следующего запуска...")
            sys.stdout.flush()
            time.sleep(10)
        sys.stdout.write("\r\n")