import requests
import time

session = requests.Session()

# NSE requires this header setup to behave like a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1'
}
session.headers.update(headers)

# Step 1: Make initial request to homepage to get cookies
home_url = "https://www.nseindia.com"
_ = session.get(home_url, timeout=10)
time.sleep(2)  # simulate delay like a browser

# Step 2: Request actual quote page
quote_url = "https://www.nseindia.com/get-quotes/equity?symbol=GAIL"
response = session.get(quote_url, timeout=10)

# Step 3: Get cookies
cookies = session.cookies
nsit = cookies.get('nsit')
nseappid = cookies.get('nseappid')

payload = {"nsit": nsit, "nseappid": nseappid}
print('payload from NSE:', payload)

# Step 4: Post to your API
API_URL = "https://trade.zahiralam.com/Fetch_Nse_Cookies/insertNsitAndnseappid"
headers = {'Content-Type': 'application/json'}

r = requests.post(API_URL, json=payload, headers=headers)
print('response from API:', r.text)
