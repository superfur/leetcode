# 3290. 最高乘法得分

## 题目描述

<p>给你一个大小为 4 的整数数组 <code>a</code> 和一个大小 <strong>至少</strong>为 4 的整数数组 <code>b</code>。</p>

<p>你需要从数组 <code>b</code> 中选择四个下标 <code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, <code>i<sub>2</sub></code>, 和 <code>i<sub>3</sub></code>，并满足 <code>i<sub>0</sub> &lt; i<sub>1</sub> &lt; i<sub>2</sub> &lt; i<sub>3</sub></code>。你的得分将是 <code>a[0] * b[i<sub>0</sub>] + a[1] * b[i<sub>1</sub>] + a[2] * b[i<sub>2</sub>] + a[3] * b[i<sub>3</sub>]</code> 的值。</p>

<p>返回你能够获得的 <strong>最大 </strong>得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]</span></p>

<p><strong>输出：</strong> <span class="example-io">26</span></p>

<p><strong>解释：</strong><br />
选择下标 0, 1, 2 和 5。得分为 <code>3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong><br />
选择下标 0, 1, 3 和 4。得分为 <code>(-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>a.length == 4</code></li>
	<li><code>4 &lt;= b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= a[i], b[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Try using dynamic programming.
2. Consider a dp with the following states: The current position in the array b, and the number of indices considered.

## 示例

```
[3,2,5,6]
[2,-6,4,-5,-3,2,-7]
[-1,4,5,-2]
[-5,-1,-3,-2,-4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxScore(int[] a, int[] b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
```

### C

```c
long long maxScore(int* a, int aSize, int* b, int bSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxScore(int[] a, int[] b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} a
 * @param {number[]} b
 * @return {number}
 */
var maxScore = function(a, b) {
    
};
```

### TypeScript

```typescript
function maxScore(a: number[], b: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $a
     * @param Integer[] $b
     * @return Integer
     */
    function maxScore($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ a: [Int], _ b: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(a: IntArray, b: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<int> a, List<int> b) {
    
  }
}
```

### Go

```golang
func maxScore(a []int, b []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def max_score(a, b)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(a: Array[Int], b: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(a: Vec<i32>, b: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score a b)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(A :: [integer()], B :: [integer()]) -> integer().
max_score(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(a :: [integer], b :: [integer]) :: integer
  def max_score(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(a: Array<Int64>, b: Array<Int64>): Int64 {

    }
}
```

