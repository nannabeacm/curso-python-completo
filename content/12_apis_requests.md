# 12. Cerebro: Requests & APIs

> "I can find anyone." - Professor X

The internet is full of specific data endpoints called **APIs** (Application Programming Interfaces). You can ask them questions and get answers. We use the `requests` library.

**Prerequisite:** `pip install requests`

## 1. The GET Request (Ask)
Getting data from a URL.
We will use `pokeapi.co` (It's free and requires no key, like a public SHIELD database).

```python
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

print(response.status_code) # 200 means OK. 404 means Not Found.
```

## 2. JSON (The Language of the Web)
Data comes back as JSON (JavaScript Object Notation). It looks exactly like a Python Dictionary.

```python
data = response.json()

name = data['name']
weight = data['weight']
abilities = data['abilities']

print(f"Name: {name}")
print(f"Weight: {weight}")
```

## 3. Query Parameters
Sometimes you need to be specific.
(Example with a hypothetical API).

```python
# Searching for movies
params = {"t": "Batman", "y": "2008"}
# output url: api.site.com?t=Batman&y=2008
```

---
**Next Step:** Extracting info without an API (Web Scraping).
