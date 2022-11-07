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
        source = stackshare()
        feed = rss(
            title = "Stackshare",
            link = "https://feeds.koudijs.app/stackshare",
            description = "Stackshare Weekly",
            items = source
        )
        return feed

    if path[0] == "human":
        source = human()
        feed = rss(
            title = "HUMAN",
            link = "https://feeds.koudijs.app/human",
            description = "Human Lees",
            items = source
        )
        return feed


    return "Page not found"
