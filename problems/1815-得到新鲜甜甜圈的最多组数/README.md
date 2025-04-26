# 1815. 得到新鲜甜甜圈的最多组数

## 题目描述

<p>有一个甜甜圈商店，每批次都烤 <code>batchSize</code> 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 <strong>所有</strong> 甜甜圈都必须已经全部销售完毕。给你一个整数 <code>batchSize</code> 和一个整数数组 <code>groups</code> ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 <code>groups[i]</code> 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。</p>

<p>当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。</p>

<p>你可以随意安排每批顾客到来的顺序。请你返回在此前提下，<strong>最多</strong> 有多少组人会感到开心。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>batchSize = 3, groups = [1,2,3,4,5,6]
<b>输出：</b>4
<b>解释：</b>你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>batchSize = 4, groups = [1,3,2,5,2,2,1,6]
<b>输出：</b>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= batchSize <= 9</code></li>
	<li><code>1 <= groups.length <= 30</code></li>
	<li><code>1 <= groups[i] <= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 记忆化搜索
- 数组
- 动态规划
- 状态压缩

## 提示

1. The maximum number of happy groups is the maximum number of partitions you can split the groups into such that the sum of group sizes in each partition is 0 mod batchSize. At most one partition is allowed to have a different remainder (the first group will get fresh donuts anyway).
2. Suppose you have an array freq of length k where freq[i] = number of groups of size i mod batchSize. How can you utilize this in a dp solution?
3. Make a DP state dp[freq][r] that represents "the maximum number of partitions you can form given the current freq and current remainder r". You can hash the freq array to store it more easily in the dp table.
4. For each i from 0 to batchSize-1, the next DP state is dp[freq`][(r+i)%batchSize] where freq` is freq but with freq[i] decremented by 1. Take the largest of all of the next states and store it in ans. If r == 0, then return ans+1 (because you can form a new partition), otherwise return ans (continuing the current partition).

## 示例

```
3
[1,2,3,4,5,6]
4
[1,3,2,5,2,2,1,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxHappyGroups(int batchSize, vector<int>& groups) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxHappyGroups(int batchSize, int[] groups) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        
```

### C

```c
int maxHappyGroups(int batchSize, int* groups, int groupsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxHappyGroups(int batchSize, int[] groups) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} batchSize
 * @param {number[]} groups
 * @return {number}
 */
var maxHappyGroups = function(batchSize, groups) {
    
};
```

### TypeScript

```typescript
function maxHappyGroups(batchSize: number, groups: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $batchSize
     * @param Integer[] $groups
     * @return Integer
     */
    function maxHappyGroups($batchSize, $groups) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxHappyGroups(_ batchSize: Int, _ groups: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxHappyGroups(batchSize: Int, groups: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxHappyGroups(int batchSize, List<int> groups) {
    
  }
}
```

### Go

```golang
func maxHappyGroups(batchSize int, groups []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} batch_size
# @param {Integer[]} groups
# @return {Integer}
def max_happy_groups(batch_size, groups)
    
end
```

### Scala

```scala
object Solution {
    def maxHappyGroups(batchSize: Int, groups: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_happy_groups(batch_size: i32, groups: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-happy-groups batchSize groups)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_happy_groups(BatchSize :: integer(), Groups :: [integer()]) -> integer().
max_happy_groups(BatchSize, Groups) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_happy_groups(batch_size :: integer, groups :: [integer]) :: integer
  def max_happy_groups(batch_size, groups) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxHappyGroups(batchSize: Int64, groups: Array<Int64>): Int64 {

    }
}
```

