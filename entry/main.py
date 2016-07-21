#!/usr/bin/python
# -*- coding: gb2312 -*-

# import tkinter
import tkinter as tk
import defs.defs.HDefine as hdef
import defs.defs


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # def createWidgets(self):
    #     self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    #     self.quitButton.grid()


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
# app = Application()
# app.master.title(hdef.)





