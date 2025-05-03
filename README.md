
# 🏥 Hospital Management System (Python Project)

A beginner-friendly **console-based CRUD application** to manage patient and doctor records, built in **Python** using the `pickle` module for binary file handling.

## ✨ Features
- 👤 Add Patient  
- 👨‍⚕️ Add Doctor  
- 📅 Book an Appointment  
- 🔍 View Patient Details  
- 📝 Update Patient Information  
- ❌ Remove Patient  
- 💾 Data stored in `.dat` files using `pickle`

## ⚙️ Technologies Used
- 🐍 Python 3.x  
- 🧃 `pickle` module  
- 💻 Python IDLE

## 🚀 How to Run
1. Clone this repository or download the ZIP  
2. Open `hospital.py` (or `project.py`) using **Python IDLE**  
3. Run the script (Press `F5` or click `Run → Run Module`)  
4. Use the menu to perform CRUD operations!

## 📁 Folder Structure
hospital-management-system/

├── project.py         # Main Python script
├── .gitignore        # Files to be ignored by Git
├── README.md         # Project documentation
....



## 🙈 .gitignore
```gitignore
# Ignore patient and doctor data files
*.dat

# Ignore Python cache files
__pycache__/
````
## 📌 Notes

* Patient and doctor data is saved in binary format using `.dat` files
* If you delete the `.dat` files, all stored data will be lost
* No third-party libraries required — runs on core Python


