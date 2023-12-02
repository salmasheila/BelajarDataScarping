import httpx
from selectolax.parser import HTMLParser


url ="https://www.rei.com/c/camping-and-hiking/f/scd-deals"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" }

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

# print(html.css_first("title").text())

# error handling
def extract_text(html, sel) :
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None
    
    
products = html.css("li.VcGDfKKy_dvNbxUqm29K")

# loop through data
for product in products:
    item = {
        "name" : extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),
        "price" : extract_text(product, "span[data-ui=sale-price]"),
        "saving" : extract_text(product, "div[data-ui=savings-percent-variant2]" )
    }
    print(item)