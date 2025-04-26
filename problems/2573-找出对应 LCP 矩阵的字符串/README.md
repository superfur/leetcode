# 2573. 找出对应 LCP 矩阵的字符串

## 题目描述

<p>对任一由 <code>n</code> 个小写英文字母组成的字符串 <code>word</code> ，我们可以定义一个 <code>n x n</code> 的矩阵，并满足：</p>

<ul>
	<li><code>lcp[i][j]</code> 等于子字符串&nbsp;<code>word[i,...,n-1]</code> 和 <code>word[j,...,n-1]</code> 之间的最长公共前缀的长度。</li>
</ul>

<p>给你一个 <code>n x n</code> 的矩阵 <code>lcp</code> 。返回与 <code>lcp</code> 对应的、按字典序最小的字符串&nbsp;<code>word</code> 。如果不存在这样的字符串，则返回空字符串。</p>

<p>对于长度相同的两个字符串 <code>a</code> 和 <code>b</code> ，如果在 <code>a</code> 和 <code>b</code> 不同的第一个位置，字符串 <code>a</code> 的字母在字母表中出现的顺序先于 <code>b</code> 中的对应字母，则认为字符串 <code>a</code> 按字典序比字符串 <code>b</code> 小。例如，<code>"aabd"</code> 在字典上小于 <code>"aaca"</code> ，因为二者不同的第一位置是第三个字母，而&nbsp;<code>'b'</code> 先于 <code>'c'</code> 出现。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
<strong>输出：</strong>"abab"
<strong>解释：</strong>lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
<strong>输出：</strong>"aaaa"
<strong>解释：</strong>lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
<strong>输出：</strong>""
<strong>解释：</strong>lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n ==&nbsp;</code><code>lcp.length == </code><code>lcp[i].length</code>&nbsp;<code>&lt;= 1000</code></li>
	<li><code><font face="monospace">0 &lt;= lcp[i][j] &lt;= n</font></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 并查集
- 数组
- 字符串
- 动态规划
- 矩阵

## 提示

1. Use the LCP array to determine which groups of elements must be equal.
2. Match the smallest letter to the group that contains the smallest unassigned index.
3. Build the LCP matrix of the resulting string then check if it is equal to the target LCP.

## 示例

```
[[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
[[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
[[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findTheString(vector<vector<int>>& lcp) {
        
    }
};
```

### Java

```java
class Solution {
    public String findTheString(int[][] lcp) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        
```

### C

```c
char* findTheString(int** lcp, int lcpSize, int* lcpColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindTheString(int[][] lcp) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} lcp
 * @return {string}
 */
var findTheString = function(lcp) {
    
};
```

### TypeScript

```typescript
function findTheString(lcp: number[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $lcp
     * @return String
     */
    function findTheString($lcp) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTheString(_ lcp: [[Int]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTheString(lcp: Array<IntArray>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findTheString(List<List<int>> lcp) {
    
  }
}
```

### Go

```golang
func findTheString(lcp [][]int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} lcp
# @return {String}
def find_the_string(lcp)
    
end
```

### Scala

```scala
object Solution {
    def findTheString(lcp: Array[Array[Int]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-the-string lcp)
  (-> (listof (listof exact-integer?)) string?)
  )
```

### Erlang

```erlang
-spec find_the_string(Lcp :: [[integer()]]) -> unicode:unicode_binary().
find_the_string(Lcp) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_the_string(lcp :: [[integer]]) :: String.t
  def find_the_string(lcp) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTheString(lcp: Array<Array<Int64>>): String {

    }
}
```

