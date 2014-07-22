Ext.define('bielbienne.iptt.view.MainView', {
    extend: 'Ext.container.Viewport',

    requires: [
        'bielbienne.iptt.view.Navigation',
        'bielbienne.iptt.view.ContentPanel',
        'Ext.panel.Panel'
    ],

    itemId: 'mainView',
    layout: 'border',

    initComponent: function() {
        var me = this;

        Ext.applyIf(me, {
            items: [
                {
                    xtype: 'mypanel4',
                    region: 'west',
                    split: true
                },
                {
                    xtype: 'ContentPanel',
                    region: 'center',
                    split: true
                }
            ]
        });

        me.callParent(arguments);
    }

});