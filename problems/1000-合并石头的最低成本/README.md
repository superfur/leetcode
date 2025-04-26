# 1000. 合并石头的最低成本

## 题目描述

<p>有 <code>n</code> 堆石头排成一排，第 <code>i</code> 堆中有&nbsp;<code>stones[i]</code>&nbsp;块石头。</p>

<p>每次 <strong>移动</strong> 需要将 <strong>连续的</strong> <code>k</code> 堆石头合并为一堆，而这次移动的成本为这 <code>k</code> 堆中石头的总数。</p>

<p>返回把所有石头合并成一堆的最低成本。如果无法合并成一堆，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stones = [3,2,4,1], K = 2
<strong>输出：</strong>20
<strong>解释：</strong>
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stones = [3,2,4,1], K = 3
<strong>输出：</strong>-1
<strong>解释：</strong>任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>stones = [3,5,1,2,6], K = 3
<strong>输出：</strong>25
<strong>解释：</strong>
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == stones.length</code></li>
	<li><code>1 &lt;= n &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 30</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 前缀和

## 示例

```
[3,2,4,1]
2
[3,2,4,1]
3
[3,5,1,2,6]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mergeStones(vector<int>& stones, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int mergeStones(int[] stones, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
```

### C

```c
int mergeStones(int* stones, int stonesSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MergeStones(int[] stones, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @param {number} k
 * @return {number}
 */
var mergeStones = function(stones, k) {
    
};
```

### TypeScript

```typescript
function mergeStones(stones: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @param Integer $k
     * @return Integer
     */
    function mergeStones($stones, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mergeStones(_ stones: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mergeStones(stones: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mergeStones(List<int> stones, int k) {
    
  }
}
```

### Go

```golang
func mergeStones(stones []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @param {Integer} k
# @return {Integer}
def merge_stones(stones, k)
    
end
```

### Scala

```scala
object Solution {
    def mergeStones(stones: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge_stones(stones: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (merge-stones stones k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec merge_stones(Stones :: [integer()], K :: integer()) -> integer().
merge_stones(Stones, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec merge_stones(stones :: [integer], k :: integer) :: integer
  def merge_stones(stones, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mergeStones(stones: Array<Int64>, k: Int64): Int64 {

    }
}
```

