import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

# Enter the username of the account here
userNameOfAccount = "elonmusk"

# Adjust the total number of scrolls
Total_scrolls = 50

link = f"https://twitter.com/{userNameOfAccount}"

# Constants for scroll optimization
SCROLL_AMOUNT = 300
SCROLL_DELAY = 4

def scroll_page(page, total_scrolls, scroll_amount, scroll_delay):
    for _ in range(total_scrolls):
        page.evaluate(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(scroll_delay)

def scrape_tweets(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    all_posts = soup.find_all('div', {'data-testid': 'cellInnerDiv'})
    data = []
    for post in all_posts:
        check_retweet = post.find('div', {'role': 'link'})
        if not check_retweet:
            try:
                tweet = post.find('div', {'data-testid': 'tweetText'}).get_text(strip=True)
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

def automate_twitter_data_scraping(user_account, total_scrolls, scroll_amount, scroll_delay):
    link = f"https://twitter.com/{user_account}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(link, timeout=500000)

        scroll_page(page, total_scrolls, scroll_amount, scroll_delay)

        page_content = page.content()

        browser.close()

    data = scrape_tweets(page_content)
    df = pd.DataFrame(data)

    # Removing duplicates...
    df.drop_duplicates(inplace=True)
    df.to_excel('output.xlsx', index=False)
    print("Data scraping completed successfully!")

if __name__ == "__main__":
    automate_twitter_data_scraping(userNameOfAccount, Total_scrolls, SCROLL_AMOUNT, SCROLL_DELAY)
