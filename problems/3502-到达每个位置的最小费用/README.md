# 3502. 到达每个位置的最小费用

## 题目描述

<p data-end="438" data-start="104">给你一个长度为 <code>n</code> 的整数数组 <code data-end="119" data-start="113">cost</code> 。当前你位于位置 <code data-end="166" data-start="163">n</code>（队伍的末尾），队伍中共有 <code data-end="187" data-start="180">n + 1</code> 人，编号从 0 到 <code>n</code> 。</p>

<p data-end="438" data-start="104">你希望在队伍中向前移动，但队伍中每个人都会收取一定的费用才能与你 <strong>交换</strong>位置。与编号 <code data-end="375" data-start="372">i</code> 的人交换位置的费用为 <code data-end="397" data-start="388">cost[i]</code> 。</p>

<p data-end="487" data-start="440">你可以按照以下规则与他人交换位置：</p>

<ul data-end="632" data-start="488">
	<li data-end="572" data-start="488">如果对方在你前面，你 <strong>必须</strong> 支付 <code data-end="546" data-start="537">cost[i]</code> 费用与他们交换位置。</li>
	<li data-end="632" data-start="573">如果对方在你后面，他们可以免费与你交换位置。</li>
</ul>

<p data-end="755" data-start="634">返回一个大小为 <code>n</code> 的数组 <code>answer</code>，其中 <code>answer[i]</code> 表示到达队伍中每个位置 <code>i</code> 所需的 <strong data-end="680" data-start="664">最小</strong> 总费用。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">cost = [5,3,4,1,3,2]</span></p>

<p><strong>输出:</strong> <span class="example-io">[5,3,3,1,1,1]</span></p>

<p><strong>解释:</strong></p>

<p>我们可以通过以下方式到达每个位置：</p>

<ul>
	<li><code>i = 0</code>。可以花费 5 费用与编号 0 的人交换位置。</li>
	<li><span class="example-io"><code>i = 1</code>。可以花费 3 费用与编号 1 的人交换位置。</span></li>
	<li><span class="example-io"><code>i = 2</code>。可以花费 3 费用与编号 1 的人交换位置，然后免费与编号 2 的人交换位置。</span></li>
	<li><span class="example-io"><code>i = 3</code>。可以花费 1 费用与编号 3 的人交换位置。</span></li>
	<li><span class="example-io"><code>i = 4</code>。可以花费 1 费用与编号 3 的人交换位置，然后免费与编号 4 的人交换位置。</span></li>
	<li><span class="example-io"><code>i = 5</code>。可以花费 1 费用与编号 3 的人交换位置，然后免费与编号 5 的人交换位置。</span></li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">cost = [1,2,4,6,7]</span></p>

<p><strong>输出:</strong> <span class="example-io">[1,1,1,1,1]</span></p>

<p><strong>解释:</strong></p>

<p>可以花费 1 费用与编号 0 的人交换位置，然后可以免费到达队伍中的任何位置 <code>i</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示</strong></p>

<ul>
	<li><code>1 &lt;= n == cost.length &lt;= 100</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Note that once you swap to a position with a lower cost, you can reach any later position for free.
2. Use a min prefix array.

## 示例

```
[5,3,4,1,3,2]
[1,2,4,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minCosts(int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minCosts(int* cost, int costSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinCosts(int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @return {number[]}
 */
var minCosts = function(cost) {
    
};
```

### TypeScript

```typescript
function minCosts(cost: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer[]
     */
    function minCosts($cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCosts(_ cost: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCosts(cost: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minCosts(List<int> cost) {
    
  }
}
```

### Go

```golang
func minCosts(cost []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @return {Integer[]}
def min_costs(cost)
    
end
```

### Scala

```scala
object Solution {
    def minCosts(cost: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_costs(cost: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-costs cost)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_costs(Cost :: [integer()]) -> [integer()].
min_costs(Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_costs(cost :: [integer]) :: [integer]
  def min_costs(cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCosts(cost: Array<Int64>): Array<Int64> {

    }
}
```

