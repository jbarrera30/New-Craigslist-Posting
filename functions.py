from bs4 import BeautifulSoup
import requests
from twilio.rest import Client




def initialize_listing(url):
    original = requests.get(url)
    return BeautifulSoup(original.text, 'html.parser')

def textme(link):
    client = Client("<Twilio ID>", "<Twilio Authorization Token")
    client.messages.create(to="<Your Phone Number>", from_="<Twilio Phone Number>", body= link)

def find_posts(html):
    return html.find_all('li', class_='result-row')

def get_link(post):
    return post.find('a', class_='result-title hdrlnk')['href']

def get_date(post):
    return post.find('time', class_='result-date')['datetime']
