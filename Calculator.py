print("==================================\n")
print("          GPA Calculator       \n")
print("==================================\n")

#################### init ####################
#hi
def number_of_courses():
	wrong_val = True
	while wrong_val:
		try:
			courses = int(input("How many courses: "))
		except ValueError:
			print("must enter a number, Try again.\n")
		except Exception:
			print("well look what you did, you broke something! Try again.\n")
		else:
			wrong_val = False
	return courses

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

courses = number_of_courses()
grades = []
credits = []
alphabet = "abcdefuxABCDEFGUX"


#################### Validation ####################

while courses<1:
	print("i don\'t think thats true...Try again\n")
	courses = number_of_courses()


#################### Main ####################

for i in range(0,courses):
	while True:
		try:
			grades.append(str(input(f"Enter Grade {i+1} : ")))
			print()
			credits.append(int(input(f"Enter Credit hours {i+1} : ")))
			print()
			if not grades[i][0] in alphabet:
				raise ValueError
			if credits[i]>3 or credits[i]<1:
				raise ValueError
		except ValueError:
			print("wrong value, Try again")
		except Exception:
			print("something went wrong, Try again")
		else:
			break



#################### Processing ####################

credit_hours = sum(credits)
avg = 0.0

for i in range(0,courses):
	avg = avg + calculate(grades[i],credits[i])

total_gpa = avg / credit_hours


#################### Result ####################

print("=================================")
print(f"Your GPA is : {total_gpa}")
print("=================================")


#################### End ####################
