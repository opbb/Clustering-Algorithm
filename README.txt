I implemented the k-means clustering algorithm. The datasets I used are as follows:

-Kepler Confirmed Planets, https://www.kaggle.com/muhakabartay/markmarkohkeplerconfirmedplanets
-Coffee and code dataset, https://www.kaggle.com/shrutikunapuli/coffee-and-code-dataset
-Food Preferences, https://www.kaggle.com/vijayashreer/food-preferences

The paths to these datasets are hardcoded into my program at the top of the main.py
file.


How to use my program:

Run the program from the terminal as shown: py main.py -run [dataset name] [number of principal components] [number of clusters]

This will generate a text file in the directory from which you run it called output.txt.

The valid dataset names are planets, coffee_and_code, food_preference and bens_dataset.

You can run the algorithm tests by using: py main.py -test

You can see the principle component values for each dataset by using: py main.py -components


Code:
I separated my code into different modules and packages for ease of organization. The main program flow is in the main.py file. There is also a small test file
for the algorithm here. The datasets directory holds most of the data and data
processing. There is a common_clean.py file here which pulls cleaned data from lower
files and runs it through PCA. There is a directory in datasets for each individual
dataset, and in each is a specific clean function for this dataset, which will pull the data
from a CSV file and return it cleaned as a list of lists of floats.

Results:
When testing my algorithm, I found that it was quite effective at clustering like
datapoints. It mostly had a perfect 1 out of one for the Jaccard Index when comparing
it’s clusters to the expected clusters. Even when its clusters differed from the expected
clusters, when you compared the individual clusters to each other their Jaccard Indices
were almost always .5 or higher. The algorithm also succeeded at clustering the
datasets I used. My favorite result was how when clustering the planets dataset, using
two principal components and forming two clusters, it separated out gas/ice giants from
terrestrial/super-earth planets quite effectively. My algorithm did sometimes have
varying results. If it randomly selected two adjacent starter points, then the clusters
would get messed up as there would be two clusters where there should have been
only one.
Conclusion:
This algorithm seems very effective at clustering like data. The limitations stem
from preparing the data and selecting the number of clusters. In the example I gave
earlier of clustering planets, its remarkable that the algorithm could see the difference
between giants and smaller planets, but it glossed over a lot of details in planet
clustering as it had only 2 bins to put planets in. Also, I had to spend a long time
manually deciding how to clean the data before feeding it into the algorithm, so my bias
might’ve slipped in. During cleaning, I cut out around ⅔ of the original features in the
planets dataset, and my cleaning algorithm cut out over ¾ of the data points. This was
necessary so I could work with complete data points, but the features I chose to keep
and the ways I transformed non-number data into numbers certainly influenced how the
planets were clustered. I’m not sure if this made it more likely for the algorithm to cluster
based on planet size, but it’s very possible.
Extra notes:
- I had to cut out a lot of features from the planets dataset to get a reasonable
number of complete data points. I documented my reasoning for each cut in a
text file in the planets directory.
- I have a “bens_dataset ” directory and cleaning file set up with a stub method for
the cleaning function. To use it, replace the CSV file in that directory with a real
dataset, keeping the name Bens_Dataset.csv. Complete the getCleanedData()
method in clean_Bens_Data.py. It should take in a file path and return a list of
lists of floats, with the first entry in every sublist being some kind of identifier.
Once this is done, you should be able to run clustering on Bens_Dataset from the
command line just like the other datasets.