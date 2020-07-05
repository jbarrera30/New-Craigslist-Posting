from functions import *




def main():
    url = 'https://orangecounty.craigslist.org/search/sss?query=fender+telecaster'
    links = []
    original_html = initialize_listing(url)
    while True: #every 15 minutes
        new_html = initialize_listing(url)
        if original_html != new_html:
            original_posts = original_html.find_all('li', class_='result-row')
            new_posts = new_html.find_all('li', class_='result-row')
            for item in new_posts:
                if item not in original_posts:
                    link = item.find('a', class_='result-title hdrlnk')
                    links.append(link['href'])
            for element in links:
                textme(element)
            original_html = new_html
            print('Found One')

if __name__ == '__main__':
    main()
