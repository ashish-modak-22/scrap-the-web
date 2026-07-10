from selenium.webdriver.common.by import By
from selenium_driver.selenium_driver_Setup import get_Driver



def scrape_deals():

    # Initialize and configure the Selenium WebDriver 
    driver = get_Driver()

    # Store all scraped product details
    deals_list = []

    try:
        driver.get("https://www.amazon.in/s?k=laptop")

        driver.implicitly_wait(6)

        products = driver.find_elements(By.XPATH, "//div[contains(@data-component-type,'s-search-result')]")

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, "h2 span").text
                link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

                try:
                    price = product.find_element(By.CLASS_NAME, "a-price-whole").text
                except:
                    price = "N/A"

                deals_list.append({
                    "title": title,
                    "price": price,
                    "link": link
                })

            except:
                continue

    except Exception as e:
        print("Error scraping deals:", e)

    finally:
        driver.quit()

    return deals_list
