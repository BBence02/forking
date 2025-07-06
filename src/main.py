from task import Task

def main():
    print("Welcome to Awesome Tasks CLI!")
    task = Task("Learn Git forks")
    print(f"Task: {task.title}, Done: {task.done}")
    print("You can now manage your tasks with this CLI.")

if __name__ == "__main__":
    main()
