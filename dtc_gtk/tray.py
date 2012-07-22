'''
Created on Jun 30, 2012

@author: hugosenari
'''
from plugnplay import Plugin
from dtc.core.interfaces.module import Module
from dtc.core.interfaces.loggable import Loggable
from dtc.core.interfaces.indictable import Indictable
import gtk

class Tray(Plugin):
    '''
    Gtk tray for dtc
    '''
    implements = [Module, Indictable]
    def __init__(self):
        self.itens = {}
        self.menu = gtk.Menu()

    #methods for Module
    @property
    def version(self, *arg, **vargs):
        return 1
       
    @property
    def require(self, *args, **vargs):
        return None
        
    @property
    def priority(self, *args, **vargs):
        return 1
    
    @property
    def title(self, *args, **vargs):
        return "system tray icon"
    
    @property
    def description(self, *args, **vargs):
        return "Implement indictable using gtk.StatusIcon"
    
    @property
    def author(self, *args, **vargs):
        return "hugosenari <hugosenari@gmail.com>"
    
    #methods for Indictable
    def appendItem(self, title, on_click, alt=None, *args, **vargs):
        menu_item = gtk.MenuItem(title)
        menu_item.connect("activate", on_click)
        menu_item.set_tooltip_text(alt)
        menu_item.show()
        self.menu.append(menu_item)
        key = len(self.itens.keys())
        self.itens[key] = menu_item
        Loggable.debug("appendItem", "'%s' => '%s'" % (key, title)) 
        return key 
    
    def removeItem(self, item_id=None, *args, **vargs):
        menu_item = self.itens.get(item_id, None)
        if menu_item:
            Loggable.debug("removeItem", item_id)
            menu_item.destroy()
    
    def show(self, name='dtc', icon='exec', tooltip='DTC - Script Runner',*args, **vargs):
        if len(self.itens):
            self.menu.show()
            try:
                #try use appindicator
                import appindicator
#                ind = appindicator.Indicator(name,
#                                          icon,
#                                          appindicator.CATEGORY_APPLICATION_STATUS)
#                ind.set_status(appindicator.STATUS_ACTIVE)
#                ind.set_label(tooltip)
#                ind.set_menu(self.menu)
#                loggable.Loggable.debug("Appindicator", "Use appindicator")
                ind = appindicator.Indicator ("debian-doc-menu","distributor-logo", appindicator.CATEGORY_APPLICATION_STATUS)
                ind.set_status (appindicator.STATUS_ACTIVE)
                menu = gtk.Menu()
                def faq_clicked(*args, **kws): print args, kws
                faq_item = gtk.MenuItem("Debian FAQ")
                faq_item.connect("activate", faq_clicked)
                faq_item.show()
                menu.append(faq_item)
                ind.set_menu(menu)
            except:
                #else use gtk.StatusIcon
                tray = gtk.StatusIcon()
                tray.set_name(name)
                tray.set_from_icon_name(icon)
                tray.set_tooltip(tooltip)
                def show_menu(self, tray, event, activate_time, menu, *args, **kws):
                    menu.popup(None, None, gtk.status_icon_position_menu, event, activate_time, tray)
                tray.connect('popup-menu', show_menu, self.menu)
                Loggable.debug("StatusIcon", "Use StatusIcon")
            Loggable.info("Starter indicator", "Your indicatior module starts", self.itens)
            gtk.main()
        else:
            Loggable.warn("Empty indicator", "No itens found to populate indicator menu")
