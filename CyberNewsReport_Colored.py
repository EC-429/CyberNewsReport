# 1. Imports
import argparse
import requests
from colorama import Style, Back, Fore
from bs4 import BeautifulSoup   # Documentation: crummy.com/software/BeautifulSoup/bs4/doc/


# 2.2. bleeping computer security news function
def bleep():
    bleep_url = 'https://www.bleepingcomputer.com/'
    bleep_page = requests.get(bleep_url)                            # make request to url
    bleep_soup = BeautifulSoup(bleep_page.text, 'html.parser')      # bs4 digest
    bleep_latest_news = str(bleep_soup.find_all(class_='tab-pane', id='nlatest'))     # save latest news text as variable
    bleep_soup2 = BeautifulSoup(bleep_latest_news, 'html.parser')         # gather text from saved variable

    bleep_titles = []                                               # empty lists to store titles
    bleep_links = []                                                # empty list to store links

    for items in bleep_soup2.find_all('img'):                       # search through text for title
        bleep_titles.append(items.get('alt'))                       # append list
    for items in bleep_soup2.find_all('a', class_='nmic'):          # search through text for link
        bleep_links.append(items.get('href'))                       # append to list

    print('Bleeping Computer Latest Cybersecurity News')
    bleep_cntr = 0                                                        # counter start at 0
    for x in bleep_titles:
        print(Back.BLUE + f' {bleep_cntr} ' + Style.RESET_ALL + f'\tTitle: {x}')                                        # print title for each item
        print(Back.LIGHTBLUE_EX + ' Link: ' + Style.RESET_ALL + f'\t{bleep_links[bleep_cntr]}')                         # print link using counter as iterator
        bleep_cntr += 1                                                   # counter iteration interval
    print('\n')
    # ---------------------------------------------------------------


# 2.5. cyberscoop security news function
def cyberscoop():
    cyberscoop_url = 'https://www.cyberscoop.com/'                              # url
    cyberscoop_page = requests.get(cyberscoop_url)                              # page request
    cyberscoop_soup = BeautifulSoup(cyberscoop_page.text, 'html.parser')        # bs4 digest

    print('cyberscoop Latest Cybersecurity News')
    cyberscoop_cntr = 0
    for items in cyberscoop_soup.find_all('a', class_='article-thumb__title'):  # search loop
        print(Back.LIGHTMAGENTA_EX + f' {cyberscoop_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get_text().strip()}")                             # print title
        print(Back.BLACK + ' Link: ' + Style.RESET_ALL + f"\t{items.get('href')}")                                     # print link
        cyberscoop_cntr += 1
    print('\n')
    # ---------------------------------------------------------------


# 2.1. krebs on security news function
def krebs():
    krebs_url = 'https://krebsonsecurity.com'
    krebs_page = requests.get(krebs_url)                            # make request to url
    krebs_soup = BeautifulSoup(krebs_page.text, 'html.parser')      # bs4 digest

    print('Krebs on Security Latest Cybersecurity News')
    krebs_cntr = 0
    for items in krebs_soup.find_all("a", rel='bookmark'):          # search loop
        print(Back.LIGHTBLACK_EX + f' {krebs_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get_text().strip()}")   # article title
        print(Back.WHITE + Fore.BLACK + ' Link: ' + Style.RESET_ALL + f"\t{items.get('href')}")                         # article link
        krebs_cntr += 1
    print('\n')
    # ---------------------------------------------------------------


# 2.3. motherboard security news function
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

    print('MOTHERBOARD Latest Cybersecurity News')
    mother_cntr = 0                                                                    # counter start at 0
    for x in mother_titles:
        print(Back.MAGENTA + f' {mother_cntr} ' + Style.RESET_ALL + f'\tTitle: {x}')   # print title for each item
        # print link using counter as iterator
        print(Back.WHITE + Fore.BLACK + ' Link: ' +
              Style.RESET_ALL +
              f'\thttps://motherboard.vice.com/en_us/topic/hacking{mother_links[mother_cntr]}')
        mother_cntr += 1
    print('\n')
    # ---------------------------------------------------------------


# 2.4. zdnet security news function
def zdnet():
    zdnet_url = 'https://www.zdnet.com/topic/security'                          # url
    zdnet_page = requests.get(zdnet_url)                                        # page request
    zdnet_soup = BeautifulSoup(zdnet_page.text, 'html.parser')                  # bs4 digest
    zdnet_latest_news = str(zdnet_soup.find_all('div', id='latest'))            # latest news text
    bleep_soup2 = BeautifulSoup(zdnet_latest_news, 'html.parser')               # bs4 digest of latest news

    print('ZDNet Latest Cyber Security News')
    zdnet_cntr = 0
    for items in bleep_soup2.find_all('a', class_='thumb'):                         # search loop
        print(Back.LIGHTRED_EX + f' {zdnet_cntr} ' + Style.RESET_ALL + f"\tTitle: {items.get('title')}")                                       # print titles
        print(Back.BLACK + ' Link: ' + Style.RESET_ALL + f"\thttps://www.zdnet.com/topic/security{items.get('href')}")     # print link
        zdnet_cntr += 1
    print('\n')

    # ---------------------------------------------------------------


# 3. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Description......')
    # 3.2. define flags
    parser.add_argument(
                        "--outlet",
                        choices=['BleepingComputer', 'cyberscoop', 'Krebs', 'Motherboard', 'ZDNet', 'All'],
                        type=str,
                        help="Enter a news outlet"
                        )
    # 3.3. save input
    args = parser.parse_args()
    # 3.4. pass input to data function
    x = str(args.outlet).lower()
    # function decision tree, based on input
    if x == 'bleepingcomputer':
        bleep()
    elif x == 'krebs':
        krebs()
    elif x == 'motherboard':
        motherboard()
    elif x == 'zdnet':
        zdnet()
    elif x == 'cyberscoop':
        cyberscoop()
    elif x == 'all':
        bleep()
        cyberscoop()
        krebs()
        motherboard()
        zdnet()
    else:
        print('Ooops! Must be smarter than the options menu to get the news. Try the -h flag.')


# 4. Call initial function in chain
main()

