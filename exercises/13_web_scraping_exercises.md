# Exercises: Web Scraping (Spidey-Sense)

## Mission 1: The Training Simulation
Since we can't scrape real sites easily in a tutorial (titles change), we will scrape a local string.

Create `scrape_sim.py`.
```python
html_doc = """
<html>
<head><title>The Avengers</title></head>
<body>
<p class="title"><b>Top Heroes</b></p>
<p class="story">
    <a href="http://example.com/ironman" class="hero" id="link1">Iron Man</a>,
    <a href="http://example.com/cap" class="hero" id="link2">Captain America</a>,
    <a href="http://example.com/thor" class="hero" id="link3">Thor</a>
</p>
</body>
</html>
"""
```
1. Import BeautifulSoup.
2. Create soup: `soup = BeautifulSoup(html_doc, 'html.parser')`.
3. Print the title of the page.
4. Use `find_all` to find all `<a>` tags.
5. Loop through them and print the hero names.

## Mission 2: The Real Deal (Books to Scrape)
There is a site specifically made for scraping practice: `http://books.toscrape.com/`.

Create `book_scraper.py`.
1. Request the URL.
2. Parse with BeautifulSoup.
3. Find all product pods (`article` with class `product_pod`).
4. Loop through the first 5 books.
5. Extract and print the title (`h3 > a`).

**Hint:** You might need to inspect the HTML in your browser (Right Click -> Inspect) to see the structure.
