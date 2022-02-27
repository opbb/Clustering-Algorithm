import csv

def getCleanedData(file_name):
    # We are going to define dictionaries to hold the number values for string
    # responses like "Coffee type".
    
    coffeeTimeDict = {"Before coding" : -1.0,
                      "Before and while coding" : 0.0,
                      "While coding" : 1.0,
                      "In the morning" : -2.0,
                      "All the time" : 0.0,
                      "After coding" : 2.0,
                      "No specific time" : 0.0}
    
    yesMaybeNoDict = {"Yes" : 1.0,
                      "Sometimes" : 0.0,
                      "No" : -1.0}
    
    # I grouped these different coffees together based on whether they were
    # brewed or instant, whether they were espresso based or not, and whether 
    # they used milk or not.
    coffeeTypeDict = {"NA" : -1.0,
                      "Nescafe" : 0.0,
                      "American Coffee" : 1.0,
                      "Turkish" : 1.0,
                      "Americano" : 2.0,
                      "Espresso (Short Black)" : 2.0,
                      "Double Espresso (Doppio)" : 2.0,
                      "CaffÃ¨ latte" : 3.0,
                      "Cappuccino" : 3.0}
    
    # Everyone in this dataset conforms to the M/F binary, but this dict could
    # be updated if new datapoints that we non-binary were added.
    genderDict = {"Female" : -1.0,
                  "Male" : 1.0}
    
    # I collapse the age ranges below down to their middle point. For NA and
    # under 18 I guess at a realistic middle point, as infant's (to my knowledge)
    # can't code.
    ageRangeDict = {"NA" : 25.0,
                    "Under 18" : 15.0,
                    "18 to 29" : 23.5,
                    "30 to 39" : 34.5,
                    "40 to 49" : 44.5,
                    "50 to 59" : 54.5}
    
    # This dict will tell what dict represents what column index.
    columnDict = {2 : coffeeTimeDict,
                  3 : yesMaybeNoDict,
                  4 : coffeeTypeDict,
                  5 : yesMaybeNoDict,
                  6 : genderDict,
                  8 : ageRangeDict}
    
    # This list will hold all of the cleaned data.
    cleaned_data = []    

    with open(file_name, "r") as file:      
        
        reader = csv.reader(file)
        
        # Skips the first row with all the names of variables
        next(reader)
        
        # The ID number to assign to each row, will be incremented.
        rowID = 0          
        
        for row in reader:
            cleaned_row = [rowID]
            rowID += 1
            for i in range(9):
                value = row[i]
                
                # The first two columns are numbers that don't need to be cleaned.
                if i == 0 or i == 1:
                    cleaned_row.append(float(value))
                # We're throwing away country data because it's all the same.
                elif i == 7:
                    continue
                # We use the column dict to interpret the value of the data.
                else:
                    cleaned_row.append(columnDict[i][value])
                
            cleaned_data.append(cleaned_row)
        
    return cleaned_data