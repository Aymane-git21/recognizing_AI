class Dataset:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.data = file.readlines()

    def tokenize(self, text):
        return text.split()  # Simple whitespace tokenization

    def preprocess(self):
        self.load_data()
        return [self.tokenize(line) for line in self.data]