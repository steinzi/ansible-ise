#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pxgrid_service_unregister
short_description: Resource module for Pxgrid Service Unregister
description:
- Manage operation create of the resource Pxgrid Service Unregister.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options: {}
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Pxgrid Service Unregister reference
  description: Complete reference of the Pxgrid Service Unregister object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.pxgrid_service_unregister:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
