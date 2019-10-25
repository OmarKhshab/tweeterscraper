import json
from Util import formatDay
from scraper import Chrome_driver , scrolling, tweetScraper


def main():
    inputWord = input("Enter the words: ")
    startDate = input("Enter the start date in (YYYY-MM-DD): ")
    endDate = input("Enter the end date in (YYYY-MM-DD): ")
    driver = Chrome_driver()
    scrolling(driver, formatDay(startDate), formatDay(endDate), inputWord)
    tweetList = tweetScraper(driver)
    driver.quit()
    

    with open('dataret.json', 'w') as outfile:
        json.dump([obj.__dict__ for obj in tweetList], outfile)

if __name__ == "__main__":
    main()