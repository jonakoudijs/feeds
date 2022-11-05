# modules
import functions_framework
import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

# functions
from functions.feed import rss
from functions.source import stackshare

@functions_framework.http
def main(request):
    # parse uri path
    path = request.path
    path = path.split("/")
    path.pop(0)

    if path[0] == "stackshare":
        source = stackshare()
        feed = rss(
            title = "Stackshare",
            link = "https://feeds.koudijs.app/stackshare",
            description = "Stackshare Weekly",
            items = source
        )
        return feed


    return "Page not found"
