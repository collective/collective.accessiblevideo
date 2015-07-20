from zope import schema
from plone.app.contenttypes.interfaces import IFile
from plone.supermodel import model

from collective.accessiblevideo import _


class ISubtitle(model.Schema, IFile):

    language = schema.TextLine(
        title=_(u"Language"),
        description=_(u"Language of the subtitle (e.g.: \"en\")"),
        required=True,
    )
