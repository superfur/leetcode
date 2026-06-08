package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String simplifyPath(String path) {
        String[] parts = path.split("/");
        List<String> stack = new ArrayList<>();

        for (String part : parts) {
            if (part.isEmpty() || part.equals(".")) {
                continue;
            } else if (part.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.remove(stack.size() - 1);
                }
            } else {
                stack.add(part);
            }
        }

        return "/" + String.join("/", stack);
    }
}
