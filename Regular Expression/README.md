# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.

- The `re` module offers a set of functions that allows us to search a string for a match:

**2. Function	Description
- `findall`	Returns a list containing all matches
- `search`	Returns a Match object if there is a match anywhere in the string
- `split`	Returns a list where the string has been split at each match
- `sub`	Replaces one or many matches with a string
