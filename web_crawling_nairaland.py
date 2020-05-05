from bs4 import BeautifulSoup
import requests
import re


#SET HEADER(This mimicks a (user)device as some websites are against crawling them)
headers = requests.utils.default_headers()

#You can get the below info from inspecting the network of a page and collecting the user agent information in a particular folder
headers.update({
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
})

#Here the url is set to the official website of nairaland
url = "https://nairaland.com"

#A variable is created here to get the url and headers of the page that you are crawling
my_request = requests.get(url, headers)

#An object soup is created after calling the class BeautifulSoup that was imported from the bs4 folder/module
soup = BeautifulSoup(my_request.content, features='html.parser')

# This helps get the html page in the terminal print(soup.prettify())


#Here we are setting the object soup in a variable 'frontpage' and tasking it to use the key word td and the class featured w 
# to get all the data on the front page because that is the location of what we are looking for
frontpage = soup.find("td", class_="featured w")

#We create a list called topic_container to hold all the information that the soup is going to crawl out of the website
topic_container = []

#Here we use a for loop to loop through the news list while enumerating our results gotten from the html anchor tag 'a' with the enumerate function
# in the line with '.append' we append the news gotten from the anchor tags into the topic_container list while indexing from 1 with i+1, and also appending the topic as text and getting the link to the topic we had just gotten
for i, topic in enumerate(frontpage.find_all('a', attrs={'href': re.compile("^https://")})):
    #Follow a specific Topic link and get the specific number of views
    further_request =requests.get(topic.get('href'), headers)
    further_soup = BeautifulSoup(further_request.content, features='html.parser')
    viewers = further_soup.find("p", class_="bold")

    topic_container.append([i+1, topic.text, str(str(viewers).split("</a> ")[4:5]).split(" <p> ")[0].strip("['")])
    
    #) topic.get('href')

#In this line of code we use a for loop to loop through and print all the items that are now enumerated in the topic_container list
for item in topic_container:
    print(item)