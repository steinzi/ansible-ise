#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sxp_vpns_bulk_request
short_description: Resource module for Sxp Vpns Bulk Request
description:
- Manage operation update of the resource Sxp Vpns Bulk Request.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  operationType:
    description: Sxp Vpns Bulk Request's operationType.
    type: str
  resourceMediaType:
    description: Sxp Vpns Bulk Request's resourceMediaType.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Sxp Vpns Bulk Request reference
  description: Complete reference of the Sxp Vpns Bulk Request object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.ise.sxp_vpns_bulk_request:
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
