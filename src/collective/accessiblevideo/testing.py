# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.accessiblevideo


class CollectiveAccessiblevideoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.accessiblevideo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.accessiblevideo:default')


COLLECTIVE_ACCESSIBLEVIDEO_FIXTURE = CollectiveAccessiblevideoLayer()


COLLECTIVE_ACCESSIBLEVIDEO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ACCESSIBLEVIDEO_FIXTURE,),
    name='CollectiveAccessiblevideoLayer:IntegrationTesting'
)


COLLECTIVE_ACCESSIBLEVIDEO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ACCESSIBLEVIDEO_FIXTURE,),
    name='CollectiveAccessiblevideoLayer:FunctionalTesting'
)


COLLECTIVE_ACCESSIBLEVIDEO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ACCESSIBLEVIDEO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveAccessiblevideoLayer:AcceptanceTesting'
)
