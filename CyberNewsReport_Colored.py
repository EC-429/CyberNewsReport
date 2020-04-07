# 1. Imports
import argparse
import requests
from colorama import Style, Back, Fore
from bs4 import BeautifulSoup   # Documentation: crummy.com/software/BeautifulSoup/bs4/doc/

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6)'}  # User Agent


# 2.1. bleeping computer security news function
def bleep():
    bleep_url = 'https://www.bleepingcomputer.com/'
    bleep_page = requests.get(bleep_url, headers=headers)                                                # make request to url
    bleep_soup = BeautifulSoup(bleep_page.text, 'html.parser')                          # bs4 digest
    bleep_latest_news = str(bleep_soup.find_all(class_='tab-pane', id='nlatest'))       # save latest news text as variable
    bleep_soup2 = BeautifulSoup(bleep_latest_news, 'html.parser')                       # gather text from saved variable

    bleep_titles = []                                               # empty lists to store titles
    bleep_links = []                                                # empty list to store links

    for items in bleep_soup2.find_all('img'):                       # search through text for title
        bleep_titles.append(items.get('alt'))                       # append list
    for items in bleep_soup2.find_all('a', class_='nmic'):          # search through text for link
        bleep_links.append(items.get('href'))                       # append to list

    print('Bleeping Computer Latest Cybersecurity News')
    bleep_cntr = 0                                                                                  # counter start at 0
    for x in bleep_titles:
        title = x.split("Image")
        print(Back.BLUE + f' {bleep_cntr} ' + Style.RESET_ALL + f'\tTitle: {title[0]}')             # print title for each item
        print(Back.LIGHTBLUE_EX + ' Link: ' + Style.RESET_ALL + f'\t{bleep_links[bleep_cntr]}')     # print link using counter as iterator
        bleep_cntr += 1                                                                             # counter iteration interval
    print('\n')
    # ---------------------------------------------------------------


# 2.2. cyberscoop security news function
def cyberscoop():
    cyberscoop_url = 'https://www.cyberscoop.com/'                              # url
    cyberscoop_page = requests.get(cyberscoop_url, headers=headers)                              # page request
    cyberscoop_soup = BeautifulSoup(cyberscoop_page.text, 'html.parser')        # bs4 digest

    print('cyberscoop Latest Cybersecurity News')
    cyberscoop_cntr = 0
    for items in cyberscoop_soup.find_all('a', class_='article-thumb__title'):  # search loop
        print(Back.LIGHTMAGENTA_EX + f' {cyberscoop_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get_text().strip()}")                             # print title
        print(Back.BLACK + ' Link: ' + Style.RESET_ALL + f"\t{items.get('href')}")                                     # print link
        cyberscoop_cntr += 1
    print('\n')
    # ---------------------------------------------------------------


# 2.3. krebs on security news function
def krebs():
    krebs_url = 'https://krebsonsecurity.com'
    krebs_page = requests.get(krebs_url, headers=headers)                                        # make request to url
    krebs_soup = BeautifulSoup(krebs_page.text, 'html.parser')                  # bs4 digest

    print('Krebs on Security Latest Cybersecurity News')
    krebs_cntr = 0
    for items in krebs_soup.find_all("a", rel='bookmark'):                                                              # search loop
        print(Back.LIGHTBLACK_EX + f' {krebs_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get_text().strip()}")        # article title
        print(Back.WHITE + Fore.BLACK + ' Link: ' + Style.RESET_ALL + f"\t{items.get('href')}")                         # article link
        krebs_cntr += 1
    print('\n')
    # ---------------------------------------------------------------


# 2.4. motherboard security news function
def motherboard():
    mother_url = 'https://motherboard.vice.com/en_us/topic/hacking'             # url
    mother_page = requests.get(mother_url, headers=headers)                                      # page request
    mother_soup = BeautifulSoup(mother_page.text, 'html.parser')                # bs4 digest

    print('MOTHERBOARD Latest Cybersecurity News')
    mother_cntr = 0
    for items in mother_soup.find_all('a', class_='topics-card__heading-link'):
        print(Back.LIGHTBLACK_EX + f' {mother_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get_text().strip()}")       # article title
        print(Back.WHITE + Fore.BLACK + ' Link: ' + Style.RESET_ALL + f"\t{items.get('href')}")                         # print link
        mother_cntr += 1
    print('\n')

    # ---------------------------------------------------------------


# 2.5. Kapersky Securelist security news function
def securelist():
    seclist_url = 'https://securelist.com/'                                       # url
    seclist_page = requests.get(seclist_url, headers=headers)                                      # page request
    seclist_soup = BeautifulSoup(seclist_page.text, 'html.parser')                # bs4 digest

    print('Securelist Latest Cyber Security News')
    seclist_cntr = 0
    for items in seclist_soup.find_all(class_='entry-title'):                     # search loop
        a_tag = items.a                                                           # scrape a tags
        a_title = a_tag.get('title')                                              # scrape title
        a_link = a_tag.get('href')                                                # scrape links
        print(Back.GREEN + f' {seclist_cntr} ' + Style.RESET_ALL + f'\tTitle: {a_title}')
        print(Back.RED + ' Link: ' + Style.RESET_ALL + f'\t{a_link}')
        seclist_cntr += 1
    print('\n')

    # ---------------------------------------------------------------


# 2.6. zdnet security news function
def zdnet():
    zdnet_url = 'https://www.zdnet.com/topic/security'                          # url
    zdnet_page = requests.get(zdnet_url, headers=headers)                                        # page request
    zdnet_soup = BeautifulSoup(zdnet_page.text, 'html.parser')                  # bs4 digest
    zdnet_latest_news = str(zdnet_soup.find_all('div', id='latest'))            # latest news text
    bleep_soup2 = BeautifulSoup(zdnet_latest_news, 'html.parser')               # bs4 digest of latest news

    print('ZDNet Latest Cyber Security News')
    zdnet_cntr = 0
    for items in bleep_soup2.find_all('a', class_='thumb'):                         # search loop
        print(Back.LIGHTRED_EX + f' {zdnet_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get('title')}")    # print titles
        print(Back.BLACK + ' Link: ' + Style.RESET_ALL + f"\thttps://www.zdnet.com{items.get('href')}")     # print link
        zdnet_cntr += 1
    print('\n')

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

