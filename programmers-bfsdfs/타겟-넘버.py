def solution(numbers, target):
    ali=[0]
    for i in numbers:
        cli=[]
        for j in ali:
            cli.append(j+i)
            cli.append(j-i)
        ali=cli
    answer=ali.count(target)        
    return answer
