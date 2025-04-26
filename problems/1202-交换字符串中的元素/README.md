# 1202. 交换字符串中的元素

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，以及该字符串中的一些「索引对」数组&nbsp;<code>pairs</code>，其中&nbsp;<code>pairs[i] =&nbsp;[a, b]</code>&nbsp;表示字符串中的两个索引（编号从 0 开始）。</p>

<p>你可以 <strong>任意多次交换</strong> 在&nbsp;<code>pairs</code>&nbsp;中任意一对索引处的字符。</p>

<p>返回在经过若干次交换后，<code>s</code>&nbsp;可以变成的按字典序最小的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入：</strong>s = &quot;dcab&quot;, pairs = [[0,3],[1,2]]
<strong>输出：</strong>&quot;bacd&quot;
<strong>解释：</strong> 
交换 s[0] 和 s[3], s = &quot;bcad&quot;
交换 s[1] 和 s[2], s = &quot;bacd&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;dcab&quot;, pairs = [[0,3],[1,2],[0,2]]
<strong>输出：</strong>&quot;abcd&quot;
<strong>解释：</strong>
交换 s[0] 和 s[3], s = &quot;bcad&quot;
交换 s[0] 和 s[2], s = &quot;acbd&quot;
交换 s[1] 和 s[2], s = &quot;abcd&quot;</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;cba&quot;, pairs = [[0,1],[1,2]]
<strong>输出：</strong>&quot;abc&quot;
<strong>解释：</strong>
交换 s[0] 和 s[1], s = &quot;bca&quot;
交换 s[1] 和 s[2], s = &quot;bac&quot;
交换 s[0] 和 s[1], s = &quot;abc&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= pairs.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= pairs[i][0], pairs[i][1] &lt;&nbsp;s.length</code></li>
	<li><code>s</code>&nbsp;中只含有小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Think of it as a graph problem.
2. Consider the pairs as connected nodes in the graph, what can you do with a connected component of indices ?
3. We can sort each connected component alone to get the lexicographically minimum string.

## 示例

```
"dcab"
[[0,3],[1,2]]
"dcab"
[[0,3],[1,2],[0,2]]
"cba"
[[0,1],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
```

### C

```c
char* smallestStringWithSwaps(char* s, int** pairs, int pairsSize, int* pairsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestStringWithSwaps(string s, IList<IList<int>> pairs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function(s, pairs) {
    
};
```

### TypeScript

```typescript
function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $pairs
     * @return String
     */
    function smallestStringWithSwaps($s, $pairs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestStringWithSwaps(_ s: String, _ pairs: [[Int]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestStringWithSwaps(s: String, pairs: List<List<Int>>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestStringWithSwaps(String s, List<List<int>> pairs) {
    
  }
}
```

### Go

```golang
func smallestStringWithSwaps(s string, pairs [][]int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} pairs
# @return {String}
def smallest_string_with_swaps(s, pairs)
    
end
```

### Scala

```scala
object Solution {
    def smallestStringWithSwaps(s: String, pairs: List[List[Int]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-string-with-swaps s pairs)
  (-> string? (listof (listof exact-integer?)) string?)
  )
```

### Erlang

```erlang
-spec smallest_string_with_swaps(S :: unicode:unicode_binary(), Pairs :: [[integer()]]) -> unicode:unicode_binary().
smallest_string_with_swaps(S, Pairs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_string_with_swaps(s :: String.t, pairs :: [[integer]]) :: String.t
  def smallest_string_with_swaps(s, pairs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestStringWithSwaps(s: String, pairs: ArrayList<ArrayList<Int64>>): String {

    }
}
```

