# 991. 坏了的计算器

## 题目描述

<p>在显示着数字&nbsp;<code>startValue</code>&nbsp;的坏计算器上，我们可以执行以下两种操作：</p>

<ul>
	<li><strong>双倍（Double）：</strong>将显示屏上的数字乘 2；</li>
	<li><strong>递减（Decrement）：</strong>将显示屏上的数字减 <code>1</code> 。</li>
</ul>

<p>给定两个整数&nbsp;<code>startValue</code>&nbsp;和&nbsp;<code>target</code>&nbsp;。返回显示数字&nbsp;<code>target</code>&nbsp;所需的最小操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>startValue = 2, target = 3
<strong>输出：</strong>2
<strong>解释：</strong>先进行双倍运算，然后再进行递减运算 {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>startValue = 5, target = 8
<strong>输出：</strong>2
<strong>解释：</strong>先递减，再双倍 {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>startValue = 3, target = 10
<strong>输出：</strong>3
<strong>解释：</strong>先双倍，然后递减，再双倍 {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= startValue, target &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 示例

```
2
3
5
8
3
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int brokenCalc(int startValue, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
```

### C

```c
int brokenCalc(int startValue, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int BrokenCalc(int startValue, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} startValue
 * @param {number} target
 * @return {number}
 */
var brokenCalc = function(startValue, target) {
    
};
```

### TypeScript

```typescript
function brokenCalc(startValue: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $startValue
     * @param Integer $target
     * @return Integer
     */
    function brokenCalc($startValue, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func brokenCalc(_ startValue: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun brokenCalc(startValue: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int brokenCalc(int startValue, int target) {
    
  }
}
```

### Go

```golang
func brokenCalc(startValue int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} start_value
# @param {Integer} target
# @return {Integer}
def broken_calc(start_value, target)
    
end
```

### Scala

```scala
object Solution {
    def brokenCalc(startValue: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn broken_calc(start_value: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (broken-calc startValue target)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec broken_calc(StartValue :: integer(), Target :: integer()) -> integer().
broken_calc(StartValue, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec broken_calc(start_value :: integer, target :: integer) :: integer
  def broken_calc(start_value, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func brokenCalc(startValue: Int64, target: Int64): Int64 {

    }
}
```

