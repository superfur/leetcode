# 2791. 树中可以形成回文的路径数

## 题目描述

<p>给你一棵 <strong>树</strong>（即，一个连通、无向且无环的图），<strong>根</strong> 节点为 <code>0</code> ，由编号从 <code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个节点组成。这棵树用一个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的数组 <code>parent</code> 表示，其中 <code>parent[i]</code> 为节点 <code>i</code> 的父节点，由于节点 <code>0</code> 为根节点，所以 <code>parent[0] == -1</code> 。</p>

<p>另给你一个长度为 <code>n</code> 的字符串 <code>s</code> ，其中 <code>s[i]</code> 是分配给 <code>i</code> 和 <code>parent[i]</code> 之间的边的字符。<code>s[0]</code> 可以忽略。</p>

<p>找出满足 <code>u &lt; v</code> ，且从 <code>u</code> 到 <code>v</code> 的路径上分配的字符可以 <strong>重新排列</strong> 形成 <strong>回文</strong> 的所有节点对&nbsp;<code>(u, v)</code> ，并返回节点对的数目。</p>

<p>如果一个字符串正着读和反着读都相同，那么这个字符串就是一个 <strong>回文</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/07/15/treedrawio-8drawio.png" style="width: 281px; height: 181px;" /></p>

<pre>
<strong>输入：</strong>parent = [-1,0,0,1,1,2], s = "acaabc"
<strong>输出：</strong>8
<strong>解释：</strong>符合题目要求的节点对分别是：
- (0,1)、(0,2)、(1,3)、(1,4) 和 (2,5) ，路径上只有一个字符，满足回文定义。
- (2,3)，路径上字符形成的字符串是 "aca" ，满足回文定义。
- (1,5)，路径上字符形成的字符串是 "cac" ，满足回文定义。
- (3,5)，路径上字符形成的字符串是 "acac" ，可以重排形成回文 "acca" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>parent = [-1,0,0,0,0], s = "aaaaa"
<strong>输出：</strong>10
<strong>解释：</strong>任何满足 u &lt; v 的节点对 (u,v) 都符合题目要求。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == parent.length == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li>对于所有 <code>i &gt;= 1</code> ，<code>0 &lt;= parent[i] &lt;= n - 1</code> 均成立</li>
	<li><code>parent[0] == -1</code></li>
	<li><code>parent</code> 表示一棵有效的树</li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 树
- 深度优先搜索
- 动态规划
- 状态压缩

## 提示

1. A string is a palindrome if the number of characters with an odd frequency is either 0 or 1.
2. Let mask[v] be a mask of 26 bits that represent the parity of each character in the alphabet on the path from node 0 to v. How can you use this array to solve the problem?

## 示例

```
[-1,0,0,1,1,2]
"acaabc"
[-1,0,0,0,0]
"aaaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countPalindromePaths(vector<int>& parent, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long countPalindromePaths(List<Integer> parent, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        
```

### C

```c
long long countPalindromePaths(int* parent, int parentSize, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountPalindromePaths(IList<int> parent, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var countPalindromePaths = function(parent, s) {
    
};
```

### TypeScript

```typescript
function countPalindromePaths(parent: number[], s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Integer
     */
    function countPalindromePaths($parent, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPalindromePaths(_ parent: [Int], _ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPalindromePaths(parent: List<Int>, s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPalindromePaths(List<int> parent, String s) {
    
  }
}
```

### Go

```golang
func countPalindromePaths(parent []int, s string) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} parent
# @param {String} s
# @return {Integer}
def count_palindrome_paths(parent, s)
    
end
```

### Scala

```scala
object Solution {
    def countPalindromePaths(parent: List[Int], s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_palindrome_paths(parent: Vec<i32>, s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-palindrome-paths parent s)
  (-> (listof exact-integer?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_palindrome_paths(Parent :: [integer()], S :: unicode:unicode_binary()) -> integer().
count_palindrome_paths(Parent, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_palindrome_paths(parent :: [integer], s :: String.t) :: integer
  def count_palindrome_paths(parent, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPalindromePaths(parent: ArrayList<Int64>, s: String): Int64 {

    }
}
```

