import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
from src.constants import GOOGLE_SEARCH_QUERY,LINK_LIMIT


def google_search_scrape(query):
    cleaned_url = []
    url = GOOGLE_SEARCH_QUERY.format(query)
    html = requests.get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "lxml")
        anchor_tags = soup.find_all("a")
        for anchor_tag in anchor_tags:
            href = anchor_tag.get("href")
            try:
                raw_url = re.search("(?P<url>https?://[^\s]+)", href)
                raw_url = raw_url.group(0)
                raw_url = raw_url.split("&")[0]
                domain = urlparse(raw_url)
                if re.search("google.com", domain.netloc):
                    continue
                else:
                    cleaned_url.append(raw_url)
            except:
                continue
    return cleaned_url[:LINK_LIMIT]
