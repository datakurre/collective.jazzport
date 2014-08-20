# -*- coding: utf-8 -*-
from plone.supermodel import model
from zope.i18nmessageid import MessageFactory

from zope.interface import Interface
from zope import schema

_ = MessageFactory('collective.jazzport')


class IJazzportLayer(Interface):
    """Marker interface that defines a Zope 3 browser layer"""


def getDefaultPortalTypes(context=None):
    return set(['File', 'Image'])


class IJazzportSettings(model.Schema):

    portal_types = schema.Set(
        title=_(u'Portal types'),
        description=_(u'Select downloadable portal types'),
        value_type=schema.Choice(
            title=_(u'Type'),
            vocabulary='plone.app.vocabularies.ReallyUserFriendlyTypes'
        ),
        defaultFactory=getDefaultPortalTypes,
        required=False
    )
