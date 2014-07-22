Ext.define('bielbienne.iptt.Application', {
    extend: 'Ext.app.Application',
    requires: [
    ],

    name: 'Login',

    views: [
        'extjs.security.view.MainView'
    ],
    
    controllers: [
        'extjs.scurity.controller.Main',
    ],
    
    launch: function() {
        Ext.create('extjs.security.view.MainView');
    }
});
