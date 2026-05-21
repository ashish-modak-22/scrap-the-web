from selenium.webdriver.common.by import By
from selenium_driver.selenium_driver_Setup import get_Driver


def scrape_job():

    driver = get_Driver()

    jobs_list = []

    try:
        driver.get("https://remoteok.com/remote-python-jobs")

        driver.implicitly_wait(10)

        jobs = driver.find_elements(
            By.CSS_SELECTOR,
            "a.preventLink"
        )

        print("TOTAL JOBS FOUND:", len(jobs))

        for job in jobs:

            try:
                title = job.find_element(
                    By.CSS_SELECTOR,
                    "h2[itemprop='title']"
                ).text

                link = job.get_attribute("href")

                jobs_list.append({
                    "title": title,
                    "company": "RemoteOK",
                    "link": link
                })

            except:
                continue

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

    return jobs_list