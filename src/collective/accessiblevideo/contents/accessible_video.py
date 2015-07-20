from zope import schema
from zope.interface import Interface

from plone.supermodel import model
from plone.namedfile.field import NamedBlobFile

from collective.accessiblevideo import _


class IAccessibleVideo(model.Schema):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    video_mp4 = NamedBlobFile(
        title=_(u"mp4 Video"),
        description=_(u"Video in the mpeg format."),
    )

    video_webm = NamedBlobFile(
        title=_(u"webm Video"),
        description=_(u"Video in the webm format."),
    )

    video_ogg = NamedBlobFile(
        title=_(u"ogg Video"),
        description=_(u"Video in the ogg format."),
    )

    audio_description = NamedBlobFile(
        title=_(u"Audio description"),
        description=_(u"Audio description of the video."),
    )