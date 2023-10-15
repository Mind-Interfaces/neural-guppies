# Importing required modules
import wx

class Guppies1_0App(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        dlg = Guppies1_0Dialog(None)
        self.SetTopWindow(dlg)
        dlg.ShowModal()
        return False
