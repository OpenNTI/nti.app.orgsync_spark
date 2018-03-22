#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

import fudge

from nti.app.orgsync_spark.tests import OrgSyncSparkApplicationTestLayer

from nti.app.testing.application_webtest import ApplicationLayerTest

from nti.app.testing.decorators import WithSharedApplicationMockDS


class TestSnapshotViews(ApplicationLayerTest):

    layer = OrgSyncSparkApplicationTestLayer

    @WithSharedApplicationMockDS(testapp=True, users=True)
    @fudge.patch('nti.app.orgsync_spark.views.snapshot_views.create_orgsync_source_snapshot_job')
    def test_snapshot(self, mock_job):
        mock_job.is_callable().with_args().returns('job')
        self.testapp.post_json('/dataserver2/orgsync/spark/@@snapshot',
                               {
                                   'timestamp': '2017-11-30'
                               },
                               status=200)
