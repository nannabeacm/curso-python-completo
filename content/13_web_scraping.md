# 13. Spidey-Sense: Web Scraping (BeautifulSoup)

> "When I put on the mask, I can focus. It makes me a better me." - Miles Morales

Sometimes there is no API. The data is just visible on the website. We interpret the HTML directly using **Web Scraping**.

**Prerequisites:**
```bash
pip install beautifulsoup4 requests
```

## 1. The Strategy
1. **GET** the page content (Requests).
2. **PARSE** the HTML (BeautifulSoup).
3. **EXTRACT** the data.

## 2. Basic Scraping
Imagine a page with this HTML:
```html
<div class="hero">
    <h1>Spiderman</h1>
    <p class="alias">Peter Parker</p>
</div>
```

**The Code:**
```python
import requests
from bs4 import BeautifulSoup

url = "http://example.com/heroes"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Finding elements
hero_name = soup.find('h1').text
real_name = soup.find('p', class_='alias').text

print(f"{hero_name} is {real_name}")
```

## 3. Finding Multiple Items
`find_all` returns a list.

```python
# HTML: <li>Iron Man</li> <li>Thor</li>
heroes = soup.find_all('li')

for h in heroes:
    print(h.text)
```

## 4. Ethical Responsibility (The Sokovia Accords)
- **Do not** spam requests (DDoS).
- **Check** `robots.txt` (e.g., `google.com/robots.txt`).
- If an API exists, **use it instead**.

---
**Next Step:** Handling corporate data (Excel/CSV).
