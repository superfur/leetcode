# 2513. 最小化两个数组中的最大值

## 题目描述

<p>给你两个数组&nbsp;<code>arr1</code> 和&nbsp;<code>arr2</code>&nbsp;，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：</p>

<ul>
	<li><code>arr1</code>&nbsp;包含&nbsp;<code>uniqueCnt1</code>&nbsp;个<strong>&nbsp;互不相同</strong>&nbsp;的正整数，每个整数都&nbsp;<strong>不能 </strong>被&nbsp;<code>divisor1</code>&nbsp;<strong>整除</strong>&nbsp;。</li>
	<li><code>arr2</code>&nbsp;包含&nbsp;<code>uniqueCnt2</code>&nbsp;个<strong>&nbsp;互不相同</strong>&nbsp;的正整数，每个整数都&nbsp;<strong>不能</strong>&nbsp;被&nbsp;<code>divisor2</code>&nbsp;<strong>整除</strong>&nbsp;。</li>
	<li><code>arr1</code> 和&nbsp;<code>arr2</code>&nbsp;中的元素&nbsp;<strong>互不相同</strong>&nbsp;。</li>
</ul>

<p>给你&nbsp;<code>divisor1</code>&nbsp;，<code>divisor2</code>&nbsp;，<code>uniqueCnt1</code>&nbsp;和&nbsp;<code>uniqueCnt2</code>&nbsp;，请你返回两个数组中&nbsp;<strong>最大元素</strong>&nbsp;的&nbsp;<strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
<b>输出：</b>4
<b>解释：</b>
我们可以把前 4 个自然数划分到 arr1 和 arr2 中。
arr1 = [1] 和 arr2 = [2,3,4] 。
可以看出两个数组都满足条件。
最大值是 4 ，所以返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
<b>输出：</b>3
<b>解释：</b>
arr1 = [1,2] 和 arr2 = [3] 满足所有条件。
最大值是 3 ，所以返回 3 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
<b>输出：</b>15
<b>解释：</b>
最终数组为 arr1 = [1,3,5,7,9,11,13,15] 和 arr2 = [2,6] 。
上述方案是满足所有条件的最优解。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= divisor1, divisor2 &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= uniqueCnt1, uniqueCnt2 &lt; 10<sup>9</sup></code></li>
	<li><code>2 &lt;= uniqueCnt1 + uniqueCnt2 &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 二分查找
- 数论

## 提示

1. Use binary search to find smallest maximum element.
2. Add numbers divisible by x in nums2 and vice versa.

## 示例

```
2
7
1
3
3
5
2
1
2
4
8
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
```

### C

```c
int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} divisor1
 * @param {number} divisor2
 * @param {number} uniqueCnt1
 * @param {number} uniqueCnt2
 * @return {number}
 */
var minimizeSet = function(divisor1, divisor2, uniqueCnt1, uniqueCnt2) {
    
};
```

### TypeScript

```typescript
function minimizeSet(divisor1: number, divisor2: number, uniqueCnt1: number, uniqueCnt2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $divisor1
     * @param Integer $divisor2
     * @param Integer $uniqueCnt1
     * @param Integer $uniqueCnt2
     * @return Integer
     */
    function minimizeSet($divisor1, $divisor2, $uniqueCnt1, $uniqueCnt2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeSet(_ divisor1: Int, _ divisor2: Int, _ uniqueCnt1: Int, _ uniqueCnt2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
    
  }
}
```

### Go

```golang
func minimizeSet(divisor1 int, divisor2 int, uniqueCnt1 int, uniqueCnt2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} divisor1
# @param {Integer} divisor2
# @param {Integer} unique_cnt1
# @param {Integer} unique_cnt2
# @return {Integer}
def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2)
    
end
```

### Scala

```scala
object Solution {
    def minimizeSet(divisor1: Int, divisor2: Int, uniqueCnt1: Int, uniqueCnt2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_set(divisor1: i32, divisor2: i32, unique_cnt1: i32, unique_cnt2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-set divisor1 divisor2 uniqueCnt1 uniqueCnt2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_set(Divisor1 :: integer(), Divisor2 :: integer(), UniqueCnt1 :: integer(), UniqueCnt2 :: integer()) -> integer().
minimize_set(Divisor1, Divisor2, UniqueCnt1, UniqueCnt2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_set(divisor1 :: integer, divisor2 :: integer, unique_cnt1 :: integer, unique_cnt2 :: integer) :: integer
  def minimize_set(divisor1, divisor2, unique_cnt1, unique_cnt2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeSet(divisor1: Int64, divisor2: Int64, uniqueCnt1: Int64, uniqueCnt2: Int64): Int64 {

    }
}
```

