package LeetCodeLearning.leetcode;

import LeetCodeLearning.leetcode.code.two_sum;

public class jlw {
    public static void main(String[] args) {
        two_sum two_sum = new two_sum();
        int[] res = two_sum.solution(new int[] {2,7,9,11}, 9);
        System.out.println(res.toString());
    }
}