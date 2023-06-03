tweet = input()
censura = input()

if censura in tweet:
    print(tweet.replace(censura,"*"))
else:
    print("tudo certo :)")
