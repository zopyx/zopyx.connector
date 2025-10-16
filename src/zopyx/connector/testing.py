# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import zopyx.connector


class ZopyxConnectorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=zopyx.connector)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "zopyx.connector:default")


ZOPYX_CONNECTOR_FIXTURE = ZopyxConnectorLayer()


ZOPYX_CONNECTOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZOPYX_CONNECTOR_FIXTURE,),
    name="ZopyxConnectorLayer:IntegrationTesting",
)


ZOPYX_CONNECTOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZOPYX_CONNECTOR_FIXTURE,),
    name="ZopyxConnectorLayer:FunctionalTesting",
)
