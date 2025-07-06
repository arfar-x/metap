import requests

class OfficialRegistry:
    headers = {
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "referer": "https://www.mql5.com/en/search",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    @staticmethod
    def get(package_name):
        """Search the package then download it."""
        result = OfficialRegistry.search(package_name)
        if result:
            return OfficialRegistry.download(result)
        return False

    @staticmethod
    def search(package_name):
        """Search the package using the official API and return first result info or None."""
        url = "https://search.mql5.com/api/query"
        params = {
            "module": "mql5.com.en.codebase|mql4.com.en.codebase",
            "keyword": package_name,
            "from": "0",
            "count": "10"
        }
        try:
            res = requests.get(url, headers=OfficialRegistry.headers, params=params)
            res.raise_for_status()
            data = res.json()
            results = data.get("results", [])
            if results:
                # Return the first result info dictionary
                return results[0]
            else:
                print(f"No results found for '{package_name}'.")
                return None
        except requests.RequestException as e:
            print(f"Error occurred while searching the package '{package_name}': {e}")
            return None

    @staticmethod
    def download(result):
        """Download the package ZIP file from the download_url in result info."""
        info = result.get("info", {})
        download_url = info.get("download_url")
        if not download_url:
            print("No download URL found for this package.")
            return False
        
        try:
            print(f"Downloading from {download_url} ...")
            response = requests.get(download_url, headers=OfficialRegistry.headers)
            response.raise_for_status()
            
            # Save the file locally with the package title as filename
            title = info.get("title", "package").replace(" ", "_")
            filename = f"{title}.zip"
            print(f"Downloaded and saved as '{filename}'.")
            return response.content
        except requests.RequestException as e:
            print(f"Failed to download the package: {e}")
            return False
