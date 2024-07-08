##TASK 3: PASSWARD GENERATOR:
import random  ## Importing the random module for generating random characters
import string  ## Importing the string module for accessing ASCII characters

while True:
    length = int(input("Enter the desired length of the password: "))          ## Asks the user for the password length
    complexity = input("Enter the desired complexity (low, medium, high): ")  
    

    if complexity == "low":                     ## Checking if the user chose low complexity
        characters = string.ascii_letters       ## Uses only ASCII letters
        
    elif complexity == "medium":                                   ## Checks if the user chose medium complexity
        characters = string.ascii_letters + string.digits          ## Uses ASCII letters and digits
   
    else:                                                                       ## If the user chose high complexity
        characters = string.ascii_letters + string.digits + string.punctuation  ## Uses ASCII letters, digits, and punctuation

## Generates a password of the specified length and complexity
    password = ''.join(random.choice(characters) for _ in range(length))  
    print("Generated Password: ", password)      
    
    
## Asks the user if they want to generate another password
    choice = input("Enter 'end' to stop generating passwords, or press enter to generate another: ")  
    if choice.lower() == "end":  
        break                       ## Exits the loop if the user chose to stop generating passwords