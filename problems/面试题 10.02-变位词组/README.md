# 面试题 10.02. 变位词组

## 题目描述

<p>编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。</p>

<p><strong>注意：</strong>本题相对原题稍作修改</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong><code>["eat", "tea", "tan", "ate", "nat", "bat"]</code>,
<strong>输出：</strong>
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>所有输入均为小写字母。</li>
	<li>不考虑答案输出的顺序。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. 你如何检查两个单词是否互为变位词？想一想如何定义“变位词”。用你自己的话来解释一下。
2. 两个单词互为变位词是指含有相同的字符，但顺序不同。怎么才能把字符排好序呢？
3. 你能利用标准排序算法吗？
4. 你真的需要真正的排序吗？或者仅需重新组织列表就够了？

## 示例

```
["eat","tea","tan","ate","nat","bat"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
};
```

### TypeScript

```typescript
function groupAnagrams(strs: string[]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    
  }
}
```

### Go

```golang
func groupAnagrams(strs []string) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    
end
```

### Scala

```scala
object Solution {
    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (group-anagrams strs)
  (-> (listof string?) (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec group_anagrams(Strs :: [unicode:unicode_binary()]) -> [[unicode:unicode_binary()]].
group_anagrams(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
  def group_anagrams(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func groupAnagrams(strs: Array<String>): ArrayList<ArrayList<String>> {

    }
}
```

