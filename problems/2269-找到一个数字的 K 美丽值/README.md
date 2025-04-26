# 2269. 找到一个数字的 K 美丽值

## 题目描述

<p>一个整数 <code>num</code>&nbsp;的&nbsp;<strong>k&nbsp;</strong>美丽值定义为&nbsp;<code>num</code>&nbsp;中符合以下条件的&nbsp;<strong>子字符串</strong>&nbsp;数目：</p>

<ul>
	<li>子字符串长度为&nbsp;<code>k</code>&nbsp;。</li>
	<li>子字符串能整除 <code>num</code> 。</li>
</ul>

<p>给你整数&nbsp;<code>num</code> 和&nbsp;<code>k</code>&nbsp;，请你返回<em>&nbsp;</em><code>num</code>&nbsp;的 k 美丽值。</p>

<p>注意：</p>

<ul>
	<li>允许有&nbsp;<strong>前缀</strong>&nbsp;<strong>0</strong>&nbsp;。</li>
	<li><code>0</code>&nbsp;不能整除任何值。</li>
</ul>

<p>一个 <strong>子字符串</strong>&nbsp;是一个字符串里的连续一段字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 240, k = 2
<b>输出：</b>2
<b>解释：</b>以下是 num 里长度为 k 的子字符串：
- "<em><strong>24</strong></em>0" 中的 "24" ：24 能整除 240 。
- "2<em><strong>40</strong></em>" 中的 "40" ：40 能整除 240 。
所以，k 美丽值为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 430043, k = 2
<b>输出：</b>2
<b>解释：</b>以下是 num 里长度为 k 的子字符串：
- "<em><strong>43</strong></em>0043" 中的 "43" ：43 能整除 430043 。
- "4<em><strong>30</strong></em>043" 中的 "30" ：30 不能整除 430043 。
- "43<em><strong>00</strong></em>43" 中的 "00" ：0 不能整除 430043 。
- "430<em><strong>04</strong></em>3" 中的 "04" ：4 不能整除 430043 。
- "4300<em><strong>43</strong></em>" 中的 "43" ：43 能整除 430043 。
所以，k 美丽值为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= num.length</code>&nbsp;（将&nbsp;<code>num</code>&nbsp;视为字符串）</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串
- 滑动窗口

## 提示

1. We should check all the substrings of num with a length of k and see if it is a divisor of num.
2. We can more easily obtain the substrings by converting num into a string and converting back to an integer to check for divisibility.

## 示例

```
240
2
430043
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int divisorSubstrings(int num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int divisorSubstrings(int num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
```

### C

```c
int divisorSubstrings(int num, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int DivisorSubstrings(int num, int k) {
        
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
var divisorSubstrings = function(num, k) {
    
};
```

### TypeScript

```typescript
function divisorSubstrings(num: number, k: number): number {
    
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
    function divisorSubstrings($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divisorSubstrings(_ num: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divisorSubstrings(num: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int divisorSubstrings(int num, int k) {
    
  }
}
```

### Go

```golang
func divisorSubstrings(num int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @param {Integer} k
# @return {Integer}
def divisor_substrings(num, k)
    
end
```

### Scala

```scala
object Solution {
    def divisorSubstrings(num: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divisor_substrings(num: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (divisor-substrings num k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec divisor_substrings(Num :: integer(), K :: integer()) -> integer().
divisor_substrings(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divisor_substrings(num :: integer, k :: integer) :: integer
  def divisor_substrings(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divisorSubstrings(num: Int64, k: Int64): Int64 {

    }
}
```

