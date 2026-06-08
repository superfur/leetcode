impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack: Vec<String> = Vec::new();
        for part in path.split('/') {
            match part {
                "" | "." => continue,
                ".." => {
                    stack.pop();
                }
                _ => stack.push(part.to_string()),
            }
        }
        format!("/{}", stack.join("/"))
    }
}
