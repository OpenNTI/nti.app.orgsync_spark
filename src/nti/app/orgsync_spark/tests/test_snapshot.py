#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

from hamcrest import none
from hamcrest import is_not
from hamcrest import assert_that

from datetime import datetime

import fudge

from nti.app.orgsync_spark.snapshot import create_orgsync_source_snapshot_job

from nti.app.orgsync_spark.tests import NoOpCM
from nti.app.orgsync_spark.tests import OrgSyncSparkApplicationTestLayer

from nti.app.testing.application_webtest import ApplicationLayerTest

from nti.app.testing.decorators import WithSharedApplicationMockDS


class TestSnapshot(ApplicationLayerTest):

    layer = OrgSyncSparkApplicationTestLayer

    @WithSharedApplicationMockDS(testapp=False, users=False)
    @fudge.patch('nti.app.orgsync_spark.snapshot.db_snapshot',
                 'nti.app.orgsync_spark.snapshot.get_redis_lock')
    def test_upload_source(self, mock_dbs, mock_sl):
        mock_dbs.is_callable().returns_fake()
        mock_sl.is_callable().returns(NoOpCM())
        job = create_orgsync_source_snapshot_job("user", datetime.now())
        assert_that(job, is_not(none()))
