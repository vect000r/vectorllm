from src.vectorllm.models.schemas import TrainableTokenizer

class MainTokenizer(TrainableTokenizer):
    def __init__(self):
        super().__init__()

    def get_stats(self):
        pass

    def merge(self):
        pass

    def train(self):
        pass

    def encode_chunks(self):
        pass

    def encode(self):
        pass

    def decode(self):
        pass