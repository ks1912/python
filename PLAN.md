# DSA + System Design Interview Prep Plan

QA → Developer transition. Language: Python. Timeline: 12 weeks, ~1-2 hrs/day.
Target: mid-level SDE roles (product-based companies).

Check items off as you complete them. Log each solved problem in `dsa/<topic>/` with
a solution file and a matching `test_*.py` (see `dsa/README.md`).

## Weeks 1-2 — Python for DSA + Complexity + Arrays/Strings
- [ ] Python refresher: lists/slicing, dict & set internals, `collections` (Counter, deque, defaultdict), string methods, comprehensions
- [ ] Big-O basics: analyze time/space of loops and simple recursion
- [ ] Pattern: two pointers
- [ ] Pattern: sliding window
- [ ] Pattern: prefix sums
- [ ] Solve 20-25 easy array/string problems (NeetCode 150 / LeetCode Easy)
- [ ] For each problem, write edge cases first (empty input, single element, duplicates, negatives) before coding

## Weeks 3-4 — Hashing, Linked Lists, Stacks/Queues, Recursion
- [ ] Hash maps/sets for O(1) lookup; rewrite 3-4 earlier brute-force solutions using hashing
- [ ] Linked lists: reversal, cycle detection (Floyd's), merge, fast/slow pointers
- [ ] Stacks/queues: valid parentheses, monotonic stack, min-stack
- [ ] Recursion fundamentals: base cases, recursion tree, recursion → iteration
- [ ] Solve ~20 problems

## Weeks 5-6 — Trees, BST, Heaps
- [ ] Binary tree traversals (DFS/BFS), height, diameter, LCA
- [ ] BST: insert/search/delete, validate BST
- [ ] Heaps: `heapq`, top-K problems, merge K sorted lists
- [ ] Solve ~20 problems

## Weeks 7-8 — Graphs
- [ ] BFS/DFS on graphs; adjacency list vs matrix
- [ ] Topological sort
- [ ] Union-find (disjoint set), cycle detection
- [ ] Shortest path: understand Dijkstra conceptually
- [ ] Solve ~15-18 problems

## Weeks 9-10 — Dynamic Programming + Greedy + Backtracking
- [ ] 1D DP (climbing stairs, house robber)
- [ ] 2D DP (grids, edit distance, knapsack)
- [ ] String DP (LCS, palindromes)
- [ ] Greedy: interval scheduling, activity selection
- [ ] Backtracking: subsets, permutations, combination sum, N-Queens (conceptual)
- [ ] Solve ~20 problems, focused on pattern recognition over memorization

## Weeks 11-12 — System Design (HLD) + Mock Interviews + Review
- [ ] Core building blocks: load balancers, caching & invalidation, CDNs, DB indexing, SQL vs NoSQL, sharding/replication, message queues, consistent hashing
- [ ] Concepts: CAP theorem, horizontal vs vertical scaling, rate limiting algorithms, consistency models
- [ ] Design: URL shortener
- [ ] Design: rate limiter
- [ ] Design: notification/messaging system
- [ ] Design: e-commerce inventory or ticket-booking system
- [ ] Design: news feed / social media timeline
- [ ] Practice format for each design: requirements → back-of-envelope estimation → high-level architecture → deep dive → trade-offs
- [ ] Redo 15-20 weakest problems from earlier weeks, timed (25-30 min each)
- [ ] Complete 2 full mock interviews

## Resources
- Problems: NeetCode 150, LeetCode (filter by pattern/company)
- Python tools to be fluent in: `collections`, `heapq`, `bisect`, `itertools`
- System design: System Design Primer (GitHub), "Grokking the System Design Interview" style material
