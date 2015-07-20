# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.accessiblevideo.testing import COLLECTIVE_ACCESSIBLEVIDEO_INTEGRATION_TESTING  # noqa
from collective.accessiblevideo.interfaces import IAccessibleVideo

import unittest2 as unittest


class AccessibleVideoIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_ACCESSIBLEVIDEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='AccessibleVideo')
        schema = fti.lookupSchema()
        self.assertEqual(IAccessibleVideo, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='AccessibleVideo')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='AccessibleVideo')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAccessibleVideo.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('AccessibleVideo', 'AccessibleVideo')
        self.assertTrue(
            IAccessibleVideo.providedBy(self.portal['AccessibleVideo'])
        )
