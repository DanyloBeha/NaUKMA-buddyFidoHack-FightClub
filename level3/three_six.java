package level3;

import java.util.Scanner;

public class three_six {

    static void isBipartite(int[][] graph, int V) {
        int[] colors = new int[V];
        for (int i = 0; i < V; i++) {
            colors[i] = -1;
        }

        for (int start = 0; start < V; start++) {
            if (colors[start] == -1) {
                if (!bfsCheck(graph, colors, start)) {
                    System.out.println("NO");
                    return;
                }
            }
        }
        System.out.println("YES");
        for (int i = 0; i < V; i++) {
            if (colors[i] == 0) 
                System.out.print((i+1) + " ");
        }
        System.out.println();
        for (int i = 0; i < V; i++) {
            if (colors[i] == 1) 
                System.out.print((i+1) + " ");
        }
    }

    static boolean bfsCheck(int[][] graph, int[] colors, int start) {
        colors[start] = 0;
        java.util.Queue<Integer> queue = new java.util.LinkedList<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v = 0; v < graph[u].length; v++) {
                if (graph[u][v] == 1) {
                    if (colors[v] == -1) {
                        colors[v] = 1 - colors[u];
                        queue.add(v);
                    } else if (colors[v] == colors[u]) {
                        return false;
                    }
                }
            }
        }
        
        return true;
    }

    static void addEdge(int[][] graph, int u, int v, int weight) {
        graph[u][v] = weight;
        graph[v][u] = weight;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int[][] graph = new int[V][V];

        for (int i = 0; i < E; i++) {
            int u = scanner.nextInt()-1;
            int v = scanner.nextInt()-1;
            addEdge(graph, u, v, 1);
        }

        isBipartite(graph, V);
    }
}