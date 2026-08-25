public class Solution {
    /**
     * 93. 复原 IP 地址
     * 回溯：依次切出长度 1~3 的一段作为一个 IP 段，
     * 段值需在 0~255 之间且不能有前导 0（除了单独的 "0"）；
     * 切出 4 段且恰好用完所有字符时才是一个合法答案。
     */
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new java.util.ArrayList<>();
        backtrack(s, 0, new java.util.ArrayList<>(), result);
        return result;
    }

    private void backtrack(String s, int start, List<String> segments, List<String> result) {
        int n = s.length();
        if (segments.size() == 4) {
            if (start == n) {
                result.add(String.join(".", segments));
            }
            return;
        }
        if (n - start > (4 - segments.size()) * 3) {
            return;
        }
        for (int length = 1; length <= 3 && start + length <= n; length++) {
            String segment = s.substring(start, start + length);
            if (length > 1 && segment.charAt(0) == '0') {
                break;
            }
            if (Integer.parseInt(segment) > 255) {
                break;
            }
            segments.add(segment);
            backtrack(s, start + length, segments, result);
            segments.remove(segments.size() - 1);
        }
    }
}
