import pandas as pd
from backend.lib.config import CONFIG


class SingleWord(object):
    def __init__(self):
        df = pd.read_csv(CONFIG.word_curve, header=None, index_col=0, keep_default_na=False)
        self.words = df.index.tolist()
        self.data = dict(zip(df.index, df.values))

    def get_curve(self, words):
        values = {}
        for word in words:
            value = self.data.get(word, [])
            if len(value) == 0:
                continue
            values[word] = value.tolist()
        years = list(range(1801, 2009))
        return {'values': values, 'years': years}

    def get_candidate_words(self, query, max_num=50):
        candidates = [x for x in self.words if query in x]
        candidates.sort(key=len)
        return candidates[:max_num]


SINGLEWORD = SingleWord()
