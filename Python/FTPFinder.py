#-*- coding: utf-8 -*-

import wx
import sys
import os

from ftplib import FTP

FileName = "FileList.txt"
contents = ""

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
    
    host, port, username, passwd = sys.argv[1:]  #可能会存在问题
    try:
        ftp=FTP()
        ftp.connect(host,port)
        ftp.login(username,passwd)
    except:
        return
    print "connected to FTP"
    filelist = open(FileName,"w")

    try:
        listdir(ftp.nlst("+WSN"),filelist,ftp)
    except:
        pass
    filelist.close()
    ftp.quit()
 
def searchFromFile(FileName):

    if not os.path.isfile(FileName):
        print 'There is no the file, because you should first get the file content for search'
        return ""
    else:
        fp=open(FileName)
        lineList = fp.readlines()
        fp.close()

        searchResult=""

        searchword=filename.GetValue().encode(in_coding)  #...
        searchword = searchword.strip()
        if searchword == "":
            for line in lineList:
                searchResult += '\n' + line
        else:
            for line in lineList:
                if searchword in line:
                    temp=searchResult
                    searchResult=temp+'\n'+line
        return searchResult
 
def showGetLists(event):
    getLists()
    contents.SetValue(open(FileName).read())
    #contents.SetValue(getLists())
 
def showSearchResult(event):
    contents.SetValue(searchFromFile(FileName).decode(in_coding))

##################### Main ##############################

if len(sys.argv) < 5:
    print '''usage: python FTPFinder.py [HostName] [Port] [UserName] [Passwd]'''
    exit(0)

app = wx.App()
win = wx.Frame(None,title = "FTP-Searcher",size=(410,335))

bkg = wx.Panel(win)
	
loadButton = wx.Button(bkg,label='GetList')
loadButton.Bind(wx.EVT_BUTTON,showGetLists)

saveButton = wx.Button(bkg,label='Search')
saveButton.Bind(wx.EVT_BUTTON,showSearchResult)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

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
