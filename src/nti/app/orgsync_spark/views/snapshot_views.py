#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from pyramid.view import view_config
from pyramid.view import view_defaults

from requests.structures import CaseInsensitiveDict

from nti.app.base.abstract_views import AbstractAuthenticatedView

from nti.app.externalization.view_mixins import ModeledContentUploadRequestUtilsMixin

from nti.app.orgsync_spark.snapshot import create_orgsync_source_snapshot_job

from nti.app.orgsync_spark.views import OrgSyncPathAdapter

from nti.app.spark.common import parse_timestamp

from nti.common.string import is_true

from nti.dataserver import authorization as nauth

from nti.externalization.interfaces import LocatedExternalDict

logger = __import__('logging').getLogger(__name__)


@view_config(name="snapshot")
@view_defaults(route_name='objects.generic.traversal',
               renderer='rest',
               request_method='POST',
               context=OrgSyncPathAdapter,
               permission=nauth.ACT_NTI_ADMIN)
class SnapshotOrgSyncView(AbstractAuthenticatedView,
                          ModeledContentUploadRequestUtilsMixin):
    """
    Schedule a orgsync snapshop job
    """

    def readInput(self, value=None):
        result = super(SnapshotOrgSyncView, self).readInput(value)
        return CaseInsensitiveDict(result)

    def __call__(self):
        result = LocatedExternalDict()
        result.__name__ = self.request.view_name
        result.__parent__ = self.request.context
        # read params
        data = self.readInput()
        # pylint: disable=no-member
        creator = self.remoteUser.username
        # parse dates
        end_date = parse_timestamp(data.get('endDate'))
        start_date = parse_timestamp(data.get('startDate'))
        timestamp = parse_timestamp(data.get('timestamp'))
        # parse bools
        archive = is_true(data.get('archive', True))
        logs = is_true(data.get('logs', False))
        # create job
        result = create_orgsync_source_snapshot_job(creator, timestamp, start_date,
                                                    end_date, logs, archive)
        return result
