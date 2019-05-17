# 1. Imports
import argparse
import requests
from bs4 import BeautifulSoup   # Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#kinds-of-filters


# 2.1. bleeping computer security news function
def bleep():
    bleep_url = 'https://www.bleepingcomputer.com/'
    bleep_page = requests.get(bleep_url)                            # make request to url
    bleep_soup = BeautifulSoup(bleep_page.text, 'html.parser')      # bs4 digest
    bleep_latest_news = str(bleep_soup.find_all(class_='tab-pane', id='nlatest'))       # save latest news text as variable
    bleep_soup2 = BeautifulSoup(bleep_latest_news, 'html.parser')                       # gather text from saved variable

    bleep_titles = []                                               # empty lists to store titles
    bleep_links = []                                                # empty list to store links

    for items in bleep_soup2.find_all('img'):                       # search through text for title
        bleep_titles.append(items.get('alt'))                       # append list
    for items in bleep_soup2.find_all('a', class_='nmic'):          # search through text for link
        bleep_links.append(items.get('href'))                       # append to list

    cntr = 0                                                        # counter start at 0
    for x in bleep_titles:
        title = x.split("Image")
        print(f'Title: {title[0]}')                                 # print title for each item
        print(f'Link: {bleep_links[cntr]}')                         # print link using counter as iterator
        cntr += 1                                                   # counter iteration interval

    # ---------------------------------------------------------------


# 2.2. cyberscoop security news function
def cyberscoop():
    cyberscoop_url = 'https://www.cyberscoop.com/'                              # url
    cyberscoop_page = requests.get(cyberscoop_url)                              # page request
    cyberscoop_soup = BeautifulSoup(cyberscoop_page.text, 'html.parser')        # bs4 digest

    for items in cyberscoop_soup.find_all('a', class_='article-thumb__title'):  # search loop
        print(f"Title: {items.get_text().strip()}")                             # print title
        print(f"Link: {items.get('href')}")                                     # print link

    # ---------------------------------------------------------------


# 2.3. krebs on security news function
def krebs():
    krebs_url = 'https://krebsonsecurity.com'
    krebs_page = requests.get(krebs_url)                            # make request to url
    krebs_soup = BeautifulSoup(krebs_page.text, 'html.parser')      # bs4 digest

    for items in krebs_soup.find_all("a", rel='bookmark'):          # search loop
        print(f"Title: {items.get_text()}")                         # article title
        print(f"Link: {items.get('href')}")                         # article link

    # ---------------------------------------------------------------


# 2.4. motherboard security news function
def motherboard():
    mother_url = 'https://motherboard.vice.com/en_us/topic/hacking'             # url
    mother_page = requests.get(mother_url)                                      # page request
    mother_soup = BeautifulSoup(mother_page.text, 'html.parser')                # bs4 digest

    mother_titles = []                                                          # empty lists
    mother_links = []

    for items in mother_soup.find_all('a'):                                     # search loop
        links = str(items.get('href'))                                          # find links

        if '/en_us/article/' in links:                                          # filter links
            mother_links.append(links)                                          # append links to list
            title_split = str(links).split('/')                                 # strip/split titles
            mother_titles.append(str(title_split[4]).replace('-', ' '))         # append titles to list

    cntr = 0                                                                    # counter start at 0
    for x in mother_titles:
        print(f'Title: {x}')                                                    # print title for each item
        # print link using counter as iterator
        print(f'Link: https://motherboard.vice.com{mother_links[cntr]}')
        cntr += 1

    # ---------------------------------------------------------------


# 2.5. Kapersky Securelist security news function
def securelist():
    seclist_url = 'https://securelist.com/'                                       # url
    seclist_page = requests.get(seclist_url)                                      # page request
    seclist_soup = BeautifulSoup(seclist_page.text, 'html.parser')                # bs4 digest

    for items in seclist_soup.find_all(class_='entry-title'):                     # search loop
        a_tag = items.a                                                           # scrape a tags
        a_title = a_tag.get('title')                                              # scrape title
        a_link = a_tag.get('href')                                                # scrape links
        print(f'Title: {a_title}')
        print(f'Link: {a_link}')

    # ---------------------------------------------------------------


# 2.6. zdnet security news function
def zdnet():
    zdnet_url = 'https://www.zdnet.com/topic/security'                          # url
    zdnet_page = requests.get(zdnet_url)                                        # page request
    zdnet_soup = BeautifulSoup(zdnet_page.text, 'html.parser')                  # bs4 digest
    zdnet_latest_news = str(zdnet_soup.find_all('div', id='latest'))            # latest news text
    bleep_soup2 = BeautifulSoup(zdnet_latest_news, 'html.parser')               # bs4 digest of latest news

    for items in bleep_soup2.find_all('a', class_='thumb'):                     # search loop
        print(f"Title: {items.get('title')}")                                   # print titles
        print(f"Link: https://www.zdnet.com{items.get('href')}")                # print link

    # ---------------------------------------------------------------


# 3. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='CyberNews Report scrapes many outlets for their most recent stories')
    # 3.2. define flags
    parser.add_argument(
                        "--outlet",
                        choices=['BleepingComputer', 'cyberscoop', 'Krebs', 'Motherboard', 'Securelist', 'ZDNet', 'All'],
                        type=str
                        )
    # 3.3. save input
    args = parser.parse_args()
    # 3.4. pass input to data function
    x = str(args.outlet).lower()
    # function decision tree, based on input
    if x == 'bleepingcomputer':
        bleep()
    elif x == 'cyberscoop':
        cyberscoop()
    elif x == 'krebs':
        krebs()
    elif x == 'motherboard':
        motherboard()
    elif x == 'securelist':
        securelist()
    elif x == 'zdnet':
        zdnet()
    elif x == 'all':
        bleep()
        cyberscoop()
        krebs()
        motherboard()
        securelist()
        zdnet()
    else:
        print('Ooops! Must be smarter than the options menu to get the news. Try the -h flag.')

# 4. Call initial function in chain
main()
