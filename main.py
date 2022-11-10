# modules
import functions_framework
import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

# functions
from functions.feed import rss
from functions.source import stackshare, human

@functions_framework.http
def main(request):
    # parse uri path
    path = request.path
    path = path.split("/")
    path.pop(0)

    if path[0] == "stackshare":
        headers = { 'Content-Type': 'application/rss+xml' }
        source = stackshare()
        feed = rss(
            title = "Stackshare",
            link = "https://feeds.koudijs.app/stackshare",
            description = "Stackshare Weekly",
            items = source
        )
        return (feed, 200, headers)

    if path[0] == "human":
        headers = { 'Content-Type': 'application/rss+xml' }
        source = human()
        feed = rss(
            title = "HUMAN",
            link = "https://feeds.koudijs.app/human",
            description = "Human Lees",
            items = source
        )
        return (feed, 200, headers)


    return ("Page not found", 404, { 'Content-Type': 'text/html' })
