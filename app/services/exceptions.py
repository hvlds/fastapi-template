class LinkNotFound(Exception):
    def __init__(self, short_url: str):
        self.short_url = short_url
        super().__init__(f"Link with short URL {short_url} not found")


class LinkExpired(Exception):
    def __init__(self, short_url: str):
        self.short_url = short_url
        super().__init__(f"Link with short URL {short_url} has expired")
