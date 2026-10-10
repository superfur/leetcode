class Solution {
    /**
     * 127. 单词接龙
     * BFS：从 beginWord 出发，每次把某一位换成 a~z，命中字典的单词就入队，
     * 并立刻从字典里删掉（等价于标记已访问）。
     * 第一次碰到 endWord 时的步数（按单词个数计，起点算 1）就是答案。
     */
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) {
            return 0;
        }

        words.remove(beginWord);
        List<String> level = new ArrayList<>();
        level.add(beginWord);
        int steps = 1;

        while (!level.isEmpty()) {
            List<String> next = new ArrayList<>();
            for (String word : level) {
                char[] cs = word.toCharArray();
                for (int i = 0; i < cs.length; i++) {
                    char orig = cs[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) {
                            continue;
                        }
                        cs[i] = c;
                        String nw = new String(cs);
                        if (words.contains(nw)) {
                            if (nw.equals(endWord)) {
                                return steps + 1;
                            }
                            words.remove(nw);
                            next.add(nw);
                        }
                    }
                    cs[i] = orig;
                }
            }
            level = next;
            steps++;
        }
        return 0;
    }
}
