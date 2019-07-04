#################### Imports ####################
import tkinter as tk
from tkinter import ttk
from tkinter import font  as tkfont
import tkinter.messagebox as msg
import os



####################Functions ####################

def popupmsg(text):
	msg.showinfo("Info",
		text)

def about():
	msg.showinfo("Info",
			'This is the work of karim kohel.\nstarted on the 2nd of june 2019 and finished after 3 months of procrastination on the @th of july 2019\nfind me @karimkohel on instagram, or github for this project\'s repository'
		)

def how_to():
	msg.showinfo(
		'isn\'t it simple enough?',
		'First you chose how many courses you applied for this semester, then it\'s as easy as adding your marks and clicking on Calculate!')

def save_results():
	pass

	# with open('results','w') as f: 
	# 	f.write(results) # --> Need Functions

#################### Classes ####################
class GPA(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        if os.name == 'nt':
        	tk.Tk.iconbitmap(self, default="calc.ico")

        tk.Tk.wm_title(self, "GPA Calculator")

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic") 
        self.normal_font = tkfont.Font(family='Helvetica', size=11)


        container = tk.Frame(self) # making the master container frame for all frames to layer in
        container.pack(side="top", fill="both", expand=True) # filling whatever space available with the master frame
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ########## Menu bar ##########
        menubar = tk.Menu(container)

        ##### file menu #####
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Calculation", command=lambda: popupmsg("Not supported yet")) #--> Need Funtion
        filemenu.add_command(label="Save results", command=lambda: popupmsg("Not supported yet")) # --> Need Function
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self,menu=menubar)

        ##### help menu #####
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="How to use",command=how_to)
        helpmenu.add_command(label="About us",command=about)
        menubar.add_cascade(label="Help", menu=helpmenu)


        # setting chnage frame mechanism by putting frame name in tuple (by order)
        self.frames = {}
        for F in (StartPage, DataEntry, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()

########## first page ##########
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Welcome to GPA Calculator 0.2", font=controller.title_font)
        label.pack()#(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("DataEntry"))
        button2 = ttk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

########## second page ##########
class DataEntry(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

########## ##########
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()






if __name__ == "__main__":
	app = GPA()
	app.geometry("400x500")
	app.mainloop()