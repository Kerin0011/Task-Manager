from data.services import*
from  functions.functions import*
task = load_data()
#while loop to prevent program closure when a value is entered
while True:
    print("\n1. Create task")
    print("2. Task list")
    print("3. Search task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")
# User menu selection and task management logic
    opcion = input("Option: ")

    if opcion == "1":
        create_task(task)
    elif opcion == "2":
        task_list(task)
    elif opcion == "3":
        search_task(task)
    elif opcion == "4":
        update_task(task)
    elif opcion == "5":
        delete_task(task)
    elif opcion == "6":
        print("Good bye")
        save_data(task)
        break
    else:
        print("Invalid option.")
        
        #Kerin Barranco Martinez
        #Clan 10 