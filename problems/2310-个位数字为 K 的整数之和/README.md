# 2310. 个位数字为 K 的整数之和

## 题目描述

<p>给你两个整数 <code>num</code> 和 <code>k</code> ，考虑具有以下属性的正整数多重集：</p>

<ul>
	<li>每个整数个位数字都是 <code>k</code> 。</li>
	<li>所有整数之和是 <code>num</code> 。</li>
</ul>

<p>返回该多重集的最小大小，如果不存在这样的多重集，返回<em> </em><code>-1</code> 。</p>

<p>注意：</p>

<ul>
	<li>多重集与集合类似，但多重集可以包含多个同一整数，空多重集的和为 <code>0</code> 。</li>
	<li><strong>个位数字</strong> 是数字最右边的数位。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 58, k = 9
<strong>输出：</strong>2
<strong>解释：</strong>
多重集 [9,49] 满足题目条件，和为 58 且每个整数的个位数字是 9 。
另一个满足条件的多重集是 [19,39] 。
可以证明 2 是满足题目条件的多重集的最小长度。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 37, k = 2
<strong>输出：</strong>-1
<strong>解释：</strong>个位数字为 2 的整数无法相加得到 37 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = 0, k = 7
<strong>输出：</strong>0
<strong>解释：</strong>空多重集的和为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 3000</code></li>
	<li><code>0 &lt;= k &lt;= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 动态规划
- 枚举

## 提示

1. Try solving this recursively.
2. Create a method that takes an integer x as a parameter. This method returns the minimum possible size of a set where each number has units digit k and the sum of the numbers in the set is x.

## 示例

```
58
9
37
2
0
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumNumbers(int num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumNumbers(int num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
```

### C

```c
int minimumNumbers(int num, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumNumbers(int num, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @param {number} k
 * @return {number}
 */
var minimumNumbers = function(num, k) {
    
};
```

### TypeScript

```typescript
function minimumNumbers(num: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $k
     * @return Integer
     */
    function minimumNumbers($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumNumbers(_ num: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumNumbers(num: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumNumbers(int num, int k) {
    
  }
}
```

### Go

```golang
func minimumNumbers(num int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @param {Integer} k
# @return {Integer}
def minimum_numbers(num, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumNumbers(num: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_numbers(num: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-numbers num k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_numbers(Num :: integer(), K :: integer()) -> integer().
minimum_numbers(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_numbers(num :: integer, k :: integer) :: integer
  def minimum_numbers(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumNumbers(num: Int64, k: Int64): Int64 {

    }
}
```

