#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: sgt
short_description: Resource module for Sgt
description:
- Manage operations create, update, delete of the resource Sgt.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
    description:
      description: Sgt's description.
      type: str
    generationId:
      description: Sgt's generationId.
      type: str
    id:
      description: Id path parameter.
      type: string
    name:
      description: Sgt's name.
      type: str
    propogateToApic:
      description: PropogateToApic flag.
      type: bool
    value:
      description: Sgt's value.
      type: int
requirements:
- ciscoisesdk
seealso:
# Reference by module name
- module: cisco.ise.plugins.module_utils.definitions.sgt
# Reference by Internet resource
- name: Sgt reference
  description: Complete reference of the Sgt object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Printers
    generationId: '0'
    name: Printers
    propogateToApic: true
    value: 999
- name: Update by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: Printers
    generationId: '0'
    id: string
    name: Printers
    propogateToApic: true
    value: 999
- name: Delete by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
- name: Ise request doc
  cisco.ise.sgt:
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