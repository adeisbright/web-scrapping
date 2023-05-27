import requests
from bs4 import BeautifulSoup
import time


def get_jobs(url: str, labels: dict) -> list:
    '''
        Description :  Scrapes any given url to get job information
        Return : A list of jobs that can be stored for further processing 
    '''
    scraped_jobs = []
    try:
        page = requests.get(url)
        time.sleep(2)
        soup = BeautifulSoup(page.content, "html.parser")
        # Get all the jobs on the page

        jobs = soup.find_all(labels.get("job_tag"),
                             class_=labels.get("job_class"))

        job_index = 1

        for job in jobs:
            try:
                title_header = job.find(labels.get(
                    "title_tag"), class_=labels.get("title_class"))

                company = job.find(labels.get("company_tag"),
                                   class_=labels.get("company_class"))
                location = job.find(labels.get("location_tag"),
                                    class_=labels.get("location_class"))
                date_posted = job.find(labels.get("date_tag"))

                link = job.find(labels.get("link_tag"),
                                class_=labels.get("link_class"))

                scraped_jobs.append({
                    "id": job_index,
                    "title": title_header.text,
                    "company": company.text,
                    "location": location.text.strip(),
                    "date": date_posted.text.strip(),
                    "link": link.get("href").strip()
                })

                job_index += 1
            except AttributeError as error:
                print(error.message)
                return scraped_jobs
        return scraped_jobs
    except Exception as e:
        print(e)
        return scraped_jobs


job_dict = {
    "job_tag": "div",
    "job_class": "card-content",
    "title_tag": "h2",
    "title_class": "title",
    "company_tag": "h3",
    "company_class": "company",
    "location_tag": "p",
    "location_class": "location",
    "link_tag": "a",
    "link_class": "card-footer-item",
}

scraped_jobs = get_jobs("https://realpython.github.io/fake-jobs/", job_dict)

print(scraped_jobs)
