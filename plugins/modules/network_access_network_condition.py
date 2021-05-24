#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: network_access_network_condition
short_description: Resource module for Network Access Network Condition
description:
- Manage operations create, update, delete of the resource Network Access Network Condition.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    cliDnisList:
      description: Network Access Network Condition's cliDnisList.
      elements:
        type: str
      type: list
    conditionType:
      description: Network Access Network Condition's conditionType.
      type: str
    description:
      description: Network Access Network Condition's description.
      type: str
    deviceGroupList:
      description: Network Access Network Condition's deviceGroupList.
      elements:
        type: str
      type: list
    deviceList:
      description: Network Access Network Condition's deviceList.
      elements:
        type: str
      type: list
    id:
      description: Network Access Network Condition's id.
      type: str
    ipAddrList:
      description: Network Access Network Condition's ipAddrList.
      elements:
        type: str
      type: list
    macAddrList:
      description: Network Access Network Condition's macAddrList.
      elements:
        type: str
      type: list
    name:
      description: Network Access Network Condition's name.
      type: str
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.network_access_network_condition
# Reference by Internet resource
- name: Network Access Network Condition reference
  description: Complete reference of the Network Access Network Condition object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.network_access_network_condition:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    {}
- name: Update by id
  cisco.ise.network_access_network_condition:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    cliDnisList:
    - string
    conditionType: string
    description: string
    deviceGroupList:
    - string
    deviceList:
    - string
    id: string
    ipAddrList:
    - string
    macAddrList:
    - string
    name: string
- name: Delete by id
  cisco.ise.network_access_network_condition:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.network_access_network_condition:
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
  - {'name': 'string', 'id': 'string', 'description': 'string', 'conditionType': 'string', 'ipAddrList': ['string'], 'macAddrList': ['string'], 'cliDnisList': ['string'], 'deviceList': ['string'], 'deviceGroupList': ['string']}
  - {'name': 'string', 'id': 'string', 'description': 'string', 'conditionType': 'string', 'ipAddrList': ['string'], 'macAddrList': ['string'], 'cliDnisList': ['string'], 'deviceList': ['string'], 'deviceGroupList': ['string']}
  - {'id': 'string'}
  - 
"""