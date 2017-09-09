#Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts
#Step 2. Download the dataset to your computer and unzip it.
import numpy as np
import pandas as pd

#Step 3. Use the csv file and assign it to a dataframe called food
food = pd.read_csv('/Code/world-food-facts/FoodFacts.csv', error_bad_lines=False)

