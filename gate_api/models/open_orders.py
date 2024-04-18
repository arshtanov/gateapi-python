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


class OpenOrders(object):
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
    openapi_types = {'currency_pair': 'str', 'total': 'int', 'orders': 'list[Order]'}

    attribute_map = {'currency_pair': 'currency_pair', 'total': 'total', 'orders': 'orders'}

    def __init__(self, currency_pair=None, total=None, orders=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, int, list[Order], Configuration) -> None
        """OpenOrders - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pair = None
        self._total = None
        self._orders = None
        self.discriminator = None

        if currency_pair is not None:
            self.currency_pair = currency_pair
        if total is not None:
            self.total = total
        if orders is not None:
            self.orders = orders

    @property
    def currency_pair(self):
        """Gets the currency_pair of this OpenOrders.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this OpenOrders.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this OpenOrders.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this OpenOrders.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def total(self):
        """Gets the total of this OpenOrders.  # noqa: E501

        The total number of pending orders for this trading pair on the current page  # noqa: E501

        :return: The total of this OpenOrders.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OpenOrders.

        The total number of pending orders for this trading pair on the current page  # noqa: E501

        :param total: The total of this OpenOrders.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def orders(self):
        """Gets the orders of this OpenOrders.  # noqa: E501


        :return: The orders of this OpenOrders.  # noqa: E501
        :rtype: list[Order]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this OpenOrders.


        :param orders: The orders of this OpenOrders.  # noqa: E501
        :type: list[Order]
        """

        self._orders = orders

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
        if not isinstance(other, OpenOrders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenOrders):
            return True

        return self.to_dict() != other.to_dict()
