package level3;

import java.util.Arrays;
import java.util.Scanner;

public class three_two {
    static final int INF = Integer.MAX_VALUE;
    
    static int[] dijkstra(int[][] graph, int start) {
        int V = graph.length;
        int[] dist = new int[V];
        Arrays.fill(dist, Integer.MAX_VALUE);
        boolean[] visited = new boolean[V];
        Arrays.fill(visited, false);
        dist[start] = 0;

        for (int i = 0; i < V; i++) {
            // find min
            int closestV = -1;
            int closestsDist = Integer.MAX_VALUE;

            for (int j = 0; j < visited.length; j++) {
                if (!visited[j] && graph[i][j] < closestsDist) {
                    closestsDist = graph[i][j];
                    closestV = j;
                }
            }
            visited[closestV] = true;
            
            for (int j = 0; j < V; j++) {
                if (!visited[j] && graph[closestV][j] != 0 && dist[closestV] != Integer.MAX_VALUE) {
                    if (graph[closestV][j] + dist[i] < dist[j]) {
                        dist[j] = graph[closestV][j] + dist[i];
                    }
                }
            }
        }

        return dist;
    }

    static String getPath(int[] dist, int[] prev, String[] names, int start, int end) {
        if (dist[end] >= INF) {
            return "UNREACHABLE";
        }

        // Збираємо шлях з кінця до початку
        int[] path = new int[prev.length];
        int length = 0;
        int current = end;

        while (current != -1) {
            path[length++] = current;
            current = prev[current];
        }

        // Розвертаємо масив
        for (int i = 0; i < length / 2; i++) {
            int temp = path[i];
            path[i] = path[length - 1 - i];
            path[length - 1 - i] = temp;
        }

        // Будуємо рядок
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(names[path[i]]);
            if (i < length - 1) {
                sb.append(" → ");
            }
        }
        sb.append(" (відстань: ").append(dist[end]).append(")");
        return sb.toString();
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
        int start = scanner.nextInt()-1;
        int end = scanner.nextInt()-1;

        for (int i = 0; i < E; i++) {
            int u = scanner.nextInt()-1;
            int v = scanner.nextInt()-1;
            int weight = scanner.nextInt();
            addEdge(graph, u, v, weight);
        }

        System.out.println(dijkstra(graph, start)[end]);
        System.out.println(getPath(dijkstra(graph, start), new int[V], new String[V], start, end));
    }
}