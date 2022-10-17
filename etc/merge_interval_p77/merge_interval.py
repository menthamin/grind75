# 출처: https://github.com/xissy/coderpad-interviews/blob/master/p77/python/p77.py


def merge_interval(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merged_intervals = []

    for interval in sorted_intervals:
        if merged_intervals and interval[0] <= merged_intervals[-1][-1]:
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], interval[1]),
            )
        else:
            merged_intervals.append(interval)

    return merged_intervals


def test_merge():
    intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
    assert merge_interval(intervals) == [(1, 3), (4, 10), (20, 25)]

    intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
    assert merge_interval(intervals) == [(1, 3), (4, 10), (20, 27)]
