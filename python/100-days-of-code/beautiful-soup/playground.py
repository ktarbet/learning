import os
from bs4 import BeautifulSoup

# import lxml
WEB_PAGE = "website.html"


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def read_file(file_name):
    if not os.path.exists(file_name):
        raise f"error, {file_name} does not exist"
    with open(file_name, encoding="utf8") as f:
        return f.read()


content = read_file(WEB_PAGE)

# soup = BeautifulSoup(content, 'lxml')
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())
print(soup.a) # gets first a tag
print(soup.p) # gets first p tag

anchor_tags = soup.find_all(name='a')
print(anchor_tags)

anchor_tags = soup.find_all(name='a')
for tag in anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

h1 = soup.find(name="h1",id="name")
print(h1)

section_heading = soup.find(name="h3", class_= "heading")
print(section_heading)
print(section_heading.name)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

name = soup.select_one(selector="#name")
print(name)

class_heading = soup.select(selector=".heading")
print(class_heading)
