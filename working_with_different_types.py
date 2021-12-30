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

# JSON file Format
# JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.
# JSON is built on two structures:
# A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary,
# hash table, keyed list, or associative array.
# An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.
# JSON is a language-independent data format. It was derived from JavaScript, but many modern programming languages
# include code to generate and parse JSON-format data. It is a very common data format with a diverse range of
# applications.
# The text in JSON is done through quoted string which contains the values in key-value mappings within { }.
# It is similar to the dictionary in Python.
# Python supports JSON through a built-in package called json. To use this feature, we import the json
# package in Python script.

# Writing JSON to a File
# This is usually called serialization. It is the process of converting an object into a special format which
# is suitable for transmitting over the network or storing in file or database.
# To handle the data flow in a file, the JSON library in Python uses the dump() or dumps() function to convert
# the Python objects into their respective JSON object. This makes it easy to write data to files.

import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
# print(person)
# {'first_name': 'Mark', 'last_name': 'abc', 'age': 27,
#  'address': {'streetAddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postalCode': '10021-3100'}}

############################# serialization using dump() function #############################
# json.dump() method can be used for writing to JSON file.
# Syntax: json.dump(dict, file_pointer)
# Parameters:
# dictionary – name of the dictionary which should be converted to JSON object.
# file pointer – pointer of the file opened in write or append mode.

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)
# print(person)
# {'first_name': 'Mark', 'last_name': 'abc', 'age': 27, 'address': {'streetAddress': '21 2nd Street',
# 'city': 'New York', 'state': 'NY', 'postalCode': '10021-3100'}}

# serialization using dumps() function
# json.dumps() that helps in converting a dictionary to a JSON object.
# It takes two parameters:
# dictionary – name of the dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation

# Serializing json
json_object = json.dumps(person, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
# print(json_object)
# {
#     "first_name": "Mark",
#     "last_name": "abc",
#     "age": 27,
#     "address": {
#         "streetAddress": "21 2nd Street",
#         "city": "New York",
#         "state": "NY",
#         "postalCode": "10021-3100"
#     }
# }

# Our Python objects are now serialized to the file. To deserialize it back to the Python object,
# we use the load() function.

# Reading JSON to a File
# This process is usually called Deserialization - it is the reverse of serialization.
# It converts the special format returned by the serialization back into a usable object.
# Using json.load()
# The JSON package has json.load() function that loads the json content from a json file into a dictionary.
# It takes one parameter:
# File pointer: A file pointer that points to a JSON file.

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

# print(json_object)
# print(type(json_object))
# {'first_name': 'Mark', 'last_name': 'abc', 'age': 27, 'address':
#     {'streetAddress': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postalCode': '10021-3100'}}
# <class 'dict'>

################################ XLSX file format ################################
# XLSX is a Microsoft Excel Open XML file format. It is another type of Spreadsheet file format.
# In XLSX data is organized under the cells and columns in a sheet.

# Reading the data from XLSX file
# Let’s load the data from XLSX file and define the sheet name.
# For loading the data you can use the Pandas library in python.

# import pandas as pd
import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
                           "IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data"
                           "/file_example_XLSX_10.xlsx", "sample.xlsx")

df = pd.read_excel("sample.xlsx")
# print(df)
#    0 First Name  Last Name  Gender        Country  Age        Date    Id
# 0  1      Dulce      Abril  Female  United States   32  15/10/2017  1562
# 1  2       Mara  Hashimoto  Female  Great Britain   25  16/08/2016  1582
# 2  3     Philip       Gent    Male         France   36  21/05/2015  2587
# 3  4   Kathleen     Hanner  Female  United States   25  15/10/2017  3549
# 4  5    Nereida    Magwood  Female  United States   58  16/08/2016  2468
# 5  6     Gaston      Brumm    Male  United States   24  21/05/2015  2554
# 6  7       Etta       Hurn  Female  Great Britain   56  15/10/2017  3598
# 7  8    Earlean     Melgar  Female  United States   27  16/08/2016  2456
# 8  9   Vincenza    Weiland  Female  United States   40  21/05/2015  6548

