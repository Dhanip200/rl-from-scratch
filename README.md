# rl-from-scratch

Learning imitation learning and reinforcement learning from scratch on CartPole (Gymnasium), alongside Berkeley CS285.

| File | What it does | Score |
|---|---|---|
| `play_random.py` | presses random buttons | ~10–20 |
| `play_expert.py` | hand-written expert rule: push the way the pole is leaning + tipping (`angle + angular velocity > 0`) | 500 (max) |

Next: record the expert, then train a network to copy it (behaviour cloning + DAgger).

## Run
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install "gymnasium[classic-control]"
python play_expert.py
```
