[![Build Status](https://github.com/jonakoudijs/feeds/actions/workflows/deploy.yml/badge.svg)](https://github.com/jonakoudijs/feeds/actions)
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

| Name       | Endpoint | Website | Status |
|------------|----------|---------|--------|
| Stackshare | [https://feeds.koudijs.app/stackshare](https://feeds.koudijs.app/stackshare) | [https://stackshare.io/weekly](https://stackshare.io/weekly) | ![UptimeRobot Status](https://img.shields.io/uptimerobot/status/m793025111-ebbb100cd61049252d097731) |
| HUMAN | [https://feeds.koudijs.app/human](https://feeds.koudijs.app/human) | [https://human.nl/lees](https://human.nl/lees) | ![UptimeRobot Status](https://img.shields.io/uptimerobot/status/m793025109-e363b28f5eda97bbb7fffc99) |

The feeds are RSS only (not Atom or an other format).

## Deployment

Hosting these feeds yourself can easily be done on most serverless offerings. These
feeds run on Google Cloud Functions and new versions of the code are deployed
automatically via [Github Actions](https://github.com/jonakoudijs/feeds/actions).

This can easily be manually deployed (with the correct credentials) by using the `gcloud` cli:
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
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
functions-framework --target main --debug
```
