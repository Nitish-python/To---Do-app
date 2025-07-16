lists = []

while True:
    print( "\n---TO DO LIST----")
    print("1.Add task")
    print("2.View tasks")
    print("3.Remove task")  
    print("4.Exit")

    choice = int(input("enter the choice: "))

    if choice == 1:
        task = input("Enter the task to add: ")
        lists.append(task)
        print(f"Task '{task}' added successfully.") 

    elif choice == 2:
        if lists:
            print("Your tasks:")
            for i, task in enumerate(lists, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")
 
    elif choice == 3:
        if not lists:
            print("no tasks to remove")

        else:
            for i ,task in enumerate(lists, start=1):
                print(f"{i}. {task}")

            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(lists):
                     removed_task = lists.pop(task_index-1)
                     print(f"Task '{removed_task}' removed successfully.")
                else:
                     print("Invalid task number.")

            except ValueError:
                    print("Invalid input. Please enter a valid task number.")

    elif choice == 4:
        print("Exiting the To-Do List application. Goodbye!")
        break   

    else:
        print("Invalid choice. Please try again.")

                      
                    