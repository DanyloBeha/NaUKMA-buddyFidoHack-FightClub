/* 
Університет прокладає оптоволоконну мережу між V корпусами. З'єднати всі корпуси можна різними способами — між кожною парою є потенційне з'єднання з певною вартістю прокладки. Потрібно з'єднати всі корпуси з мінімальними витратами — тобто знайти мінімальне кістяне дерево (MST).
Реалізуй алгоритм Крускала з використанням системи непересічних множин (DSU / Union-Find).
Вхідні дані
Перший рядок: два цілих числа V та E
Наступні E рядків: три числа u, v, w — ребро між u та v з вагою w. Граф зв'язний, без петель.

Вихідні дані
Перший рядок: сумарна вага MST.
Наступні V−1 рядків: ребра MST у форматі u v w, відсортовані за зростанням u, при рівності — за v.
Приклад
Input:
4 5
1 2 10
1 3 6
1 4 5
2 4 15
3 4 4

Output:
19
1 2 10
1 4 5
3 4 4
*/


package level3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class threePointFive {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int[][] graph = new int[V][V];

        for (int i = 0; i < E; i++) {
            addEdge(graph, scanner.nextInt() - 1, scanner.nextInt() - 1, scanner.nextInt());
        }
        scanner.close();

        int[][] mst_kruskal = kruskal(graph);
        System.out.println(getWeight(mst_kruskal));

        // outputting edges
        for (int k = 0; k < mst_kruskal.length; k++) {
            for (int l = k; l < mst_kruskal[k].length; l++) {
                if (mst_kruskal[k][l] != 0) {
                    System.out.println(k+1 + " " + (l+1) + " " + mst_kruskal[k][l]);
                }
            }
        }
    }

    static void addEdge(int[][] graph, int u, int v, int weight) {
        graph[u][v] = weight;
        graph[v][u] = weight;
    }

    static int getWeight(int[][] graph) {
        int weight = 0;
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                weight += graph[i][j];
            }
        }
        return weight / 2;
    }

    static class Edge implements Comparable<Edge> {
        int u, v, weight;

        Edge(int u, int v, int weight) {
            this.u = u; this.v = v; this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }
    }
    static class UnionFind {
        int[] parent;
        int[] rank;

        UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        boolean union(int x, int y) {
            int x_root = find(x);
            int y_root = find(y);

            if (x_root == y_root) {
                return false;
            } else if (rank[x_root] > rank[y_root]) {
                parent[y_root] = x_root;
            } else if (rank[x_root] < rank[y_root]) {
                parent[x_root] = y_root;
            } else {
                parent[y_root] = x_root;
                rank[x_root]++;
            }
            return true;
        }
    }
    
    static int[][] kruskal(int[][] graph) {
        int V = graph.length;
        int[][] mst = new int[V][V];
        
        ArrayList<Edge> edges = new ArrayList<Edge>();
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < i; j++) {
                if (graph[i][j] != 0) {
                    edges.add(new Edge(i, j, graph[i][j]));
                }
            }
        }
        Collections.sort(edges);
        UnionFind uf = new UnionFind(V);
        int c = 0;
        for (Edge e : edges) {
            if (c != V-1 && uf.union(e.u, e.v) == true) {
                mst[e.v][e.u] = e.weight;
                mst[e.u][e.v] = e.weight;
                c++;
            }
        }
        return mst;
    }
}