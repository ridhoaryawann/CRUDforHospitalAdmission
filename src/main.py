from tabulate import tabulate
from function_group import *
from data_group import db

def password():
    print ("Welcome to Hospital Database")
    while True:
        passw = input("Please enter your Password: ")
        if passw == '123AbC':
            return print ('Welcome to hospital database')
        else:
            print ('Please Input the right password')

def main_menu():
    while True:
        print ("Hospital Database Menu\nChoose the following menu to continue:\n1.Create New Patient Data\n2.Edit Patient Data\n3.Delete Patient Data\n4.Read Patient Data\n5.Analyze Patient Condition\n6.Exit Database")
        try:
            select = int(input("Please input the number to continue:"))
        except ValueError:
            print ("Please input only the NUMBER of the feature you want to select")
        else:
            if select == 1:
                print ("Create New Patient Data")
                create()
                break
            elif select == 2:
                print ("Edit Patient Data")
                update()
                break
            elif select == 3:
                print ("Delete Patient Data")
                delete()
                break
            elif select == 4:
                print ("Read Patient Data ")
                readpt()
                break
            elif select == 5:
                print ("Analyze Patient Condition")
                analyze()
                break
            elif select == 6:
                print ("Thanks, Good Bye!")
                break
            else:
                print ("Please input the right NUMBER of the feature you want to select")

def search_key():
    global db
    inputkey = input('Please input the patient key: ')
    for patient in db:
        if patient[2] == inputkey:
            print("Patient Found.")
            return patient
    print("Patient not found.")
    return None

def readpt():
    global db
    
    while True:
        choices = backtomenu()
        if choices == 1:
            print("Read Options:")
            print("1. Read all patients")
            print("2. Read only female patients")
            print("3. Read only male patients")
            print("4. Read patients with high body temperature>38")
            print("5. Read patients with diabetes")
            print("6. Read patients without diabetes")
            print("7. Read patients with hypertension")
            print("8. Read patients without hypertension")
            print("9. Read only patient")
            
            option = input("Enter your choice: ")
            
            if option == '1':
                data = db
                criteria = 'all patients'
            elif option == '2':
                data = [patient for patient in db if patient[3] == 'F']
                criteria = 'female patients'
            elif option == '3':
                data = [patient for patient in db if patient[3] == 'M']
                criteria = 'male patients'
            elif option == '4':
                data = [patient for patient in db if patient[7] >= 38]
                criteria = 'patients with temperature >= 38'
            elif option == '5':
                data = [patient for patient in db if 'diabet' in patient[8]]
                criteria = 'patients with diabetes'
            elif option == '6':
                data = [patient for patient in db if 'no diabet' in patient[8]]
                criteria = 'patients without diabetes'
            elif option == '7':
                data = [patient for patient in db if 'hypert' in patient[9]]
                criteria = 'patients with hypertension'
            elif option == '8':
                data = [patient for patient in db if 'no hypert' in patient[9]]
                criteria = 'patients without hypertension'
            elif option == '9':
                key = input('Please input patient key:')
                data = [patient for patient in db if key in patient[2]]
                criteria = 'this individual'
            else:
                print("Invalid option.")
                return
            
            count = len(data)

            headers = ["First Name", "Last Name", "Key", "Sex", "Height", "Weight", "FOP", "Temperature", "Diabetes", "Hypertension"]
            print(f"Patient data for {criteria}:")
            print(tabulate(data, headers=headers, tablefmt="pretty"))

            print(f"Number of patients for {criteria}: {count}")

        elif choices == 2:
            main_menu()
            break  

        elif choices == 3:
            print("Exiting the program.")
            break  
    
