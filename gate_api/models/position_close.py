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


class PositionClose(object):
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
        'time': 'float',
        'contract': 'str',
        'side': 'str',
        'pnl': 'str',
        'pnl_pnl': 'str',
        'pnl_fund': 'str',
        'pnl_fee': 'str',
        'text': 'str',
        'max_size': 'str',
        'first_open_time': 'int',
        'long_price': 'str',
        'short_price': 'str',
    }

    attribute_map = {
        'time': 'time',
        'contract': 'contract',
        'side': 'side',
        'pnl': 'pnl',
        'pnl_pnl': 'pnl_pnl',
        'pnl_fund': 'pnl_fund',
        'pnl_fee': 'pnl_fee',
        'text': 'text',
        'max_size': 'max_size',
        'first_open_time': 'first_open_time',
        'long_price': 'long_price',
        'short_price': 'short_price',
    }

    def __init__(
        self,
        time=None,
        contract=None,
        side=None,
        pnl=None,
        pnl_pnl=None,
        pnl_fund=None,
        pnl_fee=None,
        text=None,
        max_size=None,
        first_open_time=None,
        long_price=None,
        short_price=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (float, str, str, str, str, str, str, str, str, int, str, str, Configuration) -> None
        """PositionClose - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._contract = None
        self._side = None
        self._pnl = None
        self._pnl_pnl = None
        self._pnl_fund = None
        self._pnl_fee = None
        self._text = None
        self._max_size = None
        self._first_open_time = None
        self._long_price = None
        self._short_price = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if contract is not None:
            self.contract = contract
        if side is not None:
            self.side = side
        if pnl is not None:
            self.pnl = pnl
        if pnl_pnl is not None:
            self.pnl_pnl = pnl_pnl
        if pnl_fund is not None:
            self.pnl_fund = pnl_fund
        if pnl_fee is not None:
            self.pnl_fee = pnl_fee
        if text is not None:
            self.text = text
        if max_size is not None:
            self.max_size = max_size
        if first_open_time is not None:
            self.first_open_time = first_open_time
        if long_price is not None:
            self.long_price = long_price
        if short_price is not None:
            self.short_price = short_price

    @property
    def time(self):
        """Gets the time of this PositionClose.  # noqa: E501

        Position close time  # noqa: E501

        :return: The time of this PositionClose.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this PositionClose.

        Position close time  # noqa: E501

        :param time: The time of this PositionClose.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def contract(self):
        """Gets the contract of this PositionClose.  # noqa: E501

        Futures contract  # noqa: E501

        :return: The contract of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this PositionClose.

        Futures contract  # noqa: E501

        :param contract: The contract of this PositionClose.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def side(self):
        """Gets the side of this PositionClose.  # noqa: E501

        Position side, long or short  # noqa: E501

        :return: The side of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this PositionClose.

        Position side, long or short  # noqa: E501

        :param side: The side of this PositionClose.  # noqa: E501
        :type: str
        """
        allowed_values = ["long", "short"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and side not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}".format(side, allowed_values)  # noqa: E501
            )

        self._side = side

    @property
    def pnl(self):
        """Gets the pnl of this PositionClose.  # noqa: E501

        PNL  # noqa: E501

        :return: The pnl of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._pnl

    @pnl.setter
    def pnl(self, pnl):
        """Sets the pnl of this PositionClose.

        PNL  # noqa: E501

        :param pnl: The pnl of this PositionClose.  # noqa: E501
        :type: str
        """

        self._pnl = pnl

    @property
    def pnl_pnl(self):
        """Gets the pnl_pnl of this PositionClose.  # noqa: E501

        PNL - Position P/L  # noqa: E501

        :return: The pnl_pnl of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._pnl_pnl

    @pnl_pnl.setter
    def pnl_pnl(self, pnl_pnl):
        """Sets the pnl_pnl of this PositionClose.

        PNL - Position P/L  # noqa: E501

        :param pnl_pnl: The pnl_pnl of this PositionClose.  # noqa: E501
        :type: str
        """

        self._pnl_pnl = pnl_pnl

    @property
    def pnl_fund(self):
        """Gets the pnl_fund of this PositionClose.  # noqa: E501

        PNL - Funding Fees  # noqa: E501

        :return: The pnl_fund of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._pnl_fund

    @pnl_fund.setter
    def pnl_fund(self, pnl_fund):
        """Sets the pnl_fund of this PositionClose.

        PNL - Funding Fees  # noqa: E501

        :param pnl_fund: The pnl_fund of this PositionClose.  # noqa: E501
        :type: str
        """

        self._pnl_fund = pnl_fund

    @property
    def pnl_fee(self):
        """Gets the pnl_fee of this PositionClose.  # noqa: E501

        PNL - Transaction Fees  # noqa: E501

        :return: The pnl_fee of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._pnl_fee

    @pnl_fee.setter
    def pnl_fee(self, pnl_fee):
        """Sets the pnl_fee of this PositionClose.

        PNL - Transaction Fees  # noqa: E501

        :param pnl_fee: The pnl_fee of this PositionClose.  # noqa: E501
        :type: str
        """

        self._pnl_fee = pnl_fee

    @property
    def text(self):
        """Gets the text of this PositionClose.  # noqa: E501

        Text of close order  # noqa: E501

        :return: The text of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PositionClose.

        Text of close order  # noqa: E501

        :param text: The text of this PositionClose.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def max_size(self):
        """Gets the max_size of this PositionClose.  # noqa: E501

        Max Trade Size  # noqa: E501

        :return: The max_size of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this PositionClose.

        Max Trade Size  # noqa: E501

        :param max_size: The max_size of this PositionClose.  # noqa: E501
        :type: str
        """

        self._max_size = max_size

    @property
    def first_open_time(self):
        """Gets the first_open_time of this PositionClose.  # noqa: E501

        First Open Time  # noqa: E501

        :return: The first_open_time of this PositionClose.  # noqa: E501
        :rtype: int
        """
        return self._first_open_time

    @first_open_time.setter
    def first_open_time(self, first_open_time):
        """Sets the first_open_time of this PositionClose.

        First Open Time  # noqa: E501

        :param first_open_time: The first_open_time of this PositionClose.  # noqa: E501
        :type: int
        """

        self._first_open_time = first_open_time

    @property
    def long_price(self):
        """Gets the long_price of this PositionClose.  # noqa: E501

        When 'side' is 'long,' it indicates the opening average price; when 'side' is 'short,' it indicates the closing average price.  # noqa: E501

        :return: The long_price of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._long_price

    @long_price.setter
    def long_price(self, long_price):
        """Sets the long_price of this PositionClose.

        When 'side' is 'long,' it indicates the opening average price; when 'side' is 'short,' it indicates the closing average price.  # noqa: E501

        :param long_price: The long_price of this PositionClose.  # noqa: E501
        :type: str
        """

        self._long_price = long_price

    @property
    def short_price(self):
        """Gets the short_price of this PositionClose.  # noqa: E501

        When 'side' is 'long,' it indicates the opening average price; when 'side' is 'short,' it indicates the closing average price  # noqa: E501

        :return: The short_price of this PositionClose.  # noqa: E501
        :rtype: str
        """
        return self._short_price

    @short_price.setter
    def short_price(self, short_price):
        """Sets the short_price of this PositionClose.

        When 'side' is 'long,' it indicates the opening average price; when 'side' is 'short,' it indicates the closing average price  # noqa: E501

        :param short_price: The short_price of this PositionClose.  # noqa: E501
        :type: str
        """

        self._short_price = short_price

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
        if not isinstance(other, PositionClose):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PositionClose):
            return True

        return self.to_dict() != other.to_dict()
