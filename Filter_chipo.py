#Importing libraries

import pandas as pd

#Step 3. Assign it to a variable called chipo.
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')

#Step 4
# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices 

# make the comparison
chipo10 = chipo[chipo['item_price'] > 10.00]
chipo10.head()

len(chipo10)

#Step 5. What is the price of each item?
# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

# select only the item_name and item_price columns
price_per_item = chipo_one_prod[['item_name', 'item_price']]

# sort the values from the most to less expensive
price_per_item.sort_values(by = "item_price", ascending = False)


#Step 6. Sort by the name of the item
chipo.item_name.sort_values()
#or
chipo.sort_values(by = "item_name")

#Step 7. What was the quantity of the most expensive item ordered?
chipo.sort_values(by = "item_price", ascending = False).head(1)

#Step 8. How many times were a Veggie Salad Bowl ordered?
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)

#Step 9. How many times people orderd more than one Canned Soda?
chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)