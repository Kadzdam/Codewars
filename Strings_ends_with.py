def solution(string, ending):
    num = len(ending)
    if string[-num:] == ending or num == 0 or string == ending:
        return True
    else:
        return False