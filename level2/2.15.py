"""
Під час налагодження програми студентка Надя виявила дивну поведінку: програма зависає при обході зв'язаного списку. Вона підозрює, що в списку є цикл — один із вузлів вказує назад на попередній вузол. Щоб перевірити це, вона хоче реалізувати алгоритм Флойда («заєць і черепаха»).
На вхід подається список як масив посилань: next[i] — індекс наступного елемента після елемента i (або -1 якщо кінець). Знайди, чи є цикл, і якщо є — виведи індекс вузла, з якого цикл починається.

Вхідні дані
Перший рядок: ціле число N — кількість вузлів.
Другий рядок: N цілих чисел — масив next[0..N-1], де next[i] ∈ [-1,0..,N-1]. Список починається з вузла 0

Вихідні дані
Якщо циклу немає — NO CYCLE.
Якщо є — CYCLE AT X, де X — індекс початку циклу.
Приклад
Input:
6
1 2 3 4 2 -1

Output:
CYCLE AT 2
Input:
4
1 2 3 -1

Output:
NO CYCLE
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def hasCycle(self):
        hare = self.head
        tortoise = self.head
        cindex = 0
        while hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                print(f"CYCLE at {cindex}")
                return
        print("NO CYCLE")
        return

    def buildListFromLinks(self, links):
        nodes = []
        for i in range(len(links)):
            nodes.append(Node(0))
        for i in range((len(nodes))):
            nodes[i].next = nodes[links[i]]
        self.head = nodes[0]

def testCycle():
    n = int(input())
    linksArr = input().split()
    linksArr = list(map(int, linksArr))
    testList = LinkedList()
    testList.buildListFromLinks(linksArr)
    testList.hasCycle()

testCycle()