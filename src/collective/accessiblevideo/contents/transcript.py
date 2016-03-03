from zope import schema
from plone.app.contenttypes.interfaces import IFile
from plone.supermodel import model
from plone.namedfile.field import NamedBlobFile

from collective.accessiblevideo import _


class ITranscript(model.Schema):

    file = NamedBlobFile(
        title=_(u"Transcript file"),
        required=True,
    )