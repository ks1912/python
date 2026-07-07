# DSA Practice

Solutions are organized by topic, following the schedule in [`../PLAN.md`](../PLAN.md).

## Convention

Each problem gets two files in its topic folder:

```
dsa/<topic>/<problem_name>.py        # solution
dsa/<topic>/test_<problem_name>.py   # pytest test cases
```

Write your edge cases in the test file *before* solving the problem where possible
(empty input, single element, duplicates, negatives, large input) — this mirrors
test-first thinking and catches gaps in the solution early.

## Running tests

```bash
pip install -r requirements-dev.txt
pytest dsa/ -v
```

Run a single topic or problem:

```bash
pytest dsa/arrays_strings/ -v
pytest dsa/arrays_strings/test_two_sum.py -v
```

## Topics

- `arrays_strings/` — weeks 1-2
- `linked_lists_stacks_queues/` — weeks 3-4
- `trees_heaps/` — weeks 5-6
- `graphs/` — weeks 7-8
- `dp_greedy_backtracking/` — weeks 9-10
- `system_design/` — weeks 11-12 (notes/diagrams, not code)
