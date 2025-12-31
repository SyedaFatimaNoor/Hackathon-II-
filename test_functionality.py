"""
Test script for the CLI Todo application.
This script tests all the functionality without requiring user input.
"""
import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.task_service import TaskService
from lib.utils import format_task_list


def test_all_functionality():
    print("Testing CLI Todo Application functionality...")
    
    # Initialize the task service
    task_service = TaskService()
    
    # Test 1: Add tasks
    print("\n--- Test 1: Adding tasks ---")
    task1 = task_service.add_task("Buy groceries", "Milk, bread, eggs, fruits")
    print(f"Added task: ID {task1.id}, Title: '{task1.title}'")
    
    task2 = task_service.add_task("Finish report", "Complete the quarterly report for review")
    print(f"Added task: ID {task2.id}, Title: '{task2.title}'")
    
    # Test 2: List tasks
    print("\n--- Test 2: Listing tasks ---")
    all_tasks = task_service.list_tasks()
    print(f"Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "[X] Complete" if task.completed else "[ ] Incomplete"
        print(f"ID: {task.id}, Title: '{task.title}', Status: {status}")
    
    # Test 3: Update a task
    print("\n--- Test 3: Updating a task ---")
    update_success = task_service.update_task(task1.id, title="Buy groceries (updated)", description="Milk, bread, eggs, fruits, vegetables")
    if update_success:
        updated_task = task_service.get_task_by_id(task1.id)
        print(f"Updated task: ID {updated_task.id}, Title: '{updated_task.title}', Description: '{updated_task.description}'")
    else:
        print("Failed to update task")
    
    # Test 4: Toggle completion status
    print("\n--- Test 4: Toggling completion status ---")
    toggle_success = task_service.toggle_complete(task1.id)
    if toggle_success:
        toggled_task = task_service.get_task_by_id(task1.id)
        status = "[X] Complete" if toggled_task.completed else "[ ] Incomplete"
        print(f"Toggled task {toggled_task.id} to {status}")
    
    # Test 5: Delete a task
    print("\n--- Test 5: Deleting a task ---")
    delete_success = task_service.delete_task(task2.id)
    if delete_success:
        print(f"Deleted task with ID {task2.id}")
    else:
        print("Failed to delete task")
    
    # Test 6: Verify deletion
    print("\n--- Test 6: Verifying deletion ---")
    remaining_tasks = task_service.list_tasks()
    print(f"Remaining tasks after deletion: {len(remaining_tasks)}")
    for task in remaining_tasks:
        status = "[X] Complete" if task.completed else "[ ] Incomplete"
        print(f"ID: {task.id}, Title: '{task.title}', Status: {status}")
    
    print("\n--- All tests completed successfully! ---")


if __name__ == "__main__":
    test_all_functionality()