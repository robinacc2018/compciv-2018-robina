import scraper
url = 'https://compciv.github.io/stash/hello.html'
x = scraper.fetch_html(url)
print(x)