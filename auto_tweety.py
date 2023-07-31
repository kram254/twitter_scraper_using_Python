import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

# Enter the username of the account here
userNameOfAccount = "elonmusk"

# Constants for scroll optimization
SCROLL_AMOUNT = 300
SCROLL_DELAY = 2
MAX_SCROLLS = 100

def scroll_page(page, scroll_amount, scroll_delay):
    page.evaluate(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(scroll_delay)

def scrape_tweets(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    all_posts = soup.find_all('div', {'data-testid': 'tweet'})
    data = []
    for post in all_posts:
        try:
            tweet = post.find('div', {'data-testid': 'tweet'}).get_text(strip=True)
            comments = post.find('div', {'data-testid': 'reply'}).get_text(strip=True)
            likes = post.find('div', {'data-testid': 'like'}).get_text(strip=True)
            retweets = post.find('div', {'data-testid': 'retweet'}).get_text(strip=True)
        except AttributeError:
            continue
        data.append({
            'Likes': likes,
            'Tweet': tweet,
            'Comments': comments,
            'Re-tweets': retweets
        })
    return data

def automate_twitter_data_scraping(user_account, scroll_amount, scroll_delay, max_scrolls):
    link = f"https://twitter.com/{user_account}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(link, timeout=500000)

        scrolls = 0
        while scrolls < max_scrolls:
            scroll_page(page, scroll_amount, scroll_delay)
            scrolls += 1

        page_content = page.content()
        browser.close()

    data = scrape_tweets(page_content)
    df = pd.DataFrame(data)

    # Removing duplicates...
    df.drop_duplicates(inplace=True)

    # Saving to Excel
    df.to_excel('output.xlsx', index=False)
    print("Data scraping completed successfully!")

if __name__ == "__main__":
    automate_twitter_data_scraping(userNameOfAccount, SCROLL_AMOUNT, SCROLL_DELAY, MAX_SCROLLS)
