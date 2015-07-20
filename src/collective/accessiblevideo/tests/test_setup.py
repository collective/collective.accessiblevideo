# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.accessiblevideo.testing import COLLECTIVE_ACCESSIBLEVIDEO_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.accessiblevideo is properly installed."""

    layer = COLLECTIVE_ACCESSIBLEVIDEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.accessiblevideo is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.accessiblevideo'))

    def test_uninstall(self):
        """Test if collective.accessiblevideo is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.accessiblevideo'])
        self.assertFalse(self.installer.isProductInstalled('collective.accessiblevideo'))

    def test_browserlayer(self):
        """Test that ICollectiveAccessiblevideoLayer is registered."""
        from collective.accessiblevideo.interfaces import ICollectiveAccessiblevideoLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveAccessiblevideoLayer, utils.registered_layers())
