import k_means
import math

# The jaccard index of 2 sets.
def jaccardIndex(set1: set, set2: set) -> float:
    return len(set1.intersection(set2)) / len(set1.union(set2))

# Returns a set of sets of 2 clusters each. Predicts which clusters go together
# by grouping the two with the highest Jaccard Index.
def predClustAssociation(clust1: [[]], clust2: [[]]) -> [[[]]]:
    predClustAssociations = []
    for cluster in clust1:
        biggestIndex = 0.0
        biggestClust = None
        for other in clust2:
            if biggestClust == None or jaccardIndex(set(cluster), set(other)) > biggestIndex:
                biggestIndex = jaccardIndex(set(cluster), set(other))
                biggestClust = other
        
        predClustAssociations.append([cluster, biggestClust])
        
    return predClustAssociations

# Converts a list of lists into a set of frozensets.
def list2dToSet(list2d: [[]]) -> (()):
    retSet = set()
    for l in list2d:
        retSet.add(frozenset(l))
    return retSet

# Runs the given data through the algorithm, then compares it to the given
# expected clusters and prints the results.
def runTest(testNum: int, expectedClusters: [[]], data: [[]], metric, clustNum: int):
    print("-Test number " + str(testNum) + "-\nExpected Clusters: " + 
          str(expectedClusters))
    
    actualClusters = k_means.execute(clustNum, data, metric)
    print("Actual Clusters: " + str(actualClusters))
    
    print("Jaccard Index: " + str(jaccardIndex(list2dToSet(expectedClusters), 
                                               list2dToSet(actualClusters))))
    
    print("Individual Cluster Jaccard Indexes:")
    predAssoc = predClustAssociation(expectedClusters, actualClusters)
    jISum = 0
    for pair in predAssoc:
        ji = jaccardIndex(set(pair[0]), set(pair[1]))
        jISum += ji
        print(str(pair[0]) + " -> " + str(pair[1]) + " Jaccard Index: " +
              str(ji))  
    print("Average Individual Jaccard Index: " + str(jISum / len(predAssoc)) + "\n\n")