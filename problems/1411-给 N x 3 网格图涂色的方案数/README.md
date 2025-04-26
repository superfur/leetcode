# 1411. 给 N x 3 网格图涂色的方案数

## 题目描述

<p>你有一个 <code>n x 3</code>&nbsp;的网格图 <code>grid</code>&nbsp;，你需要用 <strong>红，黄，绿</strong>&nbsp;三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。</p>

<p>给你网格图的行数 <code>n</code>&nbsp;。</p>

<p>请你返回给&nbsp;<code>grid</code>&nbsp;涂色的方案数。由于答案可能会非常大，请你返回答案对&nbsp;<code>10^9 + 7</code>&nbsp;取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>12
<strong>解释：</strong>总共有 12 种可行的方法：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/12/e1.png" style="height: 289px; width: 450px;">
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>54
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>246
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 7
<strong>输出：</strong>106494
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>n = 5000
<strong>输出：</strong>30228214
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>grid[i].length == 3</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 提示

1. We will use Dynamic programming approach. we will try all possible configuration.
2. Let dp[idx][prev1col][prev2col][prev3col] be the number of ways to color the rows of the grid from idx to n-1 keeping in mind that the previous row (idx - 1) has colors prev1col, prev2col and prev3col. Build the dp array to get the answer.

## 示例

```
1
5000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfWays(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfWays(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfWays(self, n: int) -> int:
        
```

### C

```c
int numOfWays(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfWays(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    
};
```

### TypeScript

```typescript
function numOfWays(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numOfWays($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfWays(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfWays(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfWays(int n) {
    
  }
}
```

### Go

```golang
func numOfWays(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def num_of_ways(n)
    
end
```

### Scala

```scala
object Solution {
    def numOfWays(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-ways n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_ways(N :: integer()) -> integer().
num_of_ways(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_ways(n :: integer) :: integer
  def num_of_ways(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfWays(n: Int64): Int64 {

    }
}
```

