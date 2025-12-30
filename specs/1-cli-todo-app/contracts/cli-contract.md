# CLI Interface Contract: Todo Application

**Feature**: 1-cli-todo-app
**Date**: 2025-12-30

## Overview

This document defines the command-line interface contract for the Todo application. Since this is a console application, the "interface" consists of user prompts, menu options, and feedback messages.

## Menu Interface

### Main Menu
- **Endpoint**: Application startup / main loop
- **Input**: None (displays menu automatically)
- **Output**: Menu options displayed to user
- **Response Format**:
```
Welcome to the CLI Todo Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Mark task as complete/incomplete
6. Exit
Choose an option (1-6):
```

## Operation Endpoints

### 1. Add Task
- **Operation**: Add a new task
- **Input**: Menu selection "1", followed by user input for title and description
- **Request Format**:
  - Prompt: "Enter task title:"
  - Prompt: "Enter task description (optional):"
- **Response Format**:
  - Success: "Task added successfully with ID: {id}"
  - Error: "Error: {error_message}"

### 2. View Tasks
- **Operation**: Display all tasks
- **Input**: Menu selection "2"
- **Response Format**:
  - Success: 
```
ID | Title | Status
---|-----|------
1  | Buy groceries | ❌ Incomplete
2  | Finish report | ✅ Complete
```
  - Empty: "No tasks found."

### 3. Update Task
- **Operation**: Update existing task
- **Input**: Menu selection "3", followed by task ID and new values
- **Request Format**:
  - Prompt: "Enter task ID to update:"
  - Prompt: "Enter new title (current: '{current_title}', press Enter to keep):"
  - Prompt: "Enter new description (current: '{current_description}', press Enter to keep):"
- **Response Format**:
  - Success: "Task {id} updated successfully"
  - Error: "Error: {error_message}"

### 4. Delete Task
- **Operation**: Delete a task
- **Input**: Menu selection "4", followed by task ID
- **Request Format**:
  - Prompt: "Enter task ID to delete:"
  - Confirmation: "Are you sure you want to delete task {id}? (y/N):"
- **Response Format**:
  - Success: "Task {id} deleted successfully"
  - Error: "Error: {error_message}"

### 5. Toggle Complete
- **Operation**: Mark task as complete/incomplete
- **Input**: Menu selection "5", followed by task ID
- **Request Format**:
  - Prompt: "Enter task ID to toggle completion status:"
- **Response Format**:
  - Success: "Task {id} marked as {status}"
  - Error: "Error: {error_message}"

### 6. Exit
- **Operation**: Close the application
- **Input**: Menu selection "6"
- **Response Format**:
  - Success: "Goodbye! Your tasks are not saved (in-memory only)."