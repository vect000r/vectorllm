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

    def merge(self, token_ids, pair, new_index):

        merged = []
        i = 0
        num_tokens = len(token_ids)

        while i < num_tokens:
            if (i < num_tokens - 1) and (token_ids[i] == pair[0]) and (token_ids[i + 1] == pair[1]):
                merged.append(new_index)
                i += 2
            else:
                merged.append(token_ids[i])
                i += 1

        return merged

    def train(self):
        pass

    def encode_chunks(self):
        pass

    def encode(self):
        pass

    def decode(self):
        pass