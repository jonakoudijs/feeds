# modules
import requests
import datetime
import pytz
from bs4 import BeautifulSoup

# parse Stackshare
def stackshare():
    source = "https://stackshare.io/weekly"

    page = requests.get(source)
    soup = BeautifulSoup(page.content, "html.parser")

    parent = soup.find("table")
    entries = parent.find_all("tr")
    letters = []

    for entry in entries:
        header = entry.find("th")

        if not header:
            block = entry.find_all("td")
            cell1 = block[0].find("a")
            cell2 = block[1].find("a")

            url = cell1["href"]
            title = cell2.text

            date = cell1.text
            date = date.split("/")
            date = datetime.datetime(int(date[2]), int(date[0]), int(date[1]), tzinfo=pytz.UTC)

            object = {
                "link"  : url,
                "title" : title,
                "content" : title,
                "published" : date
            }

            letters.append(object)

    return letters


# parse HUMAN
def human():
    source = "https://www.human.nl/lees"

    page = requests.get(source)
    soup = BeautifulSoup(page.content, "html.parser")

    parent = soup.find("ul", {"id": "browsable-news-overview"})
    entries = parent.find_all("li")
    articles = []

    for entry in entries:
        url = entry.find("a")
        url = "https://www.human.nl/" + url["href"]

        article = entry.find("article")

        title = article.find("h4", {"class": "complex-teaser-title"})
        title = title.text

        date = article.find("div", {"class": "complex-teaser-data"})
        date = human_date(date.text)
        date = datetime.datetime(date["year"], date["month"], date["day"], tzinfo=pytz.UTC)

        summary = article.find("p", {"class": "complex-teaser-summary"})
        summary = summary.text

        object = {
            "link"  : url,
            "title" : title,
            "content" : summary,
            "published" : date
        }

        articles.append(object)

    return articles

def human_date(input):
    months = {
        "januari"   : "01",
        "februari"  : "02",
        "maart"     : "03",
        "april"     : "04",
        "mei"       : "05",
        "juni"      : "06",
        "juli"      : "07",
        "augustus"  : "08",
        "september" : "09",
        "oktober"   : "10",
        "november"  : "11",
        "december"  : "12"
    }

    date = input.split(" ")
    date = {
        "day"   : int(date[0].zfill(2)),
        "month" : int(months[date[1]]),
        "year"  : int(date[2])
    }

    return date