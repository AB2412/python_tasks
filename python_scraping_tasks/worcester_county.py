import requests
from bs4 import BeautifulSoup
import pdb
import os
import time
import glob
import csv

def worcester_county():
  page_no = 1
  while True:
    print(f"===================={page_no}====================")
    url = f'https://www.worcesterma.gov/finance/liens-auctions/public-auctions/tax-foreclosures?func=view;pn={page_no}'
    main_page = requests.get(url)
    main_page_response = BeautifulSoup(main_page.text, 'html.parser')
    a_tags = main_page_response.select('.list-group .row .col-md-3 a')
    outer_links = ['https://www.worcesterma.gov' + a['href'] for a in a_tags if 'href' in a.attrs]
    for inner_link in outer_links:
        inner_link_response = requests.get(inner_link)
        page_body = BeautifulSoup(inner_link_response.text, "html.parser")
        ftt_number = get_next_element(page_body, "FTT#")
        print(f'-------------{ftt_number}--------------')
        os.makedirs("html_file") if not os.path.exists("html_file") else None
        file_path = f'html_file/{ftt_number}.html'
        with open(file_path, 'w', encoding="utf-8") as file:
          file.write(inner_link_response.text)
          file.close()
    disabled_next = main_page_response.select_one('li.disabled a[title="Next"]')
    if disabled_next:
            break
    page_no += 1
  parse_and_make_csv("html_file")

def parse_and_make_csv(path):
    html_files = glob.glob(os.path.join("html_file", '*.html'))
    headers = get_headers()
    with open('worcester_county_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=headers)
      writer.writeheader()
      for file_path in html_files:
        with open(file_path, 'r') as file:
          page_body = BeautifulSoup(file, "html.parser")
          data_dict = {}
          data_dict["State"] = "Maryland"
          data_dict["County"] = "Worcester"
          data_dict["Property Address"] = get_next_element(page_body, "Address")
          data_dict["Property ID"] = get_next_element(page_body, "FTT#")
          data_dict["Tax Value"] = get_next_element(page_body, "Valuation")
          writer.writerow(data_dict)

def get_next_element(page_body, text_value):
  return [col.find_next_sibling() for row in page_body.select('.cow-row-striped') for col in row.select('.col-md-3') if col.get_text(strip=True) == text_value][0].get_text(strip=True)


def get_headers():
  return [
    "State",
    "County",
    "Property Address",
    "Property ID",
    "Tax Value",
  ]

try:
  worcester_county()
except Exception as e:
  time.sleep(4)
  worcester_county()
