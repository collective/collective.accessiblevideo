from zope import schema
from plone.app.contenttypes.interfaces import IFile
from plone.supermodel import model
from plone.namedfile.field import NamedBlobFile

from collective.accessiblevideo import _


class ICaption(model.Schema):

    file = NamedBlobFile(
        title=_(u"Caption"),
        required=True,
    )

    language = schema.TextLine(
        title=_(u"Language"),
        description=_(u"Language of the caption (e.g.: \"en\")"),
        required=True,
    )
