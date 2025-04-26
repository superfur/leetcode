# 3075. 幸福值最大化的选择方案

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>happiness</code> ，以及一个<strong> 正整数 </strong><code>k</code> 。</p>

<p><code>n</code> 个孩子站成一队，其中第 <code>i</code> 个孩子的 <strong>幸福值</strong> 是<strong> </strong><code>happiness[i]</code> 。你计划组织 <code>k</code> 轮筛选从这 <code>n</code> 个孩子中选出 <code>k</code> 个孩子。</p>

<p>在每一轮选择一个孩子时，所有<strong> 尚未 </strong>被选中的孩子的 <strong>幸福值 </strong>将减少 <code>1</code> 。注意，幸福值<strong> 不能 </strong>变成负数，且只有在它是正数的情况下才会减少。</p>

<p>选择 <code>k</code> 个孩子，并使你选中的孩子幸福值之和最大，返回你能够得到的<strong> </strong><strong>最大值</strong> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>happiness = [1,2,3], k = 2
<strong>输出：</strong>4
<strong>解释：</strong>按以下方式选择 2 个孩子：
- 选择幸福值为 3 的孩子。剩余孩子的幸福值变为 [0,1] 。
- 选择幸福值为 1 的孩子。剩余孩子的幸福值变为 [0] 。注意幸福值不能小于 0 。
所选孩子的幸福值之和为 3 + 1 = 4 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>happiness = [1,1,1,1], k = 2
<strong>输出：</strong>1
<strong>解释：</strong>按以下方式选择 2 个孩子：
- 选择幸福值为 1 的任意一个孩子。剩余孩子的幸福值变为 [0,0,0] 。
- 选择幸福值为 0 的孩子。剩余孩子的幸福值变为 [0,0] 。
所选孩子的幸福值之和为 1 + 0 = 1 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>happiness = [2,3,4,5], k = 1
<strong>输出：</strong>5
<strong>解释：</strong>按以下方式选择 1 个孩子：
- 选择幸福值为 5 的孩子。剩余孩子的幸福值变为 [1,2,3] 。
所选孩子的幸福值之和为 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == happiness.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= happiness[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Since all the unselected numbers are decreasing at the same rate, we should greedily select <code>k</code> largest values.
2. The <code>i<sup>th</code> largest number (<code>i = 1, 2, 3,…k</code>) should decrease by <code>(i - 1)</code> when it is picked.
3. Add <code>0</code> if the decreased value is negative.

## 示例

```
[1,2,3]
2
[1,1,1,1]
2
[2,3,4,5]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
```

### C

```c
long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    
};
```

### TypeScript

```typescript
function maximumHappinessSum(happiness: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $happiness
     * @param Integer $k
     * @return Integer
     */
    function maximumHappinessSum($happiness, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumHappinessSum(List<int> happiness, int k) {
    
  }
}
```

### Go

```golang
func maximumHappinessSum(happiness []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_happiness_sum(happiness: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-happiness-sum happiness k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_happiness_sum(Happiness :: [integer()], K :: integer()) -> integer().
maximum_happiness_sum(Happiness, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_happiness_sum(happiness :: [integer], k :: integer) :: integer
  def maximum_happiness_sum(happiness, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumHappinessSum(happiness: Array<Int64>, k: Int64): Int64 {

    }
}
```

