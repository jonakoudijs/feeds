# modules
from feedgen.feed import FeedGenerator

# generate RSS feed
def rss(title, link, description, items = []):
    # create initial feed
    fg = FeedGenerator()
    fg.title(title)
    fg.link(href=link, rel='self')
    fg.description(description)

    # add items to feed
    for item in items:
        fe = fg.add_entry()
        fe.id(item["id"])
        fe.title(item["title"])

        if "content" in item:
            fe.content(item["content"])
        else:
            combined = item["title"] + "</br></br>" \
                       + "Source: " + "<a href=\"" + item["id"] \
                       + "\">" + item["id"] + "</a>"
            fe.content(combined)

        if "published" in item:
            fe.published(item["published"])

    # return generated feed
    feed = fg.rss_str(pretty=True)
    return feed
