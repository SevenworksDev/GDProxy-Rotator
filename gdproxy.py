import requests, random

class GDProxy:
    def __init__(self, url_list_path):
        self.urls = self.load_urls(url_list_path)
        self.current_url_index = 0

    def load_urls(self, url_list_path):
        with open(url_list_path, 'r') as file:
            return file.read().splitlines()

    def get(self, endpoint, data=None):
        if not self.urls:
            raise ValueError('No URLs available in the URL list.')
        url = self.urls[self.current_url_index] + endpoint
        self.current_url_index = (self.current_url_index + 1) % len(self.urls)
        response = requests.post(url, data=data, headers={'User-Agent': ''})
        return response.text

gdproxy = GDProxy("gdproxy.txt")

def get(endpoint=None, data=None):
    return gdproxy.get(endpoint, data)
