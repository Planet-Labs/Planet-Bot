import random


def enf(level):
    if level < 21:
        percent = 95
        rank = "알"
    elif level < 41:
        percent = 85
        rank = "병아리"
    elif level < 61:
        percent = 81
        rank = "닭"
    elif level < 81:
        percent = 74
        rank = "강아지"
    elif level < 101:
        percent = 63
        rank = "개"
    elif level < 121:
        percent = 55
        rank = "돼지"
    elif level < 141:
        percent = 46
        rank = "소"
    elif level < 161:
        percent = 25
        rank = "말"
    elif level < 181:
        percent = 13
        rank = "호랑이"
    elif level < 201:
        percent = 7
        rank = "곰"
    else:
        percent = 5
        rank = "용"

    return percent, rank