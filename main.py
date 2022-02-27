import k_means
import math
import datasets as ds
import test_k_means as test
import sys

def euclideanDist(point1, point2):
    diffSum = 0
    for i in range(len(point1)):
        diffSum += (point1[i] - point2[i]) ** 2
    return math.sqrt(diffSum)    


metric = lambda point1, point2: euclideanDist(point1, point2)

# File paths to CSV files from here:
planetsPath = "datasets/planets/Planets.csv"
coffeeAndCodePath = "datasets/coffee_and_code/Coffee_and_Code.csv"
foodPreferencePath = "datasets/food_preference/Food_Preference.csv"
bensDatasetPath = "datasets/bens_dataset/Bens_Dataset.csv"

if len(sys.argv) > 1:
    if sys.argv[1] == "-test":
        # This runs three simple tests on the algorithm and prints them to the 
        # console. These tests will have different results each time depending on 
        # the random starting points chosen by the algoritm.
        
        # Ground Truth Clusters(n = 3):  [A,B], [C,D], [E]
        testData0 = [["A",-10,0, 10],["B",-10,1, 9],["C",8,9,9],["D",7,8,7],
                     ["E", 15, -5,-19]]
        expectedClust0 = [["A", "B"], ["C", "D"], ["E"]]
        
        # Ground Truth Clusters(n = 3): [A,B,C], [D], [E,F,G]
        testData1 = [["A",-4,5],["B",-3,5], ["C",-3.5, 5.5], ["D",0,0], ["E", 1,2], 
                     ["F",1.1,2.1],["G",1.4,1.4]]
        expectedClust1 = [["A", "B", "C"], ["D"], ["E", "F", "G"]]
        
        # Ground Truth Clusters(n = 2): [A,B,C,D], [E,F,G,H]
        testData2 = [["A",10,3],["B",11,4],["C",13,2],["D",12.4,3.3],
                     ["E",-10,-10],["F",-11,-13],["G",-9,-9],["H",-8,-14]]
        expectedClust2 = [["A","B","C","D"], ["E","F","G","H"]]
        
        
        test.runTest(0, expectedClust0, testData0, metric, 3)
        
        test.runTest(1, expectedClust1, testData1, metric, 3)
        
        test.runTest(2, expectedClust2, testData2, metric, 2)
    elif sys.argv[1] == "-components":
        # Principle Components of each cleand dataset visualized:
        print("\nPlanets Principle Components:")
        ds.visualizePrincipleComponents(ds.getPlData(planetsPath))
        print("\nCoffee and Code Principle Components:")
        ds.visualizePrincipleComponents(ds.getCaCData(coffeeAndCodePath))
        print("\nFood Preference Principle Components:")
        ds.visualizePrincipleComponents(ds.getFPData(foodPreferencePath))
        if (ds.getBensData(bensDatasetPath) != None):
            print("\nBen's Dataset Principle Components:")
            ds.visualizePrincipleComponents(ds.getBensData(bensDatasetPath))
                
    elif len(sys.argv) > 4 and sys.argv[1] == "-run":
        datasetName = sys.argv[2]
        numComponents = int(sys.argv[3])
        numClusters = int(sys.argv[4])
        
        if datasetName == "planets":
            cleaned_data = ds.getCleanedPlData(planetsPath, numComponents)
        elif datasetName == "coffee_and_code":
            cleaned_data = ds.getCleanedCaCData(coffeeAndCodePath, numComponents)
        elif datasetName == "food_preference":
            cleaned_data = ds.getCleanedFPData(foodPreferencePath, numComponents)
        elif datasetName == "bens_dataset":
            cleaned_data = ds.getCleanedBensData(bensDatasetPath, numComponents)
        else:
            print("Invalid dataset name, valid names are \"planets\"," + 
            "\"coffee_and_code\", \"food_preference\" and \"bens_dataset\"")
            cleaned_data = None
        
        if cleaned_data != None:
            clusters = k_means.execute(numClusters, cleaned_data, metric)
            
            
            outString = "Clusters:\n"
            for i in range(len(clusters)):
                outString += "Cluster " + str(i) + ":\n"
                outString += str(clusters[i]) + "\n"
            
            with open("output.txt", "w") as outFile:
                outFile.write(outString)
                
            print("Results written into output.txt")