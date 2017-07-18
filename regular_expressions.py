# Introduction
# ============
# A regular expression is a special type of pattern that is usually used find and replace
# parts of strings. They are related to other constructs of theoretical computer science
# like (regular) grammars and (finite) automata, which you could look up to understand
# more behind the motivation and where some of the short-comings (later on that) come from.


# Exercises
# ============
# The easiest regular expression is one that matches a specific string pattern exactly.
# Disregarding some special characters, the regular expression looks the same as the pattern to match:
#

rex = 'spam' # matches the string 'spam' exactly

# Python defines all the functionality regarding regular expressions in the 're' module:
import re

# The 'match' function is used to see if string matches a regular expression:
assert re.match(rex, 'spam')
assert not re.match(rex, 'eggs')

# If the string does not match the regular expression

# EXERCISE:
# write a regular expression that matches 'eggs' instead of 'spam':
# assert re.match(myrex, 'eggs')

# Matching a string exactly is not very different from just checking that two strings are equal.
# But regular expressions can do more than that. They allow for matching arbitrary characters
# instead of specific ones. The '.' (dot) character is used for that:
rex = 'spam.'
assert re.match(rex, 'spams')
assert re.match(rex, 'spamd')
assert not re.match(rex, 'spoms')

# EXERCISE:
# write a single regular expression that matches both 'egged' and 'egald'
# rex = 'somerex'
# assert re.match(rex, 'egged')
# assert re.match(rex, 'egald')

# We can match a choice of patterns by using the '|' (bar) character:
rex = 'spam|eggs'
assert re.match(rex, 'spam')
assert re.match(rex, 'eggs')

# EXERCISE:
# Write a regular expression that matches both color and colour using the bar:
# rex = 'somerex'
# assert re.match(rex, 'color')
# assert re.match(rex, 'colour')


# Sometimes we want to match strings of variable length. Regular expressions introduce
# quantifiers for this. The first one is the "optional" quantifier '?' (question mark).
# It means the character in front of it can be left out:
rex = 'spams?'
assert re.match(rex, 'spams')
assert re.match(rex, 'spam')

# This can also be used wit the dot:
rex = 'spam.?'
assert re.match(rex, 'spams')
assert re.match(rex, 'spamd')
assert re.match(rex, 'spam')

# EXERCISE:
# Write a regular expression that matches both color and colour using the question mark:
# rex = 'somerex'
# assert re.match(rex, 'color')
# assert re.match(rex, 'colour')

# The next quantifier is '*' (asterisk). It means that on top of the character being
# optional, there can be as many of them as there need to be:
rex = 'foo*'
assert re.match(rex, 'fo')
assert re.match(rex, 'foo')
assert re.match(rex, 'fooooooo')

# EXERCISE:
# Write a regular expression that matches an arbitrary number of 'o's in between two 'l's:
# rex = 'somerex'
# assert re.match(rex, 'll')
# assert re.match(rex, 'lol')
# assert re.match(rex, 'loooool')


# With the '+' (plus sign) we require there to be at least of the of preceeding character
# in the string:
rex = 'foo+'
assert not re.match(rex, 'fo')
assert re.match(rex, 'foo')
assert re.match(rex, 'fooooooo')

# You can use re.match to check if the start of a string matches a regular expression.
# To check if any part of a string matches the regular expression, you can use re.search:
rex = 'foo+'
assert not re.search(rex, 'spamfoeggs')
assert re.search(rex, 'spamfooeggs')

# EXERCISE:
# Write a regular expression that matches any word string with at least t in it.
# rex = 'myrex'
# assert not re.search(rex, 'road')
# assert re.search(rex, 'toast')

# For now we've only checked multiple occurrences of a single character. With grouping
# we can do this for a sequence of characters putting them in parentheses:
rex = "(eg)?gs"
assert re.match(rex, "gs")
assert not re.match(rex, "ggs")
assert re.match(rex, "eggs")

# Notice how 'ggs' is not matched, because the 'eg' group can only be matched as one.

# EXERCISE:
# Write a regular expression that matches an arbitrary number of arbitrary characters
# in the front but ends with either eggs or spam:
#rex = 'somerex'
#assert re.match(rex, 'some eggs')
#assert re.match(rex, 'delicious spam')
#assert not re.match(rex, 'salty ham')
