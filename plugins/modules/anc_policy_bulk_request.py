#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: anc_policy_bulk_request
short_description: Resource module for Anc Policy Bulk Request
description:
- Manage operation update of the resource Anc Policy Bulk Request.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  operationType:
    description: Anc Policy Bulk Request's operationType.
    type: str
  resourceMediaType:
    description: Anc Policy Bulk Request's resourceMediaType.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Anc Policy Bulk Request reference
  description: Complete reference of the Anc Policy Bulk Request object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.anc_policy_bulk_request:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    operationType: string
    resourceMediaType: string

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
