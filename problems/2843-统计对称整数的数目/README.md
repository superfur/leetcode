# 2843. 统计对称整数的数目

## 题目描述

<p>给你两个正整数 <code>low</code> 和 <code>high</code> 。</p>

<p>对于一个由 <code>2 * n</code> 位数字组成的整数 <code>x</code> ，如果其前 <code>n</code> 位数字之和与后 <code>n</code> 位数字之和相等，则认为这个数字是一个对称整数。</p>

<p>返回在 <code>[low, high]</code> 范围内的 <strong>对称整数的数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>low = 1, high = 100
<strong>输出：</strong>9
<strong>解释：</strong>在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>low = 1200, high = 1230
<strong>输出：</strong>4
<strong>解释：</strong>在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 枚举

## 提示

1. <div class="_1l1MA">Iterate over all numbers from <code>low</code> to <code>high</code></div>
2. <div class="_1l1MA">Convert each number to a string and compare the sum of the first half with that of the second.</div>

## 示例

```
1
100
1200
1230
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSymmetricIntegers(int low, int high) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
```

### C

```c
int countSymmetricIntegers(int low, int high) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSymmetricIntegers(int low, int high) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countSymmetricIntegers = function(low, high) {
    
};
```

### TypeScript

```typescript
function countSymmetricIntegers(low: number, high: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countSymmetricIntegers($low, $high) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSymmetricIntegers(_ low: Int, _ high: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSymmetricIntegers(low: Int, high: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSymmetricIntegers(int low, int high) {
    
  }
}
```

### Go

```golang
func countSymmetricIntegers(low int, high int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_symmetric_integers(low, high)
    
end
```

### Scala

```scala
object Solution {
    def countSymmetricIntegers(low: Int, high: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-symmetric-integers low high)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_symmetric_integers(Low :: integer(), High :: integer()) -> integer().
count_symmetric_integers(Low, High) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_symmetric_integers(low :: integer, high :: integer) :: integer
  def count_symmetric_integers(low, high) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSymmetricIntegers(low: Int64, high: Int64): Int64 {

    }
}
```

