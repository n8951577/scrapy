#class MyClass:
 #   variable = "Kiran"

  #  def function(self):
   #     print("This is a message inside the class.")

#myobjectx = MyClass()
#print(myobjectx.variable)
#myobjectx.function()
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
