# 2246. 相邻字符不同的最长路径

## 题目描述

<p>给你一棵 <strong>树</strong>（即一个连通、无向、无环图），根节点是节点 <code>0</code> ，这棵树由编号从 <code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个节点组成。用下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的数组 <code>parent</code> 来表示这棵树，其中 <code>parent[i]</code> 是节点 <code>i</code> 的父节点，由于节点 <code>0</code> 是根节点，所以 <code>parent[0] == -1</code> 。</p>

<p>另给你一个字符串 <code>s</code> ，长度也是 <code>n</code> ，其中 <code>s[i]</code> 表示分配给节点 <code>i</code> 的字符。</p>

<p>请你找出路径上任意一对相邻节点都没有分配到相同字符的 <strong>最长路径</strong> ，并返回该路径的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png" style="width: 201px; height: 241px;" /></p>

<pre>
<strong>输入：</strong>parent = [-1,0,0,1,1,2], s = "abacbe"
<strong>输出：</strong>3
<strong>解释：</strong>任意一对相邻节点字符都不同的最长路径是：0 -&gt; 1 -&gt; 3 。该路径的长度是 3 ，所以返回 3 。
可以证明不存在满足上述条件且比 3 更长的路径。 
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png" style="width: 201px; height: 221px;" /></p>

<pre>
<strong>输入：</strong>parent = [-1,0,0,0], s = "aabc"
<strong>输出：</strong>3
<strong>解释：</strong>任意一对相邻节点字符都不同的最长路径是：2 -&gt; 0 -&gt; 3 。该路径的长度为 3 ，所以返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == parent.length == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li>对所有 <code>i &gt;= 1</code> ，<code>0 &lt;= parent[i] &lt;= n - 1</code> 均成立</li>
	<li><code>parent[0] == -1</code></li>
	<li><code>parent</code> 表示一棵有效的树</li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 图
- 拓扑排序
- 数组
- 字符串

## 提示

1. Do a DFS from the root. At each node, calculate the longest path we can make from two branches of that subtree.
2. To do that, we need to find the length of the longest path from each of the node’s children.

## 示例

```
[-1,0,0,1,1,2]
"abacbe"
[-1,0,0,0]
"aabc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestPath(int[] parent, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
```

### C

```c
int longestPath(int* parent, int parentSize, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestPath(int[] parent, string s) {
        
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
var longestPath = function(parent, s) {
    
};
```

### TypeScript

```typescript
function longestPath(parent: number[], s: string): number {
    
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
    function longestPath($parent, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestPath(_ parent: [Int], _ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestPath(parent: IntArray, s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestPath(List<int> parent, String s) {
    
  }
}
```

### Go

```golang
func longestPath(parent []int, s string) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} parent
# @param {String} s
# @return {Integer}
def longest_path(parent, s)
    
end
```

### Scala

```scala
object Solution {
    def longestPath(parent: Array[Int], s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_path(parent: Vec<i32>, s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-path parent s)
  (-> (listof exact-integer?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_path(Parent :: [integer()], S :: unicode:unicode_binary()) -> integer().
longest_path(Parent, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_path(parent :: [integer], s :: String.t) :: integer
  def longest_path(parent, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestPath(parent: Array<Int64>, s: String): Int64 {

    }
}
```

