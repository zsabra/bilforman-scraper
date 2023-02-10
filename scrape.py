from bs4 import BeautifulSoup as BS
import urllib.request
import logging

baseurl = "https://xn--frmnsvrde-02ah5r.se"

html = urllib.request.urlopen(baseurl + "/formansvarde-bil")
soup = BS(html, "html.parser")
brands = soup.findAll('a', {'style': 'color:#303030'})

print("Namn;Märke;Typ;Pris;Förmånsvärde;Url")

for brand in brands:
    html = urllib.request.urlopen(baseurl + brand["href"])
    soup = BS(html, "html.parser")
    cars = soup.findAll('a', {'style': 'margin-top:1rem;'})
    for car in cars:
        html = urllib.request.urlopen(baseurl + car["href"])
        soup = BS(html, "html.parser")
        variants = soup.findAll('td', {'class': 'variant-row'})
        for variant in variants:
            engineEls = variant.select(".badge.badge-light")
            engines = ",".join(list(map(lambda item: item.text, engineEls)))
            namnEl = variant.select("div.col-10.font-weight-bold > a")
            priceEl = variant.select('.d-inline-block a')
            förmånsEl = variant.findAll('div', {'class': 'row'})[2].find("a")
            print(namnEl[0].text + ";" + brand.findAll("span", {"style": "font-size: 1.2em;font-weight: 600"})[0].text + ";" + engines + ";" + priceEl[0].text.strip() + ";" + förmånsEl.text.strip() + ";" + baseurl + namnEl[0]["href"])

