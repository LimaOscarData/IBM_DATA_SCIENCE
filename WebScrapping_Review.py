from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
html="<!DOCTYPE " \
     "html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b>" \
     "</h3><p> Salary: $ 92,000,000 </p>" \
     "<h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p>" \
     "<h3> Kevin Durant </h3><p> Salary: $73,200, 000</p>" \
     "</body></html>"
soup=BeautifulSoup(html, "html.parser")
# print(soup)

# We can use the method prettify() to display the HTML in the nested structure
# print(soup.prettify())


######################## Tags ###################################
tag_object=soup.title
# print('tag object :', tag_object)
# tag object : <title>Page Title</title>

# print('tag object type :', type(tag_object))
# tag object type : <class 'bs4.element.Tag'>

# If there is more than one Tag with the same name, the first element with that Tag name is called,
# this corresponds to the most paid player
tag_object=soup.h3
# print(tag_object)
# <h3><b id="boldest">Lebron James</b></h3>

######################## Children, Parents, and Siblings ###################################
# As stated above the Tag object is a tree of objects we can access the child of the tag or
# navigate down the branch as follows:
tag_child= tag_object.b
# print(tag_child)
# <b id="boldest">Lebron James</b>

# You can access the parent with the  parent
parent_tag= tag_child.parent
# print(parent_tag)
# <h3><b id="boldest">Lebron James</b></h3>
# this is identical to: tag_object

# tag_object parent is the body element.
# print(tag_object.parent)
# <body>
# <h3><b id="boldest">Lebron James</b></h3><p> Salary: $ 92,000,000 </p>
# <h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p>
# <h3> Kevin Durant </h3><p> Salary: $73,200, 000</p>
# </body>

# tag_object sibling is the paragraph element
sibling_1= tag_object.next_sibling
# print(sibling_1)
# <p> Salary: $ 92,000,000 </p>

# sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object
sibling_2= sibling_1.next_sibling
# print(sibling_2)
# <h3> Stephen Curry</h3>

# Exercise: next_sibling
# Using the object sibling_2 and the property next_sibling to find the salary of Stephen Curry:
sibling_3=sibling_2.next_sibling
# print(sibling_3)
# <p> Salary: $85,000, 000 </p>

######################## HTML Attributes ###################################
# If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest.
# You can access a tag’s attributes by treating the tag like a dictionary:
# print(tag_child['id'])
# boldest

# You can access that dictionary directly as attrs:
# print(tag_child.attrs)
# {'id': 'boldest'}

# We can also obtain the content if the attribute of the tag using the Python get() method.
# print(tag_child.get('id'))
# boldest

######################## Navigable String #################################
tag_string=tag_child.string # tag_child : <b id="boldest">Lebron James</b>
# print(tag_string)
# Lebron James

# print(type(tag_string))
# <class 'bs4.element.NavigableString'>

unicode_string = str(tag_string)
# print(unicode_string)
# Lebron James

######################## Filter #################################
table="<table>" \
      "<tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>" \
      "<tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr>" \
      "<tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr>" \
      "<tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr>" \
      "</table>"
table_bs = BeautifulSoup(table, "html.parser")
# print(table_bs)

######################## find All #################################
table_rows=table_bs.find_all('tr')
# print(table_rows) #this is a list
# [<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
# <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>,
# <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
# <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>]

first_row =table_rows[0]
# print(first_row)
# <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>

# print(type(first_row))
# <class 'bs4.element.Tag'>

# we can obtain the child
# print(first_row.td)
# <td id="flight">Flight No</td>

# if we iterate through the list, each element corresponds to a row in the table:
# for i,row in enumerate(table_rows):
#     print("row",i,"is",row)
# row 0 is <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
# row 1 is <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>
# row 2 is <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>
# row 3 is <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>

# print(table_rows)
# [<tr><td id="flight">Flight No</td><td>Launch site</td><td>Payload mass</td></tr>,
# <tr><td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>,
# <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
# <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>]


# for i,row in enumerate(table_rows):
#     print("row",i)
#     cells=row.find_all('td')
#     for j,cell in enumerate(cells):
#         print('colunm',j,"cell",cell)

