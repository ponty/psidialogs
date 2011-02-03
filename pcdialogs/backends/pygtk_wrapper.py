import gtk
from yapsy.IPlugin import IPlugin

class Backend(IPlugin):
    backend = 'PyGTK'
    backend_version=gtk.ver

    def _message(self, args, typ):
        dialog = gtk.MessageDialog(None,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                typ, gtk.BUTTONS_OK,
                args.message)
        dialog.set_title(args.title)      
        dialog.run()
        dialog.destroy()
        
    def _dlg(self, args, show_entry, yesno=False):
        parent = None
        title = args.title
        message = args.message
        default = args.default
        if yesno:
            buttons = (gtk.STOCK_YES, gtk.RESPONSE_OK, gtk.STOCK_NO, gtk.RESPONSE_CANCEL)
        else:
            buttons = (gtk.STOCK_OK, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        dlg = gtk.Dialog(title=title, parent=parent, buttons=buttons)
        dlg.set_default_response(gtk.RESPONSE_OK)
    
        dlg.set_border_width(10)
        dlg.vbox.set_spacing(10)
    
        l = gtk.Label(message)
        l.set_alignment(0, 0.5)
        dlg.vbox.pack_start(l, False, False)
        
        if show_entry:
            entry = gtk.Entry()
            entry.set_activates_default(True)
            entry.set_text(default)
            dlg.vbox.pack_start(entry, True, True)
    
        dlg.vbox.show_all()
    
        result = None 
        x = dlg.run()
        if show_entry:
            if x == gtk.RESPONSE_OK:
                result = entry.get_text()
        else:
            result = x == gtk.RESPONSE_OK 
        
        dlg.destroy()
    
        return result

    def message(self, args):
        self._message(args, gtk.MESSAGE_INFO)
        
    def warning(self, args):
        self._message(args, gtk.MESSAGE_WARNING)
        
    def error(self, args):
        self._message(args, gtk.MESSAGE_ERROR)
        
    def ask_string(self, args):
        return self._dlg(args, show_entry=1)
        
    def ask_ok_cancel(self, args):
        return self._dlg(args, show_entry=0)
    
    def ask_yes_no(self, args):
        return self._dlg(args, show_entry=0, yesno=1)
