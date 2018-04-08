#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import interface

from zope.cachedescriptors.property import Lazy

from zope.location.interfaces import IContained

from zope.traversing.interfaces import IPathAdapter

from nti.app.orgsync_spark import SPARK

from nti.app.orgsync_spark.interfaces import RID_ORGSYNCSPARK

from nti.dataserver.authorization import ROLE_ADMIN

from nti.dataserver.authorization_acl import ace_allowing
from nti.dataserver.authorization_acl import acl_from_aces

from nti.dataserver.interfaces import ALL_PERMISSIONS

logger = __import__('logging').getLogger(__name__)


@interface.implementer(IPathAdapter, IContained)
class SparkPathAdapter(object):

    __name__ = SPARK

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.__parent__ = context

    @Lazy
    def __acl__(self):
        aces = [
            ace_allowing(ROLE_ADMIN, ALL_PERMISSIONS, type(self)),
            ace_allowing(RID_ORGSYNCSPARK, ALL_PERMISSIONS, type(self)),
        ]
        acl = acl_from_aces(aces)
        return acl
