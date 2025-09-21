from tkinter import *
h_root = Tk()
h_root.geometry('960x600')
h_root.minsize(900,600)
#file handling operations
import json
#load tasks
def load_prev_task():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#save tasks
def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)


#for storing tasks
tasks = load_prev_task()

#main menu
def menu():
    print("------ To-Do Lists Main Menu --------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save & Exit")

#defining each menu
def view_task():
    if not tasks:
        print("There is no Task")
    else :
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")

def add_task():
    new_task = input("New Task : ")
    tasks.append(new_task)
    save_tasks(tasks)


def mark_task():
    if not tasks:
        print("Please, Add a Task First")
    else :
        view_task()
        try:
            mark = int(input("Enter Task No. to mark Completed : "))
            if " ✅" in tasks[mark-1]:
                print("Task has already marked Completed")
            else : 
                tasks[mark-1] = tasks[mark-1] + " ✅"
                print("Task marked as Completed")
        except(IndexError,ValueError):
            print("Invalid Task Number, Please Try Again")

def delete_task():
    if not tasks:
        print("Please add a Task First")
    else :
        view_task()
        delete = int(input("Enter Task No. : "))
        tasks.pop(delete-1)
        print("Task has deleted Successfully")


#working function
while True :
    print("\n")
    menu()
    user_choice = input("Choose an Option : ")

    if user_choice=='1':
        view_task()
    elif user_choice=='2':
        add_task()
    elif user_choice=='3':
        mark_task()
    elif user_choice=='4':
        delete_task()
    elif user_choice=='5':
        save_tasks(tasks)
        print("Saved Success! User Exits")
        break
    else :
        print("Invalid User Choice, Enter a Valid Option")

h_root.mainloop()
