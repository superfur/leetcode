# 2769. 找出最大的可达成数字

## 题目描述

<p>给你两个整数 <code>num</code> 和 <code>t</code> 。如果整数 <code>x</code> 可以在执行下述操作 <strong>不超过</strong> <code>t</code> 次的情况下变为与 <code>num</code> 相等，则称其为 <strong>可达成数字</strong> ：</p>

<ul>
	<li>每次操作将 <code>x</code> 的值增加或减少 <code>1</code> ，同时可以选择将 <code>num</code> 的值增加或减少 <code>1</code> 。</li>
</ul>

<p>返回所有可达成数字中的 <strong>最大</strong> 值 <code>x</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>num = 4, t = 1</p>

<p><strong>输出：</strong>6</p>

<p><strong>解释：</strong></p>

<p>执行下述操作可以使最大可达成数字等于 <code>num</code> ：</p>

<ul>
	<li>最大可达成数字减少 1 ，同时 <code>num</code> 增加 1 。</li>
</ul>
</div>

<p><strong>示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>num = 3, t = 2</p>

<p><strong>输出：</strong>7</p>

<p><strong>解释：</strong></p>

<p>执行两次下述操作可以使最大可达成数字等于 num ：</p>

<ul>
	<li>最大可达成数字减少 1 ，同时 <code>num</code> 增加 1。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num, t&nbsp;&lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Let x be the answer, it’s always optimal to decrease x in each operation and increase nums.

## 示例

```
4
1
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int theMaximumAchievableX(int num, int t) {
        
    }
};
```

### Java

```java
class Solution {
    public int theMaximumAchievableX(int num, int t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        
```

### C

```c
int theMaximumAchievableX(int num, int t) {
    
}
```

### C#

```csharp
public class Solution {
    public int TheMaximumAchievableX(int num, int t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @param {number} t
 * @return {number}
 */
var theMaximumAchievableX = function(num, t) {
    
};
```

### TypeScript

```typescript
function theMaximumAchievableX(num: number, t: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $t
     * @return Integer
     */
    function theMaximumAchievableX($num, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func theMaximumAchievableX(_ num: Int, _ t: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun theMaximumAchievableX(num: Int, t: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int theMaximumAchievableX(int num, int t) {
    
  }
}
```

### Go

```golang
func theMaximumAchievableX(num int, t int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @param {Integer} t
# @return {Integer}
def the_maximum_achievable_x(num, t)
    
end
```

### Scala

```scala
object Solution {
    def theMaximumAchievableX(num: Int, t: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn the_maximum_achievable_x(num: i32, t: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (the-maximum-achievable-x num t)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec the_maximum_achievable_x(Num :: integer(), T :: integer()) -> integer().
the_maximum_achievable_x(Num, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec the_maximum_achievable_x(num :: integer, t :: integer) :: integer
  def the_maximum_achievable_x(num, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func theMaximumAchievableX(num: Int64, t: Int64): Int64 {

    }
}
```

