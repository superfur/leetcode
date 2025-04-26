# 2761. 和等于目标值的质数对

## 题目描述

<p>给你一个整数 <code>n</code> 。如果两个整数 <code>x</code> 和 <code>y</code> 满足下述条件，则认为二者形成一个质数对：</p>

<ul>
	<li><code>1 &lt;= x &lt;= y &lt;= n</code></li>
	<li><code>x + y == n</code></li>
	<li><code>x</code> 和 <code>y</code> 都是质数</li>
</ul>

<p>请你以二维有序列表的形式返回符合题目要求的所有 <code>[x<sub>i</sub>, y<sub>i</sub>]</code> ，列表需要按 <code>x<sub>i</sub></code> 的 <strong>非递减顺序</strong> 排序。如果不存在符合要求的质数对，则返回一个空数组。</p>

<p><strong>注意：</strong>质数是大于 <code>1</code> 的自然数，并且只有两个因子，即它本身和 <code>1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 10
<strong>输出：</strong>[[3,7],[5,5]]
<strong>解释：</strong>在这个例子中，存在满足条件的两个质数对。 
这两个质数对分别是 [3,7] 和 [5,5]，按照题面描述中的方式排序后返回。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>[]
<strong>解释：</strong>可以证明不存在和为 2 的质数对，所以返回一个空数组。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 枚举
- 数论

## 提示

1. Pre-compute all the prime numbers in the range [1, n] using a sieve, and store them in a data structure where they can be accessed in O(1) time.
2. For x in the range [2, n/2], we can use the pre-computed list of prime numbers to check if both x and n - x are primes. If they are, we add them to the result.

## 示例

```
10
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findPrimePairs(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> findPrimePairs(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findPrimePairs(int n, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> FindPrimePairs(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    
};
```

### TypeScript

```typescript
function findPrimePairs(n: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function findPrimePairs($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPrimePairs(_ n: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPrimePairs(n: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> findPrimePairs(int n) {
    
  }
}
```

### Go

```golang
func findPrimePairs(n int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[][]}
def find_prime_pairs(n)
    
end
```

### Scala

```scala
object Solution {
    def findPrimePairs(n: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_prime_pairs(n: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-prime-pairs n)
  (-> exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec find_prime_pairs(N :: integer()) -> [[integer()]].
find_prime_pairs(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_prime_pairs(n :: integer) :: [[integer]]
  def find_prime_pairs(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPrimePairs(n: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

