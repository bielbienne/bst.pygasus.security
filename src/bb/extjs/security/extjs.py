from bb.extjs.core import ext
from js.extjs.theme import themes

from fanstatic import Library
from fanstatic import Resource



library = Library('securtiylogin', 'applogin')

class LoginPageContext(ext.ApplicationContext):
    ext.name('login')

    title = 'Login Page'
    application = 'bb.extjs.security.loginpage'
    namespace = 'extjs.security'
    resources = Resource(library, 'login.js',
                         depends=[ext.extjs_resources_skinless, themes['neptune']])
    
    credentials_pluggins = ()
    authentication_pluggins = ()


class AppClassPathMapping(ext.ClassPathMapping):
    namespace='extjs.security'
    path='fanstatic/securtiylogin'


class ViewClassPathMapping(ext.ClassPathMapping):
    namespace='extjs.security.view'
    path='fanstatic/securtiylogin/view'


class ControllerClassPathMapping(ext.ClassPathMapping):
    namespace='extjs.security.controller'
    path='fanstatic/securtiylogin/controller'