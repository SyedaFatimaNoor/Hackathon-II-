# Data Model: CLI Todo Application

**Feature**: 1-cli-todo-app
**Date**: 2025-12-30

## Task Entity

### Fields
- `id`: Integer (Auto-incrementing, starting at 1)
- `title`: String (Required, max 200 characters)
- `description`: String (Optional, max 1000 characters)
- `completed`: Boolean (Default: False)

### Validation Rules
- `id`: Must be a positive integer, auto-generated
- `title`: Required field, cannot be empty or whitespace only
- `description`: Optional, if provided must not exceed 1000 characters
- `completed`: Boolean value, defaults to False when creating a new task

### State Transitions
- `incomplete` → `completed`: When user marks task as complete
- `completed` → `incomplete`: When user unmarks task as complete

## Data Storage Structure

### In-Memory Storage
- `tasks`: List of Task dictionaries
- `next_id`: Integer counter for auto-incrementing IDs (starts at 1)

### Example Structure
```python
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, bread, eggs, fruits",
        "completed": False
    },
    {
        "id": 2,
        "title": "Finish report",
        "description": "Complete the quarterly report for review",
        "completed": True
    }
]
next_id = 3  # Next task will get ID 3
```