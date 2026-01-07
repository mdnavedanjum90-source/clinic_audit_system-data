import uuid

#Function to validate age
def age_validate(age):
    if not age.isdigit():
        return False,"Invalid Age"
    
    age = int(age)
    if(age<0 or age>120):
        return False,"Invalid Age"
    
    return True,age

#Function to validate Heart rate
def validate_Heart_Rate(rate):
    if not rate.isdigit():
        return False,None
    
    rate = int(rate)
    return True,rate

#Recursive function to take heart rate readings

def take_readings(n, warnings, flags):
    if n == 0:
        return
    rate_input = input(f"Enter heart rate reading: ")
    valid,rate = validate_Heart_Rate(rate_input)
    
    if not valid:
        flags.append("Invalid heart rate input")
    else:
        if rate > 180:
            warnings.append("High heart rate detected")
            
    take_readings(n-1, warnings, flags) 
     
     
# Main Program

def clinical_audit():
    print("---Clinical Data Audit System---\n")              

    audit_id = uuid.uuid4()
    patient_name = input("Enter patient name: ")
    age_input = input("Enter age: ")
    reading_count = input("Enter number of heart readings: ")
    
    flags = []
    warnings = []
    
    
    #Validate age
    valid_age, age_remark = age_validate(age_input)
    if not valid_age:
        flags.append(age_remark)
        
        
   #Validate number of readings
    if not reading_count.isdigit():
       flags.append("Invalid number of readings")
    else:
        reading_count = int(reading_count)
        take_readings(reading_count, warnings, flags) 
        
        
        
     #Final Audit Status
    if flags:
         status = "FAIL" 
    elif warnings:
        status = "REVIEW" 
    else:
        status = "PASS"     
        
        
    #Output
    
    print(" ---CLINICAL AUDIT RESULT---")
    print(f"Audit ID : {audit_id}")
    print(f"Patient : {patient_name}")
    print(f"Status : {status}")
    print(f"Flags : {flags if flags else None}")
    print(f"Warnings : {warnings if warnings else None}")
    
#Run program by function use
clinical_audit()
