# -*- coding: utf-8 -*-

from plone import api


def upgrade_1001(context):
    """
    """
    portal_setup = api.portal.get().portal_setup
    portal_setup.runImportStepFromProfile(
        'profile-collective.accessiblevideo:default',
        'typeinfo',
        run_dependencies=False,
    )
