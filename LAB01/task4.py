import sys
sys.stdin = open('input4.txt', 'r')
sys.stdout = open('output4.txt', 'w')

def insertionSort(arr):
  for i in range(1, len(arr)):
    trainName, destination, time = arr[i]
    hour = int(time.split(":")[0])
    j = i - 1
    prevTrainName, prevDestination, prevTime = arr[j][0], arr[j][1], arr[j][2]
    prevHour = int(prevTime.split(":")[0])
    while j>=0 and (prevTrainName > trainName or (prevTrainName == trainName and prevHour < hour)):
      arr[j+1] = arr[j]
      j -= 1
      prevTrainName, prevDestination, prevTime = arr[j][0], arr[j][1], arr[j][2]
      prevHour = int(prevTime.split(":")[0])
    arr[j+1] = (trainName, destination, time)
  return arr


if __name__ == "__main__":
    testCases = int(input())
    data = []

    for i in range(testCases):
        lst = input().split(" ")
        data.append((lst[0], lst[-3], lst[-1]))
    sortedData = insertionSort(data)

    for trainName, destination, time in sortedData:
        print(f"{trainName} will departure for {destination} at {time}")

