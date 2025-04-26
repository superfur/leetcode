# 1238. 循环码排列

## 题目描述

<p>给你两个整数&nbsp;<code>n</code> 和 <code>start</code>。你的任务是返回任意 <code>(0,1,2,,...,2^n-1)</code> 的排列 <code>p</code>，并且满足：</p>

<ul>
	<li><code>p[0] = start</code></li>
	<li><code>p[i]</code> 和 <code>p[i+1]</code>&nbsp;的二进制表示形式只有一位不同</li>
	<li><code>p[0]</code> 和 <code>p[2^n -1]</code>&nbsp;的二进制表示形式也只有一位不同</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2, start = 3
<strong>输出：</strong>[3,2,0,1]
<strong>解释：</strong>这个排列的二进制表示是 (11,10,00,01)
     所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, start = 2
<strong>输出：</strong>[2,6,7,5,4,0,1,3]
<strong>解释：</strong>这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>0 &lt;= start&nbsp;&lt;&nbsp;2^n</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数学
- 回溯

## 提示

1. Use gray code to generate a n-bit sequence.
2. Rotate the sequence such that its first element is start.

## 示例

```
2
3
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> circularPermutation(int n, int start) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> circularPermutation(int n, int start) {
        
    }
}
```

### Python

```python
class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* circularPermutation(int n, int start, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> CircularPermutation(int n, int start) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} start
 * @return {number[]}
 */
var circularPermutation = function(n, start) {
    
};
```

### TypeScript

```typescript
function circularPermutation(n: number, start: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer[]
     */
    function circularPermutation($n, $start) {
        
    }
}
```

### Swift

```swift
class Solution {
    func circularPermutation(_ n: Int, _ start: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun circularPermutation(n: Int, start: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> circularPermutation(int n, int start) {
    
  }
}
```

### Go

```golang
func circularPermutation(n int, start int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} start
# @return {Integer[]}
def circular_permutation(n, start)
    
end
```

### Scala

```scala
object Solution {
    def circularPermutation(n: Int, start: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn circular_permutation(n: i32, start: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (circular-permutation n start)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec circular_permutation(N :: integer(), Start :: integer()) -> [integer()].
circular_permutation(N, Start) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec circular_permutation(n :: integer, start :: integer) :: [integer]
  def circular_permutation(n, start) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func circularPermutation(n: Int64, start: Int64): ArrayList<Int64> {

    }
}
```

