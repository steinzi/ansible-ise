#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_policy_set_info
short_description: Information module for Network Access Policy Set
description:
- Get all Network Access Policy Set.
- Get Network Access Policy Set by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Policy id.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_policy_set
# Reference by Internet resource
- name: Network Access Policy Set reference
  description: Complete reference of the Network Access Policy Set object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Policy Set
  cisco.ise.network_access_policy_set_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Network Access Policy Set by id
  cisco.ise.network_access_policy_set_info
    id: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}, 'serviceName': 'string', 'isProxy': True}
  - [{'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True}, 'serviceName': 'string', 'isProxy': True}]
"""