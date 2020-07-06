from bs4 import BeautifulSoup
import requests
from twilio.rest import Client




def initialize_listing(url):
    original = requests.get(url)
    return BeautifulSoup(original.text, 'html.parser')

def textme(link):
    client = Client("AC2338c4f3e153b2965fa9af46f8e39d7c", "07207c83a8a012a64415285988c93d93")
    client.messages.create(to="+19499239560", from_="+12056512405", body= link)

def find_posts(html):
    return html.find_all('li', class_='result-row')

def get_link(post):
    return post.find('a', class_='result-title hdrlnk')['href']

def get_date(post):
    return post.find('time', class_='result-date')['datetime']