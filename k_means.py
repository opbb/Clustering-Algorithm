import random

# This module contains my implementation of the k-means algorithm and any 
# additional helper methods I wrote for it. 

#==============================================================================

# HELPER METHODS:



# Creates a dictionary of k cluster centers, with the key being the identifier of the
# randomly picked datapoint, and the value being the datapoint itself.
def initCenters(k: int, data: [[]], clusterCenters: {int: []}):
    for datapoint in random.sample(data, k):
        clusterCenters[datapoint[0]] = datapoint



# Groups all the datapoints into clusters based off of the closest center.
def clusterData(clusters: {int: [[]]}, centers: {int : []}, data: [[]], metric):
    # Ensures that clusters contains all of the centers mapped to empty lists
    for centerID in centers.keys():
        clusters[centerID] = []
    # Loops through each datapoint and assigns it to the closest center
    for datapoint in data:
        nearestCenter = None
        distance = None
        for center in centers.values():
            if distance == None:
                nearestCenter = center
                distance = metric(datapoint, center)
            elif distance > metric(datapoint, center):
                nearestCenter = center
                distance = metric(datapoint, center)
        clusters[nearestCenter[0]].append(datapoint)    
        
        
        
# Averages the data from every point in a cluster, and makes that a new center.
def generateCenters(clusters: {int: [[]]}, centers: {int: []}):
    clusterID = -1 # Identifier is negative to signal that this isn't a datapoint.
    for cluster in clusters.values():
        dataSum = None
        # Sum together all the values in the cluster.
        for datapoint in cluster:
            if dataSum == None:
                dataSum = datapoint.copy()
            else:
                for i in range(1, len(datapoint)):
                    dataSum[i] += datapoint[i]
                    
        # Divide every sum by the number of datapoints.
        for i in range(1,len(dataSum)):
            dataSum[i] /= len(cluster)
        
        # Adds an entry in centers with the new center
        dataSum[0] = clusterID
        centers[clusterID] = dataSum
        clusterID -= 1

#==============================================================================

# This function executes the k-means algorithm with _k_ clusters, using the 
# given 2D list of datapoints _data_, using the given distance metric _metric_.
# Signature: int, double[][] function -> double[][]
#------------------------------------------------------------------------------
# INVARIANTS:
# The int which is passed in must be >= 1
#
# The double[][] which is passed in must be rectangular (all sub-lists are of
# the same size). Each sub-list represents a data point, and must begin with an 
# identifier (probably an integer) which will not be used to calculate distance.
#
# The distance metric function should have the following signature and should
# not take in the identifiers,
# Metric signature: double[] double[] -> double
#------------------------------------------------------------------------------
# RETURNS:
# The double[][] which is returned will be a set where each sub-set 
# represents a cluster, and the fields of the sub-sets are the 
# datapoint-identifiers of each datapoint in said cluster.
#------------------------------------------------------------------------------
def execute(k: int, data: [[]], m) -> [[int]]:
    # Checks that the k is valid.
    if k > len(data):
        raise IndexError("Must have fewer clusters than datapoints.")
    
    # Adjusts the metric to account for the indicator data in each datapoint.
    metric = lambda point1, point2: m(point1[1:], point2[1:])
    
    # Assigns the first k datapoints to be the centers 
    # for the first clusters.   
    clusters = {}
    clusterCenters = {}
    initCenters(k, data, clusterCenters)
    
    # Records the previous centers so we can see if anything has changed.
    prevCenters = {}
        
    while(prevCenters != clusterCenters):
        prevCenters = clusterCenters.copy()
        clusters.clear()
        clusterCenters.clear()
        
        # Adds every datapoint in the dataset to the cluster 
        # of the nearest center.
        clusterData(clusters, prevCenters, data, metric)
        
        # Averages each cluster and makes that the new center.
        generateCenters(clusters,clusterCenters)
        
    ret = []
    for clusterID in clusters.keys():
        clusterRet = []
        for datapoint in clusters[clusterID]:
            clusterRet.append(datapoint[0])
        ret.append(clusterRet)
    
    return ret
    
#==============================================================================

