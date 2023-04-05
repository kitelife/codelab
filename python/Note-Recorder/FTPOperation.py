# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 07:55:57 2011

@author: Xia yongfeng
"""

import wx
import datetime
from ftplib import FTP
import os.path

class DialogForFTPUploading(wx.Frame):
    def __init__(self, parent, id, title):
        super(DialogForFTPUploading, self).__init__(parent,
                                    title = 'Dialog For FTP Uploading',
                                    size = (400, 160))
        self.InitUI()
        self.Center()
        self.Show()
    
    def InitUI(self):
        
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label = 'HOST')
        
        hbox1.Add(st1, flag = wx.RIGHT, border = 8)
        tc1 = wx.TextCtrl(panel)
        hbox1.Add(tc1, proportion = 1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,
                    border = 10)
        vbox.Add((-1,10))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        st2 = wx.StaticText(panel, label = 'USER')
        
        hbox2.Add(st2,  flag=wx.RIGHT, border = 8)
        tc2 = wx.TextCtrl(panel)
        hbox2.Add(tc2, proportion = 1)
        
        st3 = wx.StaticText(panel, label = 'PASSWD')
        
        hbox2.Add(st3, flag = wx.RIGHT, border = 8)
        tc3 = wx.TextCtrl(panel)
        hbox2.Add(tc3, proportion = 1)
        
        vbox.Add(hbox2,flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)
        vbox.Add((-1,10))

        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(panel, -1, 'OK', size = (100, -1))
        okButton.Bind(wx.EVT_BUTTON, self.SendToFTP, id = okButton.GetId())
        
        hbox3.Add(okButton, flag=wx.RIGHT, border = 8)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)
        
        panel.SetSizer(vbox)
        
        self.tc1 = tc1
        self.tc2 = tc2
        self.tc3 = tc3
        
    def SendToFTP(self, e):
        
        hostNameWithPort = self.tc1.GetValue()
        if ':' in hostNameWithPort:
            hostName, port = hostNameWithPort.split(':')
        else:
            hostName = hostNameWithPort
            port = 21
        
        
        userName = self.tc2.GetValue()
        passwd = self.tc3.GetValue()
        remoteDir = 'incoming/+User/XiaYongfeng/'
       # print hostName, port, userName, passwd, remoteDir
        
        if hostName == '':
            print 'please give me hostName'
            return 0
        elif userName == '':
            print 'please give me a username'
            return 0
        elif passwd == '':
            print 'please give me a passwd'
            return 0;
        
        f = FTP()
        try:
            f.connect(hostName, int(port))
        except:
            print "The Host is not exist or can't connect now"
            return 0
        try:
            f.login(userName, passwd)
        except:
            print 'userName or passwd is not correct'
            return 0
        try:
            f.cwd(remoteDir)
        except:
            print 'There is not a directory named %s' %remoteDir
        
        localfile = 'NoteBook'
        dateTime = (str(datetime.datetime.today())).replace('-','').\
            replace(' ','').replace(':','')
        fd = open(localfile+'.txt','rb')
        f.storbinary('STOR %s' %os.path.basename(localfile+dateTime.split('.')[0]+'.txt'),fd)
        fd.close()
        
        f.quit()
        
        self.Destroy()