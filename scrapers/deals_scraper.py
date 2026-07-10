from selenium.webdriver.common.by import By
from selenium_driver.selenium_driver_Setup import get_Driver



def scrape_deals():

    # Initialize and configure the Selenium WebDriver 
    driver = get_Driver()

    # Store all scraped product details
    deals_list = []

    try:
        # Open the Amazon search results page
        driver.get("https://www.amazon.in/s?k=laptop")

        # Wait for page elements to be loaded
        driver.implicitly_wait(6)

        # Locate all product cards on the search results page
        products = driver.find_elements(By.XPATH, "//div[contains(@data-component-type,'s-search-result')]")

        # Extract information from each product card
        for product in products:
            
            try:
                
                # Get the product title
                title = product.find_element(By.CSS_SELECTOR, "h2 span").text

                # Get the product URL
                link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

                # Try to extract the product price
                try:
                    price = product.find_element(By.CLASS_NAME, "a-price-whole").text
                
                except:

                    # Use a default value if the price is unavailable
                    price = "N/A"

                # Save the extracted product information
                deals_list.append({
                    "title": title,
                    "price": price,
                    "link": link
                })

            except:

                # Skip the current product if required data can't be extracted
                continue

    except Exception as e:
        print("Error scraping deals:", e)

    finally:
        driver.quit()

    return deals_list
