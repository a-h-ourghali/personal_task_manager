# 📋 Personal Task Manager

A simple and organized command-line task manager built with Python. Add tasks, save them locally, assign priorities, and access Admin Mode with environment-based password authentication.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-orange" alt="Learning Project">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/License-TBD-lightgrey" alt="License TBD">
</p>

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [📁 Project Structure](#-project-structure)
- [📄 File Description](#-file-description)
- [🛠️ Requirements](#️-requirements)
- [📦 Installation](#-installation)
- [🔐 Environment Setup](#-environment-setup)
- [▶️ Usage](#️-usage)
- [💻 Example Output](#-example-output)
- [📸 Screenshots](#-screenshots)
- [🎬 Demo](#-demo)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ Features

### ✅ Task Management
- Add tasks through the terminal.
- Prevent empty tasks from being added.
- Display tasks in a numbered list.
- Associate tasks with the user's name.

### 🎯 Task Priority
- Assign a priority to each task.
- Choose from three priority levels: `low`, `medium`, and `high`.
- Validate priority input and reject unsupported values.
- Display the selected priority alongside the task.

### 💾 Task Storage
- Save tasks locally in `tasks.txt`.
- Load previously saved tasks.
- Keep task data on the local machine.

### 🔐 Admin Mode
- Choose whether to enter Admin Mode.
- Verify the admin password.
- Load the password from `.env`.
- Keep the actual password outside the main Python source code.

---

## 📁 Project Structure

```text
personal_task_manager/
├── main.py
├── tasks.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── Screenshots/
│   ├── pic1.png
│   ├── pic2.png
│   └── pic3.png
└── gifs/
    └── demo.gif
```

> **Note:** `.env` and `tasks.txt` are local files and should be ignored by Git. They should not be included in the public repository.

---

## 📄 File Description

| File or Folder | Description |
|---|---|
| `main.py` | Main program and task management logic |
| `tasks.py` | Contains task-related functions |
| `.env.example` | Example environment variable configuration |
| `.gitignore` | Specifies files Git should ignore |
| `requirements.txt` | Lists required Python packages |
| `README.md` | Project documentation |
| `Screenshots/` | Stores screenshots of the program |
| `gifs/` | Stores the demo GIF |
| `.env` | Local admin password configuration; not tracked by Git |
| `tasks.txt` | Local task data; not tracked by Git |

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3
- `pip`
- `python-dotenv` (if listed in `requirements.txt`)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/a-h-ourghali/personal_task_manager.git
```

### 2. Open the project folder

```bash
cd personal_task_manager
```

### 3. Check your Python version

```bash
python --version
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

The project uses a `.env` file to store the Admin Mode password outside the Python source code.

### 1. Create `.env` from `.env.example`

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

On Linux or macOS:

```bash
cp .env.example .env
```

### 2. Set a test password

Open `.env` and configure the variable:

```dotenv
TASK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own test password.

> ⚠️ Never commit `.env` or share your real password. Keep `.env.example` in the repository without any real secrets.

---

## ▶️ Usage

### 1. Run the program

```bash
python main.py
```

### 2. Follow the prompts

1. Choose `yes` or `no` for Admin Mode.
2. If you choose `yes`, enter your configured admin password.
3. Enter your name.
4. Add tasks one by one.
5. Choose a priority (`low`, `medium`, or `high`) when prompted.
6. Type `done` when you finish entering tasks.
7. Review the displayed task list.

Run the program again with the same name to load previously saved tasks.

---

## 💻 Example Output

The following is an illustrative example. Exact prompts may vary depending on the current program version.

```text
Do you want to enter Admin Mode? (yes/no): no

Name: Alex
Welcome Alex

Enter a task or type done: Finish homework
Enter priority (low/medium/high): high
Task added

Enter a task or type done: Practice Python
Enter priority (low/medium/high): medium
Task added

Enter a task or type done: done

Your tasks:
1. Finish homework [Priority: high]
2. Practice Python [Priority: medium]
```

---

## 📸 Screenshots

The screenshots below demonstrate the program's interface. Make sure the referenced image files exist in the `Screenshots/` folder.

### 🚀 Program Start

![Program Start](Screenshots/pic1.png)

### ✍️ Adding Tasks

![Adding Tasks](Screenshots/pic2.png)

### 📋 Task List

![Task List](Screenshots/pic3.png)

---

## 🎬 Demo

Watch the program in action:

![Personal Task Manager Demo](gifs/demo.gif)

---

## 🗺️ Roadmap

- [x] Add tasks through the terminal
- [x] Validate empty task input
- [x] Save tasks locally
- [x] Load saved tasks
- [x] Display tasks in a numbered list
- [x] Add Admin Mode
- [x] Load the admin password from `.env`
- [x] Add task priorities (`low`, `medium`, `high`)
- [ ] Add task completion status
- [ ] Add task editing and deletion

---

## 🤝 Contributing

Contributions and suggestions are welcome.

If you find a bug or have an idea for improving the project, feel free to open an issue or submit a pull request.

---

## 📜 License

License information will be added later.

---

## 👨‍💻 Author

**Amirhossein Sourghali**

[![GitHub](https://img.shields.io/badge/GitHub-a--h--ourghali-181717?logo=github)](https://github.com/a-h-ourghali)

[Visit my GitHub profile](https://github.com/a-h-ourghali)
