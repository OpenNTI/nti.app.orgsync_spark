#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=inherit-non-class,no-value-for-parameter

from zope.security.permission import Permission

from nti.dataserver.authorization import ROLE_PREFIX

from nti.dataserver.authorization import StringRole

#: The ID of a role for orgsync/spark
RID_ORGSYNCSPARK_PREFIX = ROLE_PREFIX + 'nti.dataserver.orgsyncspark'
RID_ORGSYNCSPARK = StringRole(RID_ORGSYNCSPARK_PREFIX)

#: Snapshot permission
ACT_SNAPSHOPT = Permission('nti.actions.orgsyncspark.snapshot')
