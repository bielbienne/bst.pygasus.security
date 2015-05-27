from grokcore import component

from zope.security import management
from zope.component import getUtility
from zope.interface import implementer
from zope.security.interfaces import IParticipation
from zope.securitypolicy.zopepolicy import ZopeSecurityPolicy

from bb.extjs.security import _
from bb.extjs.security.principal import Principal
from bb.extjs.security.interfaces import IAuthentication
from bb.extjs.core.interfaces import IApplicationContext
from bb.extjs.wsgi.events import IApplicationStartupEvent
from bb.extjs.wsgi.interfaces import IApplicationSettings
from bb.extjs.wsgi.events import IPreRequestProcessingEvent
from bb.extjs.wsgi.events import IPostRequestProcessingEvent


ANONYMOUSE = Principal('bb_extjs.anonymouse_user',
                       _('Anonymouse'),
                       _('Anonymouse user that is not logged in'))

AUTHENTICATED = Principal('bb_extjs.authenticated_user',
                          _('Authenticated'),
                          _('Authenticated user that we know'))


@implementer(IParticipation)
class Participation(object):

    def __init__(self, principal):
        self.principal = principal
        # Note the interaction will be set by SecurityPolicy
        self.interaction = None


@component.subscribe(IApplicationSettings, IApplicationStartupEvent)
def set_policy_security(settings, event):
    management.setSecurityPolicy(ZopeSecurityPolicy)


# not finish at all, role and rights are not supported at the moment
"""
@component.subscribe(IApplicationContext, IPreRequestProcessingEvent)
def new_interaction(context, event):
    participations = list()
    principal = getUtility(IAuthentication).authenticate(event.request)
    if principal is not None:
        participations.append(Participation(principal))
        participations.append(Participation(AUTHENTICATED))
    else:
        participations.append(Participation(ANONYMOUSE))

    management.newInteraction(*participations)


@component.subscribe(IApplicationContext, IPostRequestProcessingEvent)
def end_interaction(context, event):
    management.endInteraction()
"""
