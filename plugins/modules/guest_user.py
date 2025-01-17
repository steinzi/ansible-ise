#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: guest_user
short_description: Resource module for Guest User
description:
- Manage operations create, update and delete of the resource Guest User.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  customFields:
    description: Key value map.
    type: dict
  description:
    description: Guest User's description.
    type: str
  guestAccessInfo:
    description: Guest User's guestAccessInfo.
    suboptions:
      fromDate:
        description: Guest User's fromDate.
        type: str
      groupTag:
        description: Guest User's groupTag.
        type: str
      location:
        description: Guest User's location.
        type: str
      ssid:
        description: Guest User's ssid.
        type: str
      toDate:
        description: Guest User's toDate.
        type: str
      validDays:
        description: Guest User's validDays.
        type: int
    type: dict
  guestInfo:
    description: Guest User's guestInfo.
    suboptions:
      company:
        description: Guest User's company.
        type: str
      creationTime:
        description: Guest User's creationTime.
        type: str
      emailAddress:
        description: Guest User's emailAddress.
        type: str
      enabled:
        description: This field is only for Get operation not applicable for Create,
          Update operations.
        type: bool
      firstName:
        description: Guest User's firstName.
        type: str
      lastName:
        description: Guest User's lastName.
        type: str
      notificationLanguage:
        description: Guest User's notificationLanguage.
        type: str
      password:
        description: Guest User's password.
        type: str
      phoneNumber:
        description: Phone number should be E.164 format.
        type: str
      smsServiceProvider:
        description: Guest User's smsServiceProvider.
        type: str
      userName:
        description: If account needs be created with mobile number, please provide
          mobile number here.
        type: str
    type: dict
  guestType:
    description: Guest User's guestType.
    type: str
  id:
    description: Guest User's id.
    type: str
  name:
    description: Guest User's name.
    type: str
  portalId:
    description: Guest User's portalId.
    type: str
  reasonForVisit:
    description: Guest User's reasonForVisit.
    type: str
  sponsorUserId:
    description: Guest User's sponsorUserId.
    type: str
  sponsorUserName:
    description: Guest User's sponsorUserName.
    type: str
  status:
    description: Guest User's status.
    type: str
  statusReason:
    description: Guest User's statusReason.
    type: str
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Guest User reference
  description: Complete reference of the Guest User object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update by name
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    id: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string

- name: Delete by name
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

- name: Update by id
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    id: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string

- name: Delete by id
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string

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
