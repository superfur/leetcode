# 906. 超级回文数

## 题目描述

<p>如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为 <strong>超级回文数</strong> 。</p>

<p>现在，给你两个以字符串形式表示的正整数 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="caret-color: rgb(199, 37, 78); font-size: 12.6px; background-color: rgb(249, 242, 244);">left</span></font>&nbsp;和 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="caret-color: rgb(199, 37, 78); font-size: 12.6px; background-color: rgb(249, 242, 244);">right</span></font>&nbsp; ，统计并返回区间&nbsp;<code>[left, right]</code> 中的 <strong>超级回文数</strong> 的数目。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<b>输入：</b>left = "4", right = "1000"
<b>输出：</b>4
<b>解释：</b>4、9、121 和 484 都是超级回文数。
注意 676 不是超级回文数：26 * 26 = 676 ，但是 26 不是回文数。
</pre>

<p><b>示例 2：</b></p>

<pre>
<b>输入：</b>left = "1", right = "2"
<b>输出：</b>1
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= left.length, right.length &lt;= 18</code></li>
	<li><code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;仅由数字（0 - 9）组成。</li>
	<li><code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;不含前导零。</li>
	<li><code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;表示的整数在区间&nbsp;<code>[1, 10<sup>18</sup> - 1]</code> 内。</li>
	<li><code>left</code>&nbsp;小于等于&nbsp;<code>right</code>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 枚举

## 示例

```
"4"
"1000"
"1"
"2"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int superpalindromesInRange(string left, string right) {
        
    }
};
```

### Java

```java
class Solution {
    public int superpalindromesInRange(String left, String right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        
```

### C

```c
int superpalindromesInRange(char* left, char* right) {
    
}
```

### C#

```csharp
public class Solution {
    public int SuperpalindromesInRange(string left, string right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} left
 * @param {string} right
 * @return {number}
 */
var superpalindromesInRange = function(left, right) {
    
};
```

### TypeScript

```typescript
function superpalindromesInRange(left: string, right: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $left
     * @param String $right
     * @return Integer
     */
    function superpalindromesInRange($left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func superpalindromesInRange(_ left: String, _ right: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun superpalindromesInRange(left: String, right: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int superpalindromesInRange(String left, String right) {
    
  }
}
```

### Go

```golang
func superpalindromesInRange(left string, right string) int {
    
}
```

### Ruby

```ruby
# @param {String} left
# @param {String} right
# @return {Integer}
def superpalindromes_in_range(left, right)
    
end
```

### Scala

```scala
object Solution {
    def superpalindromesInRange(left: String, right: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn superpalindromes_in_range(left: String, right: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (superpalindromes-in-range left right)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec superpalindromes_in_range(Left :: unicode:unicode_binary(), Right :: unicode:unicode_binary()) -> integer().
superpalindromes_in_range(Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec superpalindromes_in_range(left :: String.t, right :: String.t) :: integer
  def superpalindromes_in_range(left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func superpalindromesInRange(left: String, right: String): Int64 {

    }
}
```

