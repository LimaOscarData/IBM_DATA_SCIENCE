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
datatframe.to_csv("employee.csv", index=False)
# We can also read and save other file formats, we can use similar functions to pd.read_csv() and df.to_csv() for
# other data formats. The functions are listed in the following table:
