class Youtube:
    def __init__(self, browser: str):
        self.browser = browser
    
    def __repr__(self):
        return self.browser