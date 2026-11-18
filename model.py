from collections import defaultdict, Counter

class NGramModel:
    """Predicts the next observation from counts of what followed before."""

    def __init__(self, n=3):
        self.n = n
        # counts[context_tuple][next_item] = how many times it followed
        self.counts = defaultdict(Counter)

    def train(self, sequences):
        for seq in sequences:
            padded = ["<s>"] * (self.n - 1) + seq
            for size in range(1, self.n):          # contexts of length 1..n-1
                for i in range(len(padded) - size):
                    context = tuple(padded[i:i + size])
                    self.counts[context][padded[i + size]] += 1

    def predict(self, history, k=3):
        history = ["<s>"] * (self.n - 1) + history
        # back off: try the longest context first, then shorter ones
        for size in range(self.n - 1, 0, -1):
            context = tuple(history[-size:])
            if context in self.counts:
                counter = self.counts[context]
                total = sum(counter.values())
                return [(item, c / total) for item, c in counter.most_common(k)]
        return []
