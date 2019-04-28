import wx
import os
import sys
import time
from multiprocessing import Process
sys.path.insert(0,'e:\\WORK\\NISL\\Engine')
print(sys.path)
import matlab.engine
import display_graph
import reader
from display_graph import sys_entry
#import matlab.engine
# -*- coding: utf-8 -*-  
class TheApp(wx.App):
    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH_US)
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
                 size=(880,600),
                 style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER^wx.MINIMIZE_BOX^wx.MAXIMIZE_BOX,
                 name='location system ------ NISL'):
        
        super(MainFrame,self).__init__(None,id,title,pos,size,style,name)
        #show the pic number
        self.running = False # the condition 
        self.model = 0
        self.READER = None
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.showpic,self.timer)
        self.timer.Start(5000)
        #the matlab engine crash so use my algorithm
        #self.eng = matlab.engine.start_matlab('MATLAB_R2017b')
        self.position=0
        self.pos=[0,0,0,0]
        self.panel = wx.Panel(self,size=(700,500))#the back ground panel
        self.makeMenuBar()
        self.makePanel()
        self.CreateStatusBar()
        self.SetStatusText(("The work directoy is "+os.getcwd()))

    def makePanel(self):
        """
        set the buttons and other 
        the pic just for fun.
        """
        main_Hbox = wx.BoxSizer(wx.HORIZONTAL)
        ##main_hbox is used to contain the pic and buttonsbar
        ##buttonsbar(the veritcal sizer)
       
        #pic_Pnl is used to show the pic 
        bntbar_Staticbox = wx.StaticBox(self.panel,-1,'Central Panel') 
        bntbar_VStaticboxsizer = wx.StaticBoxSizer(bntbar_Staticbox,wx.VERTICAL)
    
        #the coordination below just for look(read only)
        location_Staticbox = wx.StaticBox(self.panel,-1,"Position")
        location_VStaticboxsizer = wx.StaticBoxSizer(location_Staticbox,wx.VERTICAL)

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

        location_VStaticboxsizer.Add(x_coordinate_HBoxSizer,1,wx.EXPAND)
        location_VStaticboxsizer.Add(y_coordinate_HBoxSizer,1,wx.EXPAND)

        #the radio Box below
        selectRadio=["Off-line","Real-Time"]
        self.model_radiobox=wx.RadioBox(self.panel,-1,label="Model",
        pos=wx.DefaultPosition,size=wx.DefaultSize,choices=selectRadio,majorDimension=2)
        
        #the button below
        controlbar_Staticbox = wx.StaticBox(self.panel,-1,"Control")
        controlbar_VStaticsizer = wx.StaticBoxSizer(controlbar_Staticbox,wx.VERTICAL)
        
        start_Bnt = wx.Button(self.panel,-1,'START')
        stop_Bnt = wx.Button(self.panel,-1,'STOP')
        store_Bnt = wx.Button(self.panel,-1,'STORE')
        controlbar_VStaticsizer.Add(start_Bnt,1,flag=wx.EXPAND) 
        controlbar_VStaticsizer.Add(20,5)
        controlbar_VStaticsizer.Add(stop_Bnt,1,flag=wx.EXPAND)
        controlbar_VStaticsizer.Add(20,5)
        controlbar_VStaticsizer.Add(store_Bnt,1,flag=wx.EXPAND)

        #set the order below
        bntbar_VStaticboxsizer.Add(self.model_radiobox,1,flag=wx.EXPAND)
        bntbar_VStaticboxsizer.Add((20,10))
        bntbar_VStaticboxsizer.Add(controlbar_VStaticsizer,1,flag=wx.EXPAND)
        bntbar_VStaticboxsizer.Add((20,10))
        # bntbar_VStaticboxsizer.Add(start_Bnt,1,flag=wx.EXPAND)
        # bntbar_VStaticboxsizer.Add(stop_Bnt,1,flag=wx.EXPAND)
        # bntbar_VStaticboxsizer.Add(store_Bnt,1,flag=wx.EXPAND)
        bntbar_VStaticboxsizer.Add(location_VStaticboxsizer,1,wx.EXPAND)
        bntbar_VStaticboxsizer.Add((20,10))
        # bntbar_VStaticboxsizer.Add(x_coordinate_HBoxSizer,1,wx.EXPAND)
        # bntbar_VStaticboxsizer.Add(y_coordinate_HBoxSizer,1,wx.EXPAND)

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
        self.Bind(wx.EVT_BUTTON,self.OnStopBnt,stop_Bnt)
        self.Bind(wx.EVT_BUTTON,self.OnStoreBnt,store_Bnt)
        #All distribution here
        self.panel.SetSizer(main_Hbox)
        self.panel.SetBackgroundColour('white')
        self.panel.Fit() 

    def showpic(self,evt):
        if self.running:
            pageNum = 1
            self.position,self.pos = sys_entry(self.pos)
            try :
                if self.position == [] :
                    raise FileExistsError("sys_entry func error!")
                else:
                    img_temp = wx.Image(r'.\pic\test'+str(pageNum)+'.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                    sb_temp = wx.StaticBitmap(self.panel,-1,img_temp,size=(610,460))
                    #update the position
                    self.xvalue_StaticText.SetValue(str(int(self.position[1])))
                    self.yvalue_StaticText.SetValue(str(int(self.position[0])))
                    print(self.position)
                    #time.sleep(1)
            except FileExistsError:
                self.SetStatusText("Check the E:\ ,the data lost!")
                wx.MessageBox("Please do the Start before !")
        else :
            self.SetStatusText("Stop")

    def OnStartBnt(self,event):
        """
        the pic from the engine diaplay_graph
        """
        self.model = self.model_radiobox.GetSelection()
        if self.running ==True:
            wx.MessageBox("The system is working now !")
        else:
            self.running = True
            if self.model:
                self.READER = reader.activeReader()
                self.SetStatusText("Reader Working !!!!!")
            else:
                self.SetStatusText("Offline Working !!!!!")
   
    def OnStopBnt(self,event):
        """
        the button should stop the program.
        i don't know how to do
        so i change the bnt name and
        i think is great to simplify the function
        """
        if self.running == False:
            wx.MessageBox("Click the Start!")
        if self.running == True:    
            self.running = False
            if self.model:
                self.READER.terminate()
                self.SetStatusText("Reader Terminate !")
            self.SetStatusText("System Terminate !")

    def OnStoreBnt(self,evt):
        """
        This func designed to store or sort the data which was catch by reader.
        Use the storedata() to achieve.
        storedata() in NISL/Engine/reader.py
        """
        pass
        if self.running == True :
            wx.MessageBox("STOP before STORE !")
        else:
            if os.path.exists('E:/Fre920.625.txt'): # this will be set in the config.py
                location = reader.stroeData(self.READER)
                wx.MessageBox("The file in "+location)
            else:
                wx.MessageBox("Clike the START or check the reader")

    def OnCloseMe(self,event):
        if self.running == True and self.model:
            self.READER.terminate()
            reader.stroeData(self.READER)
            self.Close(True)
        else:
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
        if self.running == True and self.model:
            self.READER.terminate()
            reader.stroeData(self.READER)
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