# row 0
# colunm 0 cell <td id="flight">Flight No</td>
# colunm 1 cell <td>Launch site</td>
# colunm 2 cell <td>Payload mass</td>
# row 1
# colunm 0 cell <td>1</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>
# colunm 2 cell <td>300 kg</td>
# row 2
# colunm 0 cell <td>2</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>
# colunm 2 cell <td>94 kg</td>
# row 3
# colunm 0 cell <td>3</td>
# colunm 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>
# colunm 2 cell <td>80 kg</td>

# If we use a list we can match against any item in that list.
# print(table_bs)
# list_input=table_bs.find_all(name=["tr", "td"])
# print(list_input)

######################## Attributes #################################
# print(table_bs.find_all(id="flight"))

# We can find all the elements that have links to the Florida Wikipedia page:
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
# print(list_input)
# [<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>,
# <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]

# If we set the  href attribute to True, regardless of what the value is, the code finds all tags with href value:
# print(table_bs.find_all(href=True))
# [<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>,
#  <a href="https://en.wikipedia.org/wiki/Texas">Texas</a>,
#  <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]

######################## Exercise: find_all ########################
# Using the logic above, find all the elements without href value
# print(table_bs.find_all(href=False))

# Using the soup object soup, find the element with the id attribute content set to "boldest".
# print(soup.find_all(id="boldest"))

# string
# With string you can search for strings instead of tags, where we find all the elments with Florida:
# print(table_bs.find_all(string="Florida"))

# find
# The find_all() method scans the entire document looking for results, it’s if you are looking for one
# element you can use the find() method to find the first element in the document. Consider the following two table:

two_tables="<h3>Rocket Launch </h3>" \
           "<p><table class='rocket'>" \
           "<tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>" \
           "<tr><td>1</td><td>Florida</td><td>300 kg</td></tr>" \
           "<tr><td>2</td><td>Texas</td><td>94 kg</td></tr>" \
           "<tr><td>3</td><td>Florida </td><td>80 kg</td></tr>" \
           "</table></p>" \
           "<p><h3>Pizza Party  </h3><table class='pizza'>" \
           "<tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr>" \
           "<tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr>" \
           "<tr><td>Little Caesars</td><td>12</td><td >144 </td></tr>" \
           "<tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
# We create a BeautifulSoup object  two_tables_bs
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

# We can find the first table using the tag name table
# print(two_tables_bs.find("table"))
# <table
# class="rocket"><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
# <tr><td>1</td><td>Florida</td><td>300 kg</td></tr>
# <tr><td>2</td><td>Texas</td><td>94 kg</td></tr>
# <tr><td>3</td><td>Florida </td><td>80 kg</td></tr>
# </table>

# We can filter on the class attribute to find the second table,
# but because class is a keyword in Python, we add an underscore.
# print(two_tables_bs.find("table",class_='pizza'))
# <table class="pizza">
# <tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr>
# <tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr>
# <tr><td>Little Caesars</td><td>12</td><td>144 </td></tr>
# <tr><td>Papa John's </td><td>15 </td><td>165</td></tr>
# </table>

################################# Downloading And Scraping The Contents Of A Web Page #################################
# We Download the contents of the web page:
url = "http://www.ibm.com"

# We use get to download the contents of the webpage in text format and store in a variable called data:
data  = requests.get(url).text
# We create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
# Scrape all links
# for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
#     print(link.get('href'))

################################# Scrape all images Tags #################################
# for link in soup.find_all('img'): # in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))

################################# Scrape data from HTML tables #################################
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-" \
      "DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# Before proceeding to scrape a web site, you need to examine the contents, and the way data is
# organized on the website. Open the above url in your browser and check how many rows and columns
# are there in the color table.

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

#Get all rows from the table
# for row in table.find_all('tr'): # in html table row is represented by the tag <tr>, find all makes a list
#     # Get all columns in each row.
#     cols = row.find_all('td') # in html a column is represented by the tag <td>, making a kind of list
#     color_name = cols[2].string # store the value in column 3 as color_name
#     color_code = cols[3].string # store the value in column 4 as color_code
#     print("{}--->{}".format(color_name,color_code))

############# Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas ###############
import pandas as pd
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

# we can see how many tables were found by checking the length of the tables list
# print(len(tables))

