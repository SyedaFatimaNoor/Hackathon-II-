"""
Main CLI application for the Todo application.

This module implements the main application loop and CLI interface as specified
in the requirements.
"""
from typing import Optional
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from services.task_service import TaskService
from lib.utils import format_task_list


class TodoApp:
    """
    Main CLI application class for the Todo application.
    """
    
    def __init__(self):
        """
        Initialize the TodoApp with a task service.
        """
        self.task_service = TaskService()
    
    def display_menu(self) -> None:
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("Welcome to the CLI Todo Application!")
        print("="*50)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("6. Exit")
        print("-"*50)
    
    def get_input(self, prompt: str) -> str:
        """
        Get input from the user with a prompt.
        
        Args:
            prompt (str): The prompt to display to the user
            
        Returns:
            str: The user's input
        """
        return input(prompt).strip()
    
    def handle_add_task(self) -> None:
        """
        Handle the add task operation.
        """
        print("\n--- Add New Task ---")
        title = self.get_input("Enter task title: ")
        
        if not title:
            print("Error: Task title cannot be empty.")
            return
        
        description = self.get_input("Enter task description (optional): ")
        
        try:
            task = self.task_service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_view_tasks(self) -> None:
        """
        Handle the view tasks operation.
        """
        print("\n--- All Tasks ---")
        tasks = self.task_service.list_tasks()
        formatted_tasks = format_task_list(tasks)
        print(formatted_tasks)
    
    def handle_update_task(self) -> None:
        """
        Handle the update task operation.
        """
        print("\n--- Update Task ---")
        try:
            task_id_str = self.get_input("Enter task ID to update: ")
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        task = self.task_service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        current_title = task.title
        current_description = task.description
        
        new_title = self.get_input(f"Enter new title (current: '{current_title}', press Enter to keep): ")
        new_description = self.get_input(f"Enter new description (current: '{current_description}', press Enter to keep): ")
        
        # Use None to indicate no change, or the new value if provided
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description else None
        
        if self.task_service.update_task(task_id, title_to_update, description_to_update):
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Error: Failed to update task {task_id}")
    
    def handle_delete_task(self) -> None:
        """
        Handle the delete task operation.
        """
        print("\n--- Delete Task ---")
        try:
            task_id_str = self.get_input("Enter task ID to delete: ")
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        # Confirm deletion
        confirm = self.get_input(f"Are you sure you want to delete task {task_id}? (y/N): ").lower()
        if confirm not in ['y', 'yes']:
            print("Task deletion cancelled.")
            return
        
        if self.task_service.delete_task(task_id):
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    
    def handle_toggle_complete(self) -> None:
        """
        Handle the toggle complete operation.
        """
        print("\n--- Toggle Task Completion ---")
        try:
            task_id_str = self.get_input("Enter task ID to toggle completion status: ")
            task_id = int(task_id_str)
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return
        
        if self.task_service.toggle_complete(task_id):
            task = self.task_service.get_task_by_id(task_id)
            status = "complete" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    
    def run(self) -> None:
        """
        Run the main application loop.
        """
        print("Starting CLI Todo Application...")
        
        while True:
            self.display_menu()
            
            choice = self.get_input("Choose an option (1-6): ")
            
            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_view_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_toggle_complete()
            elif choice == "6":
                print("\nGoodbye! Your tasks are not saved (in-memory only).")
                break
            else:
                print("Invalid option. Please choose a number between 1-6.")


def main() -> None:
    """
    Main entry point for the application.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()