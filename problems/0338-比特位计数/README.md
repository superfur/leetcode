# 338. 比特位计数

## 题目描述

<p>给你一个整数 <code>n</code> ，对于&nbsp;<code>0 &lt;= i &lt;= n</code> 中的每个 <code>i</code> ，计算其二进制表示中 <strong><code>1</code> 的个数</strong> ，返回一个长度为 <code>n + 1</code> 的数组 <code>ans</code> 作为答案。</p>

<p>&nbsp;</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,1]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>[0,1,1,2,1,2]
<strong>解释：</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>很容易就能实现时间复杂度为 <code>O(n log n)</code> 的解决方案，你可以在线性时间复杂度 <code>O(n)</code> 内用一趟扫描解决此问题吗？</li>
	<li>你能不使用任何内置函数解决此问题吗？（如，C++ 中的&nbsp;<code>__builtin_popcount</code> ）</li>
</ul>
</div>
</div>


## 难度

Easy

## 标签

- 位运算
- 动态规划

## 提示

1. You should make use of what you have produced already.
2. Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
3. Or does the odd/even status of the number help you in calculating the number of 1s?

## 示例

```
2
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countBits(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countBits(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountBits(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    
};
```

### TypeScript

```typescript
function countBits(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function countBits($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBits(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBits(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countBits(int n) {
    
  }
}
```

### Go

```golang
func countBits(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def count_bits(n)
    
end
```

### Scala

```scala
object Solution {
    def countBits(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-bits n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_bits(N :: integer()) -> [integer()].
count_bits(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_bits(n :: integer) :: [integer]
  def count_bits(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBits(n: Int64): Array<Int64> {

    }
}
```

