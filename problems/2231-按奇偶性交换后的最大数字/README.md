# 2231. 按奇偶性交换后的最大数字

## 题目描述

<p>给你一个正整数 <code>num</code> 。你可以交换 <code>num</code> 中 <strong>奇偶性</strong> 相同的任意两位数字（即，都是奇数或者偶数）。</p>

<p>返回交换 <strong>任意</strong> 次之后 <code>num</code> 的 <strong>最大</strong> 可能值<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 1234
<strong>输出：</strong>3412
<strong>解释：</strong>交换数字 3 和数字 1 ，结果得到 3214 。
交换数字 2 和数字 4 ，结果得到 3412 。
注意，可能存在其他交换序列，但是可以证明 3412 是最大可能值。
注意，不能交换数字 4 和数字 1 ，因为它们奇偶性不同。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 65875
<strong>输出：</strong>87655
<strong>解释：</strong>交换数字 8 和数字 6 ，结果得到 85675 。
交换数字 5 和数字 7 ，结果得到 87655 。
注意，可能存在其他交换序列，但是可以证明 87655 是最大可能值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 排序
- 堆（优先队列）

## 提示

1. The bigger digit should appear first (more to the left) because it contributes more to the value of the number.
2. Get all the even digits, as well as odd digits. Sort them separately.
3. Reconstruct the number by giving the earlier digits the highest available digit of the same parity.

## 示例

```
1234
65875
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestInteger(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestInteger(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestInteger(self, num: int) -> int:
        
```

### C

```c
int largestInteger(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestInteger(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var largestInteger = function(num) {
    
};
```

### TypeScript

```typescript
function largestInteger(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function largestInteger($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestInteger(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestInteger(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestInteger(int num) {
    
  }
}
```

### Go

```golang
func largestInteger(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def largest_integer(num)
    
end
```

### Scala

```scala
object Solution {
    def largestInteger(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_integer(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-integer num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_integer(Num :: integer()) -> integer().
largest_integer(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_integer(num :: integer) :: integer
  def largest_integer(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestInteger(num: Int64): Int64 {

    }
}
```

