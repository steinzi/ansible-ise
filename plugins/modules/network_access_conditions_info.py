#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_conditions_info
short_description: Information module for Network Access Conditions
description:
- Get all Network Access Conditions.
- Get Network Access Conditions by id.
- Get Network Access Conditions by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter. Condition id.
    type: str
  name:
    description:
    - Name path parameter. Condition name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_conditions
# Reference by Internet resource
- name: Network Access Conditions reference
  description: Complete reference of the Network Access Conditions object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Conditions
  cisco.ise.network_access_conditions_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
- name: Get Network Access Conditions by id
  cisco.ise.network_access_conditions_info
    id: string
  register: result
- name: Get Network Access Conditions by name
  cisco.ise.network_access_conditions_info
    name: string
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}
  - [{'conditionType': 'string', 'isNegate': True}]
"""