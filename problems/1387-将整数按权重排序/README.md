# 1387. 将整数按权重排序

## 题目描述

<p>我们将整数 <code>x</code>&nbsp;的 <strong>权重</strong> 定义为按照下述规则将 <code>x</code>&nbsp;变成 <code>1</code>&nbsp;所需要的步数：</p>

<ul>
	<li>如果&nbsp;<code>x</code>&nbsp;是偶数，那么&nbsp;<code>x = x / 2</code></li>
	<li>如果&nbsp;<code>x</code>&nbsp;是奇数，那么&nbsp;<code>x = 3 * x + 1</code></li>
</ul>

<p>比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --&gt; 10 --&gt; 5 --&gt; 16 --&gt; 8 --&gt; 4 --&gt; 2 --&gt; 1）。</p>

<p>给你三个整数&nbsp;<code>lo</code>，&nbsp;<code>hi</code> 和&nbsp;<code>k</code>&nbsp;。你的任务是将区间&nbsp;<code>[lo, hi]</code>&nbsp;之间的整数按照它们的权重&nbsp;<strong>升序排序&nbsp;</strong>，如果大于等于 2 个整数有&nbsp;<strong>相同</strong>&nbsp;的权重，那么按照数字自身的数值&nbsp;<strong>升序排序</strong>&nbsp;。</p>

<p>请你返回区间&nbsp;<code>[lo, hi]</code>&nbsp;之间的整数按权重排序后的第&nbsp;<code>k</code>&nbsp;个数。</p>

<p>注意，题目保证对于任意整数&nbsp;<code>x</code>&nbsp;<code>（lo &lt;= x &lt;= hi）</code>&nbsp;，它变成&nbsp;<code>1</code> 所需要的步数是一个 32 位有符号整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>lo = 12, hi = 15, k = 2
<strong>输出：</strong>13
<strong>解释：</strong>12 的权重为 9（12 --&gt; 6 --&gt; 3 --&gt; 10 --&gt; 5 --&gt; 16 --&gt; 8 --&gt; 4 --&gt; 2 --&gt; 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
区间内的数按权重排序以后的结果为 [12,13,14,15] 。对于 k = 2 ，答案是第二个整数也就是 13 。
注意，12 和 13 有相同的权重，所以我们按照它们本身升序排序。14 和 15 同理。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>lo = 7, hi = 11, k = 4
<strong>输出：</strong>7
<strong>解释：</strong>区间内整数 [7, 8, 9, 10, 11] 对应的权重为 [16, 3, 19, 6, 14] 。
按权重排序后得到的结果为 [8, 10, 11, 7, 9] 。
排序后数组中第 4 个数字为 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= lo &lt;= hi &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= hi - lo + 1</code></li>
</ul>


## 难度

Medium

## 标签

- 记忆化搜索
- 动态规划
- 排序

## 提示

1. Use dynamic programming to get the power of each integer of the intervals.
2. Sort all the integers of the interval by the power value and return the k-th in the sorted list.

## 示例

```
12
15
2
7
11
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getKth(int lo, int hi, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getKth(int lo, int hi, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
```

### C

```c
int getKth(int lo, int hi, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetKth(int lo, int hi, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} lo
 * @param {number} hi
 * @param {number} k
 * @return {number}
 */
var getKth = function(lo, hi, k) {
    
};
```

### TypeScript

```typescript
function getKth(lo: number, hi: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $lo
     * @param Integer $hi
     * @param Integer $k
     * @return Integer
     */
    function getKth($lo, $hi, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getKth(_ lo: Int, _ hi: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getKth(lo: Int, hi: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getKth(int lo, int hi, int k) {
    
  }
}
```

### Go

```golang
func getKth(lo int, hi int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} lo
# @param {Integer} hi
# @param {Integer} k
# @return {Integer}
def get_kth(lo, hi, k)
    
end
```

### Scala

```scala
object Solution {
    def getKth(lo: Int, hi: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-kth lo hi k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_kth(Lo :: integer(), Hi :: integer(), K :: integer()) -> integer().
get_kth(Lo, Hi, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_kth(lo :: integer, hi :: integer, k :: integer) :: integer
  def get_kth(lo, hi, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getKth(lo: Int64, hi: Int64, k: Int64): Int64 {

    }
}
```

