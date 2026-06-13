"""
Деканат факультету інформатики вирішив автоматизувати облік відвідуваності. Є N студентів і M пар на тиждень. Куратор вводить таблицю: 1 означає, що студент був присутній, 0 — відсутній. Потрібно знайти студента з найкращою відвідуваністю (найбільшою кількістю присутностей). Якщо таких кілька — вивести того, чий номер менший (нумерація з 1).
Також потрібно вивести кількість пар, на яких жоден студент не був присутній — такі пари декан вважає «привидами» і хоче їх виключити з розкладу.
Вхідні дані
Перший рядок: два цілих числа N та M (1≤N≤100, 1≤M≤100).
Наступні N рядків містять по M чисел (0 або 1) через пробіл — рядок i відповідає студенту i

Вихідні дані
Перший рядок: номер студента з найкращою відвідуваністю.
Другий рядок: кількість «пар-привидів».
Приклад
Input:
3 4
1 0 1 1
0 0 1 0
1 0 1 1

Output:
3
1 
"""
def parcitipation():
    students, lessons = input().split(' ')
    matrix = []
    bestStudent = 0
    for i in range(int(students)):
        line = input().split(' ')
        matrix.append(list(map(int, line)))
        if (matrix[i].count(1) > matrix[bestStudent].count(1)):
            bestStudent = i

    ghosts = 0
    for j in range(int(lessons)):
        localGhost = True
        for k in range(int(students)):
            if (matrix[k][j] == 1):
                localGhost = False
        if localGhost:
            ghosts += 1
    
    print(bestStudent + 1)
    print(ghosts)

    

parcitipation()