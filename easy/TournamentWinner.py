# https://www.algoexpert.io/questions/Tournament%20Winner


def tournamentWinner(competitions, results):
    # Write your code here.
    wins = []
    for i in range(0, len(competitions)):
        if results[i] == 1:
            wins.append(competitions[i][0])
        else:
            wins.append(competitions[i][1])

#     Problem is now reduced to find the mode of the wins array
    wins.sort()
    return mode(wins)

def mode(wins):
    maxT = None
    maxF = 0
    currF = 0
    currT = None
    for i in range(0,len(wins)):
        if  currT != wins[i]:
            currF=1
            currT = wins[i]
        else:
            currF = currF + 1
        if currF > maxF:
            maxF = currF
            maxT = currT
    return maxT

if __name__ == '__main__':

    comps = [
        ["Html","Python"],
        ["Html", "C#"],
        ["Html", "Python"]

    ]

    rest = [1,1,1]
    arr = [1,2,3,4,4,4,5,5,7,7,8]

    tournamentWinner(comps,rest)
    print(mode(arr))
