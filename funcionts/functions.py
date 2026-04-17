# Constants for input validation
priority_options=["high", "medium", "low"]
status_options=["pending" , "complete"]
# Add a new task to the list with ID uniqueness check
def create_task(task):
    try:
        task_id = input("ID: ")

        
        for t in task:
            if t["id"] == task_id:
                print("ID already exists.")
                return

        title = input("Title: ")
        description = input("Description: ")
        
        while True:
            priority = input("Priority (high/medium/low): ").lower()
            if priority in priority_options:
                break
            print("Enter a valid option (high/medium/low).")
            
        while True:
            status = input("Status (pending/complete): ").lower()
            if status in status_options:
                break
            print("Enter a valid option (pending/complete).")
              
        taskk = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        }

        task.append(taskk)
        print("Task added.")

    except:
        print("Invalid input.")
      
            
 # Display all existing tasks in the list           
def task_list(task):


    if not task:
        print("No tasks found.")
        return



    for t in task:
        print(t)


# Search for a specific task by its ID or Title (case-insensitive)
def search_task(task):

    value = input("Enter ID or Title: ")

    for t in task:


        if t["id"] == value or t["title"].lower() == value.lower():
            print(t)
            return



    print("Task not found.")

# Find and update task details; keeps current value if input is empty
def update_task(task):
    try:
        task_id = input("Enter ID: ")

        for t in task:
            if t["id"] == task_id:

                new_title = input(f"New Title [{t['title']}]: ")
                if new_title.strip():
                    t["title"] = new_title

                new_description = input(f"New Description [{t['description']}]: ")
                if new_description.strip():
                    t["description"] = new_description
                
                while True:

                    priority = input(f"New Priority (high/medium/low) [{t['priority']}]: ").lower()
                    if not priority.strip():
                        break
                    if priority in priority_options:
                        t["priority"] = priority
                        break
                    print("Enter a valid option.")

                while True:

                    status = input(f"New Status (pending/complete) [{t['status']}]: ").lower()
                    if not status.strip():
                        break
                    if status in status_options:
                        t["status"] = status
                        break
                    print("Enter a valid option.")

                print("Updated task.")
                return

        print("Task not found.")

    except:
        print("Invalid input.")

# Remove a task from the list based on its ID
def delete_task(task):
    task_id = input("Enter ID: ")

    for t in task:
        if t["id"] == task_id:
            task.remove(t)
            print("Deleted task.")
            return



    print("Task not found.")