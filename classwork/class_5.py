import requests

URL = "https://sapkotarabindra.com.np/courses/python/miscellaneous/libraries/common-datetime-formats"
response = requests.get(URL)
print(response.status_code)

response_text = response.text
#print(response_text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response_text, "html.parser")
table_soup = soup.find("table")
#print(table_soup)

def parse_table(table_soup):
    table_rows = table_soup.find_all("tr")
    parsed_data = []
    for row in table_rows:
        row_record = []
        table_data = row.find_all(["th", "td"])
        for data in table_data:
            col_value = data.get_text(strip=True)
            row_record.append(col_value)
            parsed_data.append(row_record)
    return parsed_data

parsed_data = parse_table(table_soup)
print(parsed_data)