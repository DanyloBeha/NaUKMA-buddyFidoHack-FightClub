package level3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Scanner;

public class three_eleven {
    static int[] bfs(int[][] graph, int start) {
        int V = graph.length;
        int[] hops = new int[V];
        for (int i = 0; i < V; i++) {
            hops[i] = -1;
        }
        hops[start] = 0;
        Set<Integer> visited = new HashSet<>();
        List<Integer> queue = new ArrayList<>();
        queue.add(start);
        visited.add(start);
        

        int curV = -1;
        while (!queue.isEmpty()) {
            curV = queue.getFirst();
            queue.remove(0);
            for (int i = 0; i < V; i++) {
                if (graph[curV][i] != 0 && !visited.contains(i)) {
                    queue.add(i);
                    visited.add(i);
                    hops[i] = hops[curV]+1;
                }
            }
        }
        
        return hops;
    }

    static void addEdge(int[][] graph, int u, int v, int weight) {
        graph[u][v] = weight;
        graph[v][u] = weight;
    }
    
    static void removeEdge(int[][] graph, int u, int v) {
        graph[u][v] = 0;
        graph[v][u] = 0;
    }

    static boolean isConnected(int[][] graph) {
        int[] hops = bfs(graph, 0);
        for (int i = 0; i < hops.length; i++) {
            if (hops[i] == -1) {
                return false;
            }
        }
        return true;
    }

    static void findAllBridges(int[][] graph, int[][] edges) {
        int V = graph.length;
        List<int[]> bridges = new ArrayList<>();
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            if (graph[u][v] != 0) {
                removeEdge(graph, u, v);
                if (!isConnected(graph)) {
                    bridges.add(new int[]{u, v});
                }
                addEdge(graph, u, v, 1);
            }
        }

        System.out.println(bridges.size());
        for (int[] bridge : bridges) {
            if (bridge[0] != 0 || bridge[1] != 0) {
                System.out.print((bridge[0]+1));
                System.out.print(" ");
                System.out.println((bridge[1]+1));
                }
            }
        }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int[][] graph = new int[V][V];

        int[][] edges = new int[E][2];

        for (int i = 0; i < E; i++) {
            int u = scanner.nextInt()-1;
            int v = scanner.nextInt()-1;

            edges[i][0] = u;
            edges[i][1] = v;
            addEdge(graph, u, v, 1);
        }
        findAllBridges(graph, edges);
    }
}


