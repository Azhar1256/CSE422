# CSE422 Artificial Intelligence Labs

Search and optimisation algorithms from **CSE422 Artificial Intelligence** at BRAC University (2022).

| File | Algorithm | Problem |
|---|---|---|
| `lab01(Question_1).py` | Depth-first search | Find the largest connected region of infected cells in a grid (8-directional) |
| `lab01(Question_2).py` | Breadth-first search | Simulate an infection spreading through a city grid and report how many minutes it takes, and whether anyone survives |
| `lab02.py` | Genetic algorithm | Choose a subset of transactions whose amounts sum to a target (subset-sum) |
| `lab03.py` | Minimax with alpha-beta pruning | A two-player game whose bounds are derived from a student ID |

## Run

```bash
python "lab01(Question_1).py"          # reads "Question1 input1.txt" -> 7
python "lab01(Question_2).py"          # reads "Question2 input1.txt"
printf '4 0\nl 100\nd -50\nl -50\nd 30\n' | python lab02.py
# ['l', 'd', 'l', 'd']
# 1110            <- take the first three: 100 - 50 - 50 = 0
echo 19301257 | python lab03.py
```

`lab02.py` needs `numpy`.

## Maintenance notes (2026)

The genetic algorithm didn't work before these fixes. It always returned the empty subset (`0000`), which trivially sums to 0.

- **Fitness:** the empty subset now scores as invalid
- **Selection:** tournament selection now keeps the fittest candidate instead of a random one
- **Crash:** the best solution started as the integer `0` instead of a candidate, which could crash

After the fixes, it found the correct subset in 30 of 30 test runs, and correctly returned `-1` when no subset exists.
