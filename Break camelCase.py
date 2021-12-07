def solution(s):
    var=""
    for x in s:
        if x.isupper() and x.isalpha():
            var+=" "+x
        else:
            var+=x
    return var
