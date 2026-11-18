import csv
from bs4 import BeautifulSoup
import requests


def scrape_news_headlines(url):
  # Set headers to mimic a real browser request
  headers = {
      'User-Agent': (
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
          ' like Gecko) Chrome/120.0.0.0 Safari/537.36'
      )
  }

  try:
    print(f'Fetching data from {url}...')
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    news_data = []

    # BBC News article container selectors
    articles = soup.find_all('div', {'data-testid': 'card-text-wrapper'})

    for article in articles:
      # 1. Extract Headline (BBC uses h2 tags with specific testids or headings)
      headline_elem = article.find(['h2', 'p'], {'data-testid': 'card-headline'})
      headline = headline_elem.get_text(strip=True) if headline_elem else 'N/A'

      # 2. Extract Publication Date / Description if available
      date_elem = article.find('span', {'data-testid': 'card-metadata-lastupdated'})
      pub_date = date_elem.get_text(strip=True) if date_elem else 'N/A'

      # 3. Category (defaulting if not explicitly tagged)
      category = 'General'

      news_data.append([headline, pub_date, category])

    # Store data in a CSV file
    filename = 'realtime_news_headlines.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      # Write header
      writer.writerow(['Headline', 'Publication Date', 'Category'])
      # Write data rows
      writer.writerows(news_data)

    print(
        f'Successfully scraped {len(news_data)} articles and saved to'
        f' {filename}'
    )

  except requests.exceptions.RequestException as e:
    print(f'Network error occurred: {e}')
  except Exception as e:
    print(f'An error occurred during parsing: {e}')


# Example Execution
if __name__ == '__main__':
  # Real live target URL
  TARGET_URL = 'https://www.bbc.com/news'
  scrape_news_headlines(TARGET_URL)