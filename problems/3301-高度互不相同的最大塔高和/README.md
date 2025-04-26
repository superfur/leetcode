# 3301. 高度互不相同的最大塔高和

## 题目描述

<p>给你一个数组&nbsp;<code>maximumHeight</code>&nbsp;，其中&nbsp;<code>maximumHeight[i]</code>&nbsp;表示第 <code>i</code>&nbsp;座塔可以达到的 <strong>最大</strong>&nbsp;高度。</p>

<p>你的任务是给每一座塔分别设置一个高度，使得：</p>

<ol>
	<li>第 <code>i</code>&nbsp;座塔的高度是一个正整数，且不超过&nbsp;<code>maximumHeight[i]</code>&nbsp;。</li>
	<li>所有塔的高度互不相同。</li>
</ol>

<p>请你返回设置完所有塔的高度后，可以达到的 <strong>最大</strong>&nbsp;总高度。如果没有合法的设置，返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><b>输入：</b>maximumHeight<span class="example-io"> = [2,3,4,3]</span></p>

<p><span class="example-io"><b>输出：</b>10</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将塔的高度设置为：<code>[1, 2, 4, 3]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><b>输入：</b>maximumHeight<span class="example-io"> = [15,10]</span></p>

<p><span class="example-io"><b>输出：</b>25</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将塔的高度设置为：<code>[15, 10]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><b>输入：</b>maximumHeight<span class="example-io"> = [2,2,1]</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><b>解释：</b></p>

<p>无法设置塔的高度为正整数且高度互不相同。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= maximumHeight.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= maximumHeight[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort the array <code>maximumHeight</code> in descending order.
2. After sorting, it can be seen that the maximum height that we can assign to the <code>i<sup>th</sup></code> element is <code>min(maximumHeight[i], maximumHeight[i - 1] - 1)</code>.

## 示例

```
[2,3,4,3]
[15,10]
[2,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumTotalSum(vector<int>& maximumHeight) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTotalSum(self, maximumHeight):
        """
        :type maximumHeight: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
```

### C

```c
long long maximumTotalSum(int* maximumHeight, int maximumHeightSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumTotalSum(int[] maximumHeight) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} maximumHeight
 * @return {number}
 */
var maximumTotalSum = function(maximumHeight) {
    
};
```

### TypeScript

```typescript
function maximumTotalSum(maximumHeight: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $maximumHeight
     * @return Integer
     */
    function maximumTotalSum($maximumHeight) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTotalSum(_ maximumHeight: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTotalSum(maximumHeight: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTotalSum(List<int> maximumHeight) {
    
  }
}
```

### Go

```golang
func maximumTotalSum(maximumHeight []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} maximum_height
# @return {Integer}
def maximum_total_sum(maximum_height)
    
end
```

### Scala

```scala
object Solution {
    def maximumTotalSum(maximumHeight: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_total_sum(maximum_height: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-total-sum maximumHeight)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_total_sum(MaximumHeight :: [integer()]) -> integer().
maximum_total_sum(MaximumHeight) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_total_sum(maximum_height :: [integer]) :: integer
  def maximum_total_sum(maximum_height) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTotalSum(maximumHeight: Array<Int64>): Int64 {

    }
}
```

