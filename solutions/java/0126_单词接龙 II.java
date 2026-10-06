class Solution {
    /**
     * 126. 单词接龙 II
     * BFS 逐层扩展，记录每个单词在最短路径上的所有前驱（只记录首次被发现的那一层），
     * 第一次碰到 endWord 就停；然后从 endWord 沿前驱表回溯到 beginWord，还原所有最短路径。
     */
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> res = new ArrayList<>();
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) {
            return res;
        }

        Map<String, List<String>> parents = new HashMap<>();
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);
        Set<String> level = new HashSet<>();
        level.add(beginWord);
        boolean found = false;

        while (!level.isEmpty() && !found) {
            Set<String> next = new HashSet<>();
            for (String w : level) {
                char[] cs = w.toCharArray();
                for (int i = 0; i < cs.length; i++) {
                    char orig = cs[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == orig) {
                            continue;
                        }
                        cs[i] = c;
                        String nw = new String(cs);
                        if (words.contains(nw) && !visited.contains(nw)) {
                            parents.computeIfAbsent(nw, k -> new ArrayList<>()).add(w);
                            next.add(nw);
                            if (nw.equals(endWord)) {
                                found = true;
                            }
                        }
                    }
                    cs[i] = orig;
                }
            }
            visited.addAll(next);
            level = next;
        }

        if (!found) {
            return res;
        }

        LinkedList<String> path = new LinkedList<>();
        path.add(endWord);
        back(endWord, beginWord, parents, path, res);
        return res;
    }

    private void back(String w, String begin, Map<String, List<String>> parents,
                      LinkedList<String> path, List<List<String>> res) {
        if (w.equals(begin)) {
            List<String> p = new ArrayList<>(path);
            Collections.reverse(p);
            res.add(p);
            return;
        }
        for (String p : parents.getOrDefault(w, Collections.emptyList())) {
            path.add(p);
            back(p, begin, parents, path, res);
            path.removeLast();
        }
    }
}
