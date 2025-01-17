#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: identity_group
short_description: Resource module for Identity Group
description:
- Manage operations create and update of the resource Identity Group.
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
  parent:
    description: Identity Group's parent.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Identity Group reference
  description: Complete reference of the Identity Group object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.identity_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    parent: string

- name: Create
  cisco.ise.identity_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    name: string
    parent: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "UpdatedFieldsList": {
        "updatedField": {
          "field": "string",
          "oldValue": "string",
          "newValue": "string"
        },
        "field": "string",
        "oldValue": "string",
        "newValue": "string"
      }
    }
"""
