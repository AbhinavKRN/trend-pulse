import requests
from typing import Optional

class ProxyManager:
    def __init__(self):
        self.username = 'aayush96'
        self.password = 'aayush@proxy96'
        self.host = 'open.proxymesh.com'

    def get_proxy_url(self) -> str:
        """Get formatted proxy URL with authentication."""
        return f"http://{self.username}:{self.password}@{self.host}:31280"

    def get_current_ip(self) -> Optional[str]:
        """Get the current IP address being used."""
        try:
            response = requests.get(
                'https://api.ipify.org?format=json',
                proxies={
                    'http': self.get_proxy_url(),
                    'https': self.get_proxy_url()
                },
                timeout=10
            )
            return response.json()['ip']
        except Exception as e:
            print(f"Error getting IP: {str(e)}")
            return None