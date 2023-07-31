# Twitter Data Scraper

## Features

**Automated Twitter Data Scraping:** The script automatically navigates to the Twitter account specified in the script and scrapes tweet data, including likes, comments, and retweets.

**Scroll Optimization:** The script implements scroll optimization techniques to load and scrape a specified number of tweets efficiently.

**Error Handling:** The script gracefully handles errors to ensure the scraping process continues even if some tweets are inaccessible or unavailable.

**Data Deduplication:** Before saving the scraped data to an Excel file, the script removes duplicate records to maintain data integrity.

## Requirements

Before running the script, make sure you have the following requirements installed:

### Python 3.x

**Playwright** library (pip install playwright)
**BeautifulSoup** library (pip install beautifulsoup4)
**Pandas** library (pip install pandas)

## Usage

Clone the repository or download the Python script (twitter_scraper.py) to your local machine.

Install the required libraries mentioned in the ``requirements.txt`` section using pip.

Open the ``twitter_scraper.py`` script in your preferred Python editor or IDE.

Modify the ``userNameOfAccount`` variable to specify the Twitter account from which you want to scrape data.

Adjust the ``Total_scrolls`` constant to set the total number of scrolls for data scraping.

Customize the ``SCROLL_AMOUNT and SCROLL_DELAY`` constants to optimize scrolling performance.

Run the script by executing the command: ``python twitter_scraper.py.``

After successful execution, the scraped tweet data will be saved in the output.xlsx file in the same directory.

### Notes

It is important to respect Twitter's usage policies and terms of service when using this script for data scraping. Be mindful of the frequency of scraping to avoid any potential account restrictions.

The number of tweets that can be scraped is subject to Twitter's limitations, and the script may not be able to scrape all historical tweets due to API restrictions.

The script is designed to run in headless mode, meaning it will not open a browser window during execution. If you want to observe the scraping process, you can set ``headless=False`` in the ``p.chromium.launch()`` function.

Feel free to modify and customize the script as per your specific requirements.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

#### Disclaimer

This script is intended for educational and personal use only. The developers are not responsible for any misuse or violation of Twitter's policies by users of this script. Use it responsibly and at your own risk.
