from plone.app.contenttypes.interfaces import IFile
from plone.supermodel import model

from collective.accessiblevideo import _


class ITranscript(model.Schema, IFile):
    pass