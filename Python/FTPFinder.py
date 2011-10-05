#-*- coding: utf-8 -*-

import wx
from ftplib import FTP
FileName = "FileList.txt"
 
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
    ftp=FTP()
    ftp.connect("202.120.40.124","2121")
    ftp.login("projectadmin","adminproject")
 
    filelist = open(FileName,"w")
 
    listdir(ftp.nlst("+WSN"),filelist,ftp)
    filelist.close()
    ftp.quit()
 
def searchFromFile(FileName):
    filelist=open(FileName)
    LineList=filelist.readlines()
    filelist.close()
 
    searchword=filename.GetValue()
 
    searchResult=""
    for line in LineList:
        if searchword.lower() in line.lower():
            temp=searchResult
            searchResult=temp+'\n'+line
    return searchResult
 
def showGetLists(event):
    getLists()
    contents.SetValue(open(FileName).read())
 
def showSearchResult(event):
    contents.SetValue(searchFromFile(FileName))

def main():
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

if __name__ == '__main__':
	main()
