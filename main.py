def minion_game(s):
    vowels = 'AEIOU'

    kev_score = 0
    stu_score = 0

    for x in range(len(s)):
        if s[x] in vowels:
            kev_score += (len(s) - x)
        else:
            stu_score += (len(s) - x)

    if kev_score > stu_score:
        print("Kevin wins with a score of: {}".format(kev_score))

    if stu_score > kev_score:
        print("Stuart wins with a score of: {}".format(stu_score))

    if kev_score == stu_score:
        print("Kevin has a score of: {}".format(kev_score))
        print("Stuart has a score of: {}".format(stu_score))
        print("Both players have the same score and it is a draw!")


if __name__ == '__main__':
    s = input("What word would you like to use? ")
    minion_game(s)