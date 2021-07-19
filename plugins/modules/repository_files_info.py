#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: repository_files_info
short_description: Information module for Repository Files
description:
- Get all Repository Files.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter. Unique name for a repository.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Repository Files reference
  description: Complete reference of the Repository Files object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Repository Files
  cisco.ise.repository_files_info:
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
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
