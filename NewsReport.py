import argparse                                             # imports
from requests_html import HTMLSession
session = HTMLSession()                                     # https-requests requisite


def bleep():
    r = session.get('https://www.bleepingcomputer.com/')    # make/store https request
    crawler = r.html.find('#nlatest', first=True)           # crawl through request
    links = crawler.absolute_links                          # find article links

    print('[+_._+] Bleeping Computer')                          # Display results
    for i in links:
        print(f'\t[-] Article: {i}')


def krebs():
    r = session.get('https://krebsonsecurity.com/')         # make/store https request
    crawler = r.html.find('#recent-posts-3', first=True)    # crawl through request
    links = crawler.absolute_links                          # find article links

    print('[+_._+] Krebs')                                      # Display results
    for i in links:
        print(f'\t[-] Article: {i}')


def motherboard():
    r = session.get('https://motherboard.vice.com/en_us/topic/hacking')     # make/store https request
    crawler = r.html.absolute_links                                         # crawl through the request/find links
    links = []                                                              # create empty list
    for x in crawler:
        links.append(x)                                                     # for all links, add to empty list

    print('[+_._+] Motherboard')                                                # Display results
    for y in links:
        if "/en_us/article/" in y:                                          # print all article
            print(f'\t[-] Article: {y}')


# 3. main argument function
def main():
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Description......')
    # 3.2. define flags
    parser.add_argument(
                        "--outlet",
                        choices=['BleepingComputer', 'Krebs', 'Motherboard', 'All'],
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
    elif x == 'all':
        bleep()
        krebs()
        motherboard()


main()
