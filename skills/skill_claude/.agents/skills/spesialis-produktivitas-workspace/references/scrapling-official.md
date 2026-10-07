# Scrapling

Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.

Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass anti-bot systems like Cloudflare Turnstile out of the box. And its spider framework lets you scale up to concurrent, multi-session crawls with pause/resume and automatic proxy rotation - all in a few lines of Python.

## CLI Usage

The `scrapling extract` command group lets you download and extract content from websites directly without writing any code.

```bash
# Basic download
scrapling extract get "https://news.site.com" news.md

# Extract only specific content using CSS selectors
scrapling extract get "https://blog.example.com" articles.md --css-selector "article"

# Wait for JavaScript to load content and finish network activity
scrapling extract fetch "https://scrapling.requestcatcher.com/" content.md --network-idle

# Bypass basic protection / Solve Cloudflare challenges
scrapling extract stealthy-fetch "https://nopecha.com/demo/cloudflare" data.txt --solve-cloudflare --css-selector "#padded_content a"
```

## Python Integration
Use `Fetcher`, `StealthyFetcher`, or `DynamicFetcher` for Python scripts. Use `Spider` for massive concurrent crawling.
