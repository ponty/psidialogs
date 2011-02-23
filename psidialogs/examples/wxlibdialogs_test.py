#
#import psidialogs
#import wx
#
#psidialogs.set_backend( psidialogs.choice(psidialogs.all_backend_names(), 'Select backend!') )
#
#if __name__ == '__main__':
#    """
#    copy from wx.lib.dialogs
#    """    
#    #import os
#    #print os.getpid()
#    
#    class MyApp(wx.App):
#
#        def OnInit(self):
#            self.frame = frame = wx.Frame(None, -1, "Dialogs", size=(400, 240))
#            panel = wx.Panel(frame, -1)
#            self.panel = panel
#
#
#            dialogNames = [
#                'alertDialog',
#                'colorDialog',
#                'directoryDialog',
#                'fileDialog',
#                'findDialog',
#                'fontDialog',
#                'messageDialog',
#                'multipleChoiceDialog',
#                'openFileDialog',
#                'saveFileDialog',
#                'scrolledMessageDialog',
#                'singleChoiceDialog',
#                'textEntryDialog',
#            ]
#
#            self.nameList = wx.ListBox(panel, -1,
#                                       size=(130, 180),
#                                       choices=dialogNames,
#                                       style=wx.LB_SINGLE)
#            self.Bind(wx.EVT_LISTBOX, self.OnNameListSelected, self.nameList)
#
#            tstyle = wx.TE_RICH2 | wx.TE_PROCESS_TAB | wx.TE_MULTILINE
#            self.text1 = wx.TextCtrl(panel, -1, size=(200, 180), style=tstyle)
#
#            sizer = wx.BoxSizer(wx.HORIZONTAL)
#            sizer.Add(self.nameList, 0, wx.EXPAND|wx.ALL, 20)
#            sizer.Add(self.text1, 1,  wx.EXPAND|wx.ALL, 20)
#
#            panel.SetSizer(sizer)
#
#            self.SetTopWindow(frame)
#            frame.Show(1)
#            return 1
#
#
#        def OnNameListSelected(self, evt):
#            sel = evt.GetString()
#            result = None
#            if sel == 'alertDialog':
#                result = alertDialog(message='Danger Will Robinson')
#            elif sel == 'colorDialog':
#                result = colorDialog()
#            #elif sel == 'directoryDialog':
#            #    result = directoryDialog()
#            #elif sel == 'fileDialog':
#            #    wildcard = "JPG files (*.jpg;*.jpeg)|*.jpeg;*.JPG;*.JPEG;*.jpg|GIF files (*.gif)|*.GIF;*.gif|All Files (*.*)|*.*"
#            #    result = fileDialog(None, 'Open', '', '', wildcard)
#            #elif sel == 'findDialog':
#            #    result = findDialog()
#            #elif sel == 'fontDialog':
#            #    result = fontDialog()
#            elif sel == 'messageDialog':
#                result = messageDialog(None, 'Hello from Python and wxPython!',
#                          'A Message Box', wx.OK | wx.ICON_INFORMATION)
##wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION)
#                #result = messageDialog(None, 'message', 'title')
#            elif sel == 'multipleChoiceDialog':
#                result = multipleChoiceDialog(None, "message", "title", ['one', 'two', 'three'])
#            elif sel == 'openFileDialog':
#                result = openFileDialog()
#            elif sel == 'saveFileDialog':
#                result = saveFileDialog()
#            elif sel == 'scrolledMessageDialog':
#                msg = "Can't find the file dialog.py"
#                try:
#                    # read this source file and then display it
#                    import sys
#                    filename = sys.argv[-1]
#                    fp = open(filename)
#                    message = fp.read()
#                    fp.close()
#                except:
#                    pass
#                result = scrolledMessageDialog(None, message, filename)
#            elif sel == 'singleChoiceDialog':
#                result = singleChoiceDialog(None, "message", "title", ['one', 'two', 'three'])
#            elif sel == 'textEntryDialog':
#                result = textEntryDialog(None, "message", "title", "text")
#
#            if result:
#                #self.text1.SetValue(pprint.pformat(result.__dict__))
#                self.text1.SetValue(str(result))
#
#    app = MyApp(True)
#    app.MainLoop()
#

