import gtk

class Backend():
    def message(self, args):
        dialog = gtk.MessageDialog(None,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                args.message )
        dialog.set_title(args.title)      
        dialog.run()
        dialog.destroy()
        
    def ask_string(self, args):
        parent = None
        title = args.title
        message = args.message
        default = args.default
        dlg = gtk.Dialog(title = title, parent = parent,
            buttons = (gtk.STOCK_OK, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
        dlg.set_default_response(gtk.RESPONSE_OK)
    
        dlg.set_border_width(10)
        dlg.vbox.set_spacing(10)
    
        l = gtk.Label(message)
        l.set_alignment(0, 0.5)
        dlg.vbox.pack_start(l, gtk.FALSE, gtk.FALSE)
    
        entry = gtk.Entry()
        entry.set_activates_default(gtk.TRUE)
        entry.set_text(default)
        dlg.vbox.pack_start(entry, gtk.TRUE, gtk.TRUE)
    
        dlg.vbox.show_all()
    
        result = None
        if dlg.run() == gtk.RESPONSE_OK:
            result = entry.get_text()
    
        dlg.destroy()
    
        return result

