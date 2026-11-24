[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/intan151/makefun-developer-excuses-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/intan151/makefun-developer-excuses-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# Make the AI Judge Laugh: Developer Excuses

A deterministic Python entry for the make.fun competition "Make the AI Judge Laugh: Developer Excuses". It writes one single-line funny excuse a developer gives when code breaks in production — 96 characters — to `/output/entry.txt`.

> My code didn't break in production — production just ran it exactly the way I wrote it at 2 a.m.

## Why this line

- **Prompt fit:** it is a developer's own excuse, told in the first person, for the exact situation — code breaking in production.
- **Fresh angle, not the stock joke:** instead of "it worked on my machine", the excuse turns inside out — the code was never fine, production merely ran it faithfully, exactly as written at 2 a.m.
- **Twist a developer recognises:** every developer has shipped 2 a.m. code and watched production expose it; the joke reveals what really happened rather than stating the obvious.
- **Tight:** 96 characters, every word working, no setup that overstays.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (1–200 characters, a single line, not only whitespace) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
