#type: ignore
import click # Import the click library
import os # Import the os library
import json

TODO_FILE = "todo.json"

def load_todos():
    if os.path.exists(TODO_FILE):
     with open(TODO_FILE, "r") as file:
       return json.load(file)
    else:
     return []

def save_todos(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
@click.group()
def cli():
    """A simple CLI for managing your todo tasks"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the todo list"""
    tasks = load_todos()
    tasks.append({"task": task, "done": False})
    save_todos(tasks)
    click.echo(f"Task '{task}' added to the todo list")

@click.command()
def list():
    """List all tasks in the todo list"""
    tasks = load_todos()
    if not tasks:
        click.echo("No tasks in the todo list")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {status} {task['task']}")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_todos()
    if 0 < task_number <= len(tasks):
     tasks[task_number - 1]["done"] = True
     save_todos(tasks)
     click.echo(f"Task {task_number} marked as complete")
    else:
     click.echo("Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the todo list"""
    tasks = load_todos()
    if 0 < task_number <= len(tasks):
     removed_task = tasks.pop(task_number - 1)
     save_todos(tasks)
     click.echo(f"Task '{removed_task['task']}' deleted from the todo list")
    else:
     click.echo("Invalid task number: {task_number}")



cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)
if __name__ == "__main__":
    cli()
