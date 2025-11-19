# powerXAI
Power Indices for Explainable AI

## Getting Started

Create and activate a virtual environment:

```bash
python -m venv env
```
```bash
source env/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

Try a minimal example:

```python
from powerxai import shapley_value

def weighted_ABC_value(players, coalition) -> float:
    weights = {"A": 1, "B": 2, "C": 3}
    return float(sum(weights.get(players[i], 0) for i in coalition))

players = ["A", "B", "C", "D"]
result = shapley_value(player_index=0, players=players, value_function=weighted_ABC_value)

print(f"The Shapley value for player 'B' is: {result}")
```

---