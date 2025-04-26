# 2790. 长度递增组的最大数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的数组 <code>usageLimits</code> 。</p>

<p>你的任务是使用从 <code>0</code> 到 <code>n - 1</code> 的数字创建若干组，并确保每个数字 <code>i</code> 在 <strong>所有组</strong> 中使用的次数总共不超过 <code>usageLimits[i]</code> 次。此外，还必须满足以下条件：</p>

<ul>
	<li>每个组必须由 <strong>不同</strong> 的数字组成，也就是说，单个组内不能存在重复的数字。</li>
	<li>每个组（除了第一个）的长度必须 <strong>严格大于</strong> 前一个组。</li>
</ul>

<p>在满足所有条件的情况下，以整数形式返回可以创建的最大组数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<code><strong>输入：</strong>usageLimits</code> = [1,2,5]
<strong>输出：</strong>3
<strong>解释：</strong>在这个示例中，我们可以使用 0 至多一次，使用 1 至多 2 次，使用 2 至多 5 次。
一种既能满足所有条件，又能创建最多组的方式是： 
组 1 包含数字 [2] 。
组 2 包含数字 [1,2] 。
组 3 包含数字 [0,1,2] 。 
可以证明能够创建的最大组数是 3 。 
所以，输出是 3 。 </pre>

<p><strong>示例 2：</strong></p>

<pre>
<code><strong>输入：</strong></code><code>usageLimits</code> = [2,1,2]
<strong>输出：</strong>2
<strong>解释：</strong>在这个示例中，我们可以使用 0 至多 2 次，使用 1 至多 1 次，使用 2 至多 2 次。
一种既能满足所有条件，又能创建最多组的方式是： 
组 1 包含数字 [0] 。 
组 2 包含数字 [1,2] 。
可以证明能够创建的最大组数是 2 。 
所以，输出是 2 。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<code><strong>输入：</strong></code><code>usageLimits</code> = [1,1]
<strong>输出：</strong>1
<strong>解释：</strong>在这个示例中，我们可以使用 0 和 1 至多 1 次。 
一种既能满足所有条件，又能创建最多组的方式是：
组 1 包含数字 [0] 。
可以证明能够创建的最大组数是 1 。 
所以，输出是 1 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= usageLimits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= usageLimits[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 数学
- 二分查找
- 排序

## 提示

1. Can we solve this problem using sorting and binary search?
2. Sort the array in increasing order and run a binary search on the number of groups, x.
3. To determine if a value x is feasible, greedily distribute the numbers such that each group receives 1, 2, 3, ..., x numbers.

## 示例

```
[1,2,5]
[2,1,2]
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxIncreasingGroups(vector<int>& usageLimits) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxIncreasingGroups(List<Integer> usageLimits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        :type usageLimits: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        
```

### C

```c
int maxIncreasingGroups(int* usageLimits, int usageLimitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxIncreasingGroups(IList<int> usageLimits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} usageLimits
 * @return {number}
 */
var maxIncreasingGroups = function(usageLimits) {
    
};
```

### TypeScript

```typescript
function maxIncreasingGroups(usageLimits: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $usageLimits
     * @return Integer
     */
    function maxIncreasingGroups($usageLimits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxIncreasingGroups(_ usageLimits: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxIncreasingGroups(usageLimits: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxIncreasingGroups(List<int> usageLimits) {
    
  }
}
```

### Go

```golang
func maxIncreasingGroups(usageLimits []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} usage_limits
# @return {Integer}
def max_increasing_groups(usage_limits)
    
end
```

### Scala

```scala
object Solution {
    def maxIncreasingGroups(usageLimits: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_increasing_groups(usage_limits: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-increasing-groups usageLimits)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_increasing_groups(UsageLimits :: [integer()]) -> integer().
max_increasing_groups(UsageLimits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_increasing_groups(usage_limits :: [integer]) :: integer
  def max_increasing_groups(usage_limits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxIncreasingGroups(usageLimits: ArrayList<Int64>): Int64 {

    }
}
```

