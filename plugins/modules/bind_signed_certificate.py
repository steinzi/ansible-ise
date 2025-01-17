#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: bind_signed_certificate
short_description: Resource module for Bind Signed Certificate
description:
- Manage operation create of the resource Bind Signed Certificate.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  admin:
    description: Use certificate to authenticate the ISE Admin Portal.
    type: bool
  allowExtendedValidity:
    description: Allow import of certificates with validity greater than 398 days.
    type: bool
  allowOutOfDateCert:
    description: Allow out of date certificates (required).
    type: bool
  allowReplacementOfCertificates:
    description: Allow Replacement of certificates (required).
    type: bool
  allowReplacementOfPortalGroupTag:
    description: Allow Replacement of Portal Group Tag (required).
    type: bool
  data:
    description: Signed Certificate in escaped format.
    type: str
  eap:
    description: Use certificate for EAP protocols that use SSL/TLS tunneling.
    type: bool
  hostName:
    description: Name of Host whose CSR ID has been provided.
    type: str
  id:
    description: ID of the generated CSR.
    type: str
  ims:
    description: Use certificate for the ISE Messaging Service.
    type: bool
  name:
    description: Friendly Name of the certificate.
    type: str
  portal:
    description: Use for portal.
    type: bool
  portalGroupTag:
    description: Set Group tag.
    type: str
  pxgrid:
    description: Use certificate for the pxGrid Controller.
    type: bool
  radius:
    description: Use certificate for the RADSec server.
    type: bool
  saml:
    description: Use certificate for SAML Signing.
    type: bool
  validateCertificateExtensions:
    description: Validate Certificate Extensions.
    type: bool
requirements:
- ciscoisesdk
seealso:
# Reference by Internet resource
- name: Bind Signed Certificate reference
  description: Complete reference of the Bind Signed Certificate object model.
  link: https://ciscoisesdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.ise.bind_signed_certificate:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    admin: true
    allowExtendedValidity: true
    allowOutOfDateCert: true
    allowReplacementOfCertificates: true
    allowReplacementOfPortalGroupTag: true
    data: string
    eap: true
    hostName: string
    id: string
    ims: true
    name: string
    portal: true
    portalGroupTag: string
    pxgrid: true
    radius: true
    saml: true
    validateCertificateExtensions: true

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "string",
        "status": "string"
      },
      "version": "string"
    }
"""
