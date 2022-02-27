import csv

def getCleanedData(file_name):
    
    # We are going to define dictionaries to hold the number values for string
    # responses.
    
    foodDict = {"Traditional food" : 0.0,
                "Western Food" : 1.0}
    
    juiceDict = {"Fresh Juice" : 0.0,
                 "Carbonated drinks" : 1.0}
    
    dessertDict = {"Yes" : 1.0,
                   "Maybe" : 0.0,
                   "No" : -1.0}
    
    columnsDict = {5 : foodDict,
                   6 : juiceDict,
                   7 : dessertDict}
    
    # This list will hold all of the cleaned data.
    cleaned_data = []    
    
    with open(file_name, "r") as file:      
        
        reader = csv.reader(file)
        
        # Skips the first row with all the names of variables
        next(reader)       
        
        for row in reader:
            cleaned_row = [row[1]]
            for i in range(5,8):
                cleaned_row.append(columnsDict[i][row[i]])
            cleaned_data.append(cleaned_row)
            
    return cleaned_data