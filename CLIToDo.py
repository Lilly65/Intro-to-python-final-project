tasks = ["Default task one", "Default task two"]

def add_mode():
    try:
        newTask = input("Input new task: ")
        if not newTask.strip():
            raise ValueError("Task name cannot be empty")
        tasks.append(newTask)
    except ValueError as e:
        print(f"Error: {e}")
    except EOFError:
        print("Input stream closed unexpectedly")
    else:
        print(f"{newTask} added to task list")
    finally:
        print()

def view_mode():
    try:
        if not tasks:
            raise ValueError("No tasks")
        for i, task in enumerate(tasks):
            print(f"{i+1}: {task}")
        print()
    except ValueError as e:
        print(e)
    finally:
        print()


def delete_mode():
    try:
        delTask = input("Choose task to delete: ")
        if delTask not in tasks:
            raise ValueError("Task not found. Check view for task list.")
        tasks.remove(delTask)
    except ValueError as e:
        print(f"Error: {e}")
    except EOFError:
        print("Input stream closed unexpectedly.")
    else:
        print(f"{delTask} has been removed")
    finally:
        print()
        

def mainLoop():
    while True:
        try:
            mode = input("Enter command (add, view, delete, quit): ").casefold()
        except EOFError:
            print("Input stream ended. Exiting program...")
        except KeyboardInterrupt:
            print("\nInterrupt recieved. Exiting program...")
            break
        
        if mode == "add":
            add_mode()
        elif mode == "view":
            view_mode()
        elif mode == "delete":
            delete_mode()
        elif mode == "quit":
            print("Exiting program...")
            print()
            break
        else:
            print("Invalid command")
            print()

mainLoop()
    