################################## XML file format ##################################
# XML is also known as Extensible Markup Language. As the name suggests, it is a markup language.
# It has certain rules for encoding data. XML file format is a human-readable and machine-readable file format.
# Pandas does not include any methods to read and write XML files. Here, we will take a look at how we can use
# other modules to read data from an XML file, and load it into a Pandas DataFrame.

import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

# Reading with xml.etree.ElementTree
# Let's have a look at a one way to read XML data and put it in a Pandas DataFrame.
# You can see the XML file in the Notepad of your local machine.

import pandas as pd

import xml.etree.ElementTree as etree

# wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml

# You would need to firstly parse an XML file and create a list of columns for data frame, then extract useful
# information from the XML file and add to a pandas data frame.
# Here is a sample code that you can use.:

# tree = etree.parse("Sample-employee-XML-file.xml")
#
# root = tree.getroot()
# columns = ["firstname", "lastname", "title", "division", "building", "room"]
#
# datatframe = pd.DataFrame(columns=columns)
#
# for node in root:
#     firstname = node.find("firstname").text
#     lastname = node.find("lastname").text
#     title = node.find("title").text
#     division = node.find("division").text
#     building = node.find("building").text
#     room = node.find("room").text
#     datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index=columns),
#                                    ignore_index=True)
# print(datatframe)

# Save Data
# Correspondingly, Pandas enables us to save the dataset to csv by using the dataframe.to_csv() method, you can
# add the file path and name along with quotation marks in the parentheses.
# For example, if you would save the dataframe df as employee.csv to your local machine, you may use the syntax below:
# datatframe.to_csv("employee.csv", index=False)
# We can also read and save other file formats, we can use similar functions to pd.read_csv() and df.to_csv() for
# other data formats. The functions are listed in the following table:

# Read/Save Other Data Formats
# Data Formate	Read	Save
# csv	pd.read_csv()	df.to_csv()
# json	pd.read_json()	df.to_json()
# excel	pd.read_excel()	df.to_excel()
# hdf	pd.read_hdf()	df.to_hdf()
# sql	pd.read_sql()	df.to_sql()
# ...	...	...

# Let's move ahead and perform some Data Analysis.

# Binary File Format
# "Binary" files are any files where the format isn't made up of readable characters. It contain formatting
# information that only certain applications or processors can understand. While humans can read text files,
# binary files must be run on the appropriate software or processor before humans can read them.
# Binary files can range from image files like JPEGs or GIFs, audio files like MP3s or binary document formats
# like Word or PDF.
# Let's see how to read an Image file.

# Reading the Image file
# Python supports very powerful tools when it comes to image processing. Let’s see how to process the images
# using the PIL library.
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.

# importing PIL
# from PIL import Image
# import urllib.request
# # Downloading dataset
# urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-"
#                            "royalty-free-image-1586966191.jpg", "dog.jpg")
#
# # Read image
# img = Image.open('dog.jpg')
#
# # Output Images
# display(img)

# Data Analysis
# In this section, you will learn how to approach data acquisition in various ways and obtain necessary insights
# from a dataset. By the end of this lab, you will successfully load the data into Jupyter Notebook and gain some
# fundamental insights via the Pandas Library.
# In our case, the Diabetes Dataset is an online source and it is in CSV (comma separated value) format. Let's use
# this dataset as an example to practice data reading.

# About this Dataset
# Context: This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.
# The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain
# diagnostic measurements included in the dataset. Several constraints were placed on the selection of these
# instances from a larger database. In particular, all patients here are females at least 21 years of age of Pima
# Indian heritage.
# Content: The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor
# variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.
# We have 768 rows and 9 columns. The first 8 columns represent the features and the last column represent the
# target/label.

# Import pandas library
import pandas as pd
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-" \
       "PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)
# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe,
# where n is an integer. Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n
# rows of the dataframe.

# show the first 5 rows using dataframe.head() method
# print("The first 5 rows of the dataframe")
# print(df.head(5))
# The first 5 rows of the dataframe
#    Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
# 0            6      148             72  ...                     0.627   50        1
# 1            1       85             66  ...                     0.351   31        0
# 2            8      183             64  ...                     0.672   32        1
# 3            1       89             66  ...                     0.167   21        0
# 4            0      137             40  ...                     2.288   33        1
#
# [5 rows x 9 columns]

