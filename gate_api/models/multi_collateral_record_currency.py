# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class MultiCollateralRecordCurrency(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency': 'str',
        'index_price': 'str',
        'before_amount': 'str',
        'before_amount_usdt': 'str',
        'after_amount': 'str',
        'after_amount_usdt': 'str',
    }

    attribute_map = {
        'currency': 'currency',
        'index_price': 'index_price',
        'before_amount': 'before_amount',
        'before_amount_usdt': 'before_amount_usdt',
        'after_amount': 'after_amount',
        'after_amount_usdt': 'after_amount_usdt',
    }

    def __init__(
        self,
        currency=None,
        index_price=None,
        before_amount=None,
        before_amount_usdt=None,
        after_amount=None,
        after_amount_usdt=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, Configuration) -> None
        """MultiCollateralRecordCurrency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._index_price = None
        self._before_amount = None
        self._before_amount_usdt = None
        self._after_amount = None
        self._after_amount_usdt = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if index_price is not None:
            self.index_price = index_price
        if before_amount is not None:
            self.before_amount = before_amount
        if before_amount_usdt is not None:
            self.before_amount_usdt = before_amount_usdt
        if after_amount is not None:
            self.after_amount = after_amount
        if after_amount_usdt is not None:
            self.after_amount_usdt = after_amount_usdt

    @property
    def currency(self):
        """Gets the currency of this MultiCollateralRecordCurrency.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MultiCollateralRecordCurrency.

        Currency  # noqa: E501

        :param currency: The currency of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def index_price(self):
        """Gets the index_price of this MultiCollateralRecordCurrency.  # noqa: E501

        Currency Index Price  # noqa: E501

        :return: The index_price of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._index_price

    @index_price.setter
    def index_price(self, index_price):
        """Sets the index_price of this MultiCollateralRecordCurrency.

        Currency Index Price  # noqa: E501

        :param index_price: The index_price of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._index_price = index_price

    @property
    def before_amount(self):
        """Gets the before_amount of this MultiCollateralRecordCurrency.  # noqa: E501

        Amount before the operation  # noqa: E501

        :return: The before_amount of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._before_amount

    @before_amount.setter
    def before_amount(self, before_amount):
        """Sets the before_amount of this MultiCollateralRecordCurrency.

        Amount before the operation  # noqa: E501

        :param before_amount: The before_amount of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._before_amount = before_amount

    @property
    def before_amount_usdt(self):
        """Gets the before_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501

        USDT Amount before the operation.  # noqa: E501

        :return: The before_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._before_amount_usdt

    @before_amount_usdt.setter
    def before_amount_usdt(self, before_amount_usdt):
        """Sets the before_amount_usdt of this MultiCollateralRecordCurrency.

        USDT Amount before the operation.  # noqa: E501

        :param before_amount_usdt: The before_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._before_amount_usdt = before_amount_usdt

    @property
    def after_amount(self):
        """Gets the after_amount of this MultiCollateralRecordCurrency.  # noqa: E501

        Amount after the operation.  # noqa: E501

        :return: The after_amount of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._after_amount

    @after_amount.setter
    def after_amount(self, after_amount):
        """Sets the after_amount of this MultiCollateralRecordCurrency.

        Amount after the operation.  # noqa: E501

        :param after_amount: The after_amount of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._after_amount = after_amount

    @property
    def after_amount_usdt(self):
        """Gets the after_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501

        USDT Amount after the operation.  # noqa: E501

        :return: The after_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501
        :rtype: str
        """
        return self._after_amount_usdt

    @after_amount_usdt.setter
    def after_amount_usdt(self, after_amount_usdt):
        """Sets the after_amount_usdt of this MultiCollateralRecordCurrency.

        USDT Amount after the operation.  # noqa: E501

        :param after_amount_usdt: The after_amount_usdt of this MultiCollateralRecordCurrency.  # noqa: E501
        :type: str
        """

        self._after_amount_usdt = after_amount_usdt

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiCollateralRecordCurrency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiCollateralRecordCurrency):
            return True

        return self.to_dict() != other.to_dict()
