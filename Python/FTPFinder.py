#-*- coding: utf-8 -*-
import socket

import wx
import sys
import os
from ftplib import FTP

FileName = "FileList.txt"
contents = None

in_coding = ""
#print sys.platform
if sys.platform == "win32":
    in_coding = "gbk"
else:
    in_coding = "utf-8"
#print in_coding

def listdir(dirlist,filelist,ftp):
    eachList=""
    for dir in dirlist:
        subdirs=ftp.nlst(dir)
        length=len(subdirs)
        if length>1:
            listdir(subdirs,filelist,ftp)
        elif length == 1:
            temp = eachList
            eachList = temp+"\n"+subdirs[0]
            filelist.write(subdirs[0]+"\n")
    return eachList
 
def getLists():
    
    host, port, username, passwd = filename.GetValue().encode(in_coding).split(':')[:4]  #可能会存在问题
    filename.SetValue("")
    
    try:
        ftp=FTP()
        ftp.connect(host,port)
        ftp.login(username,passwd)
    except:
        
        return
    #print "connected to FTP"
    filelist = open(FileName,"w")
    
    contents.SetValue("Connected to FTP server, begin to tranverse the fold tree...please waiting\n\n")
    
    try:
        listdir(ftp.nlst("+WSN"),filelist,ftp)
    except socket.error, e:
        contents.AppendText(str(e.message)+"\n")
    filelist.close()
    ftp.quit()
 
def searchFromFile(FileName):

    if not os.path.isfile(FileName):
        contents.SetValue('There is no the file, because you should first get the file content for search')
        return ""
    else:
        fp=open(FileName)
        lineList = fp.readlines()
        fp.close()

        searchResult=""

        searchword=filename.GetValue().encode(in_coding)  #...
        searchword = searchword.strip()
        if searchword == "":
            pass
        else:
            for line in lineList:
                if searchword in line:
                    temp=searchResult
                    searchResult=temp+'\n'+line
        return searchResult
 
def showGetLists(event):
    getLists()
    fileContent = open(FileName).read()
    if fileContent == "":
        pass
    else:
        try:
            contents.AppendText(fileContent.decode(in_coding)+"\n\n")
        except UnicodeDecodeError, e:
            contents.AppendText("UnicodeDecodeError: "+e.reason + "\n\n")
    #contents.SetValue(getLists())
 
def showSearchResult(event):
    searchResult = searchFromFile(FileName)
    if searchResult == "":
        pass
    else:
        try:
            contents.AppendText(searchResult.decode(in_coding)+"\n\n")
        except UnicodeDecodeError, e:
            contents.AppendText("UnicodeDecodeError: "+e.reason+ "\n\n")
##################### Main ##############################

Tips = '''
1.
If you want to "GetList" from FTP server, you should first
input "[HostName|IP]:[Port]:[UserName]:[Passwd]" in the
textBox above, then click Button "GetList"

2.
If you want to search from local file which is produced by
step 1, you should first input the KeyWord in the textBox
above, then click Button "Search"
'''

app = wx.App()
win = wx.Frame(None,title = "FTP-Searcher",size=(410,335))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg,label='GetList')
loadButton.Bind(wx.EVT_BUTTON,showGetLists)

saveButton = wx.Button(bkg,label='Search')
saveButton.Bind(wx.EVT_BUTTON,showSearchResult)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

contents.SetValue(Tips)

hbox = wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()