# Assume that we are looking for the 10 most densly populated countries table, we can
# look through the tables list and find the right one we are look for based on the data
# in each table or we can search for the table name if it is in the table but this option
# might not always work.

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
# print(table_index)

# We can use the method prettify() to display the HTML in the nested structure
# print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population,
                                                  "Area":area, "Density":density}, ignore_index=True)

# print(population_data)
#   Rank           Country   Population     Area Density
# 0    1         Singapore    5,704,000      710   8,033
# 1    2        Bangladesh  171,930,000  143,998   1,194
# 2    3  \n Palestine\n\n    5,266,785    6,020     847
# 3    4           Lebanon    6,856,000   10,452     656
# 4    5            Taiwan   23,604,000   36,193     652
# 5    6       South Korea   51,781,000   99,538     520
# 6    7            Rwanda   12,374,000   26,338     470
# 7    8             Haiti   11,578,000   27,065     428
# 8    9       Netherlands   17,670,000   41,526     426
# 9   10            Israel    9,450,000   22,072     428

############# Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html ###############
# Using the same url, data, soup, and tables object as in the last section we can use the read_html
# function to create a DataFrame.
# Remember the table we need is located in tables[table_index]
# We can now use the pandas function read_html and give it the string version of the table as well as
# the flavor which is the parsing engine bs4.
# print(pd.read_html(str(tables[5]), flavor='bs4'))
# [   Rank      Country  Population  Area(km2)  Density(pop/km2)
# 0     1    Singapore     5704000        710              8033
# 1     2   Bangladesh   171930000     143998              1194
# 2     3    Palestine     5266785       6020               847
# 3     4      Lebanon     6856000      10452               656
# 4     5       Taiwan    23604000      36193               652
# 5     6  South Korea    51781000      99538               520
# 6     7       Rwanda    12374000      26338               470
# 7     8        Haiti    11578000      27065               428
# 8     9  Netherlands    17670000      41526               426
# 9    10       Israel     9450000      22072               428]

# The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0] # if you put [0] there wont be any brackets
# print(population_data_read_html)
#    Rank      Country  Population  Area(km2)  Density(pop/km2)
# 0     1    Singapore     5704000        710              8033
# 1     2   Bangladesh   171930000     143998              1194
# 2     3    Palestine     5266785       6020               847
# 3     4      Lebanon     6856000      10452               656
# 4     5       Taiwan    23604000      36193               652
# 5     6  South Korea    51781000      99538               520
# 6     7       Rwanda    12374000      26338               470
# 7     8        Haiti    11578000      27065               428
# 8     9  Netherlands    17670000      41526               426
# 9    10       Israel     9450000      22072               428

############# Scrape data from HTML tables into a DataFrame using read_html ###############
# We can also use the read_html function to directly get DataFrames from a url.
dataframe_list = pd.read_html(url, flavor='bs4')
# We can see there are 25 DataFrames just like when we used find_all on the soup object.
# print(len(dataframe_list))

# Finally we can pick the DataFrame we need out of the list.
# print(dataframe_list[5])
#    Rank      Country  Population  Area(km2)  Density(pop/km2)
# 0     1    Singapore     5704000        710              8033
# 1     2   Bangladesh   171930000     143998              1194
# 2     3    Palestine     5266785       6020               847
# 3     4      Lebanon     6856000      10452               656
# 4     5       Taiwan    23604000      36193               652
# 5     6  South Korea    51781000      99538               520
# 6     7       Rwanda    12374000      26338               470
# 7     8        Haiti    11578000      27065               428
# 8     9  Netherlands    17670000      41526               426
# 9    10       Israel     9450000      22072               428

# We can also use the match parameter to select the specific table we want.
# If the table contains a string matching the text it will be read.
# print(pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0])
#    Rank      Country  Population  Area(km2)  Density(pop/km2)
# 0     1    Singapore     5704000        710              8033
# 1     2   Bangladesh   171930000     143998              1194
# 2     3    Palestine     5266785       6020               847
# 3     4      Lebanon     6856000      10452               656
# 4     5       Taiwan    23604000      36193               652
# 5     6  South Korea    51781000      99538               520
# 6     7       Rwanda    12374000      26338               470
# 7     8        Haiti    11578000      27065               428
# 8     9  Netherlands    17670000      41526               426
# 9    10       Israel     9450000      22072               428