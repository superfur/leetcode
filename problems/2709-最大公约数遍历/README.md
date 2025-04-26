# 2709. 最大公约数遍历

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，你可以在一些下标之间遍历。对于两个下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>（<code>i != j</code>），当且仅当&nbsp;<code>gcd(nums[i], nums[j]) &gt; 1</code>&nbsp;时，我们可以在两个下标之间通行，其中&nbsp;<code>gcd</code>&nbsp;是两个数的 <strong>最大公约数</strong>&nbsp;。</p>

<p>你需要判断 <code>nums</code>&nbsp;数组中&nbsp;<strong>任意&nbsp;</strong>两个满足 <code>i &lt; j</code>&nbsp;的下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code> ，是否存在若干次通行可以从 <code>i</code>&nbsp;遍历到 <code>j</code>&nbsp;。</p>

<p>如果任意满足条件的下标对都可以遍历，那么返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,6]
<b>输出：</b>true
<b>解释：</b>这个例子中，总共有 3 个下标对：(0, 1) ，(0, 2) 和 (1, 2) 。
从下标 0 到下标 1 ，我们可以遍历 0 -&gt; 2 -&gt; 1 ，我们可以从下标 0 到 2 是因为 gcd(nums[0], nums[2]) = gcd(2, 6) = 2 &gt; 1 ，从下标 2 到 1 是因为 gcd(nums[2], nums[1]) = gcd(6, 3) = 3 &gt; 1 。
从下标 0 到下标 2 ，我们可以直接遍历，因为 gcd(nums[0], nums[2]) = gcd(2, 6) = 2 &gt; 1 。同理，我们也可以从下标 1 到 2 因为 gcd(nums[1], nums[2]) = gcd(3, 6) = 3 &gt; 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,9,5]
<b>输出：</b>false
<b>解释：</b>我们没法从下标 0 到 2 ，所以返回 false 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [4,3,12,8]
<b>输出：</b>true
<b>解释：</b>总共有 6 个下标对：(0, 1) ，(0, 2) ，(0, 3) ，(1, 2) ，(1, 3) 和 (2, 3) 。所有下标对之间都存在可行的遍历，所以返回 true 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 数组
- 数学
- 数论

## 提示

1. Create a (prime) factor-numbers list for all the indices.
2. Add an edge between the neighbors of the (prime) factor-numbers list. The order of the numbers doesn’t matter. We only need edges between 2 neighbors instead of edges for all pairs.
3. The problem is now similar to checking if all the numbers (nodes of the graph) are in the same connected component.
4. Any algorithm (i.e., BFS, DFS, or Union-Find Set) should work to find or check connected components

## 示例

```
[2,3,6]
[3,9,5]
[4,3,12,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canTraverseAllPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canTraverseAllPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
```

### C

```c
bool canTraverseAllPairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanTraverseAllPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canTraverseAllPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function canTraverseAllPairs(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canTraverseAllPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canTraverseAllPairs(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canTraverseAllPairs(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canTraverseAllPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func canTraverseAllPairs(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def can_traverse_all_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def canTraverseAllPairs(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-traverse-all-pairs nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_traverse_all_pairs(Nums :: [integer()]) -> boolean().
can_traverse_all_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_traverse_all_pairs(nums :: [integer]) :: boolean
  def can_traverse_all_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canTraverseAllPairs(nums: Array<Int64>): Bool {

    }
}
```

