from grokcore import component
from zope.interface import implementer

from bb.extjs.session.interfaces import ISession
from bb.extjs.security.principal import Principal
from bb.extjs.security.interfaces import ICredentialsPlugin
from bb.extjs.security.interfaces import IAuthenticatorPlugin


XREMOTEUSER = 'xremoteuser'
FORM_LOGIN = 'loginform.login'
FORM_PASSWORD = 'loginform.password'
SESSION_CREDENTIALS = 'bb.extjs.security.session.credentials'


@implementer(ICredentialsPlugin)
class XRemoteCredentialsPlugin(component.GlobalUtility):
    """ Fetch remote user from HTTP headers. This headers must
        be set via rewrite proxy e.g. apache. Normally this plugin
        works with XRemoteAuthenticatorPlugin.
    """
    component.name('xremoteuser')

    def extractCredentials(self, request):
        """ fetch remote user in the http headers
            and create credentials with it.
        """
        remote_user = request.headers.get('X-Remote-User')
        if remote_user is None:
            return None
        return {XREMOTEUSER:remote_user}

    def challenge(self, request):
        return False

    def logout(self, request):
        return False


@implementer(ICredentialsPlugin)
class RequestCredentialsPlugin(component.GlobalUtility):
    """ Fetch credentials from HTTP headers.
    """
    component.name('request_credentials')

    def extractCredentials(self, request):
        """ fetch remote user in the http headers
            and create credentials with it.
        """
        session = ISession(request)
        cred = dict(login = request.params.get(FORM_LOGIN, None),
                    password = request.params.get(FORM_PASSWORD, None))
        if None in cred.values():
            if SESSION_CREDENTIALS in session:
                return session[SESSION_CREDENTIALS]
            else:
                return None
        session[SESSION_CREDENTIALS] = cred
        return cred

    def challenge(self, request):
        return False

    def logout(self, request):
        session = ISession(request)
        re = SESSION_CREDENTIALS in session
        del session[SESSION_CREDENTIALS]
        return re


@implementer(IAuthenticatorPlugin)
class XRemoteAuthenticatorPlugin(component.GlobalUtility):

    component.name('xremoteuser')

    def authenticateCredentials(self, credentials):
        if XREMOTEUSER not in credentials:
            return None
        return self.principalInfo(credentials[XREMOTEUSER])

    def principalInfo(self, id):
        return Principal(id)
