from tabulate import tabulate
from function_group import *
from data_group import db

###########################Dev per Variable###########################

def validate(val):
    while True:
        decision = input(f"Do you want to add '{val}' to this data? Y/N ")
        if decision.upper() == 'Y':
            return val
            break
        elif decision.upper() == 'N':
            print ('getting back to the last menu...')
            return 'back'
        else:
            print ('Please only input Y for continue and N for back to the last menu')

def create_fname():
    while True:
        f_name = input("Please input the first name of the patient:")
        if f_name.isalpha() == True:
            # fname.append({f_name})
            break
        else:
            print ('Please fill the blank with alphabet')
            continue
    return f_name.upper()

def create_lname():
    while True:
        l_name = input("Please input the last name of the patient:")
        if l_name.isalpha() == True:
            break
        else:
            print ('Please fill the blank with alphabet')
            continue
    return l_name.upper()

def create_sex():
    while True:
        sexs = input("Please input the sex of the patient (M/F): ")
        if sexs.upper() == 'M': 
            break
        elif sexs.upper() == 'F': 
            break
        else:
            print ('Please only input M for male or F for female')
    return sexs

def create_height():
    while True:
        heights = (input("Please input the height of the patient in cm:"))
        try:
            heighto = int(heights)
        except ValueError:
            print ('Please only input NUMBERS for the height')
        else:
            if len(heights)<3 or heighto>300:
                print ('Please input the right NUMBERS of the patients height')
            else:
                break
    return heights
          
def create_weight():   
    while True:
        weights = input("Please input the weight of the patient in kg:")
        try:
            weighta = int(weights)
        except ValueError:
            print ('Please only input NUMBERS for the weight')
        else:
            if weighta==0 or len(weights)>4:
                print ('Please input the right NUMBERS of the patient weight')
            else:
                break
    return weights

def create_fop():
    while True:
        formofpayment = input("Please input the form of payment of the patient with BPJS/INSURANCE/PRIVATE:")
        if formofpayment.upper() == 'BPJS': 
            return ('BPJS')
            break
        elif formofpayment.upper() == 'INSURANCE': 
            return ('INSURANCE')
            break
        elif formofpayment.upper() == 'PRIVATE': 
            return ('PRIVATE')
            break
        else:
            print ('Please only input BPJS or Insurance or Private ')

def create_temperature():
    while True:
        temperature = (input("Please input the temperature of the patient in celcius:"))
        try:
            temps = int(temperature)
        except ValueError:
            print ('Please only input NUMBERS for the temperatures')
        else:
            if temps > 46 or temps < 13:
                print ('This number is either too high or too low. Please input the thrue temperatures of the patient.')
            else:
                return temperature
                break

def create_diabetes():
    while True:
        diabetes = input("Does the patient have diabetes? (Y/N): ")
        if diabetes.upper() == 'Y': 
            return ('diabet')
            break
        elif diabetes.upper() == 'N': 
            return ('no diabet')
            break
        else:
            print ('Please only input Y for diabetes patient or N for non-diabetes patient')

def create_hypertension(): 
    while True:
        hypert = input("Does the patient have hypertension? (Y/N): ")
        if hypert.upper() == 'Y': 
            return('hypert')
            break
        elif hypert.upper() == 'N': 
            return('no hypert')
            break
        else:
            print ('Please only input Y for hypertension patient or N for non-hypertension patient')

def read_all():
        global db
        data = []
        for item, patient in enumerate(db, start=1):
            data.append([item] + patient)

        headers = [ "First Name", "Last Name","Key","Sex", "Height", "Weight", "FOP", "Temperature", "Diabetes", "Hypertension"]
        print(tabulate(data, headers=headers, tablefmt="pretty"))

def backtomenu():
    while True:
        print("\nSelect what to do:")
        print("1. Continue to the feature you have been selected")
        print("2. Go back to main menu")
        print("3. Exit the program")
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


