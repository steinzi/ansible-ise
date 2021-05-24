#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_dictionary_attribute
short_description: Resource module for Network Access Dictionary Attribute
description:
- Manage operations create, update, delete of the resource Network Access Dictionary Attribute.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    allowedValues:
      description: All of the allowed values for the dictionary attribute.
      suboptions:
      - suboptions:
          isDefault:
            description: True if this key value is the default between the allowed values
              of the dictionary attribute.
            type: bool
          key:
            description: Network Access Dictionary Attribute's key.
            type: str
          value:
            description: Network Access Dictionary Attribute's value.
            type: str
        type: dict
      type: list
    dataType:
      description: The data type for the dictionary attribute.
      type: str
    description:
      description: The description of the Dictionary attribute.
      type: str
    dictionaryName:
      description: The name of the dictionary which the dictionary attribute belongs to.
      type: str
    directionType:
      description: The direction for the useage of the dictionary attribute.
      type: str
    id:
      description: Identifier for the dictionary attribute.
      type: str
    internalName:
      description: The internal name of the dictionary attribute.
      type: str
    name:
      description: The dictionary attribute's name.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_dictionary_attribute
# Reference by Internet resource
- name: Network Access Dictionary Attribute reference
  description: Complete reference of the Network Access Dictionary Attribute object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string
- name: Update by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string
- name: Delete by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    dictionaryName: string
    name: string
- name: Ise request doc
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: complex
  sample:
  - {'id': 'string', 'directionType': 'string', 'name': 'string', 'description': 'string', 'internalName': 'string', 'dataType': 'string', 'dictionaryName': 'string', 'allowedValues': [{'key': 'string', 'value': 'string', 'isDefault': True}]}
  - {'id': 'string', 'directionType': 'string', 'name': 'string', 'description': 'string', 'internalName': 'string', 'dataType': 'string', 'dictionaryName': 'string', 'allowedValues': [{'key': 'string', 'value': 'string', 'isDefault': True}]}
  - {'id': 'string', 'directionType': 'string', 'name': 'string', 'description': 'string', 'internalName': 'string', 'dataType': 'string', 'dictionaryName': 'string', 'allowedValues': [{'key': 'string', 'value': 'string', 'isDefault': True}]}
  - 
"""