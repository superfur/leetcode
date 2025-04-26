# 2338. 统计理想数组的数目

## 题目描述

<p>给你两个整数 <code>n</code> 和 <code>maxValue</code> ，用于描述一个 <strong>理想数组</strong> 。</p>

<p>对于下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>arr</code> ，如果满足以下条件，则认为该数组是一个 <strong>理想数组</strong> ：</p>

<ul>
	<li>每个 <code>arr[i]</code> 都是从 <code>1</code> 到 <code>maxValue</code> 范围内的一个值，其中 <code>0 &lt;= i &lt; n</code> 。</li>
	<li>每个 <code>arr[i]</code> 都可以被 <code>arr[i - 1]</code> 整除，其中 <code>0 &lt; i &lt; n</code> 。</li>
</ul>

<p>返回长度为 <code>n</code> 的 <strong>不同</strong> 理想数组的数目。由于答案可能很大，返回对 <code>10<sup>9</sup> + 7</code> 取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, maxValue = 5
<strong>输出：</strong>10
<strong>解释：</strong>存在以下理想数组：
- 以 1 开头的数组（5 个）：[1,1]、[1,2]、[1,3]、[1,4]、[1,5]
- 以 2 开头的数组（2 个）：[2,2]、[2,4]
- 以 3 开头的数组（1 个）：[3,3]
- 以 4 开头的数组（1 个）：[4,4]
- 以 5 开头的数组（1 个）：[5,5]
共计 5 + 2 + 1 + 1 + 1 = 10 个不同理想数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5, maxValue = 3
<strong>输出：</strong>11
<strong>解释：</strong>存在以下理想数组：
- 以 1 开头的数组（9 个）：
   - 不含其他不同值（1 个）：[1,1,1,1,1] 
   - 含一个不同值 2（4 个）：[1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - 含一个不同值 3（4 个）：[1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- 以 2 开头的数组（1 个）：[2,2,2,2,2]
- 以 3 开头的数组（1 个）：[3,3,3,3,3]
共计 9 + 1 + 1 = 11 个不同理想数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= maxValue &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学
- 数论

## 提示

1. Notice that an ideal array is non-decreasing.
2. Consider an alternative problem: where an ideal array must also be strictly increasing. Can you use DP to solve it?
3. Will combinatorics help to get an answer from the alternative problem to the actual problem?

## 示例

```
2
5
5
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int idealArrays(int n, int maxValue) {
        
    }
};
```

### Java

```java
class Solution {
    public int idealArrays(int n, int maxValue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
```

### C

```c
int idealArrays(int n, int maxValue) {
    
}
```

### C#

```csharp
public class Solution {
    public int IdealArrays(int n, int maxValue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} maxValue
 * @return {number}
 */
var idealArrays = function(n, maxValue) {
    
};
```

### TypeScript

```typescript
function idealArrays(n: number, maxValue: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $maxValue
     * @return Integer
     */
    function idealArrays($n, $maxValue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func idealArrays(_ n: Int, _ maxValue: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun idealArrays(n: Int, maxValue: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int idealArrays(int n, int maxValue) {
    
  }
}
```

### Go

```golang
func idealArrays(n int, maxValue int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} max_value
# @return {Integer}
def ideal_arrays(n, max_value)
    
end
```

### Scala

```scala
object Solution {
    def idealArrays(n: Int, maxValue: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ideal_arrays(n: i32, max_value: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ideal-arrays n maxValue)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ideal_arrays(N :: integer(), MaxValue :: integer()) -> integer().
ideal_arrays(N, MaxValue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ideal_arrays(n :: integer, max_value :: integer) :: integer
  def ideal_arrays(n, max_value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func idealArrays(n: Int64, maxValue: Int64): Int64 {

    }
}
```

