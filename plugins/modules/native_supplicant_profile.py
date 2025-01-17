#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: native_supplicant_profile
short_description: Resource module for Native Supplicant Profile
description:
- Manage operations update and delete of the resource Native Supplicant Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  description:
    description: Native Supplicant Profile's description.
    type: str
  id:
    description: Native Supplicant Profile's id.
    type: str
  name:
    description: Native Supplicant Profile's name.
    type: str
  wirelessProfiles:
    description: Native Supplicant Profile's wirelessProfiles.
    suboptions:
      actionType:
        description: Action type for WifiProfile. Allowed values - ADD, - UPDATE, -
          DELETE (required for updating existing WirelessProfile).
        type: str
      allowedProtocol:
        description: Native Supplicant Profile's allowedProtocol.
        type: str
      certificateTemplateId:
        description: Native Supplicant Profile's certificateTemplateId.
        type: str
      previousSsid:
        description: Previous ssid for WifiProfile (required for updating existing WirelessProfile).
        type: str
      ssid:
        description: Native Supplicant Profile's ssid.
        type: str
    type: list
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Native Supplicant Profile reference
  description: Complete reference of the Native Supplicant Profile object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.native_supplicant_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    wirelessProfiles:
    - actionType: string
      allowedProtocol: string
      certificateTemplateId: string
      previousSsid: string
      ssid: string

- name: Delete by id
  cisco.ise.native_supplicant_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

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
