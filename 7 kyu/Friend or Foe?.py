def friend(x):
    sure_friends = []
    for name in x:
        if len(name) == 4:
            sure_friends.append(name)
    return sure_friends