# To view the dimensions of the dataframe, we use the .shape parameter.
# print(df.shape)
# (768, 9)

####################### Statistical Overview of dataset #######################
# print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 768 entries, 0 to 767
# Data columns (total 9 columns):
#  #   Column                    Non-Null Count  Dtype
# ---  ------                    --------------  -----
#  0   Pregnancies               768 non-null    int64
#  1   Glucose                   768 non-null    int64
#  2   BloodPressure             768 non-null    int64
#  3   SkinThickness             768 non-null    int64
#  4   Insulin                   768 non-null    int64
#  5   BMI                       768 non-null    float64
#  6   DiabetesPedigreeFunction  768 non-null    float64
#  7   Age                       768 non-null    int64
#  8   Outcome                   768 non-null    int64
# dtypes: float64(2), int64(7)
# memory usage: 54.1 KB
# None

# This method prints information about a DataFrame including the index dtype and columns, non-null values and
# memory usage.


# print(df.describe())
#        Pregnancies     Glucose  ...         Age     Outcome
# count   768.000000  768.000000  ...  768.000000  768.000000
# mean      3.845052  120.894531  ...   33.240885    0.348958
# std       3.369578   31.972618  ...   11.760232    0.476951
# min       0.000000    0.000000  ...   21.000000    0.000000
# 25%       1.000000   99.000000  ...   24.000000    0.000000
# 50%       3.000000  117.000000  ...   29.000000    0.000000
# 75%       6.000000  140.250000  ...   41.000000    1.000000
# max      17.000000  199.000000  ...   81.000000    1.000000
#
# [8 rows x 9 columns]

# Pandas describe() is used to view some basic statistical details like percentile, mean, standard deviation, etc.
# of a data frame or a series of numeric values. When this method is applied to a series of strings, it returns a
# different output


######################## Identify and handle missing values ########################
# We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:
# .isnull()
# .notnull()
# The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.
missing_data = df.isnull()
# print(missing_data.head(5))
#    Pregnancies  Glucose  ...    Age  Outcome
# 0        False    False  ...  False    False
# 1        False    False  ...  False    False
# 2        False    False  ...  False    False
# 3        False    False  ...  False    False
# 4        False    False  ...  False    False
#
# [5 rows x 9 columns]

# "True" stands for missing value, while "False" stands for not missing value.


# Count missing values in each column
# Using a for loop in Python, we can quickly figure out the number of missing values in each column. As mentioned above,
# "True" represents a missing value, "False" means the value is present in the dataset. In the body of the for loop
# the method ".value_counts()" counts the number of "True" values.

# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("")

# Pregnancies
# False    768
# Name: Pregnancies, dtype: int64
#
# Glucose
# False    768
# Name: Glucose, dtype: int64
#
# BloodPressure
# False    768
# Name: BloodPressure, dtype: int64
#
# SkinThickness
# False    768
# Name: SkinThickness, dtype: int64
#
# Insulin
# False    768
# Name: Insulin, dtype: int64
#
# BMI
# False    768
# Name: BMI, dtype: int64
#
# DiabetesPedigreeFunction
# False    768
# Name: DiabetesPedigreeFunction, dtype: int64
#
# Age
# False    768
# Name: Age, dtype: int64
#
# Outcome
# False    768
# Name: Outcome, dtype: int64

# As you can see above, there is no missing values in the dataset.


# Correct data format
# Check all data is in the correct format (int, float, text or other).
# In Pandas, we use
# .dtype() to check the data type
# .astype() to change the data type
# Numerical variables should have type 'float' or 'int'.

# print(df.dtypes)

# Pregnancies                   int64
# Glucose                       int64
# BloodPressure                 int64
# SkinThickness                 int64
# Insulin                       int64
# BMI                         float64
# DiabetesPedigreeFunction    float64
# Age                           int64
# Outcome                       int64
# dtype: object


# Visualization
# Visualization is one of the best way to get insights from the dataset. Seaborn and Matplotlib are two of Python's
# most powerful visualization libraries.

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()

# As you can see above, 65.10% females are Diabetic and 34.90% are Not Diabetic.