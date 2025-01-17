#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AnsibleISEException(Exception):
    """Base class for all Ansible ISE package exceptions."""
    pass


class InconsistentParameters(AnsibleISEException):
    """Provided parameters are not consistent."""
    pass
