package com.company.CodingScales.Standard_Problems;

import java.util.HashSet;
import java.util.Set;

class Main {
    static int nodecount(char[][] adj, char chr) {
        int k = 0;
        for(char[] edge : adj) {
            if(edge[1] == chr)
                k+= nodecount(adj, edge[0]);
        }
        return 1 + k;
    }

    static void countFamilyNodes() {
        char[][] adj = new char[][] { { 'A', 'C' }, { 'B', 'C' }, { 'D', 'E' }, { 'F', 'E' }, { 'E', 'B' } };
        Set<Character> chars = new HashSet<Character>();
        for(char[] arr : adj) {
            if(chars.add(arr[1])) {
                int count = nodecount(adj, arr[1]) - 1;
                System.out.printf("%s : %d\r\n", arr[1], count);
            }
        }
        for(char[] arr : adj) {
            if(chars.add(arr[0])) {
                System.out.printf("%s : %d\r\n", arr[0], 0);
            }
        }
    }

    public static void main(String[] args) {
        countFamilyNodes();
    }
}