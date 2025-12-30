"""
Task data model for the CLI Todo application.

This module defines the Task entity with validation rules as specified in the
data-model.md document.
"""
from typing import Dict, Any, Optional


class Task:
    """
    Represents a single todo task with validation.
    
    Attributes:
        id (int): Auto-incrementing identifier
        title (str): Task title (required)
        description (str): Task description (optional)
        completed (bool): Completion status (default: False)
    """
    
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Task instance.
        
        Args:
            task_id (int): The unique identifier for the task
            title (str): The task title
            description (str): The task description (optional)
            completed (bool): The completion status (default: False)
        
        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = description
        self.completed = completed
    
    @staticmethod
    def _validate_title(title: str) -> str:
        """
        Validate the task title.
        
        Args:
            title (str): The title to validate
            
        Returns:
            str: The validated title
            
        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")
        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        return title.strip()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Task instance to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create a Task instance from a dictionary.
        
        Args:
            data (Dict[str, Any]): Dictionary containing task data
            
        Returns:
            Task: New Task instance
        """
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False)
        )