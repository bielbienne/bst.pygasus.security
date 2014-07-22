Ext.define('extjs.security.Controller', {
    extend: 'Ext.app.Controller',
    
    requires: [
        'scaffolding.model.Credentials'
    ],
    
    refs: [{
        ref: 'loginWindow',
        selector: '#loginwindow'
    }, {
        ref: 'form',
        selector: 'FormCredentials'
    }, {
        ref: 'successField',
        selector: 'form checkboxfield'
    }],

    stores: ['scaffolding.store.Credentials'],


    init: function(){
        this.control({
            'button[name=submit]': {
                click: this.onSubmit
            },
            'FormCredentials': {
                render: this.onContentRendered
            }
        });
    },


    onContentRendered: function(){
        // just hide success field because it was autocreated
        this.getSuccessField().hide();
        var form = this.getForm();
        var store = this.getScaffoldingStoreCredentialsStore();
        store.on('write', this.onStoreUpdate, this);
        store.on({
            scope:this,
            load: function(){
                var creds = store.getAt(0);
                this.getForm().loadRecord(creds);
            }
        });
    },


    onStoreUpdate: function(store, operator){
        var model = operator.records[0];
        if (model.get('success')){
            
        } else {
            
        }
    },


    onSubmit: function(){
        var form = this.getForm();
        if (!form.isValid()){
            this.shake();
            return;
        }
        form.updateRecord(form.getRecord());
    },


    shake: function(){
        var win = this.getLoginWindow();
        var pos = win.getPosition()[0];
        var move = function(p){
            win.el.animate({duration:30, to:{x:p}});
        };
        
        for (var i=0; i < 10; i++) {
            if (i%2 == 0)
                move(pos-15);
            else
                move(pos+15);
        };
        move(pos);
    }


});
