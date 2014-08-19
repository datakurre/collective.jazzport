# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from zExceptions import NotFound

from collective.jazzport.iterators import AsyncWorkerStreamIterator
from collective.jazzport.utils import ZipExport


class ZipDownloadView(BrowserView):

    def __call__(self):
        pc = getToolByName(self.context, 'portal_catalog')
        query = {'path': '/'.join(self.context.getPhysicalPath())}
        urls = sorted([brain.getURL() for brain in pc(query)])

        if not urls:
            raise NotFound(self.context, self.__name__, self.request)

        return AsyncWorkerStreamIterator(
            ZipExport('{0:s}.zip'.format(self.context.getId()),
                      urls, cookies=self.request.cookies),
            self.request
        )
