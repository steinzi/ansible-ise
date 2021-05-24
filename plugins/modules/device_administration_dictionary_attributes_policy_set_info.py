#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: device_administration_dictionary_attributes_policy_set_info
short_description: Information module for Device Administration Dictionary Attributes Policy Set
description:
- Get all Device Administration Dictionary Attributes Policy Set.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.device_administration_dictionary_attributes_policy_set
# Reference by Internet resource
- name: Device Administration Dictionary Attributes Policy Set reference
  description: Complete reference of the Device Administration Dictionary Attributes Policy Set object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Administration Dictionary Attributes Policy Set
  cisco.ise.device_administration_dictionary_attributes_policy_set_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - [{'id': 'string', 'directionType': 'string', 'name': 'string', 'description': 'string', 'internalName': 'string', 'dataType': 'string', 'dictionaryName': 'string', 'allowedValues': [{'key': 'string', 'value': 'string', 'isDefault': True}]}]
"""