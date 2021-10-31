


def monotonic(arr):
    if len(arr) <=1:
        return True
    isIncreasing=False
    isDecreasing=False

    for i in range(1,len(arr)):
        if isDecreasing & isIncreasing:
            return False
        if arr[i] < arr[i-1]:
            isDecreasing = True
        if arr[i] > arr[i-1]:
            isIncreasing = True

    if isDecreasing & isIncreasing:
        return False
    else:
        return True

if __name__ == '__main__':
    arr=[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(monotonic(arr))





