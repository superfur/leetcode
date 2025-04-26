# 2226. 每个小孩最多能分到多少糖果

## 题目描述

<p>给你一个 <strong>下标从 0 开始</strong> 的整数数组 <code>candies</code> 。数组中的每个元素表示大小为 <code>candies[i]</code> 的一堆糖果。你可以将每堆糖果分成任意数量的 <strong>子堆</strong> ，但 <strong>无法</strong> 再将两堆合并到一起。</p>

<p>另给你一个整数 <code>k</code> 。你需要将这些糖果分配给 <code>k</code> 个小孩，使每个小孩分到 <strong>相同</strong> 数量的糖果。每个小孩可以拿走 <strong>至多一堆</strong> 糖果，有些糖果可能会不被分配。</p>

<p>返回每个小孩可以拿走的 <strong>最大糖果数目</strong><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>candies = [5,8,6], k = 3
<strong>输出：</strong>5
<strong>解释：</strong>可以将 candies[1] 分成大小分别为 5 和 3 的两堆，然后把 candies[2] 分成大小分别为 5 和 1 的两堆。现在就有五堆大小分别为 5、5、3、5 和 1 的糖果。可以把 3 堆大小为 5 的糖果分给 3 个小孩。可以证明无法让每个小孩得到超过 5 颗糖果。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>candies = [2,5], k = 11
<strong>输出：</strong>0
<strong>解释：</strong>总共有 11 个小孩，但只有 7 颗糖果，但如果要分配糖果的话，必须保证每个小孩至少能得到 1 颗糖果。因此，最后每个小孩都没有得到糖果，答案是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candies.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= candies[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>12</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. For a fixed number of candies c, how can you check if each child can get c candies?
2. Use binary search to find the maximum c as the answer.

## 示例

```
[5,8,6]
3
[2,5]
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumCandies(int[] candies, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
```

### C

```c
int maximumCandies(int* candies, int candiesSize, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumCandies(int[] candies, long k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var maximumCandies = function(candies, k) {
    
};
```

### TypeScript

```typescript
function maximumCandies(candies: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candies
     * @param Integer $k
     * @return Integer
     */
    function maximumCandies($candies, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumCandies(_ candies: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumCandies(candies: IntArray, k: Long): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumCandies(List<int> candies, int k) {
    
  }
}
```

### Go

```golang
func maximumCandies(candies []int, k int64) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} candies
# @param {Integer} k
# @return {Integer}
def maximum_candies(candies, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumCandies(candies: Array[Int], k: Long): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-candies candies k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_candies(Candies :: [integer()], K :: integer()) -> integer().
maximum_candies(Candies, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_candies(candies :: [integer], k :: integer) :: integer
  def maximum_candies(candies, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumCandies(candies: Array<Int64>, k: Int64): Int64 {

    }
}
```

