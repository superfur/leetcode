# 3208. 交替组 II

## 题目描述

<p>给你一个整数数组 <code>colors</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，<code>colors</code>表示一个由红色和蓝色瓷砖组成的环，第 <code>i</code>&nbsp;块瓷砖的颜色为&nbsp;<code>colors[i]</code>&nbsp;：</p>

<ul>
	<li><code>colors[i] == 0</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;块瓷砖的颜色是 <strong>红色</strong>&nbsp;。</li>
	<li><code>colors[i] == 1</code>&nbsp;表示第 <code>i</code>&nbsp;块瓷砖的颜色是 <strong>蓝色</strong>&nbsp;。</li>
</ul>

<p>环中连续 <code>k</code>&nbsp;块瓷砖的颜色如果是 <strong>交替</strong>&nbsp;颜色（也就是说除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它<strong>&nbsp;左边</strong>&nbsp;和 <strong>右边</strong>&nbsp;的颜色都不同），那么它被称为一个 <strong>交替</strong>&nbsp;组。</p>

<p>请你返回 <strong>交替</strong>&nbsp;组的数目。</p>

<p><b>注意</b>&nbsp;，由于&nbsp;<code>colors</code>&nbsp;表示一个 <strong>环</strong>&nbsp;，<strong>第一块</strong>&nbsp;瓷砖和 <strong>最后一块</strong>&nbsp;瓷砖是相邻的。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>colors = [0,1,0,1,0], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>交替组包括：</p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong><img alt="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>colors = [0,1,0,0,1,0,1], k = 6</span></p>

<p><b>输出：</b>2</p>

<p><b>解释：</b></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>交替组包括：</p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p><strong>示例 3：</strong></p>

<p><strong>输入：</strong>colors = [1,1,0,1], k = 4</p>

<p><strong>输出：</strong>0</p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= colors.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= colors[i] &lt;= 1</code></li>
	<li><code>3 &lt;= k &lt;= colors.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 提示

1. Try to find a tile that has the same color as its next tile (if it exists).
2. Then try to find maximal alternating groups by starting a single for loop from that tile.

## 示例

```
[0,1,0,1,0]
3
[0,1,0,0,1,0,1]
6
[1,1,0,1]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
```

### C

```c
int numberOfAlternatingGroups(int* colors, int colorsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfAlternatingGroups(int[] colors, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} colors
 * @param {number} k
 * @return {number}
 */
var numberOfAlternatingGroups = function(colors, k) {
    
};
```

### TypeScript

```typescript
function numberOfAlternatingGroups(colors: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @param Integer $k
     * @return Integer
     */
    function numberOfAlternatingGroups($colors, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfAlternatingGroups(List<int> colors, int k) {
    
  }
}
```

### Go

```golang
func numberOfAlternatingGroups(colors []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} colors
# @param {Integer} k
# @return {Integer}
def number_of_alternating_groups(colors, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfAlternatingGroups(colors: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-alternating-groups colors k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_alternating_groups(Colors :: [integer()], K :: integer()) -> integer().
number_of_alternating_groups(Colors, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer], k :: integer) :: integer
  def number_of_alternating_groups(colors, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfAlternatingGroups(colors: Array<Int64>, k: Int64): Int64 {

    }
}
```

