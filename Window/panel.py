import wx
import os
import sys
sys.path.insert(0,'e:\\WORK\\NISL\\Engine')
print(sys.path)

import display_graph
from display_graph import sys_entry
#import matlab.engine
# -*- coding: utf-8 -*-  
class TheApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
        
    def OnExit(self):
        """
        del the app if not ,the program will crash.
        """
        del self
        print("the obj extinct")
        return True

class MainFrame(wx.Frame):
    def __init__(self,parent,
                 id=wx.ID_ANY,title='location system ------ NISL',
                 pos=wx.DefaultPosition,
                 size=(850,600),
                 style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MINIMIZE_BOX^wx.MAXIMIZE_BOX,
                 name='location system ------ NISL'):
        
        super(MainFrame,self).__init__(None,id,title,pos,size,style,name)
        #the pic number
        self.maxPage = 10
        self.pageNum = 0
        #the matlab engine
        #self.eng = matlab.engine.start_matlab('MATLAB_R2017b')

        self.panel = wx.Panel(self,size=(700,500))#the back ground panel
        self.makeMenuBar()
        self.makePanel()
        self.CreateStatusBar()
        self.SetStatusText(("The work directoy is "+os.getcwd()))

    def makePanel(self):
        main_Hbox = wx.BoxSizer(wx.HORIZONTAL)
        ##main_hbox is used to contain the pic and buttonsbar
        ##buttonsbar(the veritcal sizer)
       
        #pic_Pnl is used to show the pic 
        bntbar_Staticbox = wx.StaticBox(self.panel,-1,'Control') 
        bntbar_VStaticboxsizer = wx.StaticBoxSizer(bntbar_Staticbox,wx.VERTICAL)
    
        #the coordination below just for look(read only)
        x_StaticText = wx.StaticText(self.panel,-1,'x :->')
        y_StaticText = wx.StaticText(self.panel,-1,'y :->')
        self.xvalue_StaticText = wx.TextCtrl(self.panel,-1,'0',style=wx.TE_READONLY)
        self.yvalue_StaticText = wx.TextCtrl(self.panel,-1,'0',style=wx.TE_READONLY)

        x_coordinate_HBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        y_coordinate_HBoxSizer = wx.BoxSizer(wx.HORIZONTAL)

        x_coordinate_HBoxSizer.Add(x_StaticText,1,wx.EXPAND)
        x_coordinate_HBoxSizer.Add(self.xvalue_StaticText,1,wx.EXPAND)
        y_coordinate_HBoxSizer.Add(y_StaticText,1,wx.EXPAND)
        y_coordinate_HBoxSizer.Add(self.yvalue_StaticText,1,wx.EXPAND)

        #the button below
        start_Bnt = wx.Button(self.panel,-1,'START')
        next_Bnt = wx.Button(self.panel,-1,'NEXT')      
        bntbar_VStaticboxsizer.Add(start_Bnt,1,flag=wx.EXPAND)
        bntbar_VStaticboxsizer.Add(next_Bnt,1,flag=wx.EXPAND)
       
        bntbar_VStaticboxsizer.Add((20,40))
        bntbar_VStaticboxsizer.Add(x_coordinate_HBoxSizer,1,wx.EXPAND)
        bntbar_VStaticboxsizer.Add(y_coordinate_HBoxSizer,1,wx.EXPAND)

        quit_Bnt = wx.Button(self.panel,-1,'Quit')
        bntbar_VStaticboxsizer.Add((20,40))
        bntbar_VStaticboxsizer.Add(quit_Bnt,1,wx.EXPAND)

        #the pics show here
        
        img_test = wx.Image(r'.\pic\8.jpg',wx.BITMAP_TYPE_ANY)
        w = img_test.GetWidth()
        h = img_test.GetHeight()
        img_test = img_test.Scale(w/4,h/4).ConvertToBitmap()
        sb_test = wx.StaticBitmap(self.panel,-1,img_test,size=(300,300))
        #the main_Hbox add all elements
        main_Hbox.Add(sb_test,3,wx.ALL,10)
        main_Hbox.Add(bntbar_VStaticboxsizer,1,wx.ALL,10)
        
        # bind the function here
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,quit_Bnt)
        self.Bind(wx.EVT_BUTTON,self.OnStartBnt,start_Bnt)
        self.Bind(wx.EVT_BUTTON,self.OnNextBnt,next_Bnt)
        #All distribution here
        self.panel.SetSizer(main_Hbox)
        self.panel.SetBackgroundColour('white')
        self.panel.Fit() 

     #def OnPaint(self,event):
     #   buffer = wx.ClientDc(self.panel)

    # def OnStartBnt_True(self,event):
    #     #pass
    #     """
    #     this func use the data to make the pic
    #     """
    #     sys_entry()


    def OnStartBnt(self,event):
        """
        the pic from the engine diaplay_graph
        """
        self.SetStatusText("Working !!!!!")
        self.pageNum = 0
        sys_entry()
        self.SetStatusText("Finish !!!!!")
        # img_temp = wx.Image(r'.\pic\test3.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # sb_temp = wx.StaticBitmap(self.panel,-1,img_temp,size=(300,300))
        
    def OnNextBnt(self,event):
        """
        the button should stop the program.
        i don't know how to do
        so i change the bnt name and
        i think is great to simplify the function
        """
        try :

         img_temp = wx.Image(r'.\pic\test'+str(self.pageNum)+'.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
         sb_temp = wx.StaticBitmap(self.panel,-1,img_temp,size=(580,460))
         #update the position
         self.xvalue_StaticText.SetValue('100')
         self.yvalue_StaticText.SetValue('100')
        #
         self.pageNum += 1
         if self.pageNum >= self.maxPage:
             wx.MessageBox("This is the last pic,Will show the beginning")
             self.pageNum = self.pageNum % self.maxPage
        except :
            wx.MessageBox("Please do the Start before !")

    def OnCloseMe(self,event):
        self.Close(True)
        
    def OnCloseWindow(self,event):
        self.Destroy()

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """
        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(1,
                                    "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = TheApp(False)
    app.MainLoop()