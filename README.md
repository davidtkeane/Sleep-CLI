# Sleep-CLI

Send your Macbook's to sleep over the network using SSH from the command line. Might work with Linux OS. (Might).

## Introduction

Welcome to the Sleep CLI Application! This command-line tool is designed to help you manage sleep-related tasks efficiently. Whether you need to schedule sleep, monitor sleep patterns, or set sleep reminders, this application provides a simple and intuitive interface to handle all your sleep management needs.

## Description 

The Sleep CLI Application allows you to automate and manage sleep-related tasks from the command line. It uses various system commands to interact with the operating system and provides a user-friendly interface for scheduling and monitoring sleep activities.

## Features

- **Schedule Sleep:** Set sleep schedules and reminders.
- **Monitor Sleep:** Track and monitor sleep patterns.
- **System Commands:** Execute necessary system commands with `subprocess`.
- **Cross-Platform:** Designed to run on Unix-based systems (Linux, macOS).

## Github 

[![Sleep CLI](https://img.shields.io/badge/Sleep-CLI-blue)](https://github.com/davidtkeane/Sleep-CLI)
[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue)](https://github.com/davidtkeane/PhoneBook-CLI)
[![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray)](https://github.com/davidtkeane/gmail-multi-cli)
[![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)](https://github.com/davidtkeane/gmail-multi-cli)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/Sleep-CLI?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/Sleep-CLI?authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/Sleep-CLI?style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/davidtkeane)

![Discord](https://img.shields.io/discord/815701213827301396)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green) 

## Prerequisites

- Python 3.x
- Unix-based system (Linux, macOS)
- `sudo` privileges

## Installation

Instructions for running the application:

## Phone.py

1. Run the application using the following command:

```bash
python sleep.py
```

## Phone Install:

## Installation to be able to run sleep_all in the terminal.

1. Download the file:

A: Use this command in the terminal.

```bash
git clone https://github.com/yourusername/Sleep-CLI/
```

B: Now enter into the Sleep-CLI folder and install the requirements.

```bash
cd Sleep-CLI
pip install requirements.txt
```

## Install using the usr-bin.sh script.

This will automatically copy sleep.ph to sleep_all file, then it will chmod sleep_all to make it executable and ready to be used after being sent to the /usr/local/bin folder. The process will ask you for your password to proceed.

```bash
bash usr-bin.sh 
```

## Install using commands.

2. After downloading the file, run the following command to make it executable:

```bash
chmod +x sleep
```

3. Copy or move the file to a directory in your PATH to run it from anywhere:

```bash
sudo cp phone /usr/local/bin/sleep
```
4. Run the application using the following command if not in the PATH:

```bash
./sleep
```
5. Run the application using the following command if in the PATH:

```bash
sleep
```

## Why sudo is needed:

The application requires sudo to run commands that need elevated privileges, such as creating directories and files in system-protected locations (e.g., bin). It also ensures that the password file and database file have the correct permissions to prevent unauthorized access.

<br>

## Screenshots:

<p>
    <img alt="PhoneBook CLI" src="https://img.shields.io/badge/Sleep-CLI-blue">
</p>
<br>

## License:

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgment:

Created by Ranger (Dec 2024) Version 1.0.0
Modified by David Keane (Dec 31st 2024) Version 2.0.1

Feel free to customize the content as needed.
