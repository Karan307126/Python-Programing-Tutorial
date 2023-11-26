def game():
    score=int(input("Enter the score:-"))
    return score

score=game()
with open('hiscore.txt') as f:
    hiscorestr=f.read()

if hiscorestr=='':
    with open('hiscore.txt','w') as f:
        f.write(str(score))
elif int(hiscorestr)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))