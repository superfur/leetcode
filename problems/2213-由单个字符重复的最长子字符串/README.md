# 2213. 由单个字符重复的最长子字符串

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> 。另给你一个下标从 <strong>0</strong> 开始、长度为 <code>k</code> 的字符串 <code>queryCharacters</code> ，一个下标从 <code>0</code> 开始、长度也是 <code>k</code> 的整数 <strong>下标</strong> 数组&nbsp;<code>queryIndices</code> ，这两个都用来描述 <code>k</code> 个查询。</p>

<p>第 <code>i</code> 个查询会将 <code>s</code> 中位于下标 <code>queryIndices[i]</code> 的字符更新为 <code>queryCharacters[i]</code> 。</p>

<p>返回一个长度为 <code>k</code> 的数组 <code>lengths</code> ，其中 <code>lengths[i]</code> 是在执行第 <code>i</code> 个查询 <strong>之后</strong> <code>s</code> 中仅由 <strong>单个字符重复</strong> 组成的 <strong>最长子字符串</strong> 的 <strong>长度</strong> <em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
<strong>输出：</strong>[3,3,4]
<strong>解释：</strong>
- 第 1 次查询更新后 s = "<em>b<strong>b</strong>b</em>acc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
- 第 2 次查询更新后 s = "bbb<em><strong>c</strong>cc</em>" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
- 第 3 次查询更新后 s = "<em>bbb<strong>b</strong></em>cc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
因此，返回 [3,3,4] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
<strong>输出：</strong>[2,3]
<strong>解释：</strong>
- 第 1 次查询更新后 s = "ab<strong>a</strong><em>zz</em>" 。由单个字符重复组成的最长子字符串是 "zz" ，长度为 2 。
- 第 2 次查询更新后 s = "<em>a<strong>a</strong>a</em>zz" 。由单个字符重复组成的最长子字符串是 "aaa" ，长度为 3 。
因此，返回 [2,3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>k == queryCharacters.length == queryIndices.length</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>queryCharacters</code> 由小写英文字母组成</li>
	<li><code>0 &lt;= queryIndices[i] &lt; s.length</code></li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组
- 字符串
- 有序集合

## 提示

1. Use a segment tree to perform fast point updates and range queries.
2. We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.
3. We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.
4. Use this information to properly merge the two segment tree nodes together.

## 示例

```
"babacc"
"bcb"
[1,3,3]
"abyzz"
"aa"
[2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestRepeating(char* s, char* queryCharacters, int* queryIndices, int queryIndicesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] LongestRepeating(string s, string queryCharacters, int[] queryIndices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} queryCharacters
 * @param {number[]} queryIndices
 * @return {number[]}
 */
var longestRepeating = function(s, queryCharacters, queryIndices) {
    
};
```

### TypeScript

```typescript
function longestRepeating(s: string, queryCharacters: string, queryIndices: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $queryCharacters
     * @param Integer[] $queryIndices
     * @return Integer[]
     */
    function longestRepeating($s, $queryCharacters, $queryIndices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestRepeating(_ s: String, _ queryCharacters: String, _ queryIndices: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestRepeating(s: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> longestRepeating(String s, String queryCharacters, List<int> queryIndices) {
    
  }
}
```

### Go

```golang
func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} query_characters
# @param {Integer[]} query_indices
# @return {Integer[]}
def longest_repeating(s, query_characters, query_indices)
    
end
```

### Scala

```scala
object Solution {
    def longestRepeating(s: String, queryCharacters: String, queryIndices: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_repeating(s: String, query_characters: String, query_indices: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (longest-repeating s queryCharacters queryIndices)
  (-> string? string? (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec longest_repeating(S :: unicode:unicode_binary(), QueryCharacters :: unicode:unicode_binary(), QueryIndices :: [integer()]) -> [integer()].
longest_repeating(S, QueryCharacters, QueryIndices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_repeating(s :: String.t, query_characters :: String.t, query_indices :: [integer]) :: [integer]
  def longest_repeating(s, query_characters, query_indices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestRepeating(s: String, queryCharacters: String, queryIndices: Array<Int64>): Array<Int64> {

    }
}
```

