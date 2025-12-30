"""
Task service for the CLI Todo application.

This module implements the CRUD operations for tasks as specified in the
requirements.
"""
from typing import List, Dict, Any, Optional
import sys
import os
# Add the src directory to the path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.task import Task


class TaskService:
    """
    Service class for managing tasks with CRUD operations.
    """
    
    def __init__(self):
        """
        Initialize the TaskService with an empty task list and next ID counter.
        """
        self.tasks: List[Task] = []
        self.next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.
        
        Args:
            title (str): The task title
            description (str): The task description (optional)
            
        Returns:
            Task: The newly created task
        """
        task = Task(task_id=self.next_id, title=title, description=description, completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def list_tasks(self) -> List[Task]:
        """
        Get a list of all tasks.
        
        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.
        
        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)
            
        Returns:
            bool: True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        if title is not None:
            # Validate the new title
            task.title = task._validate_title(title)
        
        if description is not None:
            task.description = description
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self.tasks.remove(task)
        return True
    
    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id (int): The ID of the task to toggle
            
        Returns:
            bool: True if the task status was toggled, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = not task.completed
        return True