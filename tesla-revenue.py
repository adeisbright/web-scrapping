import requests
from bs4 import BeautifulSoup
import time

url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

tesla_revenue_list = []
try:
    with open("tesla.html", "r") as tesla_file:
        soup = BeautifulSoup(tesla_file, "html.parser")
        print("File is availabe on disk......")
        tesla_revenue = soup.find_all("table", class_="historical_data_table")

        table_body = tesla_revenue[1].tbody

        for i, row in enumerate(table_body.children):
            if not isinstance(row, str):
                first_child = row.td
                revenue_date = first_child.string.strip()
                revenue_amount = first_child.next_sibling.next_sibling.string.strip()
                tesla_revenue_list.append({
                    "date": revenue_date,
                    "amount": revenue_amount
                })

except AttributeError as error:
    print(error)
except IOError as error:
    print("File is not available on disk, now fetching from web ....")
    page = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(page.content, "html.parser")
    with open("tesla.html", "w") as tesla_file:
        tesla_file.write(soup.prettify())

    print("File now stored, you can retry the process.")
except Exception as error:
    print(error)

print(tesla_revenue_list)
