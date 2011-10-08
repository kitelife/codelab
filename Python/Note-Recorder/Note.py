# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 02:08:17 2011

@author: Xia yongfeng
"""

import os
import sys
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

import FTPOperation

class DialogForAddNote(wx.Frame):
    
    def __init__(self, parent, id, title):
        super(DialogForAddNote, self).__init__(parent, title = 'DialogForAddNote',
                                                size = (320, 130))
        self.InitUI()
        self.Center()
        self.Show()
    
    def InitUI(self):
        
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)
        
        text = wx.StaticText(panel, label = 'Add Note:')
        sizer.Add(text, pos = (0, 0), flag = wx.TOP|wx.LEFT|wx.BOTTOM, border = 5)
        
        tc = wx.TextCtrl(panel)
        
        self.noteAdded = tc
        
        sizer.Add(tc, pos = (1, 0), span = (1, 5),
                      flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 5)
        okButton = wx.Button(panel, label = 'OK', size = (90, 28))
        okButton.Bind(wx.EVT_BUTTON, self.storeNote)        
        sizer.Add(okButton, pos = (2, 2))
        
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)
        
        
    def storeNote(self,e):
        noteToBeStored = self.noteAdded.GetValue()
        if not (noteToBeStored == ''):
            fp = open('NoteBook.txt', 'a')
            fp.write(noteToBeStored.encode("gbk") + '\n')  #gbk or gb2312 or cp936
            fp.close()
        
        self.DestroyChildren()
        self.Close()    #
        
class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style = wx.LC_REPORT|wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class DialogForDelNote(wx.Frame):
    
    def __init__(self,parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (450, 400))   
        
        panel = wx.Panel(self, -1)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        leftPanel = wx.Panel(panel, -1)
        rightPanel = wx.Panel(panel, -1)
        
        
        self.log = wx.TextCtrl(rightPanel, -1, style = wx.TE_MULTILINE)
        self.list = CheckListCtrl(rightPanel)
        self.list.InsertColumn(0, 'NOTE')
        
        
        fp = open('NoteBook.txt')
        noteLists = fp.readlines()
        
        for noteLine in noteLists:
            self.list.InsertStringItem(sys.maxint, noteLine)
        
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        
        sel = wx.Button(leftPanel, -1, 'Select All', size = (100, -1))
        des = wx.Button(leftPanel, -1, 'Deselect All', size = (100, -1))
        delNotes = wx.Button(leftPanel, -1, 'Delete Notes', size = (100, -1))
        
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id = sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, id = des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeleteNotes, id = delNotes.GetId())
        
        vbox2.Add(sel, 0, wx.TOP, 5)
        vbox2.Add(des)
        vbox2.Add(delNotes)
        
        leftPanel.SetSizer(vbox2)
        
        vbox.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
        vbox.Add((-1, 10))
        vbox.Add(self.log, 0.5, wx.EXPAND)
        vbox.Add((-1, 10))
        
        rightPanel.SetSizer(vbox)
        
        hbox.Add(leftPanel, 0 ,wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(rightPanel, 1, wx.EXPAND)
        hbox.Add((3, -1))
        
        panel.SetSizer(hbox)
        
        self.Center()
        self.Show(True)
        
    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)
            
    def OnDeselectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)
    
    def OnDeleteNotes(self, event):
        num = self.list.GetItemCount()
        
        notesRemain = list()
        
        for i in range(num):
            if i == 0:
                self.log.Clear()
            if self.list.IsChecked(i):
                self.log.AppendText(self.list.GetItemText(i))
            if not self.list.IsChecked(i):
                notesRemain.append(self.list.GetItemText(i))
        
        self.list.DeleteAllItems()
        fp = open('NoteBook.txt','w')
        for note in notesRemain:
            fp.write(note)
            self.list.InsertStringItem(sys.maxint, note)
            
        fp.close()
        
class NoteMenu(wx.Menu):
    
    def __init__(self, parent):
        super(NoteMenu, self).__init__()
        
        self.parent = parent
        
        addNoteItem = wx.MenuItem(self, wx.NewId(), 'Add Note')
        self.AppendItem(addNoteItem)
        self.Bind(wx.EVT_MENU, self.addNote, addNoteItem)
        
        delNoteItem = wx.MenuItem(self, wx.NewId(), 'Delete Note')
        self.AppendItem(delNoteItem)
        self.Bind(wx.EVT_MENU, self.deleteNote, delNoteItem)
        
        sendToFTP = wx.MenuItem(self, wx.NewId(), 'Send to FTP')
        self.AppendItem(sendToFTP)
        self.Bind(wx.EVT_MENU, self.SendToFTP, sendToFTP)
        
        closeFrame = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(closeFrame)
        self.Bind(wx.EVT_MENU, self.OnClose, closeFrame)
        
        #print self.parent
        
    def addNote(self, e):
        app = wx.App()
        DialogForAddNote(None, -1, 'Dialog For Add Note')
        app.MainLoop()

    def deleteNote(self, e):
        app = wx.App()
        DialogForDelNote(None, -1, 'Dialog For Delete Note')
        app.MainLoop()
    
    def SendToFTP(self, e):
        app = wx.App()
        FTPOperation.DialogForFTPUploading(None, -1, 'Dialog For Sending to FTP')
        app.MainLoop()
       
    def OnClose(self, e):
        self.parent.DestroyChildren()
        self.parent.Close()
    
class NoteFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(NoteFrame, self).__init__(*args, **kwargs)
        
        self.fileName = 'NoteBook.txt'
        
        self.InitUI()
        
    def InitUI(self):
        
        #dirPath = os.getcwd()
        if not os.path.isfile(self.fileName):
            open(self.fileName,'w')
        
        NoteBookContent = self.ReadNotes(self.fileName)    
    
        panel = wx.Panel(self, -1)
        
        panel.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        panel.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDoubleClick)        
        
        Notes = wx.TextCtrl(panel, pos = (0, 0), size = (495, 375), 
                            style = wx.TE_MULTILINE | wx.HSCROLL)
        Notes.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        Notes.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDoubleClick)
        Notes.SetValue(NoteBookContent)
        
        
        self.Notes = Notes
        self.SetSize((500, 400))
        self.SetTitle('Note Recorder')
        self.Center()
        self.Show()
    
    def OnRightDown(self, e):
        self.PopupMenu(NoteMenu(self), e.GetPosition())
    
    def OnLeftDoubleClick(self, e):
        NoteBookContent = self.ReadNotes(self.fileName)
        self.Notes.SetValue(NoteBookContent)
        
    def ReadNotes(self,fileName):
        fp = open(fileName)
        NoteBookLines = fp.readlines()
        fp.close()
        
        NoteBookContent = ''
        
        index = 1
        for line in NoteBookLines:
            NoteBookContent = NoteBookContent + str(index) + '. ' + line + '\n'
            index = index + 1
        
        return NoteBookContent
        
def main():
    
    note = wx.App()
    NoteFrame(None, style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    note.MainLoop()
    
if __name__ == '__main__':
    main()
