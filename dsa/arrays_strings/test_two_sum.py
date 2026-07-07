from two_sum import two_sum


def test_basic_pair():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_pair_at_end():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]


def test_duplicate_values():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_no_solution_returns_empty():
    assert two_sum([1, 2, 3], 100) == []


def test_single_element_no_solution():
    assert two_sum([5], 5) == []


def test_negative_numbers():
    assert sorted(two_sum([-3, 4, 3, 90], 0)) == [0, 2]


def test_empty_input():
    assert two_sum([], 0) == []
