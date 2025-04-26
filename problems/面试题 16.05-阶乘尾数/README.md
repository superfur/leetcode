# 面试题 16.05. 阶乘尾数

## 题目描述

<p>设计一个算法，算出 n 阶乘有多少个尾随零。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>3
<strong>输出：</strong>0
<strong>解释：</strong>3! = 6, 尾数中没有零。</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>5
<strong>输出：</strong>1
<strong>解释：</strong>5! = 120, 尾数中有 1 个零.</pre>

<p><strong>说明: </strong>你算法的时间复杂度应为&nbsp;<em>O</em>(log&nbsp;<em>n</em>)<em>&nbsp;</em>。</p>


## 难度

Easy

## 标签

- 数学

## 提示

1. 0如何变成n!？这是什么意思？
2. n!中的每个0表示n能被10整除一次。这是什么意思？
3. n!中每一个因子10都意味着n!能被5和2整除。
4. 你能计算出5和2的因数的个数吗？需要两者都计算吗？
5. 你是否考虑过25实际上记录了两次因数5？

## 示例

```
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int trailingZeroes(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
```

### C

```c
int trailingZeroes(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int TrailingZeroes(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    
};
```

### TypeScript

```typescript
function trailingZeroes(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function trailingZeroes($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func trailingZeroes(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trailingZeroes(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int trailingZeroes(int n) {
    
  }
}
```

### Go

```golang
func trailingZeroes(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def trailing_zeroes(n)
    
end
```

### Scala

```scala
object Solution {
    def trailingZeroes(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (trailing-zeroes n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec trailing_zeroes(N :: integer()) -> integer().
trailing_zeroes(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec trailing_zeroes(n :: integer) :: integer
  def trailing_zeroes(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func trailingZeroes(n: Int64): Int64 {

    }
}
```

