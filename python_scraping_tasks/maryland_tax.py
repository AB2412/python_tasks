import requests
from bs4 import BeautifulSoup
import pdb
import os
import time
import glob
import csv

def maryland_tax():
  # url = "https://garrett.marylandtaxsale.com/index.cfm?folder=auctionResults&mode=preview"
  # main_page = requests.get(url)
  # print(f"=================={main_page}===============")
  # page_no = 1
  # while True:
  #   data = {
  #   'loginID': '00',
  #   'folder': 'auctionResults',
  #   'itemIDList': '',
  #   'itemSetIDList': '',
  #   'interest': '',
  #   'premium': '',
  #   'justFirstCertOnGroups': '1',
  #   'doSearch': 'true',
  #   'pageNum': f'{str(page_no)}',
  #   'orderBy': 'AdvNum',
  #   'orderDir': 'asc',
  #   'task': '',
  #   'mode': 'preview',
  #   }
  #   pagination_page = requests.get(url, data=data)
  #   page_response = BeautifulSoup(pagination_page.text, "html.parser")
  #   hrefs = [a['href'] for row in page_response.select('tbody tr') for parcel_td in row.select('td.parcel') for a in parcel_td.find_all('a', href=True)]
  #   for inner_url in hrefs:
  #     inner_page = requests.get(inner_url)
  #     os.makedirs("maryland_tax") if not os.path.exists("maryland_tax") else None
  #     file_path = f'maryland_tax/{inner_url.split("=")[-1]}.html'
  #     with open(file_path, 'w', encoding="utf-8") as file:
  #       file.write(inner_page.text)
  #       file.close()
  #   pagination_num = page_response.select("#pagiNext")[0].get_text(strip=True)
  #   if pagination_num == '':
  #     break
  #   page_no += 1
  parse_and_make_csv()

def parse_and_make_csv():
  csv_headers = get_csv_headers()
  html_files = glob.glob(os.path.join("maryland_tax", '*.html'))
  with open('mayland_tax_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()
    for file_path in html_files:
      with open(file_path, 'r') as file:
        page_body = BeautifulSoup(file, "html.parser")
        data_dict = {}
        data_dict["State"] = "Maryland"
        data_dict["County"] = "Garrett County"
        address = page_body.select('#cphMainContentArea_ucSearchType_wzrdRealPropertySearch_query_ucDetailsSearch_query_dlstDetaisSearch_lblMailingAddress_0')[0].decode_contents().strip().replace("-","").split("<br/>")
        data_dict["Property Address"] = " ".join(address)
        data_dict["Property City"], data_dict["Property State"], data_dict["Property Zip Code"] = clean_address(data_dict["Property Address"])
        data_dict["Property ID"] = page_body.select('#cphMainContentArea_ucSearchType_wzrdRealPropertySearch_query_ucDetailsSearch_query_dlstDetaisSearch_lblDetailsStreetHeader_0')[0].get_text(strip=True).split("-")[-1]
        # pdb.set_trace()
        writer.writerow(data_dict)

def clean_address(address):
  return address.split()[-3:]


def get_csv_headers():
  return [
      "State",
      "County",
      "Property Address",
      "Property City",
      "Property State",
      "Property Zip Code",
      "Property ID",
    ]





maryland_tax()