#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
import tkMessageBox

LARGE_FONT = ("Verdana",12)

class DDosAttackApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, udpPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
def buttonMeth(param):
    print(param)
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="DDos Attacker", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button=[]

        button.append(tk.Button(self, text="UDP Flood",
                                command=lambda: controller.show_frame(udpPage)))


        button.append(tk.Button(self, text="ICMP Flood", command=buttonMeth))
        button.append(tk.Button(self, text="Syn Flood", command=buttonMeth))
        button.append(tk.Button(self, text="Ping of Death", command=buttonMeth))
        button.append(tk.Button(self, text="Slowloris", command=buttonMeth))
        button.append(tk.Button(self, text="HTTP Flood", command=buttonMeth))
        button.append(tk.Button(self, text="HTTP Post", command=buttonMeth))
        button.append(tk.Button(self, text="RST/FIN attack", command=buttonMeth))
        button.append(tk.Button(self, text="DNS Flood", command=buttonMeth))
        button.append(tk.Button(self, text="Synonymous IP Attack", command=buttonMeth))
        for i in range(0,len(button)):
            button[i].pack()

class udpPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Udp Flooder", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button =[]
        button.append(tk.Button(self, text="Back to Home",
                                command=lambda: controller.show_frame(StartPage)))
        for i in range(0,len(button)):
            button[i].pack()                        

app = DDosAttackApp()
app.mainloop()

'''
top = Tkinter.Tk()


def udpFlooder():
    B = tkMessageBox.showinfo("The attack","Great attack")
def icmpFlooder():
    print("hey")
def icmpFLood():
    print("meh")





top.mainloop()
'''
