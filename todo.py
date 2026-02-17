import sqlite3

# connecting to database

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# creation of table

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT NOT NULL
)"""
)
conn.commit()


# function : add task
def add_task():
    task = input("Enter the task: ")
    cursor.execute("INSERT INTO tasks(task,status) VALUES (?,?)", (task, "pending"))
    conn.commit()
    print("Task added successfully")


# function: view task
def view_task():
    cursor.execute("SELECT*FROM tasks")
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found")
        return

    print("\n To-Do List")
    for row in rows:
        print(f"ID:{row[0]} | TASK:{row[1]} | STATUS:{row[2]}")


# function: complete task
def complete_task():
    task_id = input("Enter your task id to mark as completed: ")
    cursor.execute("UPDATE tasks SET status='completed'WHERE id=?", (task_id,))
    conn.commit()
    print("Task marked as completed...")


# function: delete task
def delete_task():
    task_id = input("Enter task id to delete: ")
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id))
    conn.commit()
    print("Task deleted...")


# Menu Loop
while True:
    print("\n_ _ _ To-Do List Menu _ _ _")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.Try again!")

conn.close()
