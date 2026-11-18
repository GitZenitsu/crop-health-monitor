# Crop Health Sequence Monitor

A small command-line tool that predicts which pest or symptom is likely to appear next in a crop field, based on the sequence of observations so far.

## How it works

The model is an n-gram predictor built from simple counts, with no neural network. It reads observed sequences from `data/sequences.txt` and counts which observation followed each previous one or two observations. To predict, it looks at the last two observations first. If it has never seen that pair, it backs off to just the last observation. The counts are converted to percentages.

## How to run

Requires Python 3.

```
python main.py
```

Type the observations separated by spaces, or `quit` to exit.

## Example

```
Observed so far: aphids leaf_curl
Likely next:
  yellowing  (50%)
  sooty_mold  (25%)
  wilting  (25%)
```

## Files

- `main.py`: command-line interface
- `model.py`: n-gram model with backoff
- `data/sequences.txt`: sample observation sequences
