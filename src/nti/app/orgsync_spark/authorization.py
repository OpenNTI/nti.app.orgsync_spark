#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import component
from zope import interface

from nti.app.orgsync_spark.interfaces import RID_ORGSYNCSPARK

from nti.dataserver.interfaces import IUser
from nti.dataserver.interfaces import IGroupMember

logger = __import__('logging').getLogger(__name__)


@component.adapter(IUser)
@interface.implementer(IGroupMember)
class NextthoughtDotComOUSparkAdmin(object):

    def __init__(self, context):
        groups = ()
        if context.username.endswith('@nextthought.com'):
            groups = (RID_ORGSYNCSPARK,)
        self.groups = groups
