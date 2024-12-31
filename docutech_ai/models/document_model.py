class DocumentModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def summary(self):
        return f"Document: {self.title[:50]}..."
