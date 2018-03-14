import numpy as np
import Levenshtein as lev

from dirty_cat import similarity_encoder, target_encoder


def test_similarity_encoder(similarity='levenshtein-ratio'):
    model = similarity_encoder.SimilarityEncoder(
        similarity_type='levenshtein-ratio', handle_unknown='ignore')
    X = np.array(['aa', 'aaa', 'aaab']).reshape(-1, 1)
    X_test = np.array([['aa', 'aaa', 'aaa', 'aaab', 'aaac']]).reshape(-1, 1)
    model.fit(X)
    encoder = model.transform(X_test)
    ans = np.zeros((len(X_test), len(X)))
    for i, x_t in enumerate(X_test.reshape(-1)):
        for j, x in enumerate(X.reshape(-1)):
            ans[i, j] = lev.ratio(x_t, x)
    assert np.array_equal(encoder, ans)
