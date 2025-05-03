import pickle
import os

# Method to add a patient
def addPatient():
    with open("patient.dat", "ab") as file:
        pid = input("\n\tEnter Patient ID: ")
        name = input("\tEnter Patient Name: ")
        add = input("\tEnter Patient Address: ")
        age = input("\tEnter Patient Age: ")
        dis = input("\tEnter Patient Disease: ")
        pickle.dump((pid, name, add, age, dis), file)
        print("\n\t--- Patient Added Successfully! ---")
    input("\n\t----- Press Enter To Continue -----")

# Method to add a doctor
def addDoctor():
    with open("doctor.dat", "ab") as file:
        did = input("\n\tEnter Doctor ID: ")
        name = input("\tEnter Doctor Name: ")
        spec = input("\tEnter Doctor Specialization: ")
        pickle.dump((did, name, spec), file)
        print("\n\t---- Doctor Added Successfully! ----")
    input("\n\t----- Press Enter To Continue -----")

# Method to get patient details
def getPatient(pid):
    try:
        with open("patient.dat", "rb") as file:
            while True:
                data = pickle.load(file)
                if data[0] == pid:
                    return data
    except (EOFError, FileNotFoundError):
        return None

# Method to get doctor details
def getDoctor(did):
    try:
        with open("doctor.dat", "rb") as file:
            while True:
                data = pickle.load(file)
                if data[0] == did:
                    return data
    except (EOFError, FileNotFoundError):
        return None

# Method to book an appointment
def bookApp():
    pid = input("\n\tEnter Patient ID: ")
    pat = getPatient(pid)
    if pat:
        print("\n\tPatient Name:", pat[1])
        print("\tPatient Age:", pat[3])
        print("\tPatient Disease:", pat[4])
        
        did = input("\n\tEnter Doctor ID: ")
        doc = getDoctor(did)
        if doc:
            print("\n\tDoctor Name:", doc[1])
            print("\tDoctor Specialization:", doc[2])
            date = input("\tEnter Appointment Date (YYYY/MM/DD): ")
            print("\n\tAppointment Booked!")
        else:
            print("\n\tDoctor Not Found!")
    else:
        print("\n\tPatient Not Found!")
    input("\n\t----- Press Enter To Continue -----")

# Method to view patient details
def viewPatient():
    pid = input("\n\tEnter Patient ID: ")
    pat = getPatient(pid)
    if pat:
        print("\n\t--- Patient Details ---")
        print("\tPatient ID:", pat[0])
        print("\tName:", pat[1])
        print("\tAddress:", pat[2])
        print("\tAge:", pat[3])
        print("\tDisease:", pat[4])
    else:
        print("\n\tPatient Not Found!")
    input("\n\t----- Press Enter To Continue -----")

# Method to remove a patient
def removePatient():
    pid = input("\n\tEnter Patient ID to Remove: ")
    patients = []
    found = False

    try:
        with open("patient.dat", "rb") as file:
            while True:
                try:
                    data = pickle.load(file)
                    if data[0] != pid:
                        patients.append(data)
                    else:
                        found = True
                except EOFError:
                    break

        if found:
            with open("patient.dat", "wb") as file:
                for patient in patients:
                    pickle.dump(patient, file)
            print("\n\t--- Patient Removed Successfully! ---")
        else:
            print("\n\tPatient Not Found!")
    except FileNotFoundError:
        print("\n\tNo patient records found!")
    
    input("\n\t----- Press Enter To Continue -----")

# Method to update patient details
def updatePatient():
    pid = input("\n\tEnter Patient ID to Update: ")
    patients = []
    found = False

    try:
        with open("patient.dat", "rb") as file:
            while True:
                try:
                    data = pickle.load(file)
                    if data[0] == pid:
                        print("\n\t--- Updating Patient Details ---")
                        name = input("\tEnter New Name (leave blank to keep unchanged): ") or data[1]
                        add = input("\tEnter New Address (leave blank to keep unchanged): ") or data[2]
                        age = input("\tEnter New Age (leave blank to keep unchanged): ") or data[3]
                        dis = input("\tEnter New Disease (leave blank to keep unchanged): ") or data[4]
                        patients.append((pid, name, add, age, dis))
                        found = True
                    else:
                        patients.append(data)
                except EOFError:
                    break

        if found:
            with open("patient.dat", "wb") as file:
                for patient in patients:
                    pickle.dump(patient, file)
            print("\n\t--- Patient Updated Successfully! ---")
        else:
            print("\n\tPatient Not Found!")
    except FileNotFoundError:
        print("\n\tNo patient records found!")
    
    input("\n\t----- Press Enter To Continue -----")

# Dashboard
while True:
    print("\n\t******* HOSPITAL MANAGEMENT SYSTEM ********")
    print("\n\t1. Add Patient")
    print("\t2. Add Doctor")
    print("\t3. Book an Appointment")
    print("\t4. View Patient")
    print("\t5. Remove Patient")
    print("\t6. Update Patient")
    print("\t7. Exit")

    try:
        ch = int(input("\n\tEnter Choice: "))
        if ch == 7:
            print("\n\t---- BYE-BYE ADMIN! ----")
            break
        elif ch == 1:
            addPatient()
        elif ch == 2:
            addDoctor()
        elif ch == 3:
            bookApp()
        elif ch == 4:
            viewPatient()
        elif ch == 5:
            removePatient()
        elif ch == 6:
            updatePatient()
        else:
            print("\n\tInvalid Choice! Please try again.")
    except ValueError:
        print("\n\tInvalid Input! Please enter a number.")
