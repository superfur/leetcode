# 1090. 受标签影响的最大值

## 题目描述

<p>以两个整数数组 &nbsp;<code>values</code>&nbsp;和 <code>labels</code>&nbsp;给定&nbsp;<code>n</code>&nbsp;个项的值和标签，并且给出两个整数&nbsp;<code>numWanted</code>&nbsp;和 <code>useLimit</code> 。</p>

<p>你的任务是从这些项中找到一个值的和 <strong>最大</strong> 的子集使得：</p>

<ul>
	<li>项的数量 <strong>最多</strong> 为&nbsp;<code>numWanted</code>。</li>
	<li>相同标签的项的数量&nbsp;<strong>最多 </strong>为&nbsp;<code>useLimit</code>。</li>
</ul>

<p>返回最大的和。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1</span></p>

<p><strong>输出：</strong><span class="example-io">9</span></p>

<p><strong>解释：</strong></p>

<p>选择的子集是第一个、第三个和第五个项，其值之和为 5 + 3 + 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2</span></p>

<p><strong>输出：</strong><span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p>选择的子集是第一个、第二个和第三个项，其值之和为 5 + 4 + 3。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1</span></p>

<p><strong>输出：</strong><span class="example-io">16</span></p>

<p><strong>解释：</strong></p>

<p>选择的子集是第一个和第四个项，其值之和为 9 + 7。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == values.length == labels.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= values[i], labels[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= numWanted, useLimit &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数
- 排序

## 提示

1. Consider the items in order from largest to smallest value, and greedily take the items if they fall under the use_limit.  We can keep track of how many items of each label are used by using a hash table.

## 示例

```
[5,4,3,2,1]
[1,1,2,2,3]
3
1
[5,4,3,2,1]
[1,3,3,3,2]
3
2
[9,8,8,7,6]
[0,0,0,1,1]
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
```

### C

```c
int largestValsFromLabels(int* values, int valuesSize, int* labels, int labelsSize, int numWanted, int useLimit) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} values
 * @param {number[]} labels
 * @param {number} numWanted
 * @param {number} useLimit
 * @return {number}
 */
var largestValsFromLabels = function(values, labels, numWanted, useLimit) {
    
};
```

### TypeScript

```typescript
function largestValsFromLabels(values: number[], labels: number[], numWanted: number, useLimit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $values
     * @param Integer[] $labels
     * @param Integer $numWanted
     * @param Integer $useLimit
     * @return Integer
     */
    function largestValsFromLabels($values, $labels, $numWanted, $useLimit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestValsFromLabels(_ values: [Int], _ labels: [Int], _ numWanted: Int, _ useLimit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestValsFromLabels(values: IntArray, labels: IntArray, numWanted: Int, useLimit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestValsFromLabels(List<int> values, List<int> labels, int numWanted, int useLimit) {
    
  }
}
```

### Go

```golang
func largestValsFromLabels(values []int, labels []int, numWanted int, useLimit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} values
# @param {Integer[]} labels
# @param {Integer} num_wanted
# @param {Integer} use_limit
# @return {Integer}
def largest_vals_from_labels(values, labels, num_wanted, use_limit)
    
end
```

### Scala

```scala
object Solution {
    def largestValsFromLabels(values: Array[Int], labels: Array[Int], numWanted: Int, useLimit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_vals_from_labels(values: Vec<i32>, labels: Vec<i32>, num_wanted: i32, use_limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-vals-from-labels values labels numWanted useLimit)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_vals_from_labels(Values :: [integer()], Labels :: [integer()], NumWanted :: integer(), UseLimit :: integer()) -> integer().
largest_vals_from_labels(Values, Labels, NumWanted, UseLimit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_vals_from_labels(values :: [integer], labels :: [integer], num_wanted :: integer, use_limit :: integer) :: integer
  def largest_vals_from_labels(values, labels, num_wanted, use_limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestValsFromLabels(values: Array<Int64>, labels: Array<Int64>, numWanted: Int64, useLimit: Int64): Int64 {

    }
}
```

