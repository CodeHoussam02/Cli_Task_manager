from rich import print 
from rich.panel import Panel 
from rich.table import Table, Column
from time import sleep
from rich.console import Console
import sys

# app name
app: str = ' Task Manager '
# options list
opt: list = ['Add task', 'Update task', 'Task check', 'View Tasks', 'Remove task']
# tasks array
tasks: list = []
# create a console instance 
console = Console()
# create a table instance to showcase our tasks 
table = Table(title="Tasks")
# create our table columns
table.add_column('# Task id', style="cyan", no_wrap=True)
table.add_column('Task name', style="cyan")
table.add_column('Done', style="cyan")
table.add_column('Description', style="cyan")
table.add_column('Status', style="green")
# create an infinite loop
while True:
	# display options list 
	opt_str: str = ''
	for num, op in enumerate(opt, 1):
		opt_str += f"[cyan]{num}.[/cyan] {op}\n"
	print(Panel(opt_str.strip(), title=app, width=50))
	# get user input 
	answer: str = input('| Please shoose an option : ')
	# check for options match
	if answer == '1':
		status: bool = False
		task_name: str = input('| Enter the name of task : ').strip()	
		task_desc: str = input('| Enter a description for your task : ').strip()
		# push the new task to the tasks array
		task_id: int = len(tasks) + 1
		tasks.append((task_id, task_name, status, task_desc))
	elif answer == '2':
		found: bool = False
		# get the task name 
		tsk_name: str = input('| Enter the task name : ').strip()
		# loop through tasks 
		for task in range(len(tasks) - 1):
			if tsk_name in tasks[task]:
				# change the found value
				found = True
				# get other infos
				new_description: str = input('| Enter the new description please : ')
				# update the task 
				tit, stat, des = tasks[task]
				des = new_description
				tasks[task] = tit, stat, des
		if not found:
			print(':sad:[red]Task wasn\'t found in our database :cloud:')
	elif answer == '3':
		# add all of the tasks into the tasks table
		for t_id, t_title, t_status, t_desc in tasks: 
			check = '✅' if t_status else '❌'
			table.add_row(str(t_id), t_title, str(t_status), t_desc, check)
		# print out the tasks table
		print(table)
		# get the id of the task 
		task_id: int = int(input('| Enter the task id : '))
		task: list   = list(tasks[task_id - 1])
		# change the status from unchcked to checked 
		if not task[2]:
			task[2] = True
			print(task)
			tasks[task_id - 1] = tuple(task)
		else: 
			task[2] = False
			print(task)
			tasks[task_id - 1] = tuple(task)
	elif answer == '4':
		# add all of the tasks into the tasks table
		for t_id, t_title, t_status, t_desc in tasks: 
			check = '✅' if t_status else '❌'
			table.add_row(str(t_id), t_title, str(t_status), t_desc, check)
		# print out the tasks table
		console.print(table)
		# clear the console to start fresh 
		console.clear()
	elif answer == '5':
		break

