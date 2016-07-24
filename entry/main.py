#!/usr/bin/python
# -*- coding: gb2312 -*-

# import tkinter

from tkinter import *
import tkinter as tk
import defs.defs as ddefs
import defs.defs


import pysvn

import os

hdef = ddefs.HDefine

# uriVar = StringVar()


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.__class__.instanceCount += 1
        self.__class__.__privateInstanceCount += 1


    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

        self.uriEntry = tk.Entry(self)#, textvariable=uriVar)
        self.uriEntry.pack()
        self.uriEntry.grid()
        self.count += 1

    def getPrivateCount(self):
        return self.__privateInstanceCount

    count = 0
    instanceCount = 0
    __privateInstanceCount = 0






# mDefine = defs.defs.HDefine()
#
#
# mRoot = tk.Tk()
# mRoot.title(mDefine.hTitle)
# mRoot.geometry(mDefine.hGeometry)
# mRoot.resizable(width=False, height=True)
# mRoot.mainloop()
#
#
# pipe = os.popen("svn log http://10.10.10.210/svn/voyage/branches/ExModules")
# content = pipe.read()
# print(content)

# print(content.find("/"))

# pipe.close()

# uriVar = content
# app = Application()
# app.master.title(hdef.title)
# app.master.geometry(hdef.geometry)

# app.uriEntry.setvar(uriVar, uriVar[0])
# app.uriEntry.setvar(uriVar, 'aaa\nbbb\n')

# app.__uriVar__ = 'sad'

# app.mainloop()

# dir()

actions = pysvn.wc_notify_action
print(callable(pysvn.PysvnWcInfo))
print(callable(actions))

print(actions)
print(type(actions))

print(Application.instanceCount)
print(Application().count)
print(Application.instanceCount)
print(Application().instanceCount)
print(Application.instanceCount)
print(Application().getPrivateCount())
print("?=%d" % Application._Application__privateInstanceCount)


envIRON = os.environ
print("type=%s" % type(envIRON))
print("dir=%s" % dir(envIRON))

mDic = {1: "as", 2: "dd", "ad": 3}
print("mDic type=%s" % type(mDic))
for mdK, mdV in mDic.items():
    print("k=%s, v=%s" % (mdK, mdV))
# for k, v in os.environ.items():
#     print("%s=%s" % (k, v))

print("\n".join(["%s = %s" % (k, v) for k, v in envIRON.items()]))

# print(os.environ.items())
# print(str(actions))
# print(actions.status_completed)
# # print(pysvn.copyright)
# version = pysvn.version
# print(version)
# print(type(version))
#
# listVar = ["asd", "bb", 'cc']
# print(listVar)
# print(type(listVar))
#
# print(type(actions))
# print(dir(pysvn.PysvnWcInfo))
#
#
# listA = ['abc', 'bbb', 'ccc', 'ddddd', 'eeeeee', 'ffffffff']
#
# resultA = [elemA for elemA in listA if elemA.endswith('f')]
# print(resultA)
#
#
# gf = lambda x, y: x + 2 * y
# print(gf(10, 20))
#
# s = "this   is\na\ttest"
# ns = ' '
# ns = ' '.join(s.split())
# print(ns)

