#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: identity_group
short_description: Resource module for Identity Group
description:
- Manage operations create, update, delete of the resource Identity Group.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Identity Group's description.
      type: str
    id:
      description: Identity Group's id.
      type: str
    name:
      description: Identity Group's name.
      type: str
    systemDefined:
      description: SystemDefined flag.
      type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.identity_group
# Reference by Internet resource
- name: Identity Group reference
  description: Complete reference of the Identity Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.identity_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: 'Identity Group for Profile: Cisco-Meraki-Device'
    id: 1e2700a0-8c00-11e6-996c-525400b48521
    name: Cisco-Meraki-Device
    systemDefined: true
- name: Update by id
  cisco.ise.identity_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: 'Identity Group for Profile: Cisco-Meraki-Device'
    id: 1e2700a0-8c00-11e6-996c-525400b48521
    name: Cisco-Meraki-Device
    systemDefined: true
- name: Delete by id
  cisco.ise.identity_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.identity_group:
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
  - {}
  - {}
  - {}
  - 
"""