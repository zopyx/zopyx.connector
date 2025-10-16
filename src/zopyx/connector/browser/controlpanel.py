# -*- coding: utf-8 -*-

################################################################
# zopyx.connector
# (C) 2025,  Andreas Jung, www.zopyx.com, Tuebingen, Germany
################################################################

import json

from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from zopyx.connector import _
from zopyx.connector.interfaces import IConnectorSettings
from zope.component import getUtility


class DBSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IConnectorSettings
    label = _(u'ZOPYX Connector settings')
    description = _(u'')

    def updateFields(self):
        super(DBSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(DBSettingsEditForm, self).updateWidgets()


class DBSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = DBSettingsEditForm

    @property
    def settings(self):
        """ Returns setting as dict """
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IConnectorSettings)
        result = dict()
        for name in settings.__schema__:
            result[name] = getattr(settings, name)
        return result

    def settings_json(self):
        """ Returns setting as JSON """
        return json.dumps(self.settings)
