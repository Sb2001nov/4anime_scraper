from bs4 import BeautifulSoup
import requests
import concurrent.futures
import sys


def main(url):
    '''
        Main Function
    '''
    print('welcome to 4anime downloader link scraper')
    try:
        open("batch_links.txt", "w").close()
    except:
        pass

    ep_link = []
    url = url
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    ul = soup.find("ul", class_="episodes range active")

    for a in ul.find_all('a', href=True):
        ep_link.append(a['href'])
    print('total episord found : ', len(ep_link))
    def links(link):
        url = link
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        ul = soup.find_all('script', type='text/javascript')
        ep_vid_link = str(ul[13])
        with open('batch_links.txt', 'a') as file:
            file.write(ep_vid_link[79:-62] + '\n')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(links, ep_link)
    print('finished scraping')

if __name__ == "__main__":
    main(sys.argv[1])
