#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tacacs_command_sets_info
short_description: Information module for Tacacs Command Sets
description:
- Get all Tacacs Command Sets.
- Get Tacacs Command Sets by id.
- Get Tacacs Command Sets by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Tacacs Command Sets reference
  description: Complete reference of the Tacacs Command Sets object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Tacacs Command Sets
  cisco.ise.tacacs_command_sets_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Tacacs Command Sets by id
  cisco.ise.tacacs_command_sets_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Tacacs Command Sets by name
  cisco.ise.tacacs_command_sets_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "permitUnmatched": true,
      "commands": {
        "commandList": [
          {
            "grant": "string",
            "command": "string",
            "arguments": "string"
          }
        ]
      },
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }
"""
