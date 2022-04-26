from html.entities import html5
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with: ")
unfamiliar_skills = input(">")
print(f"Filtering out {unfamiliar_skills}")


def find_jobs():
    # "connecting" to a website
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            # get rid of empty space
            company_name = job.find(
                "h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find(
                "span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfamiliar_skills not in skills:
                with open(f"Posts/{index}.txt", "w") as f:
                    # .strip gets ride of space at beginning and end
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")
                print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        find_jobs()
        minutes = 10
        print(f"Waiting {minutes} minutes...")
        time.sleep(minutes * 60)
