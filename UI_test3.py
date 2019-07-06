######################################## Imports ########################################

from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk # theme class
import os
import sys



######################################## Inits ########################################

root = Tk()
root.title("GPA Calculator")
if os.name == 'nt':
	Tk.iconbitmap(root, default="calc.ico")

# root.geometry('300x550')

head_font = 'Times 13 bold'
main_font = 'Times'

courses_num = [3,4,5,6,7,8]
courses = IntVar()
courses.set(courses_num[4])

grades_selection = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
grade1 = StringVar()
grade2 = StringVar()
grade3 = StringVar()
grade4 = StringVar()
grade5 = StringVar()
grade6 = StringVar()
grade7 = StringVar()
grade8 = StringVar()

grade1.set(grades_selection[0])
grade2.set(grades_selection[0])
grade3.set(grades_selection[0])
grade4.set(grades_selection[0])
grade5.set(grades_selection[0])
grade6.set(grades_selection[0])
grade7.set(grades_selection[0])
grade8.set(grades_selection[0])

cred1 = IntVar()
cred2 = IntVar()
cred3 = IntVar()
cred4 = IntVar()
cred5 = IntVar()
cred6 = IntVar()
cred7 = IntVar()
cred8 = IntVar()

cred1.set(3)
cred2.set(3)
cred3.set(3)
cred4.set(3)
cred5.set(3)
cred6.set(3)
cred7.set(3)
cred8.set(3)

grades = []
credits = []
labels = []


#################### frames ####################


######################################## Functions ########################################

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def about_us():
	msg.showinfo('Info',
		'This is the work of Karim Kohel.\nstarted on the 2nd of june 2019 and finished after 3 months of procrastination on the 5th of july 2019\nfind me @karimkohel on instagram, or github for this project\'s repository\n\n  copyright © KarimKohel\n'
		)

def how_to():
	msg.showinfo(
		'isn\'t it simple enough?',
		'First you chose how many courses you applied for this semester, then it\'s as easy as adding your grades, credit hours and clicking on Calculate!')

def append_courses(times):

	if times == 3:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred2.get())

	elif times == 4:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())
		grades.append(grade4.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred3.get())
		credits.append(cred4.get())

	elif times == 5:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())
		grades.append(grade4.get())
		grades.append(grade5.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred3.get())
		credits.append(cred4.get())
		credits.append(cred5.get())

	elif times == 6:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())
		grades.append(grade4.get())
		grades.append(grade5.get())
		grades.append(grade6.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred3.get())
		credits.append(cred4.get())
		credits.append(cred5.get())
		credits.append(cred6.get())

	elif times == 7:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())
		grades.append(grade4.get())
		grades.append(grade5.get())
		grades.append(grade6.get())
		grades.append(grade7.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred3.get())
		credits.append(cred4.get())
		credits.append(cred5.get())
		credits.append(cred6.get())
		credits.append(cred7.get())

	elif times == 8:
		grades.append(grade1.get())
		grades.append(grade2.get())
		grades.append(grade3.get())
		grades.append(grade4.get())
		grades.append(grade5.get())
		grades.append(grade6.get())
		grades.append(grade7.get())
		grades.append(grade8.get())

		credits.append(cred1.get())
		credits.append(cred2.get())
		credits.append(cred3.get())
		credits.append(cred4.get())
		credits.append(cred5.get())
		credits.append(cred6.get())
		credits.append(cred7.get())
		credits.append(cred8.get())

	avg = 0.0

	for i in range(times):
		avg = avg + calculate(grades[i],credits[i])

	credit_hours = sum(credits)
	total_gpa = avg / credit_hours

	results(total_gpa)

def results(GPA):
	msg.showinfo("Results",f"youre GPA is\n {GPA}")
	root.destroy()
		
