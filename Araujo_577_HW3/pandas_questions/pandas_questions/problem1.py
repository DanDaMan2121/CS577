# 1. Pandas practice. Complete the assignment in the .ipynb file named, “HW4_Pandas_questions.”

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the file "hotel_booking_data.csv" into a DataFrame. Show the first 4 rows of the DataFrame.
df = pd.read_csv("hotel_booking_data.csv")
print(df.head(4)) # prints the rows starting from the head
print("=======")


# 2. How many data points and features does this data set have? List the features of the data set. 
print(f"number of rows: {df.shape[0]}")
print(f"number of columns: {df.shape[1]}")
print(f"number of cells: {df.shape[1] * df.shape[0]}")
print(f"features: {df.columns.tolist()}")
print("=======")


# 3. Is there any missing data? If so, which column has the most missing data?
missing_data = df.isnull().sum().sum() # check to see which cells are null and returns the sum of all the null cells
print(f"number of missing data: {missing_data}")
column_most_missing = df.isnull().sum().idxmax() # finds the index of the column with the most missing data
print(f"column with the most missing data: {column_most_missing}")
count = df.isnull().sum().max()
print(f"count of data lost: {count}")
print("=======")



# 4. Print the non-null count and data type of each column.
print(df.info())
print("=======")

# 5. Remove the 'company' column from the data set.
df.drop('company', axis=1, inplace=True)
# print("=======")

# 6. What are the top 5 most common country codes in the dataset? Answer using a single line of code.
most_common_country_codes = df['country'].value_counts().head(5)
print(most_common_country_codes)
print("=======")
# 7. The adr is the average daily rate for a person's stay at the hotel. What is the mean adr across all the hotel stays in the dataset? Round this to 2 decimal points.
adr = round(df['adr'].mean(), 2)
print(f"adr: {adr}")
print("=======")
# 8. What is the average (mean) number of nights for a stay across the entire data set? Round this to 2 decimal points.
mean_number_of_nights = round((df['stays_in_week_nights'] + df['stays_in_weekend_nights']).mean(), 2)
print(f"mean number of nights: {mean_number_of_nights}" )
print("=======")
# 9. What is the average *total cost* for a stay in the dataset? Not average daily cost, but *total stay* cost. (You will need to calculate total cost your self by using ADR and week day and weeknight stays). Round this to 2 decimal points.
average_total_cost = round(mean_number_of_nights * adr, 2)
print(f"average total cost for a stay: {average_total_cost}")
print("=======")
# 10. What are the names and emails of people who made exactly 5 "Special Requests"?
special_requests = df[df['total_of_special_requests'] == 5][['name', 'email']]
print(special_requests)
print("=======")
# 11. What are the top 5 most common last name in the dataset? Bonus: Can you figure this out in one line of pandas code?
#     - For simplicity treat the a title such as MD as a last name, for example Caroline Conley MD can be said to have the last name MD.
#     - You may have to revisit string methods and lambda functions for this question.    
five_most_common_last_names = df['name'].apply(lambda name: name.split()[-1]).value_counts().head(5)
print(f"top 5 most common last name: {five_most_common_last_names}")
print("=======")
# 12. How many arrivals took place between the 1st and the 15th of the month (inclusive of 1 and 15)? Bonus: Can you do this in one line of pandas code?
arrivals = df[df['arrival_date_day_of_month'].between(1, 15)].shape[0]
print(f"arrivals between 1st and 15th of the month: {arrivals}")