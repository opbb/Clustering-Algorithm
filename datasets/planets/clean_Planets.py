import csv

# A function to clean the data at the given file path and return it in list form.
def getCleanedData(file_name) -> [[float]]:
    # This list will hold all of the cleaned data, 
    # with any datapoints which lack a value having been removed.
    cleaned_data = []

    with open(file_name, "r") as planets:
        reader = csv.reader(planets)
        
        # Skips the first row with all the names of variables
        next(reader)
        
        for row in reader:
            # Adds the rowID here so we can avoid acidentally "cleaning" it
            cleaned_row = [row[0]]
            for value in row[1:]:
                if value == "":
                    # If a value is missing, we make rowID -1 as a flag then exit the loop
                    cleaned_row[0] = -1
                    break
                elif value.isalpha():
                    if value == "TRUE":
                        cleaned_row.append(1)
                    elif value == "FALSE":
                        cleaned_row.append(0)
                    else:
                        cleaned_row.append(ord(value) - 96.0)
                else:
                    cleaned_row.append(float(value))
            if (cleaned_row[0] != -1):
                cleaned_data.append(cleaned_row)
                
        return cleaned_data
    
