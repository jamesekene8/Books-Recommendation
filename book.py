from bs4 import BeautifulSoup
import requests
import csv


class Scraper:
    def __init__(self):
        print("Initializing Scaper...")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
        self.header = ["title", "url", "author", "year", "price"]

    def selfHelpBooks(self):
        with open('books.csv', 'a+', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(self.header)
            for p in range(2, 74):
                amazonSite = requests.get(
                    f'https://www.amazon.co.uk/s?i=stripbooks&rh=n%3A275645&fs=true&page={p}&qid=1682881312&ref=sr_pg_{p}', headers=self.headers)
                soup = BeautifulSoup(amazonSite.text, "html.parser")
                searchResult = soup.find_all('div', class_="s-result-list")[0]
                for i in range(1, 20):
                    bookTitle = soup.find_all(
                        "h2", class_="a-size-mini")[i].find_all("span", class_="a-size-medium")[0].text
                    bookURL = "https://www.amazon.co.uk" + soup.find_all(
                        "h2", class_="a-size-mini")[i].find_all("a", class_="s-underline-link-text")[0]["href"]

                    bookAuthor = soup.find_all("div", class_="s-title-instructions-style")[i].find_all("div", class_="a-color-secondary")[
                        0].find_all("div", class_="a-row")[0].find_all("a", class_="s-underline-link-text")
                    try:
                        bookAuthor = soup.find_all("div", class_="s-title-instructions-style")[i].find_all("div", class_="a-color-secondary")[
                            0].find_all("div", class_="a-row")[0].find_all("a", class_="s-underline-link-text")[0].text
                    except:
                        bookAuthor = soup.find_all("div", class_="s-title-instructions-style")[i].find_all(
                            "div", class_="a-color-secondary")[0].find_all("div", class_="a-row")[0].find_all("span", "a-size-base")[1].text
                    try:
                        bookYear = soup.find_all("div", class_="s-title-instructions-style")[i].find_all("div", class_="a-color-secondary")[
                            0].find_all("div", class_="a-row")[0].find_all("span", "a-text-normal")[0].text
                    except:
                        bookYear = "Unknown"
                    bookPrice = soup.find_all(
                        "span", class_="a-price")[i].find_all("span", class_="a-offscreen")[0].text

                    writer.writerow(
                        [bookTitle, bookURL, bookAuthor, bookYear, bookPrice])
