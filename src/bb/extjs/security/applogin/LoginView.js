Ext.define('extjs.security.LoginView', {
    extend: 'Ext.container.Viewport',

    requires: [

    ],

    layout: {
        type: 'vbox',
        align: 'center',
        pack: 'center'
    },
    initComponent: function() {
        var me = this;

        Ext.applyIf(me, {
            items: [{
                xtype: 'window',
                closable: false,
                resizable: false,
                draggable: false,
                itemId: 'loginwindow',
                title: 'Please Login',
                autoShow: true,
                layout: 'border',
                width: 550,
                height: 250,
                dockedItems: [{
                    rtl : false,
                    xtype: 'toolbar',
                    dock: 'bottom',
                    layout : {
                        type : 'hbox',
                        align : 'stretch'
                    },
                    items: [{
                        xtype : 'tbspacer',
                        flex : 1
                    }, {
                        xtype: 'button',
                        name: 'submit',
                        text: 'Login',
                        icon: 'login/fanstatic/securtiylogin/resources/key.png',
                        iconCls: 'key-icon',
                        minWidth: 140,
                        height: 36,
                        margin: '0 32 10 0'
                    }]
                }],
                items: [{
                    xtype: 'panel',
                    region: 'west',
                    width: 128,
                    height: 200,
                    border: false,
                    html: '<img src="login/fanstatic/securtiylogin/resources/login_icon.png" />',
                }, {
                    xtype: 'form',
                    region: 'center',
                    frame: false,
                    bodyPadding: 15,
                    defaults: {
                        xtype: 'textfield',
                        anchor: '100%',
                        labelWidth: 70,
                        margin: 20
                    },
                    items: [
                        {
                            name: 'user',
                            fieldLabel: "User"
                        },
                        {
                            inputType: 'password',
                            name: 'password',
                            fieldLabel: "Password"
                        }
                    ]
                }]
            }]
        });

        me.callParent(arguments);
    }

});