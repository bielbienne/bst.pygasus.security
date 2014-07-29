from bb.extjs.core import ext
from js.extjs.theme import themes

from zope import schema
from zope.interface import Interface
from zope.component import getUtility

from fanstatic import Library
from fanstatic import Resource

from bb.extjs.security.plugins import FORM_LOGIN
from bb.extjs.security.plugins import FORM_PASSWORD
from bb.extjs.security.interfaces import IAuthentication


library = Library('securtiylogin', 'applogin')
style = Resource(library, 'resources/style.css')


class LoginPageContext(ext.ApplicationContext):
    """ Base class to easily create a login page in your
        application. All you need is inherited in your project.
    """
    ext.baseclass()
    ext.name('login')

    title = 'Login Page'
    application = 'extjs.security.LoginPageApplication'
    namespace = 'extjs.security'
    resources = Resource(library, 'application.js',
                         depends=[ext.extjs_resources_skinless,
                                  themes['neptune'],
                                  style])
    
    credentials_pluggins = ('request_credentials',)
    authentication_pluggins = ()


class AppClassPathMapping(ext.ClassPathMapping):
    namespace='extjs.security'
    path='fanstatic/securtiylogin'


@ext.scaffolding('Credentials')
class ICredentials(Interface):
    
    login = schema.TextLine(title = 'Username',
                               required = True,
                           )

    password = schema.Password(title = 'Password',
                                required = True,
                           )
    
    success = schema.Bool(title = 'Success',
                           required = False,
                           )


class Credentials(ext.Model):
    ext.schema(ICredentials)
    login = ''
    password = ''
    success = False


class CredentialsHandler(ext.AbstractModelHandler):
    """ This handler will just push the credential to request. After that a
        credential-plugin will create the information for the auth-plugin.
    """
    
    ext.adapts(Credentials, ext.IRequest)
    def get(self, model):
        """ just return a empty list
        """
        return [model], 1

    def create(self, model):
        raise NotImplementedError('not possible...')

    def delete(self, model):
        raise NotImplementedError('not possible...')

    def update(self, model):
        self.request.GET.add(FORM_LOGIN, model.login)
        self.request.GET.add(FORM_PASSWORD, model.password)
        
        principal = getUtility(IAuthentication).authenticate(self.request)
        model.success = principal is not None
        return [model], 1