def create():
    global db
    while True:
        choices = backtomenu()
        if choices == 1:
            print('If the patient do not have keys, input anything')
            existingpatient = search_key()
            if existingpatient:
                print("A patient with the same key already exists.")
                duplicate_choice = input("Do you want to duplicate the data? (Y/N): ")
                if duplicate_choice.upper() == 'Y':
                     data = list(existing_patient)
                else:
                    continue
            else:
                # First Name
                while True:
                    fname = create_fname()
                    fnamed = validate(fname)
                    if fnamed != 'back':
                        break 
                    print("Restarting from First Name...")
                # Last Name
                while True:
                    lname = create_lname()
                    lnamed = validate(lname)
                    if lnamed != 'back':
                        break  
                    print("Restarting from Last Name...")
                # Sex
                while True:
                    sex = create_sex()
                    sexed = validate(sex)
                    if sexed != 'back':
                        break  
                    print("Restarting from Sex...")
                # Height
                while True:
                    height = create_height()
                    heighted = validate(height)
                    if heighted != 'back':
                        break  
                    print("Restarting from Height...")
                # Weight
                while True:
                    weight = create_weight()
                    weighted = validate(weight)
                    if weighted != 'back':
                        break  
                    print("Restarting from Weight...")
                # FOP
                while True:
                    fop = create_fop()
                    foped = validate(fop)
                    if foped != 'back':
                        break 
                    print("Restarting from FOP...")
                # Temperature
                while True:
                    temp = create_temperature()
                    temped = validate(temp)
                    if temped != 'back':
                        break  
                    print("Restarting from Temperature...")
                # Diabetes
                while True:
                    diabet = create_diabetes()
                    diabeted = validate(diabet)
                    if diabeted != 'back':
                        break  
                    print("Restarting from Diabetes...")
                # Hypertension
                while True:
                    hypert = create_hypertension()
                    hyperted = validate(hypert)
                    if hyperted != 'back':
                        break  
                    print("Restarting from Hypertension...")
                # PrimaryKey
                key = fname[:2] + str(height[-1]) + lname[:2]

                data = [fname, lname, key, sex, height, weight, fop, temp, diabet, hypert]
                print(data)
                # save data
                datad = validate(data)
                if datad == 'back':
                    return create()
                else:
                    db.append(data)
                    print ('data succesfully saved')
                    print("Current Patient Data:")
                    read_all()

        elif choices == 2:
            main_menu()
            break  

        elif choices == 3:
            print("Exiting the program.")
            break

def update():
    global db
    
    print("Current Patient Data:")
    read_all() 

    while True:
        choices = backtomenu()
        if choices == 1:
            print("Current Patient Data:")
            read_all()    
            patientupdate = search_key()
            if patientupdate:
                while True:
                    key_input = input("Re-enter the key of the patient to confirm: ")
                    if key_input == patientupdate[2]:  
                        break
                    else:
                        print("Invalid primary key. Please enter the correct primary key.")

                while True:
                    print("Select the item to edit:")
                    print("1. First Name")
                    print("2. Last Name")
                    print("3. Sex")
                    print("4. Height")
                    print("5. Weight")
                    print("6. Form of Payment")
                    print("7. Temperature")
                    print("8. Diabetes Status")
                    print("9. Hypertension Status")
                    try:
                        choice = int(input("Enter your choice (1-9): "))
                        if 1 <= choice <= 9:
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 9.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                if choice == 1:
                    patientupdate[0] = create_fname()
                elif choice == 2:
                    patientupdate[1] = create_lname()
                elif choice == 3:
                    patientupdate[3] = create_sex()
                elif choice == 4:
                    patientupdate[4] = create_height()
                elif choice == 5:
                    patientupdate[5] = create_weight()
                elif choice == 6:
                    patientupdate[6] = create_fop()
                elif choice == 7:
                    patientupdate[7] = create_temperature()
                elif choice == 8:
                    patientupdate[8] = create_diabetes()
                elif choice == 9:
                    patientupdate[9] = create_hypertension()

                print("Patient data updated successfully.")

                print("Updated Patient Data:")
                read_all()
            else:
                print("Patient not found.")
                update()
        elif choices == 2:
            main_menu()
            break  

        elif choices == 3:
            print("Exiting the program.")
            break
                    
def delete():
    global db

    while True:
        choices = backtomenu()
        if choices == 1:
            print("Current Patient Data:")
            read_all()  
            patient = search_key()
            if patient:
                db.remove(patient)
                print("Patient data deleted successfully.")
                read_all()
            else:
                print("Patient not found.")
    
        elif choices == 2:
            main_menu()
            break  

        elif choices == 3:
            print("Exiting the program.")
            break
            
def analyze():
    global db
    
    while True:
        choices = backtomenu()
        if choices == 1:
            print("Current Patient Data:")
            read_all()  
            patient = search_key()
            if patient:
                score = 0
                if 'hypert' in patient[9]:
                    score += 2
                if 'diabet' in patient[8]:
                    score += 2
                if patient[7] >= 39:
                    score += 3
                
                if score >= 5:
                    category = "Critical"
                elif score == 3:
                    category = "Medium"
                else:
                    category = "Low"
                
                result = [[patient[0], patient[1], patient[2], category]]

                headers = ["First Name", "Last Name", "Key", "Category"]
                print(tabulate(result, headers=headers, tablefmt="pretty"))
            else:
                print("Patient not found.")
                
        elif choices == 2:
            main_menu()
            break  

        elif choices == 3:
            print("Exiting the program.")
            break

password()
main_menu()
