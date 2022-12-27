

def my_headers():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/81.0.4044.141 Safari/537.36'
    return {
        'User-Agent': user_agent,
        'Accept-Encoding': 'gzip, deflate', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive', 'Accept-Language': 'en-US,en;q=0.5', 'Cache-Control': 'no-cache', 'DNT': '1'}
