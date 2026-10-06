use std::collections::{HashMap, HashSet};

impl Solution {
    /// 126. 单词接龙 II
    /// BFS 逐层扩展，记录每个单词在最短路径上的所有前驱（只记录首次被发现的那一层），
    /// 第一次碰到 endWord 就停；然后从 endWord 沿前驱表回溯到 beginWord，还原所有最短路径。
    pub fn find_ladders(begin_word: String, end_word: String, word_list: Vec<String>) -> Vec<Vec<String>> {
        let words: HashSet<String> = word_list.into_iter().collect();
        if !words.contains(&end_word) {
            return vec![];
        }

        let mut parents: HashMap<String, Vec<String>> = HashMap::new();
        let mut visited: HashSet<String> = HashSet::new();
        visited.insert(begin_word.clone());
        let mut level: Vec<String> = vec![begin_word.clone()];
        let mut found = false;

        while !level.is_empty() && !found {
            let mut next: HashSet<String> = HashSet::new();
            for w in &level {
                let mut chars: Vec<u8> = w.bytes().collect();
                for i in 0..chars.len() {
                    let orig = chars[i];
                    for c in b'a'..=b'z' {
                        if c == orig {
                            continue;
                        }
                        chars[i] = c;
                        let nw = String::from_utf8(chars.clone()).unwrap();
                        if words.contains(&nw) && !visited.contains(&nw) {
                            parents.entry(nw.clone()).or_default().push(w.clone());
                            if nw == end_word {
                                found = true;
                            }
                            next.insert(nw);
                        }
                    }
                    chars[i] = orig;
                }
            }
            visited.extend(next.iter().cloned());
            level = next.into_iter().collect();
        }

        if !found {
            return vec![];
        }

        fn back(
            w: &str,
            begin: &str,
            parents: &HashMap<String, Vec<String>>,
            path: &mut Vec<String>,
            res: &mut Vec<Vec<String>>,
        ) {
            if w == begin {
                let mut p = path.clone();
                p.reverse();
                res.push(p);
                return;
            }
            if let Some(ps) = parents.get(w) {
                for p in ps {
                    path.push(p.clone());
                    back(p, begin, parents, path, res);
                    path.pop();
                }
            }
        }

        let mut res = Vec::new();
        let mut path = vec![end_word.clone()];
        back(&end_word, &begin_word, &parents, &mut path, &mut res);
        res
    }
}
