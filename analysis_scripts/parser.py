from bs4 import BeautifulSoup
# # Read the XML file
# with open('text/bijoux.xml', 'r') as file:
#     xml_data = file.read()

# # Create a Beautiful Soup object with the XML data and the parser
# soup = BeautifulSoup(xml_data, 'xml')

# # Perform operations on the parsed XML data
# # For example, access specific tags or attributes
# title = soup.find('title').text
# print(f"Title: {title}")

# # Extract data from multiple elements
# for item in soup.find_all('item'):
#     name = item.find('name').text
#     value = item.find('value').text
#     print(f"Name: {name}, Value: {value}")



# Read the TEI XML file
with open('text/bijoux.xml', 'r') as file:
    xml_data = file.read()

# Create a Beautiful Soup object with the XML data and the 'lxml' parser
soup = BeautifulSoup(xml_data, features='lxml')


# Find all <interp> tags
interp_tags = soup.find_all('interp')

# Extract the content of each <interp> tag
interps = [tag.text for tag in interp_tags]

# Print the extracted content
for interp in interps:
    print(interp)


interp_love = soup.find_all('interp', ana='#love')
print(interp_love)