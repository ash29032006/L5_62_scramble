# Lab 5: Static Code Analysis — Word Scramble Arena

**Program:** `Word Scramble Arena (62_scramble)`

Follow the lab handout for full instructions.

## About the program

Word Scramble Arena is a Pygame-based anagram puzzle game where players are presented with scrambled words from a dictionary pool and unscramble them before a round countdown timer expires. The game includes letter tile rearrangement rack, progressive letter hints with score penalties, countdown timer bar, and score tracking.

While functional, the codebase contains style, code quality, and security issues that Flake8, Pylint, and Bandit are designed to detect.

## What to do

1. **Run it first** and verify gameplay:

   ```bash
   python main.py
   ```

2. **Install the tools:**

   ```bash
   python -m pip install pylint bandit flake8
   ```

3. **Run the analysis and save the reports:**

   ```bash
   python -m pylint main.py game/ > pylint_report.txt
   python -m bandit -r . > bandit_report.txt
   python -m flake8 . > flake8_report.txt
   ```

4. **Document the issues** in `issues.md` using the table (high and medium severity first):

   | Issue | Tool | Severity / Type | Line(s) | Description | Fix Approach |
   |---|---|---|---|---|---|
   | ... | ... | ... | ... | ... | ... |

5. **Fix the code.** Fix the issues documented, then rerun all three tools to confirm they are resolved. The game should remain fully functional.

6. **Reflect.** Answer the four reflection questions from the handout in `reflection.md`.

## Deliverables

- Cleaned codebase with issues fixed across Bandit, Flake8, and Pylint.
- `bandit_report_before.txt` and `bandit_report_after.txt` (and `bandit_report.txt`).
- `flake8_report_before.txt` and `flake8_report_after.txt` (and `flake8_report.txt`).
- `pylint_report_before.txt` and `pylint_report_after.txt` (and `pylint_report.txt`).
- `issues.md`: Completed issue tracking table.
- `reflection.md`: Technical answers to the four lab reflection questions.

**Target:** Aim for a Pylint score above 9.5 (10.00/10 target).
