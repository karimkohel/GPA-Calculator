######################################## Imports ########################################

from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk # theme class


######################################## Inits ########################################

root = Tk()
root.title("GPA Calculator")
root.iconbitmap('calc.ico')
# root.geometry('300x400') --> not needed after all

head_font = 'Times 13 bold'
main_font = 'Times'

courses_num = [1,2,3,4,5,6,7,8,9,10]
courses = IntVar()
courses.set(courses_num[6])

global frame

#################### frames ####################

frame1 = Frame(root).grid(row=0,column=0)

frame2 = Frame(root).grid(row=0,column=0)

######################################## Functions ########################################

def about_us():
	msg.showinfo('Info',
		'This is the work of karim kohel.\nstarted on the 2nd of june 2019 and finished after 3 months of procrastination on the @th of july 2019\nfind me @karimkohel on instagram, or github for this project\'s repository'
		)

def how_to():
	msg.showinfo(
		'isn\'t simple enough?',
		'First you chose how many courses you applied for this semester, then it\'s as easy as adding your marks and clicking on Calculate!')

def close():
	root.destroy()
	# filler text

def swap(framechange):
	frame = framechange


######################################## Main ########################################

#################### top bar ####################

# init the topbar parent menu then showing it
bar = Menu(root) 
root.config(menu=bar)

# creating sub menu file
file_menu = Menu(bar,tearoff=0)
bar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New Calculation')
file_menu.add_command(label='Exit',command=close)

# creating sub menu view
view_menu = Menu(bar,tearoff=0)
bar.add_cascade(label='View',menu=view_menu)
view_menu.add_command(label='Minimize')

# creating sub menu help
help_menu = Menu(bar,tearoff=0)
bar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='How to use',command=how_to)
help_menu.add_command(label='About',command=about_us)



#################### body ####################

# frame 1
greet_label = Label(frame1,text="Welcome to GPA Calculator 1.0",padx=50,pady=10,font=head_font).grid(row=0,column=0)
l2 = Label(frame1,text="How many courses ?",padx=10,pady=10,font=main_font).grid(row=1,column=0)
drop = OptionMenu(frame1,courses,*courses_num).grid(row=2,column=0,padx=50,pady=5)
start_btn = Button(frame1,text="Start",command=lambda: swap(frame2)).grid(row=3,column=0,padx=50,pady=5)

# frame 2
label = Label(frame2,text='this is frame 2')



######################################## End ########################################

root.mainloop()