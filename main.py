from scrapers.job_scraper import scrape_job
from scrapers.deals_scraper import scrape_deals
from utils.data_filter import remove_Duplicates
from utils.json_manager import json_save



def main():

    # Display a welcome message when the bot starts 
    print("---------- Your smart web bot is started ----------\n")

    
    # Keep the bot running until the user chooses to exit
    while True:

        # The available menu options 
        print("\n----- Menu Underlisted: -----")
        print("1. Scrape the Jobs")
        print("2. Scrape the Deals")
        print("3. Exit the Bot")

        choice = input("\nEnter your choice ----> 1/2/3: ")

        
        # Handle job scrapping
        if choice == "1":
            print("\nOk, you want to scrape the job details.....\n")

            # Scrape job listings
            jobs = scrape_job()

            # Check if any jobs were found
            if not jobs:
                print("Sorry, we haven't found any jobs at the moment!")
                continue

            jobs = remove_Duplicates(jobs, "title")
            json_save("data/jobs.json", jobs)

            print(f"Jobs saved successfully and the number of jobs saved is: {len(jobs)}")

            for job in jobs[:10]:
                print(job)

        elif choice == "2":
            print("\nOk, you want to scrape the deal details.....\n")

            deals = scrape_deals()

            if not deals:
                print("Sorry, we haven't found any deals at the moment!")
                continue

            deals = remove_Duplicates(deals, "title")
            json_save("data/deals.json", deals)

            print(f"Deals saved successfully and the number of deals saved is: {len(deals)}")

            for deal in deals[:10]:
                print(deal)

        elif choice == "3":
            print("\nExiting the bot. Have a nice day!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

    
