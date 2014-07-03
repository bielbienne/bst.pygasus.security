from grokcore import component

from zope.interface import implementer
from zope.authentication.interfaces import PrincipalLookupError

from bb.extjs.security import interfaces


@implementer(interfaces.IAuthentication)
class PluggableUtility(component.GlobalUtility):
    """ Default pluggable authentication utility
        with similar functionality as zope framework.
    """

    def _credentials_pluggins(self):
        application = getUtility(IApplicationContext)
        for name in application.credentials_pluggins:
            pluggin = queryUtility(interfaces.ICredentialsPlugin, name=name)
            if pluggin is not None:
                yield pluggin
    
    def _authentication_pluggins(self):
        application = getUtility(IApplicationContext)
        for name in application.authentication_pluggins:
            pluggin = queryUtility(interfaces.IAuthenticatorPlugin, name=name)
            if pluggin is not None:
                yield pluggin

    def authenticate(request):
        for cred in self._credentials_pluggins():
            for auth in self._authentication_pluggins():
                principal = auth.authenticateCredentials(cred.extractCredentials())
                if principal is not None:
                    return principal
        return None

    def unauthenticatedPrincipal():
        return None

    def unauthorized(id, request):
        raise Notimplemented('just not implemented at the moment')

    def getPrincipal(id):
        for auth in self._authentication_pluggins():
            principal = auth.principalInfo(id)
            if principal is None:
                continue
            return principal
        raise PrincipalLookupError(id)

    def logout(self, request):
        for cred in self._credentials_pluggins():
            if cred.logout(request):
                return True
        return False
