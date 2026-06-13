"""
Легенда
Аналітик університетської їдальні записав зміну виручки за кожну годину роботи: позитивне число — прибуток, від'ємне — збиток. Він хоче знайти неперервний проміжок годин, за який сумарна виручка була максимальною — щоб зрозуміти, в який час відкривати буфет.
Наївний підхід O(N^2)занадто повільний для великих даних. Реалізуй алгоритм Кадане за O(N)
Вхідні дані
Перший рядок: ціле число NN N (1≤N≤1051 \le N \le 10^5 1≤N≤105).
Другий рядок: N
Вихідні дані
Виведіть три числа: максимальну суму, індекс початку та індекс кінця підмасиву (індексація з 0). Якщо кілька відповідей — виводити ту, що починається раніше; при рівному початку — ту, що закінчується раніше.
Приклад
Input:
9
-2 1 -3 4 -1 2 1 -5 4

Output:
6 3 6
"""
def maxSubarr():
    l = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    currentMax = arr[0]
    globalMax = arr[0]

    tempStart = 0
    startIndex = 0
    endIndex = 0

    for i in range(1, len(arr)):
        if currentMax + arr[i] < arr[i]:
            currentMax = arr[i]
            tempStart = i
        else:
            currentMax += arr[i]

        if currentMax > globalMax:
            startIndex = tempStart
            globalMax = currentMax
            endIndex = i
    
    print(f"{globalMax} {startIndex} {endIndex}")

maxSubarr()