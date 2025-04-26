# 3206. 交替组 I

## 题目描述

<p>给你一个整数数组 <code>colors</code>&nbsp;，它表示一个由红色和蓝色瓷砖组成的环，第 <code>i</code>&nbsp;块瓷砖的颜色为&nbsp;<code>colors[i]</code>&nbsp;：</p>

<ul>
	<li><code>colors[i] == 0</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;块瓷砖的颜色是 <strong>红色</strong>&nbsp;。</li>
	<li><code>colors[i] == 1</code>&nbsp;表示第 <code>i</code>&nbsp;块瓷砖的颜色是 <strong>蓝色</strong>&nbsp;。</li>
</ul>

<p>环中连续 3 块瓷砖的颜色如果是 <strong>交替</strong>&nbsp;颜色（也就是说中间瓷砖的颜色与它<strong>&nbsp;左边</strong>&nbsp;和 <strong>右边</strong>&nbsp;的颜色都不同），那么它被称为一个 <strong>交替</strong>&nbsp;组。</p>

<p>请你返回 <strong>交替</strong>&nbsp;组的数目。</p>

<p><b>注意</b>&nbsp;，由于&nbsp;<code>colors</code>&nbsp;表示一个 <strong>环</strong>&nbsp;，<strong>第一块</strong>&nbsp;瓷砖和 <strong>最后一块</strong>&nbsp;瓷砖是相邻的。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>colors = [1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-53-171.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>colors = [0,1,0,0,1]</span></p>

<p><b>输出：</b>3</p>

<p><b>解释：</b></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-47-491.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>交替组包括：</p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-50-441.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong><img alt="" src="https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-48-211.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-49-351.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= colors.length &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 滑动窗口

## 提示

1. For each tile, check that the previous and the next tile have different colors from that tile or not.

## 示例

```
[1,1,1]
[0,1,0,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfAlternatingGroups(int[] colors) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
```

### C

```c
int numberOfAlternatingGroups(int* colors, int colorsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfAlternatingGroups(int[] colors) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} colors
 * @return {number}
 */
var numberOfAlternatingGroups = function(colors) {
    
};
```

### TypeScript

```typescript
function numberOfAlternatingGroups(colors: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function numberOfAlternatingGroups($colors) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfAlternatingGroups(_ colors: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfAlternatingGroups(colors: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfAlternatingGroups(List<int> colors) {
    
  }
}
```

### Go

```golang
func numberOfAlternatingGroups(colors []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} colors
# @return {Integer}
def number_of_alternating_groups(colors)
    
end
```

### Scala

```scala
object Solution {
    def numberOfAlternatingGroups(colors: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-alternating-groups colors)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_alternating_groups(Colors :: [integer()]) -> integer().
number_of_alternating_groups(Colors) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer]) :: integer
  def number_of_alternating_groups(colors) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfAlternatingGroups(colors: Array<Int64>): Int64 {

    }
}
```

