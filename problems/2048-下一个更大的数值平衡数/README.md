# 2048. 下一个更大的数值平衡数

## 题目描述

<p>如果整数&nbsp; <code>x</code> 满足：对于每个数位&nbsp;<code>d</code> ，这个数位&nbsp;<strong>恰好</strong> 在 <code>x</code> 中出现 <code>d</code> 次。那么整数 <code>x</code> 就是一个 <strong>数值平衡数</strong> 。</p>

<p>给你一个整数 <code>n</code> ，请你返回 <strong>严格大于</strong> <code>n</code> 的 <strong>最小数值平衡数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>22
<strong>解释：</strong>
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次 
这也是严格大于 1 的最小数值平衡数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1000
<strong>输出：</strong>1333
<strong>解释：</strong>
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 1000 的最小数值平衡数。
注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3000
<strong>输出：</strong>3133
<strong>解释：</strong>
3133 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 3000 的最小数值平衡数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 回溯
- 计数
- 枚举

## 提示

1. How far away can the next greater numerically balanced number be from n?
2. With the given constraints, what is the largest numerically balanced number?

## 示例

```
1
1000
3000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nextBeautifulNumber(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int nextBeautifulNumber(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
```

### C

```c
int nextBeautifulNumber(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NextBeautifulNumber(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function(n) {
    
};
```

### TypeScript

```typescript
function nextBeautifulNumber(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function nextBeautifulNumber($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nextBeautifulNumber(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nextBeautifulNumber(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nextBeautifulNumber(int n) {
    
  }
}
```

### Go

```golang
func nextBeautifulNumber(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def next_beautiful_number(n)
    
end
```

### Scala

```scala
object Solution {
    def nextBeautifulNumber(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn next_beautiful_number(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (next-beautiful-number n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec next_beautiful_number(N :: integer()) -> integer().
next_beautiful_number(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec next_beautiful_number(n :: integer) :: integer
  def next_beautiful_number(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nextBeautifulNumber(n: Int64): Int64 {

    }
}
```

