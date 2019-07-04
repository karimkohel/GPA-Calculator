######################################## Imports ########################################

from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk # theme class
import os



######################################## Inits ########################################

root = Tk()
root.title("GPA Calculator")
if os.name == 'nt':
	tk.Tk.iconbitmap(self, default="calc.ico")

# root.geometry('300x400') --> not needed after all

head_font = 'Times 13 bold'
main_font = 'Times'

courses_num = [1,2,3,4,5,6,7,8,9,10]
courses = IntVar()
courses.set(courses_num[6])

grades_selection = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
grades = []
#################### frames ####################


######################################## Functions ########################################

def about_us():
	msg.showinfo('Info',
		'This is the work of karim kohel.\nstarted on the 2nd of june 2019 and finished after 3 months of procrastination on the @th of july 2019\nfind me @karimkohel on instagram, or github for this project\'s repository'
		)

def how_to():
	msg.showinfo(
		'isn\'t it simple enough?',
		'First you chose how many courses you applied for this semester, then it\'s as easy as adding your marks and clicking on Calculate!')

def calculate(grade,credit):
	if grade == 'A+':
		temp = 4 * credit
	elif grade == 'A':
		temp = 3.86 * credit
	elif grade == 'A-':
		temp = 3.7 * credit
	elif grade == 'B+':
		temp = 3.3 * credit
	elif grade == 'B':
		temp = 3 * credit
	elif grade == 'B-':
		temp = 2.7 * credit
	elif grade == 'C+':
		temp = 2.3 * credit
	elif grade == 'C':
		temp = 2 * credit
	elif grade == 'C-':
		temp = 1.7 * credit
	elif grade == 'D+':
		temp = 1.3 * credit
	elif grade == 'D':
		temp = 1 * credit
	else:
		temp = 0 * credit
	return temp

######################################## Main ########################################

#################### top bar ####################

# init the topbar parent menu then showing it
bar = Menu(root) 
root.config(menu=bar)


# creating sub menu file
file_menu = Menu(bar,tearoff=0)
bar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New Calculation')
# filemenu.add_command(label="Save results", command=pass) ------> needs work
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)


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

greet_label = Label(root,text="Welcome to GPA Calculator #",padx=50,pady=10,font=head_font).grid(row=0,column=0)
courses_label = Label(root,text="How many courses ?",padx=10,pady=10,font=main_font).grid(row=1,column=0)
drop = OptionMenu(root,courses,*courses_num).grid(row=2,column=0,padx=50,pady=5)

for i in range(courses.get()):
	drop = OptionMenu(root,grades[i],*courses_num).grid(row=2,column=0,padx=50,pady=5)



######################################## End ########################################

root.mainloop()