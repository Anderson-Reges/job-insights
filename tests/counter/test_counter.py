from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    assert count_ocurrences(path, 'miN') == 6324
    assert count_ocurrences(path, 'Max') == 248
