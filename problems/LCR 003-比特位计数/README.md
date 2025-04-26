# LCR 003. 比特位计数

## 题目描述

<p>给定一个非负整数 <code>n</code><b>&nbsp;</b>，请计算 <code>0</code> 到 <code>n</code> 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>n =<strong> </strong>2
<strong>输出: </strong>[0,1,1]
<strong>解释: 
</strong>0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入: </strong>n =<strong> </strong>5
<strong>输出: </strong><code>[0,1,1,2,1,2]
</code><span style="white-space: pre-wrap;"><strong>解释:</strong>
</span>0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

<p>&nbsp;</p>

<p><strong>说明 :</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶:</strong></p>

<ul>
	<li>给出时间复杂度为&nbsp;<code>O(n*sizeof(integer))</code><strong>&nbsp;</strong>的解答非常容易。但你可以在线性时间&nbsp;<code>O(n)</code><strong>&nbsp;</strong>内用一趟扫描做到吗？</li>
	<li>要求算法的空间复杂度为&nbsp;<code>O(n)</code>&nbsp;。</li>
	<li>你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的&nbsp;<code>__builtin_popcount</code><strong>&nbsp;</strong>）来执行此操作。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 338&nbsp;题相同：<a href="https://leetcode-cn.com/problems/counting-bits/">https://leetcode-cn.com/problems/counting-bits/</a></p>


## 难度

Easy

## 标签

- 位运算
- 动态规划

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
int* countBits(int n, int* returnSize){

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

