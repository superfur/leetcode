# 692. 前K个高频单词

## 题目描述

<p>给定一个单词列表&nbsp;<code>words</code>&nbsp;和一个整数 <code>k</code> ，返回前&nbsp;<code>k</code><em>&nbsp;</em>个出现次数最多的单词。</p>

<p>返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， <strong>按字典顺序</strong> 排序。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
<strong>输出:</strong> ["i", "love"]
<strong>解析:</strong> "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
<strong>输出:</strong> ["the", "is", "sunny", "day"]
<strong>解析:</strong> "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 500</code></li>
	<li><code>1 &lt;= words[i] &lt;= 10</code></li>
	<li><code>words[i]</code>&nbsp;由小写英文字母组成。</li>
	<li><code>k</code> 的取值范围是&nbsp;<code>[1, <strong>不同</strong> words[i] 的数量]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>尝试以&nbsp;<code>O(n log k)</code> 时间复杂度和&nbsp;<code>O(n)</code> 空间复杂度解决。</p>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 桶排序
- 计数
- 排序
- 堆（优先队列）

## 示例

```
["i","love","leetcode","i","love","coding"]
2
["the","day","is","sunny","the","the","the","sunny","is","is"]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> TopKFrequent(string[] words, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    
};
```

### TypeScript

```typescript
function topKFrequent(words: string[], k: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer $k
     * @return String[]
     */
    function topKFrequent($words, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func topKFrequent(_ words: [String], _ k: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun topKFrequent(words: Array<String>, k: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> topKFrequent(List<String> words, int k) {
    
  }
}
```

### Go

```golang
func topKFrequent(words []string, k int) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Integer} k
# @return {String[]}
def top_k_frequent(words, k)
    
end
```

### Scala

```scala
object Solution {
    def topKFrequent(words: Array[String], k: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (top-k-frequent words k)
  (-> (listof string?) exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec top_k_frequent(Words :: [unicode:unicode_binary()], K :: integer()) -> [unicode:unicode_binary()].
top_k_frequent(Words, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec top_k_frequent(words :: [String.t], k :: integer) :: [String.t]
  def top_k_frequent(words, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func topKFrequent(words: Array<String>, k: Int64): ArrayList<String> {

    }
}
```

