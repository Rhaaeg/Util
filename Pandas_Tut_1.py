# Data Processing 

#Importing libraries
#Step 1. Import the necessary libraries
import pandas as pd #import datasets

#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

#Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv(url ,sep = '\t')

#Step 4. See the first 10 entries
chipo.head(10)

#Step 5. What is the number of observations in the dataset?
chipo.info()
#or
#Shape represents the dimensions lines x columns
chipo.shape[0]

#Step 6. What is the number of columns in the dataset?
chipo.shape[1]

#Step 7. Print the name of all the columns.
chipo.columns

#Step 8. How is the dataset indexed?
chipo.index

#Step 9. Which was the most ordered item?
chipo.item_name.value_counts().head(1)

#Step 10. How many items were ordered?
chipo.item_name.value_counts().max()

#Step 11. What was the most ordered item in the choice_description column?
chipo.choice_description.value_counts().head(1)

#Step 12. How many items were orderd in total?
chipo.quantity.sum()

#Step 13. Turn the item price into a float
dollar = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollar)

#Step 14. How much was the revenue for the period in the dataset?¶
chipo.item_price.sum()

#Step 15. How many orders were made in the period?
chipo.order_id.value_counts().count()

#Step 16. What is the average amount per order?
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['item_price']

#Step 17. How many different items are sold?
chipo.item_name.value_counts().count()

