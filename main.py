import requests
from bs4 import BeautifulSoup
from random import randint

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
# Print the page for review on how to parse
print(soup.prettify())

# Get all the jobs on the page
jobs = soup.find_all("div", class_="card-content")
scraped_jobs = []
job_index = 1
for job in jobs:
    try:
        title_header = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")
        date_posted = job.find("time")
        link = job.find("a", class_="card-footer-item")
        scraped_jobs.append({
            "id": job_index,  # randint(1, 1000),
            "title": title_header.text,
            "company": company.text,
            "location": location.text.strip(),
            "date": date_posted.text.strip(),
            "link": link.get("href").strip()
        })

        job_index += 1
    except AttributeError as error:
        print(error.message)
        break

print(scraped_jobs)
