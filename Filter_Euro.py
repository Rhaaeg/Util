# Data Processing 

#Importing libraries
import pandas as pd #import datasets

#Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/jokecamp/FootballData/master/Euro%202012/Euro%202012%20stats%20TEAM.csv'
#Step 3. Assign it to a variable called euro12.
euro = pd.read_csv(url)

#Step 4. Select only the Goal column.
euro['Goals']

#Step 5. How many team participated in the Euro2012?
euro.shape[0]
euro.Team.count()

#Step 6. What is the number of columns in the dataset?
euro.shape[1]

#Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro[['Team', 'Yellow Cards', 'Red Cards']]
discipline

#Step 8. Sort the teams by Red Cards, then to Yellow Cards
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)

#Step 9. Calculate the mean Yellow Cards given per Team
round(discipline['Yellow Cards'].mean())

#Step 10. Filter teams that scored more than 6 goals
euro[euro.Goals > 6].Team

#Step 11. Select the teams that start with G
euro[euro.Team.str.startswith('G')].Team

#Step 12. Select the first 7 columns
euro.iloc[:, :7]

#Step 13. Select all columns except the last 3.
euro.iloc[:,:-3]

#Step 14. Present only the Shooting Accuracy from England, Italy and Russia
euro.loc[euro.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]

