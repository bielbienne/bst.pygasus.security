Ext.define('extjs.security.Controller', {
    extend: 'Ext.app.Controller',
    
    refs: [{
        ref: 'loginwindow',
        selector: '#loginwindow'
    }],


    init: function(){
        this.control({
            'button[name=submit]': {
                click: this.onClick
            }
        });
    },

    onClick: function(){
        debugger
    }

});
