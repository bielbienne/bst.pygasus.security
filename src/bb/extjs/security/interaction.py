"""

this will be used later!!!!









from grokcore import component

from zope.security import management

from bb.extjs.core.interfaces import IApplicationContext
from bb.extjs.wsgi.events import IPreRequestProcessingEvent
from bb.extjs.wsgi.events import IPostRequestProcessingEvent



@component.subscribe(IApplicationContext, IPreRequestProcessingEvent)
def new_interaction(context, event):
        management.newInteraction()


@component.subscribe(IApplicationContext, IPostRequestProcessingEvent)
def end_interaction(context, event):
        management.endInteraction()

"""