import requests
import config
from bs4 import BeautifulSoup

cookies = {
    '$Cookie: SignOnDefault': '',
    'PS_DEVICEFEATURES': '',
    '_ga': 'GA1.2.1998562932.1611697475',
    'concordia-cookie': 'nGOyP76CZ4eBOsPKhoLgIFyUFDkMgO-Z\\u0021802858945',
    'ExpirePage': 'https://my.concordia.ca/psp/upprpr9/',
    'PS_LOGINLIST': 'https://my.concordia.ca/upprpr9',
    'PS_TOKEN': 'qQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AgQg4AC4AMQAwABTm8i7sJ0GIx2xIJ91DU3NV5VlSQWkAAAAFAFNkYXRhXXicZYtBDkBAEARrEUdv8AFiLZajA26yCXdv8S+P0/ZqOqnuzPTcQJYmxsifhDhloPlpwOEZpZ58YWejCBysnFwEZrpWtRZLFb1S8pGOWhsvOr1/edR9Ei28PWQNEQ==',
    'ps_theme': 'node:EMPL portal:EMPLOYEE theme_id:PAPPBR_THEME_TANGERINE accessibility:N',
    'HPTabName': 'CU_MY_FRONT_PAGE2',
    'HPTabNameRemote': '',
    'psback': '"url":"https%3A%2F%2Fmy.concordia.ca%2Fpsp%2Fupprpr9%2FEMPLOYEE%2FEMPL%2Fh%2F%3Ftab%3DCU_MY_FRONT_PAGE2" "label":"Home" "origin":"PIA"',
    'https%3a%2f%2fmy.concordia.ca%2fpsp%2fupprpr9%2femployee%2fempl%2frefresh': 'list:%20%3Ftab%3Dcu_campus_services%7C%3Frp%3Dcu_campus_services%7C%3Ftab%3Dremoteunifieddashboard%7C%3Frp%3Dremoteunifieddashboard%7C%7C%7C',
    'PS_TOKENEXPIRE': '17_Feb_2021_23:07:58_GMT',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://fis.encs.concordia.ca',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://fis.encs.concordia.ca/helpdesk-cgi/available-hosts.cgi',
    'Accept-Language': 'en-US,en-CA;q=0.9,en;q=0.8',
}

data = {
  'login_name': config.ENCS_LOGIN_NAME,
  'user_pass': config.ENCS_PASSWORD,
  'Authenticate': 'Authenticate'
}

url = "https://fis.encs.concordia.ca/helpdesk-cgi/available-hosts-result.cgi"

s = requests.Session()

response = s.post(url=url, headers=headers, cookies=cookies, data=data)

soup = BeautifulSoup(response.content, 'html.parser')

tags = soup.find_all("h3")

print(tags)

