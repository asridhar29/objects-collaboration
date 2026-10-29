"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.

This feed belongs to the Riverbend Board Game Club: three members
posting about Thursday game night.
"""

from lab_classes import User, Tweet


def build_feed():
    # The three members who keep game night running.
    mira = User('mira_rolls')
    dev = User('dev_the_dealer')
    june = User('june_meeples')
    users = [mira, dev, june]

    # What they posted this week.
    posts = [
        Tweet(mira.username, 'Thursday game night is on! #GameNight #Riverbend'),
        Tweet(dev.username, 'I am bringing the big box of dice #GameNight'),
        Tweet(june.username, 'Who wants to teach me Wingspan? no hashtags here'),
        Tweet(mira.username, 'Reminder: snacks rotation starts with Dev #BringSnacks!'),
    ]

    # Mira announces the night, so the club finds her first.
    mira.follow()
    mira.follow()
    mira.follow()
    dev.follow()
    june.follow()
    june.follow()
    # June goes quiet for a week and loses one of those followers.
    june.unfollow()

    # The announcement is the popular post.
    posts[0].like()
    posts[0].like()
    posts[0].like()
    posts[1].like()
    posts[2].like()
    posts[3].like()
    posts[3].like()
    # Dev reads the snacks reminder again and takes his like back.
    posts[3].unlike()

    return users, posts


def main():
    users, posts = build_feed()

    print('Riverbend Board Game Club')
    print('=' * 30)

    print('\nMembers:')
    for user in users:
        print(f'  {user} - {user.followers} followers')

    print('\nFeed:')
    for post in posts:
        print(f'  {post}')
        print(f'    likes: {post.likes}')
        print(f'    hashtags: {post.hashtags()}')


if __name__ == '__main__':
    main()
