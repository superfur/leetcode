# 646. 最长数对链

## 题目描述

<p>给你一个由&nbsp;<code>n</code>&nbsp;个数对组成的数对数组&nbsp;<code>pairs</code>&nbsp;，其中&nbsp;<code>pairs[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;且&nbsp;<code>left<sub>i</sub>&nbsp;&lt; right<sub>i</sub></code><sub> 。</sub></p>

<p>现在，我们定义一种 <strong>跟随</strong> 关系，当且仅当&nbsp;<code>b &lt; c</code>&nbsp;时，数对&nbsp;<code>p2 = [c, d]</code>&nbsp;才可以跟在&nbsp;<code>p1 = [a, b]</code>&nbsp;后面。我们用这种形式来构造 <strong>数对链</strong> 。</p>

<p>找出并返回能够形成的 <strong>最长数对链的长度</strong> 。</p>

<p>你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>pairs =&nbsp;[[1,2], [2,3], [3,4]]
<strong>输出：</strong>2
<strong>解释：</strong>最长的数对链是 [1,2] -&gt; [3,4] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>pairs = [[1,2],[7,8],[4,5]]
<b>输出：</b>3
<b>解释：</b>最长的数对链是 [1,2] -&gt; [4,5] -&gt; [7,8] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == pairs.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>-1000 &lt;= left<sub>i</sub>&nbsp;&lt; right<sub>i</sub>&nbsp;&lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划
- 排序

## 示例

```
[[1,2],[2,3],[3,4]]
[[1,2],[7,8],[4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLongestChain(int[][] pairs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
```

### C

```c
int findLongestChain(int** pairs, int pairsSize, int* pairsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLongestChain(int[][] pairs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} pairs
 * @return {number}
 */
var findLongestChain = function(pairs) {
    
};
```

### TypeScript

```typescript
function findLongestChain(pairs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $pairs
     * @return Integer
     */
    function findLongestChain($pairs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLongestChain(_ pairs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLongestChain(pairs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLongestChain(List<List<int>> pairs) {
    
  }
}
```

### Go

```golang
func findLongestChain(pairs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} pairs
# @return {Integer}
def find_longest_chain(pairs)
    
end
```

### Scala

```scala
object Solution {
    def findLongestChain(pairs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_longest_chain(pairs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-longest-chain pairs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_longest_chain(Pairs :: [[integer()]]) -> integer().
find_longest_chain(Pairs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_longest_chain(pairs :: [[integer]]) :: integer
  def find_longest_chain(pairs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLongestChain(pairs: Array<Array<Int64>>): Int64 {

    }
}
```

