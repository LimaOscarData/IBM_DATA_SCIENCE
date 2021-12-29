# Data Engineering Process
# There are several steps in Data Engineering process.
# Extract - Data extraction is getting data from multiple sources. Ex. Data extraction from a website using
# Web scraping or gathering information from the data that are stored in different formats(JSON, CSV, XLSX etc.).
# Transform - Tarnsforming the data means removing the data that we don't need for further analysis and converting
# the data in the format that all the data from the multiple sources is in the same format.
# Load - Loading the data inside a data warehouse. Data warehouse essentially contains large volumes of data that
# are accessed to gather insights.

########################### Reading data from CSV in Python ###########################
# The Pandas Library is a useful tool that enables us to read various datasets into a Pandas data frame
# Let us look at how to read a CSV file in Pandas Library.
# We use pandas.read_csv() function to read the csv file. In the parentheses, we put the file path along with a
# quotation mark as an argument, so that pandas will read the file into a data frame from that address. The file
# path can be either a URL or your local file address.

import pandas as pd
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-' \
     'SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)
# print(df)
#                     John       Doe  ...   NJ  08075
# 0                   Jack  McGinnis  ...   PA   9119
# 1          John "Da Man"    Repici  ...   NJ   8075
# 2                Stephen     Tyler  ...   SD  91234
# 3                    NaN  Blankman  ...   SD    298
# 4  Joan "the bone", Anne       Jet  ...   CO    123
#
# [5 rows x 6 columns]

# Adding column name to the DataFrame
# We can add columns to an existing DataFrame using its columns attribute.
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
# print(df)
#               First Name Last Name  ... State Area Code
# 0                   Jack  McGinnis  ...    PA      9119
# 1          John "Da Man"    Repici  ...    NJ      8075
# 2                Stephen     Tyler  ...    SD     91234
# 3                    NaN  Blankman  ...    SD       298
# 4  Joan "the bone", Anne       Jet  ...    CO       123
#
# [5 rows x 6 columns]

# Selecting a single column
# To select the first column 'First Name', you can pass the column name as a string to the indexing operator.
# print(df["First Name"])
# 0                     Jack
# 1            John "Da Man"
# 2                  Stephen
# 3                      NaN
# 4    Joan "the bone", Anne
# Name: First Name, dtype: object

# Selecting multiple columns
# To select multiple columns, you can pass a list of column names to the indexing operator.
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
# print(df)
#               First Name Last Name  ... State Area Code
# 0                   Jack  McGinnis  ...    PA      9119
# 1          John "Da Man"    Repici  ...    NJ      8075
# 2                Stephen     Tyler  ...    SD     91234
# 3                    NaN  Blankman  ...    SD       298
# 4  Joan "the bone", Anne       Jet  ...    CO       123
#
# [5 rows x 6 columns]

# Selecting rows using .iloc and .loc :
# Now, let's see how to use .loc for selecting rows from our DataFrame.
# loc() : loc() is label based data selecting method which means that we have to pass the name of
# the row or column which we want to select.

# To select the first row
# print(df.loc[0])
# First Name            Jack
# Last Name         McGinnis
# Location      220 hobo Av.
# City                 Phila
# State                   PA
# Area Code             9119
# Name: 0, dtype: object

# To select the 0th,1st and 2nd row of "First Name" column only
# print(df.loc[[0,1,2], "First Name"])
# 0             Jack
# 1    John "Da Man"
# 2          Stephen
# Name: First Name, dtype: object

# print(df.loc[[0,1,2], ["First Name","City"]])
#       First Name       City
# 0           Jack      Phila
# 1  John "Da Man"  Riverside
# 2        Stephen   SomeTown

# Now, let's see how to use .iloc for selecting rows from our DataFrame.
# iloc() : iloc() is a indexed based selecting method which means that we have to pass integer
# index in the method to select specific row/column.

# To select the 0th,1st and 2nd row of "First Name" column only
# print(df.iloc[[0,1,2], 0])
# 0             Jack
# 1    John "Da Man"
# 2          Stephen
# Name: First Name, dtype: object

# Transform Function in Pandas
# Python’s Transform function returns a self-produced dataframe with transformed values after
# applying the function specified in its parameter.
# Let's see how Transform function works.

import pandas as pd
import numpy as np
#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# Let’s say we want to add 10 to each element in a dataframe:
#applying the transform function
df = df.transform(func = lambda x : x + 10)
# print(df)
#     a   b   c
# 0  11  12  13
# 1  14  15  16
# 2  17  18  19

# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
# print(result)
#           a         b         c
#        sqrt      sqrt      sqrt
# 0  3.316625  3.464102  3.605551
# 1  3.741657  3.872983  4.000000
# 2  4.123106  4.242641  4.358899

# result = df.transform(func = 'sqrt')
# print(result)
#           a         b         c
# 0  3.316625  3.464102  3.605551
# 1  3.741657  3.872983  4.000000
# 2  4.123106  4.242641  4.358899

#  for more info : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html?
#  utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-
#  Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01

