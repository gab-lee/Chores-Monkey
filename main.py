# YL code
print ("baboon")
# gab code 
print("First code")
# Vikki
print("bananas are friends not food")

task_name = None
task_state = None 

def getTaskName():
    pass

def displayTaskName():
    pass

def setTaskState():
    global task_state
    states = {
        "1": "To Do",
        "2": "In Progress",
        "3": "Done"
    }

    print("Choose task state:")
    print("1. To Do (planned)")
    print("2. In Progress (active)")
    print("3. Done (completed)")

    choice = input("Enter 1, 2, or 3: ").strip()

    while choice not in states:
        choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

    task_state = states[choice]

def displayTaskState():
    print("Task state:", task_state)

getTaskName()
displayTaskName()
setTaskState()
displayTaskState()