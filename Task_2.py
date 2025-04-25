"""
2. Concurrency
Implement a multi-threaded program that downloads multiple web pages concurrently. Use the
`concurrent.futures` module.
"""



import concurrent.futures
import requests

def download_web_pages(url):
    response = requests.get(url)
    return response.content

urls = ["https://www.geeksforgeeks.org/", "https://www.python.org"]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download_web_pages, urls)
    for result in results:
        print(result[:100]) 