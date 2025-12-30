# Quickstart Guide: CLI Todo Application

**Feature**: 1-cli-todo-app
**Date**: 2025-12-30

## Getting Started

1. Ensure you have Python 3.13+ installed on your system
2. Clone or download the repository
3. Navigate to the project directory
4. Run the application with: `python src/cli/main.py`

## Using the Application

When you start the application, you'll see a welcome message and a menu with the following options:

```
Welcome to the CLI Todo Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Mark task as complete/incomplete
6. Exit
```

### Adding a Task
1. Select option 1
2. Enter the task title when prompted
3. Optionally enter a description when prompted
4. The task will be added with an auto-generated ID

### Viewing Tasks
1. Select option 2
2. All tasks will be displayed with their ID, Title, and Completion Status

### Updating a Task
1. Select option 3
2. Enter the Task ID when prompted
3. Enter the new title (or press Enter to keep the current title)
4. Enter the new description (or press Enter to keep the current description)

### Deleting a Task
1. Select option 4
2. Enter the Task ID when prompted
3. Confirm deletion if prompted

### Marking a Task as Complete/Incomplete
1. Select option 5
2. Enter the Task ID when prompted
3. The completion status will be toggled

### Exiting the Application
1. Select option 6
2. The application will close

## Development

To modify the application:

1. All source code is located in the `src/` directory
2. The main application logic is in `src/cli/main.py`
3. Task data model is defined in `src/models/task.py`
4. Task service logic is in `src/services/task_service.py`
5. Remember to follow PEP 8 style guidelines and include type hints