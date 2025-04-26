# 2443. 反转之后的数字和

## 题目描述

<p>给你一个 <strong>非负</strong> 整数 <code>num</code> 。如果存在某个 <strong>非负</strong> 整数 <code>k</code> 满足 <code>k + reverse(k) = num</code>&nbsp; ，则返回 <code>true</code> ；否则，返回<em> </em><code>false</code> 。</p>

<p><code>reverse(k)</code> 表示 <code>k</code> 反转每个数位后得到的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 443
<strong>输出：</strong>true
<strong>解释：</strong>172 + 271 = 443 ，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 63
<strong>输出：</strong>false
<strong>解释：</strong>63 不能表示为非负整数及其反转后数字之和，返回 false 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = 181
<strong>输出：</strong>true
<strong>解释：</strong>140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 枚举

## 提示

1. The constraints are small enough that we can check every number.
2. To reverse a number, first convert it to a string. Then, create a new string that is the reverse of the first one. Finally, convert the new string back into a number.

## 示例

```
443
63
181
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool sumOfNumberAndReverse(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean sumOfNumberAndReverse(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
```

### C

```c
bool sumOfNumberAndReverse(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SumOfNumberAndReverse(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var sumOfNumberAndReverse = function(num) {
    
};
```

### TypeScript

```typescript
function sumOfNumberAndReverse(num: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function sumOfNumberAndReverse($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfNumberAndReverse(_ num: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfNumberAndReverse(num: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool sumOfNumberAndReverse(int num) {
    
  }
}
```

### Go

```golang
func sumOfNumberAndReverse(num int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Boolean}
def sum_of_number_and_reverse(num)
    
end
```

### Scala

```scala
object Solution {
    def sumOfNumberAndReverse(num: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_number_and_reverse(num: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-number-and-reverse num)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec sum_of_number_and_reverse(Num :: integer()) -> boolean().
sum_of_number_and_reverse(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_number_and_reverse(num :: integer) :: boolean
  def sum_of_number_and_reverse(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfNumberAndReverse(num: Int64): Bool {

    }
}
```

