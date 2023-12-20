from datetime import date, timedelta
import requests
import pandas as pd

# Calculate the start date (25 days ago)
start_date = date.today() - timedelta(days=25)

# Iterate from start_date to today
for n in range(26):
    crawl_date = (start_date + timedelta(n)).strftime("%b%d%Y")
    url = 'https://www.fpi.nsdl.co.in/web/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_'+crawl_date+'.html'
    print(url)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    html = requests.get(url, headers=headers, timeout=30).content

    try:
        df_list = pd.read_html(html)
        tablez = df_list[0]
        json_data = tablez.to_json(orient = "split")
        print(json_data)

        date_str = (start_date + timedelta(n)).strftime("%b-%d-%Y")
        API_URL = "https://trade.zahiralam.com/fii-dii/get-nsdl-sectore-invest-data-of-fpi-fii"
        data = {'json_data':json_data, 'date':date_str, 'server':'hostinger'} 
        r = requests.post(url = API_URL, data = data)
    except ValueError:
        print(f"No table found for {url}")
