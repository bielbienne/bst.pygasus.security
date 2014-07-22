/*
  This controller take the sidemenu as reference and build all required content panel.
  You also only need to put the id in each itemmenu with the same name as content class.
*/


Ext.define('bielbienne.iptt.controller.Main', {
    extend: 'Ext.app.Controller',
    
    refs: [{
        ref: 'sideMenu',
        selector: '#sideMenu'
    }, {
        ref: 'contentPanel',
        selector: '#contentPanel'
    }],
    


    init: function(){
        
        this.control({
            '#sideMenu': {
                click: this.onMenuClicked
            }, 
             'ContentPanel': {
                 render: this.onContentPanelRendered
            }
        });
    },


    onMenuClicked: function(menu, menuitem, event){
        var me = this;
        Ext.each(menu.items.items, function(item, index){
            if (item.getId() == menuitem.getId()){
                me.switchContent(index);
                return false;
            }
        });
    },


    onContentPanelRendered: function(){
        var tpl =  { xtype: 'forwardingcontent',
                     hidden: true,
                    };
        var panels = this.getContentPanel();
        Ext.each(this.getSideMenu().items.items, function(item){
            Ext.require('bielbienne.iptt.view.' + item.getId(), function() {
                var xtype = item.getId().toLowerCase() + 'content';
                panels.add(Ext.merge(tpl, {xtype: xtype}));
            });
        });
        this.switchContent(0);
    },


    switchContent: function(pos){
        Ext.each(this.getContentPanel().items.items, function(item, index){
            item.setVisible(pos == index);
        });
        Ext.each(this.getSideMenu().items.items, function(item, index){
            item.getEl().setStyle('font-weight',pos == index?'bold':'normal');
        });
    }


});
