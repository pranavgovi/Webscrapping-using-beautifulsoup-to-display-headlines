import sys
import time
from bs4 import BeautifulSoup
import requests

try:

    page = requests.get(
        'https://timesofindia.indiatimes.com/home/headlines')  # this might throw an exception if something goes wrong.

except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK:', url)
    print(error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('span', attrs={'class': 'w_tle'})
for i in links:
    print(i.text)
    print("\n")