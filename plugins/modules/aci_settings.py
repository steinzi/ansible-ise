#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: aci_settings
short_description: Resource module for Aci Settings
description:
- Manage operation update of the resource Aci Settings.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  aci50:
    description: Enable 5.0 ACI Version.
    type: bool
  aci51:
    description: Enable 5.1 ACI Version.
    type: bool
  aciipaddress:
    description: ACI Domain manager Ip Address.
    type: str
  acipassword:
    description: ACI Domain manager Password.
    type: str
  aciuserName:
    description: ACI Domain manager Username.
    type: str
  adminName:
    description: ACI Cluster Admin name.
    type: str
  adminPassword:
    description: ACI Cluster Admin password.
    type: str
  allSxpDomain:
    description: AllSxpDomain flag.
    type: bool
  defaultSgtName:
    description: Aci Settings's defaultSgtName.
    type: str
  enableAci:
    description: Enable ACI Integration.
    type: bool
  enableDataPlane:
    description: EnableDataPlane flag.
    type: bool
  enableElementsLimit:
    description: EnableElementsLimit flag.
    type: bool
  id:
    description: Resource UUID value.
    type: str
  ipAddressHostName:
    description: ACI Cluster IP Address / Host name.
    type: str
  l3RouteNetwork:
    description: Aci Settings's l3RouteNetwork.
    type: str
  maxNumIepgFromAci:
    description: Aci Settings's maxNumIepgFromAci.
    type: int
  maxNumSgtToAci:
    description: Aci Settings's maxNumSgtToAci.
    type: int
  specificSxpDomain:
    description: SpecificSxpDomain flag.
    type: bool
  specifixSxpDomainList:
    description: Aci Settings's specifixSxpDomainList.
    elements: str
    type: list
  suffixToEpg:
    description: Aci Settings's suffixToEpg.
    type: str
  suffixToSgt:
    description: Aci Settings's suffixToSgt.
    type: str
  tenantName:
    description: Aci Settings's tenantName.
    type: str
  untaggedPacketIepgName:
    description: Aci Settings's untaggedPacketIepgName.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Aci Settings reference
  description: Complete reference of the Aci Settings object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by id
  cisco.ise.aci_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aci50: true
    aci51: true
    aciipaddress: string
    acipassword: string
    aciuserName: string
    adminName: string
    adminPassword: string
    allSxpDomain: true
    defaultSgtName: string
    enableAci: true
    enableDataPlane: true
    enableElementsLimit: true
    id: string
    ipAddressHostName: string
    l3RouteNetwork: string
    maxNumIepgFromAci: 0
    maxNumSgtToAci: 0
    specificSxpDomain: true
    specifixSxpDomainList:
    - string
    suffixToEpg: string
    suffixToSgt: string
    tenantName: string
    untaggedPacketIepgName: string

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
