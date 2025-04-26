# 1420. 生成数组

## 题目描述

<p>给定三个整数 <code>n</code>、<code>m</code> 和 <code>k</code> 。考虑使用下图描述的算法找出正整数数组中最大的元素。</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/19/e.png" style="height: 372px; width: 424px;" /></p>

<p>请你构建一个具有以下属性的数组 <code>arr</code> ：</p>

<ul>
	<li><code>arr</code> 中包含确切的&nbsp;<code>n</code> 个整数。</li>
	<li><code>1 &lt;= arr[i] &lt;= m</code> 其中 <code>(0 &lt;= i &lt; n)</code> 。</li>
	<li>将上面提到的算法应用于 <code>arr</code>&nbsp;之后，<code>search_cost</code> 的值等于 <code>k</code> 。</li>
</ul>

<p>返回在满足上述条件的情况下构建数组 <code>arr</code> 的 <em>方法数量</em>&nbsp;，由于答案可能会很大，所以 <strong>必须</strong> 对 <code>10^9 + 7</code> 取余。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2, m = 3, k = 1
<strong>输出：</strong>6
<strong>解释：</strong>可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5, m = 2, k = 3
<strong>输出：</strong>0
<strong>解释：</strong>没有数组可以满足上述条件
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 9, m = 1, k = 1
<strong>输出：</strong>1
<strong>解释：</strong>唯一可能的数组是 [1, 1, 1, 1, 1, 1, 1, 1, 1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划
- 前缀和

## 提示

1. Use dynamic programming approach. Build dp table where dp[a][b][c] is the number of ways you can start building the array starting from index a where the search_cost = c and the maximum used integer was b.
2. Recursively, solve the small sub-problems first. Optimize your answer by stopping the search if you exceeded k changes.

## 示例

```
2
3
1
5
2
3
9
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfArrays(int n, int m, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
```

### C

```c
int numOfArrays(int n, int m, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfArrays(int n, int m, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
var numOfArrays = function(n, m, k) {
    
};
```

### TypeScript

```typescript
function numOfArrays(n: number, m: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer $k
     * @return Integer
     */
    function numOfArrays($n, $m, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfArrays(n: Int, m: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfArrays(int n, int m, int k) {
    
  }
}
```

### Go

```golang
func numOfArrays(n int, m int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def num_of_arrays(n, m, k)
    
end
```

### Scala

```scala
object Solution {
    def numOfArrays(n: Int, m: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-arrays n m k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_arrays(N :: integer(), M :: integer(), K :: integer()) -> integer().
num_of_arrays(N, M, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_arrays(n :: integer, m :: integer, k :: integer) :: integer
  def num_of_arrays(n, m, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfArrays(n: Int64, m: Int64, k: Int64): Int64 {

    }
}
```

