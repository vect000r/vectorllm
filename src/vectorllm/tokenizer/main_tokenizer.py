from src.vectorllm.models.schemas import TrainableTokenizer

class MainTokenizer(TrainableTokenizer):
    def __init__(self):
        super().__init__()
        self.pattern = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
        self.vocab = {}

    def get_stats(self, token_ids, stats):

        for pair in zip(token_ids, token_ids[1:]):
            stats[pair] = stats.get(pair, 0) + 1
        return stats

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