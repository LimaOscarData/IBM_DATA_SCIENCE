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
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

