# 1866. 恰有 K 根木棍可以看到的排列数目

## 题目描述

<p>有 <code>n</code> 根长度互不相同的木棍，长度为从 <code>1</code> 到 <code>n</code> 的整数。请你将这些木棍排成一排，并满足从左侧 <strong>可以看到</strong> <strong>恰好</strong> <code>k</code> 根木棍。从左侧 <strong>可以看到</strong> 木棍的前提是这个木棍的 <strong>左侧</strong> 不存在比它 <strong>更长的</strong> 木棍。</p>

<ul>
	<li>例如，如果木棍排列为 <code>[<em><strong>1</strong></em>,<em><strong>3</strong></em>,2,<em><strong>5</strong></em>,4]</code> ，那么从左侧可以看到的就是长度分别为 <code>1</code>、<code>3</code> 、<code>5</code> 的木棍。</li>
</ul>

<p>给你 <code>n</code> 和 <code>k</code> ，返回符合题目要求的排列 <strong>数目</strong> 。由于答案可能很大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 3, k = 2
<strong>输出：</strong>3
<strong>解释：</strong>[<strong><em>1</em></strong>,<strong><em>3</em></strong>,2], [<em><strong>2</strong></em>,<em><strong>3</strong></em>,1] 和 [<em><strong>2</strong></em>,1,<em><strong>3</strong></em>] 是仅有的能满足恰好 2 根木棍可以看到的排列。
可以看到的木棍已经用粗体+斜体标识。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5, k = 5
<strong>输出：</strong>1
<strong>解释：</strong>[<em><strong>1</strong></em>,<em><strong>2</strong></em>,<em><strong>3</strong></em>,<em><strong>4</strong></em>,<em><strong>5</strong></em>] 是唯一一种能满足全部 5 根木棍可以看到的排列。
可以看到的木棍已经用粗体+斜体标识。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 20, k = 11
<strong>输出：</strong>647427950
<strong>解释：</strong>总共有 647427950 (mod 10<sup>9 </sup>+ 7) 种能满足恰好有 11 根木棍可以看到的排列。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. Is there a way to build the solution from a base case?
2. How many ways are there if we fix the position of one stick?

## 示例

```
3
2
5
5
20
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rearrangeSticks(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int rearrangeSticks(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
```

### C

```c
int rearrangeSticks(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int RearrangeSticks(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var rearrangeSticks = function(n, k) {
    
};
```

### TypeScript

```typescript
function rearrangeSticks(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function rearrangeSticks($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rearrangeSticks(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rearrangeSticks(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int rearrangeSticks(int n, int k) {
    
  }
}
```

### Go

```golang
func rearrangeSticks(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def rearrange_sticks(n, k)
    
end
```

### Scala

```scala
object Solution {
    def rearrangeSticks(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rearrange_sticks(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (rearrange-sticks n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec rearrange_sticks(N :: integer(), K :: integer()) -> integer().
rearrange_sticks(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rearrange_sticks(n :: integer, k :: integer) :: integer
  def rearrange_sticks(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rearrangeSticks(n: Int64, k: Int64): Int64 {

    }
}
```

