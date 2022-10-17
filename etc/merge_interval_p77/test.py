from .merge_interval import merge_interval


def test_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge_interval(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge_interval(intervals) == [(1, 3), (4, 10), (20, 27)]
