#Creating the to do list with python

ToDo_List = [] #Creating the Sequence

#To Show the Tasks in Numerical Order
def Show_AllTasks():
	if not ToDo_List:
		print("There are not any tasks on this list.")
	else:
		for i, Task in enumerate(ToDo_List, start =1):
			print(f"{i},{Task}")

#To Add Tasks
def Add_Tasks(Task):
	ToDo_List.append(Task)
	print(f'The Task: "{Task}" was added')

#To Show if a Task is Completed
def Complete_Tasks(number_of_task):
	try:
		Completed_Tasks = ToDo_List.pop(number_of_task - 1)
		print(f'The Task: "{Completed_Tasks}" was completed and removed from your todo list')
	except IndexError:
		print("That Task number does not exist. Please Enter a valid task number.")

#To Delete Tasks
def Delete_Tasks(number_of_task):
	try:
		Deleted_Tasks = ToDo_List.pop(number_of_task - 1)
		print(f'Task: "{Deleted_Tasks}" was deleted from your todo list.')
	except IndexError:
		print("That Task number does not exist. Please enter a valid task number")

#To Sort the Tasks Alphabetically
def Sort_Tasks():
	ToDo_List.sort()
	print("Your ToDo List has been sorted Alphabetically.")

while True:
	print("""ToDo List(Select A Number)
				1. Add Task
				2. View Tasks
				3. Complete Tasks
				4. Delete Tasks
				5. Sort Tasks
				6. Exit""")
	x = input("Choose an option for your ToDo List:")
	
	if x == "1":
		Task = input("Please Enter A Task:")
		Add_Tasks(Task)
	elif x == "2":
		Show_AllTasks()
	elif x == "3":
		number_of_task = int(input("Enter the task number you want to mark as completed."))
		Complete_Tasks(number_of_task)
	elif x == "4":
		number_of_task = int(input("Enter the number of the task you want to delete from your list"))
		Delete_Tasks(number_of_task)
	elif x == "5":
		Sort_Tasks()
	elif x =="6":
		break
	else:
		print("You have entered an Invalid Choice. Please Enter A Valid Choice Number.")
