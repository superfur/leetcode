# 1432. 改变一个整数能得到的最大差值

## 题目描述

<p>给你一个整数&nbsp;<code>num</code>&nbsp;。你可以对它进行如下步骤恰好 <strong>两次</strong>&nbsp;：</p>

<ul>
	<li>选择一个数字&nbsp;<code>x (0&nbsp;&lt;= x &lt;= 9)</code>.</li>
	<li>选择另一个数字&nbsp;<code>y (0&nbsp;&lt;= y &lt;= 9)</code>&nbsp;。数字&nbsp;<code>y</code>&nbsp;可以等于&nbsp;<code>x</code>&nbsp;。</li>
	<li>将 <code>num</code>&nbsp;中所有出现 <code>x</code>&nbsp;的数位都用 <code>y</code>&nbsp;替换。</li>
	<li>得到的新的整数 <strong>不能</strong>&nbsp;有前导 0 ，得到的新整数也 <strong>不能</strong>&nbsp;是 0&nbsp;。</li>
</ul>

<p>令两次对 <code>num</code>&nbsp;的操作得到的结果分别为&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>&nbsp;。</p>

<p>请你返回&nbsp;<code>a</code> 和&nbsp;<code>b</code>&nbsp;的 <strong>最大差值</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 555
<strong>输出：</strong>888
<strong>解释：</strong>第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 999 和 b = 111 ，最大差值为 888
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 9
<strong>输出：</strong>8
<strong>解释：</strong>第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 9 和 b = 1 ，最大差值为 8
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = 123456
<strong>输出：</strong>820000
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>num = 10000
<strong>输出：</strong>80000
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>num = 9288
<strong>输出：</strong>8700
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10^8</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. We need to get the max and min value after changing num and the answer is max - min.
2. Use brute force, try all possible changes and keep the minimum and maximum values.

## 示例

```
555
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDiff(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDiff(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDiff(self, num: int) -> int:
        
```

### C

```c
int maxDiff(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDiff(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var maxDiff = function(num) {
    
};
```

### TypeScript

```typescript
function maxDiff(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function maxDiff($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDiff(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDiff(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDiff(int num) {
    
  }
}
```

### Go

```golang
func maxDiff(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def max_diff(num)
    
end
```

### Scala

```scala
object Solution {
    def maxDiff(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_diff(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-diff num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_diff(Num :: integer()) -> integer().
max_diff(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_diff(num :: integer) :: integer
  def max_diff(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDiff(num: Int64): Int64 {

    }
}
```

