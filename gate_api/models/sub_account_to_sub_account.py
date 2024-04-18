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


class SubAccountToSubAccount(object):
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
        'sub_account_type': 'str',
        'sub_account_from': 'str',
        'sub_account_from_type': 'str',
        'sub_account_to': 'str',
        'sub_account_to_type': 'str',
        'amount': 'str',
    }

    attribute_map = {
        'currency': 'currency',
        'sub_account_type': 'sub_account_type',
        'sub_account_from': 'sub_account_from',
        'sub_account_from_type': 'sub_account_from_type',
        'sub_account_to': 'sub_account_to',
        'sub_account_to_type': 'sub_account_to_type',
        'amount': 'amount',
    }

    def __init__(
        self,
        currency=None,
        sub_account_type=None,
        sub_account_from=None,
        sub_account_from_type=None,
        sub_account_to=None,
        sub_account_to_type=None,
        amount=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, Configuration) -> None
        """SubAccountToSubAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._sub_account_type = None
        self._sub_account_from = None
        self._sub_account_from_type = None
        self._sub_account_to = None
        self._sub_account_to_type = None
        self._amount = None
        self.discriminator = None

        self.currency = currency
        if sub_account_type is not None:
            self.sub_account_type = sub_account_type
        self.sub_account_from = sub_account_from
        self.sub_account_from_type = sub_account_from_type
        self.sub_account_to = sub_account_to
        self.sub_account_to_type = sub_account_to_type
        self.amount = amount

    @property
    def currency(self):
        """Gets the currency of this SubAccountToSubAccount.  # noqa: E501

        Transfer currency name  # noqa: E501

        :return: The currency of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SubAccountToSubAccount.

        Transfer currency name  # noqa: E501

        :param currency: The currency of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def sub_account_type(self):
        """Gets the sub_account_type of this SubAccountToSubAccount.  # noqa: E501

        Transfer from the account. (deprecate, use `sub_account_from_type` and `sub_account_to_type` instead)  # noqa: E501

        :return: The sub_account_type of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, sub_account_type):
        """Sets the sub_account_type of this SubAccountToSubAccount.

        Transfer from the account. (deprecate, use `sub_account_from_type` and `sub_account_to_type` instead)  # noqa: E501

        :param sub_account_type: The sub_account_type of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """

        self._sub_account_type = sub_account_type

    @property
    def sub_account_from(self):
        """Gets the sub_account_from of this SubAccountToSubAccount.  # noqa: E501

        Transfer from the user id of the sub-account  # noqa: E501

        :return: The sub_account_from of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_from

    @sub_account_from.setter
    def sub_account_from(self, sub_account_from):
        """Sets the sub_account_from of this SubAccountToSubAccount.

        Transfer from the user id of the sub-account  # noqa: E501

        :param sub_account_from: The sub_account_from of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account_from is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account_from`, must not be `None`")  # noqa: E501

        self._sub_account_from = sub_account_from

    @property
    def sub_account_from_type(self):
        """Gets the sub_account_from_type of this SubAccountToSubAccount.  # noqa: E501

        The sub-account's outgoing trading account, spot - spot account, futures - perpetual contract account, delivery - delivery contract account, cross_margin - cross-margin account.\"  # noqa: E501

        :return: The sub_account_from_type of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_from_type

    @sub_account_from_type.setter
    def sub_account_from_type(self, sub_account_from_type):
        """Sets the sub_account_from_type of this SubAccountToSubAccount.

        The sub-account's outgoing trading account, spot - spot account, futures - perpetual contract account, delivery - delivery contract account, cross_margin - cross-margin account.\"  # noqa: E501

        :param sub_account_from_type: The sub_account_from_type of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account_from_type is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account_from_type`, must not be `None`")  # noqa: E501

        self._sub_account_from_type = sub_account_from_type

    @property
    def sub_account_to(self):
        """Gets the sub_account_to of this SubAccountToSubAccount.  # noqa: E501

        Transfer to the user id of the sub-account  # noqa: E501

        :return: The sub_account_to of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_to

    @sub_account_to.setter
    def sub_account_to(self, sub_account_to):
        """Sets the sub_account_to of this SubAccountToSubAccount.

        Transfer to the user id of the sub-account  # noqa: E501

        :param sub_account_to: The sub_account_to of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account_to is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account_to`, must not be `None`")  # noqa: E501

        self._sub_account_to = sub_account_to

    @property
    def sub_account_to_type(self):
        """Gets the sub_account_to_type of this SubAccountToSubAccount.  # noqa: E501

        The sub-account's incoming trading account, spot - spot account, futures - perpetual contract account, delivery - delivery contract account, cross_margin - cross-margin account.  # noqa: E501

        :return: The sub_account_to_type of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_to_type

    @sub_account_to_type.setter
    def sub_account_to_type(self, sub_account_to_type):
        """Sets the sub_account_to_type of this SubAccountToSubAccount.

        The sub-account's incoming trading account, spot - spot account, futures - perpetual contract account, delivery - delivery contract account, cross_margin - cross-margin account.  # noqa: E501

        :param sub_account_to_type: The sub_account_to_type of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account_to_type is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account_to_type`, must not be `None`")  # noqa: E501

        self._sub_account_to_type = sub_account_to_type

    @property
    def amount(self):
        """Gets the amount of this SubAccountToSubAccount.  # noqa: E501

        Transfer amount  # noqa: E501

        :return: The amount of this SubAccountToSubAccount.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubAccountToSubAccount.

        Transfer amount  # noqa: E501

        :param amount: The amount of this SubAccountToSubAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if not isinstance(other, SubAccountToSubAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccountToSubAccount):
            return True

        return self.to_dict() != other.to_dict()
