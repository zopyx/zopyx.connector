# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility
from zopyx.connector.content.mountpoint import IMountpoint  # NOQA E501
from zopyx.connector.testing import ZOPYX_CONNECTOR_INTEGRATION_TESTING  # noqa

import unittest


class MountpointIntegrationTest(unittest.TestCase):

    layer = ZOPYX_CONNECTOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_mountpoint_schema(self):
        fti = queryUtility(IDexterityFTI, name="Mountpoint")
        schema = fti.lookupSchema()
        self.assertEqual(IMountpoint, schema)

    def test_ct_mountpoint_fti(self):
        fti = queryUtility(IDexterityFTI, name="Mountpoint")
        self.assertTrue(fti)

    def test_ct_mountpoint_factory(self):
        fti = queryUtility(IDexterityFTI, name="Mountpoint")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMountpoint.providedBy(obj),
            "IMountpoint not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_mountpoint_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Mountpoint",
            id="mountpoint",
        )

        self.assertTrue(
            IMountpoint.providedBy(obj),
            "IMountpoint not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("mountpoint", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("mountpoint", parent.objectIds())

    def test_ct_mountpoint_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Mountpoint")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))
