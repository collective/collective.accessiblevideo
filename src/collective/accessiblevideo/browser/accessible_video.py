from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from plone.memoize.view import memoize


class AccessibleVideoView(BrowserView):

    def __call__(self, *args, **kwargs):
        self.catalog = getToolByName(self.context, 'portal_catalog')
        self.context_path = '/'.join(self.context.getPhysicalPath())
        return super(AccessibleVideoView, self).__call__(*args, **kwargs)

    def _get_file_url(self, context, field='file', download=False):
        return '{0}/@@{1}/{2}'.format(
            context.absolute_url(),
            download and 'download' or 'display-file',
            field
        )

    @memoize
    def get_captions(self):
        captions = []
        brains = self.catalog(
            path={'query': self.context_path, 'depth': 1},
            portal_type='Caption'
        )
        for brain in brains:
            obj = brain.getObject()
            captions.append({
                'label': obj.title,
                'src': self._get_file_url(obj, download=True),
                'lang': obj.language,
            })
        return captions

    @memoize
    def get_transcripts(self):
        transcripts = []
        brains = self.catalog(
            path={'query': self.context_path, 'depth': 1},
            portal_type='Transcript'
        )
        for brain in brains:
            obj = brain.getObject()
            transcripts.append({
                'title': obj.title,
                'src': self._get_file_url(obj),
            })
        return transcripts
