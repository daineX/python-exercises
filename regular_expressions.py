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

# The 'match' function is used to see if the beginning of a string matches a regular expression:
assert re.match(rex, 'spam')
assert re.match(rex, 'spammer')
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

# Python also allows for checking for a specific number of occurrences. For this
# '{}' (curly braces) are used:
rex = 'ba{5}'
assert re.match(rex, 'baaaaa')
assert not re.match(rex, 'baaa')

rex = 'ba{3,5}'
assert re.match(rex, 'baaaaa')
assert re.match(rex, 'baaa')
assert not re.match(rex, 'ba')

# EXERCISE:
# Write a regular expression that matches three to six 'o's followed by 'uf':
# rex = 'somerex'
# assert re.match(rex, 'ooouf')
# assert re.match(rex, 'oooooouf')
# assert not re.match(rex, 'ouf')


# For now we've only checked multiple occurrences of a single character. With grouping
# we can do this for a sequence of characters putting them in parentheses:
rex = "(eg)?gs"
assert re.match(rex, "gs")
assert not re.match(rex, "ggs")
assert re.match(rex, "eggs")

# Notice how 'ggs' is not matched, because the 'eg' group can only be matched as one.

# EXERCISE:
# Write a regular expression that matches 'some', then an arbitrary number of arbitrary characters
# in the middle and ends with either 'eggs' or 'spam':
#rex = 'somerex'
#assert re.match(rex, 'some classy eggs')
#assert re.match(rex, 'some delicious spam')
#assert not re.match(rex, 'some salty ham')
#assert not re.match(rex, 'any spammy spam')

# The '|' (bar) can be used mutiple times:
rex = 'a|b|c'
assert re.match(rex, 'at home')
assert re.match(rex, 'bar none')
assert re.match(rex, 'cute kittens')
assert not re.match(rex, 'dumb dogs')

# But this can be become tedious if we want to match then just a few characters or patterns.
# For this purpose, we can square braces as more compact way of writing these expressions:

rex = '[abc]'
assert re.match(rex, 'at home')
assert re.match(rex, 'bar none')
assert re.match(rex, 'cute kittens')
assert not re.match(rex, 'dumb dogs')

# Furthermore, we can use ranges of characters by putting dashes in between:
rex = '[a-c]'
assert re.match(rex, 'at home')
assert re.match(rex, 'bar none')
assert re.match(rex, 'cute kittens')
assert not re.match(rex, 'dumb dogs')

# For example, we can use [A-Z] to match all capital letters:
rex = '[A-Z]'
assert re.match(rex, 'Cute kittens')
assert not re.match(rex, 'cute kittens')

# EXERCISE:
# Write a regular expression that matches any string containing a number from 1 to 9
# rex = 'somerex'
# assert re.match(rex, 'toaster 3 still works')
# assert not re.match(rex, 'bread')
# assert not re.match(rex, 'number 0 is gone')

# We can also have multiple ranges in the same square brace expression:
rex = '[A-Za-z]+'
assert re.match(rex, 'immadeoutofletters')
assert not re.match(rex, '77Istartwithanumber')

# Python defines shortcuts for some of these ranges. You can use \d to match
# numerals and \w to match numerals and letters and underscores:
rex = '\d+\w*\d+' # match a string starting with a numeral, maybe followed by any
                  # letter or number, then followed by at least a numeral again
assert re.match(rex, '0spam3')
assert not re.match(rex, '0 45')
assert not re.match(rex, '0spam')

# EXERCISE:
# Write a regular expression, that matches 'there are x kittens in the kitchen',
# with x being any number.
# rex = 'somerex'
# assert re.match(rex, 'there are 5 kittens in the kitchen')
# assert re.match(rex, 'there are 25 kittens in the kitchen')
# assert not re.match(rex, 'there are no kittens in the kitchen')
# assert not re.match(rex, 'there are kittens in the kitchen')

# When a string matches a regular expression both re.match and re.search return
# Match objects which contains information about that particular match:
rex = '\d+' # find numbers in the string
match = re.search(rex, 'Some 100 flowers were trampled.')
assert match.start() == 5
assert match.end() == 8

# By using grouping, we can extract the matching part of the string directly, using
# the 'groups' method. It will return the values of the matches as a tuple:
rex = '(\d+).+(\d+)'
match = re.search(rex, 'Some 100 flowers made a mess in 5 different cities.')
assert match.groups() == ('100', '5')

# We can also access the value of the group directly via the 'group' function.
# The 0th group is the part of the string that matches the whole expression:
assert match.group(0) == '100 flowers made a mess in 5'
assert match.group(1) == '100'
assert match.group(2) == '5'

# EXERCISE:
# Write a function, that extracts

## TODO
