from functions import *
import datetime

#check date
def main():
    url = '<your url here>'
    original_html = initialize_listing(url)
    while True:
        new_html = initialize_listing(url)
        if original_html != new_html:
            print('newlistings')
            original_posts = find_posts(original_html)
            new_posts = find_posts(new_html)
            links = []
            for item in new_posts:
                datestr = get_date(item)
                postdate = datetime.datetime.strptime(datestr,'%Y-%m-%d %H:%M' )
                if item not in original_posts and postdate.date() == datetime.datetime.now().date():
                    link = get_link(item)
                    textme(link)
                    print('Found One')

            original_html = new_html

if __name__ == '__main__':
    main()
