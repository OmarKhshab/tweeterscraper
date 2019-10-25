from bs4 import BeautifulSoup
import datetime
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tweet import Tweet


def Chrome_driver():
    CDriver = webdriver.Chrome("C:\chromedriver")
    CDriver.wait = WebDriverWait(CDriver, 10)
    return CDriver

def scrolling(driver,startDay,endDay,word):
    url = "https://twitter.com/search?q="
    url += "{}%20".format(word)
    url += "since%3A{}%20until%3A{}&".format(startDay, endDay)
    url += "src=typd"
    driver.get(url)
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    loopCounter = 0
    while True:
        if loopCounter > 499:
            break; 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        loopCounter = loopCounter + 1
    
def tweetScraper (driver):
    try:
        tweeterDivs = driver.page_source
        obj = BeautifulSoup(tweeterDivs, "html.parser")
        allTweets = obj.find_all("div", class_="tweet")
        tweetList = []

        for tweet in allTweets:
          
            tweetText = tweet.find("p",class_="tweet-text").getText()
            screenName = tweet.find("strong", class_="fullname").getText()
            username = tweet.find(class_="username").getText()
            tweetId = tweet['data-tweet-id']
            userId = tweet['data-user-id']
            timestamp = tweet.find(class_="tweet-timestamp")['title']
           
            timestamp = datetime.datetime.strptime(timestamp.split('-')[1], " %d %b %Y")
            timestamp =  str(timestamp.date())
            tweetList.append(Tweet(tweetId,tweetText,username,userId,screenName,timestamp))
    

    except Exception as e:  
        print("Something went wrong!")
        driver.quit()

    return tweetList
