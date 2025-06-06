# 1621. 大小为 K 的不重叠线段的数目

## 题目描述

<p>给你一维空间的 <code>n</code> 个点，其中第 <code>i</code> 个点（编号从 <code>0</code> 到 <code>n-1</code>）位于 <code>x = i</code> 处，请你找到 <strong>恰好</strong> <code>k</code> <strong>个不重叠</strong> 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 <strong>整数坐标</strong> 。这 <code>k</code> 个线段不需要全部覆盖全部 <code>n</code> 个点，且它们的端点 <strong>可以 </strong>重合。</p>

<p>请你返回 <code>k</code> 个不重叠线段的方案数。由于答案可能很大，请将结果对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/17/ex1.png" style="width: 179px; height: 222px;" />
<pre>
<b>输入：</b>n = 4, k = 2
<b>输出：</b>5
<strong>解释：
</strong>如图所示，两个线段分别用红色和蓝色标出。
上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, k = 1
<b>输出：</b>3
<strong>解释：</strong>总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 30, k = 7
<b>输出：</b>796297179
<strong>解释：</strong>画 7 条线段的总方案数为 3796297200 种。将这个数对 10<sup>9</sup> + 7 取余得到 796297179 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>n = 5, k = 3
<b>输出：</b>7
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<b>输入：</b>n = 3, k = 2
<b>输出：</b>1</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>1 <= k <= n-1</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. Try to use dynamic programming where the current index and remaining number of line segments to form can describe any intermediate state.
2. To make the computation of each state in constant time, we could add another flag to the state that indicates whether or not we are in the middle of placing a line (placed start point but no endpoint).

## 示例

```
4
2
3
1
30
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSets(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSets(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
```

### C

```c
int numberOfSets(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSets(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numberOfSets = function(n, k) {
    
};
```

### TypeScript

```typescript
function numberOfSets(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numberOfSets($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSets(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSets(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSets(int n, int k) {
    
  }
}
```

### Go

```golang
func numberOfSets(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_sets(n, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSets(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_sets(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-sets n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_sets(N :: integer(), K :: integer()) -> integer().
number_of_sets(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_sets(n :: integer, k :: integer) :: integer
  def number_of_sets(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSets(n: Int64, k: Int64): Int64 {

    }
}
```

