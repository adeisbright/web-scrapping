I added the virtual environment using :

python3 -m venv env

Then I activated the environment with :

source env/bin/activate

because I was running my code on mac

The next thing I need to do is install the tool I will use for
webscrapping.

I will also install some other additional tools for analysis such as
pandas and numpy.

python3 -m pip install requests beautifulsoup

## Making a requests

import requests

target_url= 'example.com/jobs'

page = requests.get(target_url)

## Add Beautifulsoup for Parsing Document

import requests
from bs4 import BeautifulSoup

target_url= 'example.com/jobs'

page = requests.get(target_url)

soup = BeautifulSoup(page.content , "html.parser")

`## Find all the anchor tags on the page `

anchors = soup.find_all("a")

```# Each soup returns a nested document of objects. So, you can
treat each of the object as a python dictionary. Thereby
enabling you to use dot notation and other attributes of a
dictionary.

The document you want to cook can be stored either on disk , available
on the world wide web, etc.
You have to load the document, and then cook your soup.

```

for anchor in anchors :
print(anchor.get("href"))

/\*\*

-   Kinds of Objects in Beautiful soup
    > Tags : They correspond to HTML tags  
    > A tag has a name , and attributes.

tag.name , tag.attrs

The atributes are returned as a dictionary where each key corresponds to the attribute name and the value is the atrribute value.

> NavigableString
> These are the contents that are held within a tag. They
> are unicode .
> You can convert them to python string using str(tag.string)

ta.string_replace_with("New string")

> BeautifulSoup
> This represents the fully parsed document.

To get the first anchor tag

soup.a

To get the anchor tag under a div

soup.div.a

The children of a tag are contained as a list in the contents
property

soup.div.contents

soup.div.parent => List the parent of div
soup.div.parents => List the parents of div

You can use the next_sibling and previous_sibling property to navigate a document

soup.div.next_sibling => The next sibling of the div
soup.div.previous_sibling => The previous sibling of div

\*\*/
