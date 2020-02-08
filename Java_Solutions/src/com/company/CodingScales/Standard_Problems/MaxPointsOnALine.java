package com.company.CodingScales.Standard_Problems;

import java.util.HashMap;

public class MaxPointsOnALine {

    public static int maxPoints(int[][] points) {
        int globalMax = 1;
        for (int i = 0; i < points.length; i ++) {
            int []pointA = points[i];
            int localMax = 1;
            int same = 0;
            HashMap<Double, Integer> slopeToPointCount = new HashMap<Double, Integer>();
            for (int j = i + 1; j < points.length; j ++) {
                int []otherPoint = points[j];
                if (isSame(pointA, otherPoint)) {
                    same++;
                    continue;
                }
                Double slope = getSlope(pointA, otherPoint);
                slopeToPointCount.put(slope, slopeToPointCount.getOrDefault(slope, 1) + 1);
                localMax = Math.max(localMax, slopeToPointCount.get(slope));
            }
            globalMax = Math.max(globalMax, localMax + same);
        }
        return globalMax;
    }

    private static Double getSlope(int[] pointA, int[] otherPoint) {
        int x1, y1, x2, y2;
        x1 = pointA[0];
        y1 = pointA[1];
        x2 = otherPoint[0];
        y2 = otherPoint[1];

        if (x1 == x2) {
            return (double) Integer.MAX_VALUE;
        }
        if (y1 == y2) {
            return (double) 0;
        }
        return (double) ((y2 - y1) / (x2 - x1));

    }

    private static boolean isSame(int[] pointA, int[] otherPoint) {
        return pointA[0] == otherPoint[0] && pointA[1] == otherPoint[1];
    }

    public static void main(String[] args) {
        int [][] input = {{1, 1}, {2, 2}, {3, 3}}; // 3
        System.out.println(maxPoints(input));
        int [][] anotherInput = {{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}}; // 4
        System.out.println(maxPoints(anotherInput));
        int [][] yetAnotherInput = {{0, 0}, {94911151, 94911150}, {94911152, 94911151}};
        System.out.println(maxPoints(yetAnotherInput)); // 2
    }
}
