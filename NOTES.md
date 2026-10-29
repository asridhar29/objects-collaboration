# Experiment Notes

Community: the **Riverbend Board Game Club** — three members posting about
Thursday game night. Run the experiments with `python experiments.py`.

Each experiment below records the prediction made *before* running the code,
then what actually happened.

## 1. Two names for one post

**Predicted:** both names show the same count, because `same_post = posts[0]`
copies the reference, not the object.

**Happened:** as predicted. One `same_post.like()` moved the count from 3 to 4,
and `posts[0].likes` and `same_post.likes` both read 4. `same_post is posts[0]`
is `True` — there is one `Tweet` on the heap with two names pointing at it.
Assignment never copies an object in Python.

## 2. `==` versus `is`

**Predicted:** `==` is `True` (same username), `is` is `False` (two objects).

**Happened:** as predicted. With `a` at 2 followers and `b` at 0,
`a == b` is `True` and `a is b` is `False`. `__eq__` compares only the data I
told it to compare, so the follower counts are irrelevant; `is` asks the
different question of whether the two names refer to one object.
`a == 'mira_rolls'` is `False` because of the `isinstance` guard — without it,
`other.username` would raise `AttributeError` instead of returning `False`.

**Surprise:** defining `__eq__` without `__hash__` makes `User` **unhashable** —
`{User('a'), User('a')}` raises
`TypeError: unhashable type: 'User'`. Python drops the inherited `__hash__`
when a class defines `__eq__`, since two objects that compare equal would
otherwise be allowed to hash differently. Nothing in this lab needs users in a
set or dict key, so the class is left as the spec describes; adding
`__hash__ = lambda self: hash(self.username)` would be the fix if it ever does.

## 3. Hashtag edge cases

**Predicted:** repeats stay duplicated, trailing punctuation stays attached, and
a `#` inside a word produces nothing.

**Happened:** as predicted.

| text | `hashtags()` |
| --- | --- |
| `Game night #Games #Games #BringSnacks!` | `['Games', 'Games', 'BringSnacks!']` |
| `word#inside is not a tag` | `[]` |
| `a bare # by itself` | `['']` |
| `#Tag.  #tag #TAG` | `['Tag.', 'tag', 'TAG']` |
| `` (empty text) | `[]` |
| `   #spaced   #out   ` | `['spaced', 'out']` |

Two details worth naming. A bare `#` is a word that starts with `#`, so slicing
off that one character leaves the empty string — which is what the spec asks
for. And `.split()` with no argument collapses runs of whitespace and ignores
leading and trailing whitespace, so the padded text needs no special handling;
`.split(' ')` would have produced empty strings instead.

## 4. Duck typing

**Predicted:** the tweet and the announcement both print; the dictionary raises,
because a `'text'` key is not a `.text` attribute.

**Happened:** as predicted. `show()` printed both objects, and the dict raised
`AttributeError: 'dict' object has no attribute 'text'`.

**What `show` needs:** only that its argument support attribute access named
`text`. It never asks what class the argument is, so `Tweet` and `Announcement`
work without sharing a base class — that is the whole of duck typing. The dict
stores the same string under a *key*, reached with `post['text']`, which is a
different operation. `Announcement` lives in `experiments.py`, outside the
`posts` list that `build_feed()` returns, since that list is for tweets.

## Checking that the display follows the data

Appending a fourth user and a fifth tweet, and editing an existing tweet's text,
all showed up in the output with no change to `main()` — the loops read whatever
`build_feed()` returns rather than hard-coded strings.
