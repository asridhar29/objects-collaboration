#!/usr/bin/python3
'''Starter types for the community feed lab.'''


class User:
    def __init__(self, username):
        '''
        Create a user with the given username and zero followers.

        >>> u = User('rtealwitter')
        >>> u.username
        'rtealwitter'
        >>> u.followers
        0
        '''
        # TODO: store username on self, and start followers at 0

    def follow(self):
        '''
        Gain one follower.

        >>> u = User('alice')
        >>> u.follow()
        >>> u.follow()
        >>> u.followers
        2
        '''
        # TODO: add one to self.followers

    def unfollow(self):
        '''
        Lose one follower, but never drop below zero.

        >>> u = User('alice')
        >>> u.follow()
        >>> u.follow()
        >>> u.unfollow()
        >>> u.followers
        1
        >>> u.unfollow()
        >>> u.unfollow()
        >>> u.followers
        0
        '''
        # TODO: subtract one from self.followers, but not below 0

    def __str__(self):
        '''
        Show a user as an @-handle.

        >>> print(User('alice'))
        @alice
        >>> str(User('bob'))
        '@bob'
        '''
        # TODO: return the username with an '@' in front

    def __eq__(self, other):
        '''
        Two users are equal when they have the same username.

        >>> User('alice') == User('alice')
        True
        >>> User('alice') == User('bob')
        False
        >>> User('alice') == 'alice'
        False
        '''
        # TODO: return True when other is a User with the same username


class Tweet:
    def __init__(self, author, text):
        '''
        Create a tweet by `author` saying `text`, starting with zero likes.

        >>> t = Tweet('alice', 'hello world')
        >>> t.author
        'alice'
        >>> t.text
        'hello world'
        >>> t.likes
        0
        '''
        # TODO: store author and text on self, and start likes at 0

    def like(self):
        '''
        Add one like.

        >>> t = Tweet('alice', 'hello')
        >>> t.like()
        >>> t.like()
        >>> t.likes
        2
        '''
        # TODO: add one to self.likes

    def unlike(self):
        '''
        Remove one like, but never drop below zero.

        >>> t = Tweet('alice', 'hello')
        >>> t.like()
        >>> t.unlike()
        >>> t.unlike()
        >>> t.likes
        0
        '''
        # TODO: subtract one from self.likes, but not below 0

    def hashtags(self):
        '''
        Return the hashtags in the text, without the leading '#'.

        >>> Tweet('alice', 'learning #python and #oop today').hashtags()
        ['python', 'oop']
        >>> Tweet('bob', 'just a normal tweet').hashtags()
        []
        >>> Tweet('alice', '#Games #Games #BringSnacks! word#inside #').hashtags()
        ['Games', 'Games', 'BringSnacks!', '']
        '''
        # TODO: split the text into words; keep the ones starting with '#',
        # returning each one without its leading '#'

    def __str__(self):
        '''
        Show a tweet as "@author: text".

        >>> print(Tweet('alice', 'hello world'))
        @alice: hello world
        '''
        # TODO: return the author and text formatted as '@author: text'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
