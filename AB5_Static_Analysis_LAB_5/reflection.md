# AB5: Static Code Analysis --- Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were missing docstrings, inconsistent function
naming, unused variables, and whitespace problems. These required small
changes. The hardest issues were logical bugs such as duplicate voting,
accepting invalid candidates, calculating turnout incorrectly, and
validating imported postal ballots. These required understanding how the
program behaved and correcting its logic.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

I did not confirm a definite false positive in the reports. For example,
Pylint reported an unused `receipt` variable. This was a valid warning
because the variable was assigned but never used. The warning helped
identify code that could be removed or handled more clearly.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Pylint, Flake8, and Bandit during development and before
committing changes. I would also configure them in a Git pre-commit hook
or a CI/CD pipeline so that code is checked automatically. This would
help detect style problems, programming mistakes, and potential security
issues early.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The Pylint score improved from 6.86/10 to 10.00/10. The code became more
readable through docstrings, consistent function names, and removal of
unused variables. Logic fixes prevent duplicate voting, reject invalid
candidates, enforce the poll closing time, handle empty calculations,
and correct candidate announcements. Postal ballot input validation was
also improved. These changes improve maintainability and robustness,
although the system would need further security review and testing
before any real-world use.
