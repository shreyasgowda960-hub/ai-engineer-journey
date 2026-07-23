# Week 1 — Python Core · Day-by-Day Plan

*Phase 0, Week 1. ~2–3 focused hours a day. Each task maps to a tag in your tracker (1.1–1.9).*

---

## Before you start: pick ONE spine

The biggest beginner trap is collecting ten courses and finishing none. Choose **one** main resource to move through, and use the per-topic links only for practice and reference.

- **Fast spine (recommended for you):** freeCodeCamp's *Python Full Course for Beginners* on YouTube (~4–5 hrs). Free, no signup — search that exact title on YouTube. Since you're rebuilding, not starting cold, you can move quickly.
- **Deeper spine (if you want rigor):** Harvard's **CS50P** — *CS50's Introduction to Programming with Python*, free on edX or YouTube. Excellent teaching, tougher problem sets. Slower but more thorough.

**Per-topic reference/practice (use daily, don't "study" cover to cover):**
- W3Schools Python — quick syntax lookups (`w3schools.com/python`)
- Programiz — clean explanations with examples (`programiz.com/python-programming`)
- Real Python — deeper articles when a concept won't click (`realpython.com`)
- **Exercism (Python track)** — free mentored practice (`exercism.org/tracks/python`) — this is your daily practice home
- HackerRank Python track or Codewars — extra drills

---

## The daily routine (repeat every day)

1. **Learn (~60–90 min):** watch/read that day's topic from your spine.
2. **Practice (~45–60 min):** solve 3–5 small exercises on the topic (Exercism / HackerRank).
3. **Write something tiny (~15 min):** a few lines of your own that use the concept.
4. **Commit (~5 min):** save your practice files and `git commit` — keep the streak and the green GitHub history alive.
5. Open the tracker, tick the task, log the session.

---

## Day 1 — Variables, data types, operators  ·  `1.1`
Set your foundation. Numbers, strings, booleans; `int` vs `float` vs `str`; arithmetic, comparison, and logical operators; `input()` and `print()`; f-strings for formatting.
- **Do:** write a program that takes two numbers as input and prints their sum, difference, product, and average.
- **Commit message idea:** "Day 1: variables and operators"

## Day 2 — Conditionals and loops  ·  `1.2`
`if / elif / else`; `for` and `while` loops; `range()`; `break` and `continue`.
- **Do:** print all even numbers from 1 to 50; then a number-guessing game using a loop.

## Day 3 — Functions  ·  `1.3`
Defining functions, parameters and arguments, `return`, default arguments, and variable scope (local vs global).
- **Do:** rewrite Day 1's calculator as reusable functions; write a function `is_prime(n)`.

## Day 4 — Lists, tuples, dicts, sets  ·  `1.4`
The four core data structures: when to use each, indexing/slicing, adding/removing items, looping over them, and dictionary key–value access.
- **Do:** count how many times each word appears in a sentence using a dictionary.

## Day 5 — Comprehensions + strings  ·  `1.5` `1.6`
List and dict comprehensions (write the loop version first, *then* the comprehension — understand before you compress). Then string methods: `.split()`, `.join()`, `.strip()`, `.lower()`, `.replace()`, slicing.
- **Do:** one comprehension that returns the squares of even numbers 0–20; a program that checks if a word is a palindrome.

## Day 6 — File I/O + exceptions  ·  `1.7` `1.8`
Reading and writing files with `with open(...)`; the difference between read/write/append modes. Then error handling: `try / except / finally`, and why you catch specific errors (`FileNotFoundError`, `ValueError`).
- **Do:** a program that reads a text file, counts its lines and words, and safely handles the file not existing.

## Day 7 — Build 5 tiny programs + review  ·  `1.9`
Lighter consolidation day. No new theory — just build, using everything from the week. Suggested five:
1. FizzBuzz
2. Palindrome checker
3. Word-frequency counter (reads a file)
4. Number-guessing game
5. Simple to-do list saved to a text file

Push all five to your `ai-engineer-journey` repo, each with a one-line description in the README. Then skim back over anything from the week that felt shaky.

---

## End-of-week checkpoint

By Sunday night you should be able to, without googling basic syntax:
- write a function that takes input, loops, and returns a result
- choose the right data structure (list vs dict vs set) for a small problem
- read and write a file with error handling

If any of those feel wobbly, spend an extra day on it before starting Week 2 (OOP). Depth now saves you pain later.

**A reminder that matters more than any resource:** watching is not learning — *typing* is. Keep the ratio in favour of writing code over watching it. Every day you code, commit. That's the whole game.
