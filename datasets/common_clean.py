from .planets import getCleanedData as pData
from .coffee_and_code import getCleanedData as cacData
from .food_preference import getCleanedData as fpData
from .bens_dataset import getCleanedData as bData
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
import numpy as np
import math

# Puts the data into a dataframe then centers, scales and PCA's it, the returns it
# as a list of list of floats.
def commonClean(data: [[float]], pcaDim: int) -> [[float]]:
    dataCopy = []
    for i in range(len(data)):
        dataCopy.append([])
        for j in range(1, len(data[0])):
            dataCopy[i].append(data[i][j])
    scaled_data = pd.DataFrame(centerAndScale(dataCopy))    
    pca = PCA(n_components = pcaDim)
    pca.fit(scaled_data)
    pca_data = pca.transform(scaled_data)
    ret = pca_data.tolist()
    # Adds all of the datapoint IDs back in.
    for i in range(len(pca_data)):
        ret[i].insert(0, data[i][0])
        
    return ret

# Centers and scales the data to preprocess it before PCA.
def centerAndScale(data: [[float]]) -> [[float]]:
    sums = []
    for i in range(len(data[0])):
        sums.append(0)
        
    for i in range(len(data)):
        for j in range(len(data[0])):
            sums[j] += data[i][j]
        
    for i in range(len(sums)):
        sums[i] /= len(data)
        
    means = sums
    sums = []
    for i in range(len(data[0])):
        sums.append(0)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            sums[j] += abs(data[i][j] - means[j])
    
    for i in range(len(sums)):
        sums[i] /= len(data)
        sums[i] = math.sqrt(sums[i])
    stdDev = sums
    
    # Make a new list so as not to mutate old data.
    scaledData = []
    for i in range(len(data)):
        scaledData.append([])
        for j in range(len(data[0])):
            scaledData[i].append(0)
        
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (stdDev[j] == 0):
                scaledData[i][j] = 0.0
            else:
                scaledData[i][j] = (data[i][j] - means[j]) / stdDev[j]
            
    return scaledData

# This is my attempt at writing a PCA function. 
#def commonClean(data: [[float]], pcaDim: int) -> [[float]]:
    #IDs = []
    #data = data.copy() # Copy data so we can mutate it.
    #for i in range(len(data)):
        #IDs.append(data[i][0])
        #del data[i][0]
    
    #scaled_data = np.asarray(centerAndScale(data))
    #covMatrix = np.cov(scaled_data, rowvar=False)
    #eigenValues, eigenVectors = np.linalg.eig(covMatrix)
    
    #components = []
    #compToVector = {}
    #for i in range(len(eigenValues)):
        #compToVector[eigenValues[i]] = eigenVectors[i]
    #eigenValues.tolist().sort(reverse=True)
    #relevantVectors = []
    #for i in range(pcaDim):
        #relevantVectors.append(compToVector[eigenValues[i]])
    #relevantVectors = np.asarray(relevantVectors)
    
    #ret = np.dot(relevantVectors, scaled_data.transpose()).transpose()
    #ret = ret.tolist()
    
    #for i in range(len(ret)):
        #ret[i].insert(0, IDs[i])
    
    #return ret
    
def visualizePrincipleComponents(data: [[float]]):
    data = data.copy() # Copy data so we can mutate it.
    for i in range(len(data)):
        del data[i][0]
    
    scaled_data = np.asarray(centerAndScale(data))
    covMatrix = np.cov(scaled_data.T)
    eigenValues, eigenVectors = np.linalg.eig(covMatrix)
    
    components = []
    for i in range(len(eigenValues)):
        components.append(eigenValues[i] / np.sum(eigenValues))    
    components.sort(reverse=True)
    
    return components

def getCleanedPlData(file_name: str, pcaDim: int) -> [[float]]:
    data = pData(file_name)
    return commonClean(data, pcaDim)

def getCleanedCaCData(file_name: str, pcaDim: int) -> [[float]]:
    data = cacData(file_name)
    return commonClean(data, pcaDim)    

def getCleanedFPData(file_name: str, pcaDim: int) -> [[float]]:
    data = fpData(file_name)
    return commonClean(data, pcaDim)

def getCleanedBensData(file_name: str, pcaDim: int) -> [[float]]:
    data = bData(file_name)
    return commonClean(data, pcaDim)    

