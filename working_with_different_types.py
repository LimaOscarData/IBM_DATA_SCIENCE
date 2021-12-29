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

