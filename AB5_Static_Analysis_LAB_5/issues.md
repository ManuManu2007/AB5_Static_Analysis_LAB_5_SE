# AB5: Static Code Analysis — Issues Report

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Duplicate voting allowed | Logic / Security | 31–39 | A voter can vote multiple times because the existing `voted` flag is not checked. | Reject votes if the voter has already voted. |
| Invalid candidate accepted | Logic | 31–39 | The program accepts invalid candidates such as `bob`. | Validate candidates against the allowed candidate list. |
| Incorrect closing-time check | Logic | 31–39 | Votes after 18:00 are accepted because the code checks only `when.hour > 18`. | Reject votes at or after the closing time. |
| Division by zero | Runtime error | 59–64 | Percentage and turnout calculations fail when ballots or registered voters are empty. | Handle zero denominators before division. |
| Incorrect announcements | Logic | 75–81 | Lambda functions capture the same loop variable, so all announcements show the last candidate. | Use a list comprehension or bind the candidate value correctly. |
| Hardcoded admin password | Security | 6 | The administrator password is stored directly in the source code. | Use secure configuration and proper authentication. |
| Insecure MD5 hashing | Security | 17 | MD5 is not suitable for security-sensitive hashing. | Use a suitable secure hashing method if hashing is needed. |
| Missing docstrings | Code quality | Multiple | Functions and the module lack documentation. | Add a module docstring and function docstrings. |
| Non-standard function names | Code style | Multiple | Function names use camelCase instead of Python's snake_case convention. | Rename functions using snake_case. |
| Unused variables | Code quality | 37, 63 | Variables such as `receipt` and `now` are assigned but never used. | Remove them or use them meaningfully. |
| Missing final newline | Code style | End of file | The file does not end with a newline. | Add a newline at the end of the file. |