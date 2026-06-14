# To-Do List Manager
# Features:
# - Add Task
# - Show Tasks
# - Complete Task
# - Delete Task
# - Save Data using JSON
# - Load Data from JSON
import json

tasks = []

def save_tasks():
    with open("task.json","w") as file:
        json.dump(tasks,file)

try:
    with open("task.json", "r") as file:
        tasks = json.load(file)

except (json.JSONDecodeError, FileNotFoundError):
    tasks = []

while True:
    print("="*25)
    print("     TO DO LIST     ")
    print("="*25)
    print("1. Add Task")
    print("2. Show Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("="*25)

    choice = input("Enter your choice:")

    if choice == "1":
        task = input("Enter task to add:")
        tasks.append(task)

        save_tasks()
        print("Task Added")
    elif choice == "2":
        
        if (len(tasks)) == 0:
            print("No tasks yet")
        else:
            print("Your Tasks")
            print("-"*25)
            for i, t in enumerate(tasks,start = 1):
             print(f"{i}.{t}")
    elif choice == "3":
      if len(tasks) == 0:
        print("No tasks yet.")
     
      else:
        print("\n📝 Your Tasks")
        print("-" * 25)

        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            completed = tasks.pop(number - 1)
            save_tasks()
            print(f"Task '{completed}' completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
       if len(tasks) == 0:
          print("No Tasks yet")
       else:
          print("Your Tasks:")
          print("-"*25)
          for i, t in enumerate(tasks,start=1):
             print(f"{i}.{t}")
          number = int(input("Enter task number to delete:"))
          if 1<= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                save_tasks()
                print(f"Task '{deleted}' deleted!")
          else:
                print("Invalid choice")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")