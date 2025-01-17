#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_access_dictionary_info
short_description: Information module for Network Access Dictionary
description:
- Get all Network Access Dictionary.
- Get Network Access Dictionary by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter. The dictionary name.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Network Access Dictionary reference
  description: Complete reference of the Network Access Dictionary object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Network Access Dictionary
  cisco.ise.network_access_dictionary_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
  register: result

- name: Get Network Access Dictionary by name
  cisco.ise.network_access_dictionary_info:
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
      "response": {
        "description": "string",
        "dictionaryAttrType": "string",
        "id": "string",
        "link": {
          "href": "string",
          "rel": "string",
          "type": "string"
        },
        "name": "string",
        "version": "string"
      },
      "version": "string"
    }
"""
