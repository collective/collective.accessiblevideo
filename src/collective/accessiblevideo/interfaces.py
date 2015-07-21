# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema

from collective.accessiblevideo import _


class ICollectiveAccessiblevideoLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAccessibleVideoSettings(Interface):

    defaultFontsize = schema.Decimal(
        title=_(u"Default font size"),
    )

    defaultOpacity = schema.Decimal(
        title=_(u"Default opacity"),
    )

    colors = schema.Text(
        title=_(u"Colors"),
    )
