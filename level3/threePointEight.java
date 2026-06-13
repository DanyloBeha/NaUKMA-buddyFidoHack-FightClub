/*
Легенда
Університетська мережа після збою розпалася на ізольовані сегменти. Системний адміністратор отримав список активних з'єднань між комп'ютерами і хоче знати: скільки ізольованих компонент зв'язності утворилося, яка найбільша компонента і які вузли до неї входять?
Реалізуй пошук компонент через DFS або Union-Find.
Вхідні дані
Перший рядок: два цілих числа V та E
Наступні E рядків: два числа u та v — неорієнтоване ребро.

Вихідні дані
Перший рядок: кількість компонент зв'язності.
Другий рядок: розмір найбільшої компоненти.
Третій рядок: вузли найбільшої компоненти у зростаючому порядку через пробіл (якщо кілька однакових за розміром — вибрати ту, що містить мінімальний вузол).
Приклад
Input:
7 4
1 2
2 3
4 5
6 7

Output:
3
2
1 2 3
*/

package level3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class threePointEight {
    static ArrayList<Integer> largestNodes = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int[][] graph = new int[V][V];

        for (int i = 0; i < E; i++) {
            addEdge(graph, scanner.nextInt() - 1, scanner.nextInt() - 1, 1);
        }
        scanner.close();

        int[] result = countComponents(graph);
        Collections.sort(largestNodes);
        System.out.println();       
        System.out.println(result[0]);
        System.out.println(result[1]);
        for (int n : largestNodes) {
            System.out.print(n + " ");
        }
    }

    static int dfs(int[][] graph, int node, boolean[] visited, int localCount, ArrayList<Integer> component) {
        localCount++;
        visited[node] = true;
        component.add(node + 1);

        for (int i = 0; i < graph.length; i++) {
            if (graph[node][i] > 0 && !visited[i]) {
                localCount = dfs(graph, i, visited, localCount, component);
            }
        }
        return localCount;
    }

    static int[] countComponents(int[][] graph) {
        boolean[] marked = new boolean[graph.length];
        int count = 0;
        int largestComponent = 0;
        for (int i = 0; i < graph.length; i++) {
            int localCount = 0;
            if (!marked[i]) {
                count++;
                ArrayList<Integer> component = new ArrayList<>();
                localCount = dfs(graph, i, marked, 0, component);
                if (localCount > largestComponent) {
                    largestComponent = localCount;
                    largestNodes = component;
                }
            }
        }
        return new int[] {count, largestComponent};
    }

    static void addEdge(int[][] graph, int u, int v, int weight) {
        graph[u][v] = weight;
        graph[v][u] = weight;
    }
}