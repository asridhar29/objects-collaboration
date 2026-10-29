"""Experiments from the 'Try to Surprise Yourself' section.

Announcements live here, not in the posts list that build_feed() returns.
"""

from lab_classes import User, Tweet
from feed_demo import build_feed


class Announcement:
    """A club notice that is not a tweet, but does have .text."""

    def __init__(self, text):
        self.text = text


def show(post):
    """Print anything that has a .text attribute."""
    print(post.text)


def experiment_aliasing():
    print('--- 1. two names for one post ---')
    users, posts = build_feed()
    same_post = posts[0]
    before = posts[0].likes
    same_post.like()
    print(f'posts[0].likes before: {before}')
    print(f'same_post.like() called once')
    print(f'posts[0].likes now:    {posts[0].likes}')
    print(f'same_post.likes now:   {same_post.likes}')
    print(f'same object? {same_post is posts[0]}')


def experiment_equality():
    print('\n--- 2. == versus is ---')
    a = User('mira_rolls')
    b = User('mira_rolls')
    a.follow()
    a.follow()
    print(f'a has {a.followers} followers, b has {b.followers}')
    print(f'a == b: {a == b}')
    print(f'a is b: {a is b}')
    print(f'a == User("dev_the_dealer"): {a == User("dev_the_dealer")}')
    print(f'a == "mira_rolls": {a == "mira_rolls"}')


def experiment_hashtags():
    print('\n--- 3. hashtag edge cases ---')
    cases = [
        'Game night #Games #Games #BringSnacks!',
        'word#inside is not a tag',
        'a bare # by itself',
        '#Tag.  #tag #TAG',
        '',
        '   #spaced   #out   ',
    ]
    for text in cases:
        print(f'{text!r:45} -> {Tweet("mira_rolls", text).hashtags()}')


def experiment_duck_typing():
    print('\n--- 4. duck typing ---')
    show(Tweet('dev_the_dealer', 'a tweet has .text'))
    show(Announcement('an announcement also has .text'))
    try:
        show({'text': 'a dict only has a key'})
    except AttributeError as e:
        print(f'dict raised AttributeError: {e}')


if __name__ == '__main__':
    experiment_aliasing()
    experiment_equality()
    experiment_hashtags()
    experiment_duck_typing()
