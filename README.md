[![CodeFactor](https://www.codefactor.io/repository/github/jonakoudijs/feeds/badge)](https://www.codefactor.io/repository/github/jonakoudijs/feeds)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Feeds

Custom RSS feeds created from various online sources that currently don't offer
them. I created these for personal use but are publicly available and are free
to use for everybody.

Keep in mind that most of these feeds are Dutch websites. If you have any
recommendations or requests let me know in a Github issue.

## RSS Feeds

The following RSS feeds are currently available:

| Name       | Endpoint | Website |
|------------|----------|---------|
| Stackshare | [https://feeds.koudijs.app/stackshare](https://feeds.koudijs.app/stackshare) | [https://stackshare.io/weekly](https://stackshare.io/weekly) |
| HUMAN | [https://feeds.koudijs.app/human](https://feeds.koudijs.app/human) | [https://human.nl/lees](https://human.nl/lees) |

## Deployment

Running these feeds yourself can easily be done most serverless offerings. These
feeds run on Google Cloud Functions and new versions of the code are deployed
automatically via [Github Actions](https://github.com/jonakoudijs/feeds/actions).

This can easily be manually deployed (with the correct credentials) by `gcloud` cli:
```
gcloud functions deploy my-function \
  --gen2 \
  --runtime=python310 \
  --region=europe-west1 \
  --entry-point=main \
  --trigger-http
```

## Development

Test locally by running the development server:
```
functions-framework --target main --debug
```
