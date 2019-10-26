import json
from Util import formatDay
from scraper import Chrome_driver , scrolling, tweetScraper


def main():
    inputWord = input("Enter the words: ") #screach keyword
    startDate = input("Enter the start date in (YYYY-MM-DD): ") # retrival start date
    endDate = input("Enter the end date in (YYYY-MM-DD): ") # retrival end date
    driver = Chrome_driver() #intailizing chrome driver
    scrolling(driver, formatDay(startDate), formatDay(endDate), inputWord) #reaching the bottomm the page
    tweetList = tweetScraper(driver) #retriving the page source
    driver.quit()
    

    with open('dataret.json', 'w') as outfile:
        json.dump([obj.__dict__ for obj in tweetList], outfile)

if __name__ == "__main__":
    main()