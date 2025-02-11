
# Python Scripting & API Integration Training

## Objective  
This repository is designed to train a team in **Python scripting and API integration**, focusing on practical, hands-on learning. The key goals include:  

- **Python Scripting** – Writing automation scripts, working with files, and executing system commands.
- **API Integration** – Fetching, sending, and handling data through APIs using Python.
- **Linux Workflow** – Running and automating Python scripts on Linux using cron jobs.

---

## 1. Python Scripting Basics  
Python scripting is used to **automate repetitive tasks, process data, and interact with system files**.  

### **Setting Up Python on Linux:**  
1. **Check if Python is Installed:**  
   ```bash
   python3 --version
   ```  
   If Python is not installed, install it:  
   ```bash
   sudo apt update && sudo apt install python3 python3-pip -y  # Ubuntu/Debian  
   sudo dnf install python3 python3-pip -y  # Fedora  
   ```

2. **Create and Run a Simple Python Script:**  
   ```python
   print("Hello, this is my first Python script!")
   ```  
   Save as `script.py` and run:
   ```bash
   python3 script.py
   ```

---

## 2. API Integration Using Python  
APIs allow Python scripts to **interact with external services like databases, web applications, and cloud platforms**.  

### **Installing Required Library:**  
```bash
pip install requests
```

### **Making a Simple API Request:**  
```python
import requests  

API_URL = "https://jsonplaceholder.typicode.com/todos/1"  

response = requests.get(API_URL)  

if response.status_code == 200:  
    data = response.json()  
    print("API Response:", data)  
else:  
    print("Failed to fetch data:", response.status_code)
```

### **Example API Response:**  
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

### **Extracting and Using API Data in Python:**  
```python
print(f"Task Title: {data['title']}")
print(f"Completed: {'Yes' if data['completed'] else 'No'}")
```

**Expected Output:**  
```
Task Title: delectus aut autem
Completed: No
```

---

## 3. Running and Automating Python Scripts on Linux  
### **Making the Script Executable:**  
1. Add a shebang at the top of the script:
   ```python
   print("This script is now executable!")
   ```
2. Change permissions to make it executable:  
   ```bash
   chmod +x script.py
   ```
3. Run it directly:  
   ```bash
   ./script.py
   ```

### **Automating Python Scripts with Cron Jobs:**  
To run a Python script automatically on Linux, schedule it using **cron jobs**.

1. Open the crontab editor:  
   ```bash
   crontab -e
   ```
2. Add a cron job to run the script every day at 12 AM:  
   ```bash
   0 0 * * * /usr/bin/python3 /home/user/script.py >> /home/user/log.txt 2>&1
   ```
3. Save and exit (`CTRL + X`, then `Y`, then `Enter`).  

To **check scheduled jobs**, run:  
```bash
crontab -l
```

---

## Final Summary  
| Topic | What You Will Learn |
|--------|--------------------|
| **Python Scripting** | Writing automation scripts, handling files, and executing commands. |
| **API Integration** | Sending & receiving data using REST APIs in Python. |
| **Linux Execution** | Running, automating, and scheduling scripts using cron jobs. |

This **training program** will help the team **become proficient in Python scripting and API integration on Linux**. 🚀

