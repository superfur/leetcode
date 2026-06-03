package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < words.length) {
            int lineLen = words[i].length();
            int j = i + 1;
            while (j < words.length && lineLen + 1 + words[j].length() <= maxWidth) {
                lineLen += 1 + words[j].length();
                j++;
            }

            String[] lineWords = new String[j - i];
            for (int k = 0; k < j - i; k++) {
                lineWords[k] = words[i + k];
            }

            int totalChars = 0;
            for (String w : lineWords) {
                totalChars += w.length();
            }
            int gaps = lineWords.length - 1;
            boolean isLastLine = j == words.length;

            if (gaps == 0 || isLastLine) {
                StringBuilder sb = new StringBuilder(String.join(" ", lineWords));
                while (sb.length() < maxWidth) {
                    sb.append(' ');
                }
                result.add(sb.toString());
            } else {
                int totalSpaces = maxWidth - totalChars;
                int spacePerGap = totalSpaces / gaps;
                int extraSpaces = totalSpaces % gaps;
                StringBuilder sb = new StringBuilder();
                for (int k = 0; k < lineWords.length; k++) {
                    sb.append(lineWords[k]);
                    if (k < gaps) {
                        int spaces = spacePerGap + (extraSpaces > 0 ? 1 : 0);
                        if (extraSpaces > 0) {
                            extraSpaces--;
                        }
                        for (int s = 0; s < spaces; s++) {
                            sb.append(' ');
                        }
                    }
                }
                result.add(sb.toString());
            }

            i = j;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        String[] words1 = {"This", "is", "an", "example", "of", "text", "justification."};
        List<String> result1 = sol.fullJustify(words1, 16);
        for (String line : result1) {
            System.out.println("\"" + line + "\"");
        }

        String[] words2 = {"What", "must", "be", "acknowledgment", "shall", "be"};
        List<String> result2 = sol.fullJustify(words2, 16);
        for (String line : result2) {
            System.out.println("\"" + line + "\"");
        }

        String[] words3 = {"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"};
        List<String> result3 = sol.fullJustify(words3, 20);
        for (String line : result3) {
            System.out.println("\"" + line + "\"");
        }
    }
}
