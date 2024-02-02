import requests
from server.models import Provider, Model, Price
from bs4 import BeautifulSoup

PRICING_PAGES = [
    "https://docs.perplexity.ai/docs/pricing",
    "https://www.together.ai/pricing",
    "https://docs.mistral.ai/platform/pricing/",
    "https://openai.com/pricing",
    "https://docs.endpoints.anyscale.com/pricing/",
    "https://aws.amazon.com/de/bedrock/pricing/",
    "https://azure.microsoft.com/de-de/pricing/details/cognitive-services/openai-service/",
]

# TODO add more for randomization
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
]

headers = {
    "User-Agent": USER_AGENTS[0]
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.content, "html.parser")
price_element = soup.find("ul", class_="pricing-list")
print(price_element)
