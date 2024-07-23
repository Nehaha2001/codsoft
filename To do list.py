tasks=[]

def add_task(task):
    tasks.append({"task":task,"completed":False})
    print(("Task added"))

def list_tasks():
    print("To Do List \n")
    for index,task in enumerate(tasks,start=1):
        if task["completed"]:
            status="complete"
        else:
            status=" "
        print(f"{index}.[{status}] {task['task']}")
    print()

def mark_completed(index):
    if 1<= index <= len(tasks):
        tasks[index-1]["completed"]=True
        print("Task marked as complete")
    else:
        print("Invalid task Index")

while True:
    print("Options \n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark as complete")

    ch=input("Enter your choice (1/2/3)")

    if ch=="1":
        task=input("Enter task:")
        add_task(task)
    elif ch=="2":
        list_tasks()
    elif ch=="3":
        list_tasks()
        index=int(input("Enter task number"))
        mark_completed(index)
    else:
        print("Invalid Choice. Please choose 1,2,3")