def page_2(times):

	# greet_label.destroy()
	courses_label.destroy()
	courses_drop.destroy()
	courses_B.destroy()

	Label2 = Label(root,text="Enter Grade and Credit hours for each course",font=main_font)
	Label2.grid(row=2,pady=5,columnspan=3)

	if times == 3:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,columnspan=3)


		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

	elif times == 4:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,padx=50,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,padx=50,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,padx=50,columnspan=3)

		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,padx=50,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,padx=50,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,padx=50,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

		L4 = Label(root,text=f"course 4", font=main_font)
		L4.grid(row=9,column=0,padx=50,columnspan=3)

		M4 = OptionMenu(root, grade4, *grades_selection)
		M4.grid(row=10,column=0,padx=50,pady=5)

		R4a = Radiobutton(root, text='2', variable=cred4, value=2)
		R4b = Radiobutton(root, text='3', variable=cred4, value=3)
		R4a.grid(row=10, column=1)
		R4b.grid(row=10, column=2)

	elif times == 5:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,padx=50,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,padx=50,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,padx=50,columnspan=3)

		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,padx=50,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,padx=50,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,padx=50,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

		L4 = Label(root,text=f"course 4", font=main_font)
		L4.grid(row=9,column=0,padx=50,columnspan=3)

		M4 = OptionMenu(root, grade4, *grades_selection)
		M4.grid(row=10,column=0,padx=50,pady=5)

		R4a = Radiobutton(root, text='2', variable=cred4, value=2)
		R4b = Radiobutton(root, text='3', variable=cred4, value=3)
		R4a.grid(row=10, column=1)
		R4b.grid(row=10, column=2)

		L5 = Label(root,text=f"course 5", font=main_font)
		L5.grid(row=11,column=0,padx=50,columnspan=3)

		M5 = OptionMenu(root, grade5, *grades_selection)
		M5.grid(row=12,column=0,padx=50,pady=5)

		R5a = Radiobutton(root, text='2', variable=cred5, value=2)
		R5b = Radiobutton(root, text='3', variable=cred5, value=3)
		R5a.grid(row=12, column=1)
		R5b.grid(row=12, column=2)

	elif times == 6:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,padx=50,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,padx=50,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,padx=50,columnspan=3)

		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,padx=50,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,padx=50,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,padx=50,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

		L4 = Label(root,text=f"course 4", font=main_font)
		L4.grid(row=9,column=0,padx=50,columnspan=3)

		M4 = OptionMenu(root, grade4, *grades_selection)
		M4.grid(row=10,column=0,padx=50,pady=5)

		R4a = Radiobutton(root, text='2', variable=cred4, value=2)
		R4b = Radiobutton(root, text='3', variable=cred4, value=3)
		R4a.grid(row=10, column=1)
		R4b.grid(row=10, column=2)

		L5 = Label(root,text=f"course 5", font=main_font)
		L5.grid(row=11,column=0,padx=50,columnspan=3)

		M5 = OptionMenu(root, grade5, *grades_selection)
		M5.grid(row=12,column=0,padx=50,pady=5)

		R5a = Radiobutton(root, text='2', variable=cred5, value=2)
		R5b = Radiobutton(root, text='3', variable=cred5, value=3)
		R5a.grid(row=12, column=1)
		R5b.grid(row=12, column=2)

		L6 = Label(root,text=f"course 6", font=main_font)
		L6.grid(row=13,column=0,padx=50,columnspan=3)

		M6 = OptionMenu(root, grade6, *grades_selection)
		M6.grid(row=14,column=0,padx=50,pady=5)

		R6a = Radiobutton(root, text='2', variable=cred6, value=2)
		R6b = Radiobutton(root, text='3', variable=cred6, value=3)
		R6a.grid(row=14, column=1)
		R6b.grid(row=14, column=2)

	elif times == 7:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,padx=50,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,padx=50,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,padx=50,columnspan=3)

		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,padx=50,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,padx=50,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,padx=50,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

		L4 = Label(root,text=f"course 4", font=main_font)
		L4.grid(row=9,column=0,padx=50,columnspan=3)

		M4 = OptionMenu(root, grade4, *grades_selection)
		M4.grid(row=10,column=0,padx=50,pady=5)

		R4a = Radiobutton(root, text='2', variable=cred4, value=2)
		R4b = Radiobutton(root, text='3', variable=cred4, value=3)
		R4a.grid(row=10, column=1)
		R4b.grid(row=10, column=2)

		L5 = Label(root,text=f"course 5", font=main_font)
		L5.grid(row=11,column=0,padx=50,columnspan=3)

		M5 = OptionMenu(root, grade5, *grades_selection)
		M5.grid(row=12,column=0,padx=50,pady=5)

		R5a = Radiobutton(root, text='2', variable=cred5, value=2)
		R5b = Radiobutton(root, text='3', variable=cred5, value=3)
		R5a.grid(row=12, column=1)
		R5b.grid(row=12, column=2)

		L6 = Label(root,text=f"course 6", font=main_font)
		L6.grid(row=13,column=0,padx=50,columnspan=3)

		M6 = OptionMenu(root, grade6, *grades_selection)
		M6.grid(row=14,column=0,padx=50,pady=5)

		R6a = Radiobutton(root, text='2', variable=cred6, value=2)
		R6b = Radiobutton(root, text='3', variable=cred6, value=3)
		R6a.grid(row=14, column=1)
		R6b.grid(row=14, column=2)

		L7 = Label(root,text=f"course 7", font=main_font)
		L7.grid(row=15,column=0,padx=50,columnspan=3)

		M7 = OptionMenu(root, grade7, *grades_selection)
		M7.grid(row=16,column=0,padx=50,pady=5)

		R7a = Radiobutton(root, text='2', variable=cred7, value=2)
		R7b = Radiobutton(root, text='3', variable=cred7, value=3)
		R7a.grid(row=16, column=1)
		R7b.grid(row=16, column=2)

	elif times == 8:

		L1 = Label(root,text=f"course 1", font=main_font)
		L1.grid(row=3,column=0,padx=50,columnspan=3)

		M1 = OptionMenu(root, grade1, *grades_selection)
		M1.grid(row=4,column=0,padx=50,pady=5)

		R1a = Radiobutton(root, text='2', variable=cred1, value=2)
		R1b = Radiobutton(root, text='3', variable=cred1, value=3)
		R1a.grid(row=4, column=1)
		R1b.grid(row=4, column=2)

		L2 = Label(root,text=f"course 2", font=main_font)
		L2.grid(row=5,column=0,padx=50,columnspan=3)

		M2 = OptionMenu(root, grade2, *grades_selection)
		M2.grid(row=6,column=0,padx=50,pady=5)

		R2a = Radiobutton(root, text='2', variable=cred2, value=2)
		R2b = Radiobutton(root, text='3', variable=cred2, value=3)
		R2a.grid(row=6, column=1)
		R2b.grid(row=6, column=2)

		L3 = Label(root,text=f"course 3", font=main_font)
		L3.grid(row=7,column=0,padx=50,columnspan=3)

		M3 = OptionMenu(root, grade3, *grades_selection)
		M3.grid(row=8,column=0,padx=50,pady=5)

		R3a = Radiobutton(root, text='2', variable=cred3, value=2)
		R3b = Radiobutton(root, text='3', variable=cred3, value=3)
		R3a.grid(row=8, column=1)
		R3b.grid(row=8, column=2)

		L4 = Label(root,text=f"course 4", font=main_font)
		L4.grid(row=9,column=0,padx=50,columnspan=3)

		M4 = OptionMenu(root, grade4, *grades_selection)
		M4.grid(row=10,column=0,padx=50,pady=5)

		R4a = Radiobutton(root, text='2', variable=cred4, value=2)
		R4b = Radiobutton(root, text='3', variable=cred4, value=3)
		R4a.grid(row=10, column=1)
		R4b.grid(row=10, column=2)

		L5 = Label(root,text=f"course 5", font=main_font)
		L5.grid(row=11,column=0,padx=50,columnspan=3)

		M5 = OptionMenu(root, grade5, *grades_selection)
		M5.grid(row=12,column=0,padx=50,pady=5)

		R5a = Radiobutton(root, text='2', variable=cred5, value=2)
		R5b = Radiobutton(root, text='3', variable=cred5, value=3)
		R5a.grid(row=12, column=1)
		R5b.grid(row=12, column=2)

		L6 = Label(root,text=f"course 6", font=main_font)
		L6.grid(row=13,column=0,padx=50,columnspan=3)

		M6 = OptionMenu(root, grade6, *grades_selection)
		M6.grid(row=14,column=0,padx=50,pady=5)

		R6a = Radiobutton(root, text='2', variable=cred6, value=2)
		R6b = Radiobutton(root, text='3', variable=cred6, value=3)
		R6a.grid(row=14, column=1)
		R6b.grid(row=14, column=2)

		L7 = Label(root,text=f"course 7", font=main_font)
		L7.grid(row=15,column=0,padx=50,columnspan=3)

		M7 = OptionMenu(root, grade7, *grades_selection)
		M7.grid(row=16,column=0,padx=50,pady=5)

		R7a = Radiobutton(root, text='2', variable=cred7, value=2)
		R7b = Radiobutton(root, text='3', variable=cred7, value=3)
		R7a.grid(row=16, column=1)
		R7b.grid(row=16, column=2)

		L8 = Label(root,text=f"course 8", font=main_font)
		L8.grid(row=17,column=0,padx=50,columnspan=3)

		M8 = OptionMenu(root, grade8, *grades_selection)
		M8.grid(row=18,column=0,padx=50,pady=5)

		R8a = Radiobutton(root, text='2', variable=cred8, value=2)
		R8b = Radiobutton(root, text='3', variable=cred8, value=3)
		R8a.grid(row=18, column=1)
		R8b.grid(row=18, column=2)


	B2 = ttk.Button(root, text="Calculate", command=lambda :append_courses(times))
	B2.grid(row=20,pady=5,columnspan=3)

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
file_menu.add_command(label='New Calculation',command=restart)
# filemenu.add_command(label="Save results", command=pass) ------> needs work
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)


# # creating sub menu view
# view_menu = Menu(bar,tearoff=0)
# bar.add_cascade(label='View',menu=view_menu)
# view_menu.add_command(label='Minimize')


# creating sub menu help
help_menu = Menu(bar,tearoff=0)
bar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='How to use',command=how_to)
help_menu.add_command(label='About',command=about_us)



#################### body ####################

greet_label = Label(root,text="Welcome to GPA Calculator 1.1",padx=50,pady=10,font=head_font)
greet_label.grid(row=0,column=0,columnspan=3)

courses_label = Label(root,text="How many courses ?",padx=10,pady=10,font=main_font)
courses_label.grid(row=1,column=0,columnspan=3)

courses_drop = OptionMenu(root,courses,*courses_num)
courses_drop.grid(row=2,column=0,padx=50,pady=10,columnspan=3)

courses_B = ttk.Button(root, text="Start",command=lambda: page_2(courses.get()))
courses_B.grid(row=3,column=0,padx=50,pady=10,columnspan=3)




######################################## End ########################################

root.mainloop()