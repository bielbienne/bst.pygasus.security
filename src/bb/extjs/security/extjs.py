from bb.extjs.core import ext
from js.extjs.theme import themes

from fanstatic import Library
from fanstatic import Resource



library = Library('securtiylogin', 'applogin')
style = Resource(library, 'resources/style.css')

class LoginPageContext(ext.ApplicationContext):
    ext.name('login')

    title = 'Login Page'
    application = 'extjs.security.LoginPageApplication'
    namespace = 'extjs.security'
    resources = Resource(library, 'application.js',
                         depends=[ext.extjs_resources_skinless,
                                  themes['neptune'],
                                  style])
    
    credentials_pluggins = ()
    authentication_pluggins = ()


class AppClassPathMapping(ext.ClassPathMapping):
    namespace='extjs.security'
    path='fanstatic/securtiylogin'
