# 1402. 做菜顺序

## 题目描述

<p>一个厨师收集了他&nbsp;<code>n</code>&nbsp;道菜的满意程度&nbsp;<code>satisfaction</code>&nbsp;，这个厨师做出每道菜的时间都是 1 单位时间。</p>

<p>一道菜的 「&nbsp;<strong>like-time 系数&nbsp;</strong>」定义为烹饪这道菜结束的时间（包含之前每道菜所花费的时间）乘以这道菜的满意程度，也就是&nbsp;<code>time[i]</code>*<code>satisfaction[i]</code>&nbsp;。</p>

<p>返回厨师在准备了一定数量的菜肴后可以获得的最大 <strong>like-time 系数</strong> 总和。</p>

<p>你可以按&nbsp;<strong>任意</strong>&nbsp;顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>satisfaction = [-1,-8,0,5,-9]
<strong>输出：</strong>14
<strong>解释：</strong>去掉第二道和最后一道菜，最大的 like-time 系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>satisfaction = [4,3,2]
<strong>输出：</strong>20
<strong>解释：可以</strong>按照任意顺序做菜 (2*1 + 3*2 + 4*3 = 20)
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>satisfaction = [-1,-4,-5]
<strong>输出：</strong>0
<strong>解释：</strong>大家都不喜欢这些菜，所以不做任何菜就可以获得最大的 like-time 系数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == satisfaction.length</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>-1000 &lt;= satisfaction[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 动态规划
- 排序

## 提示

1. Use dynamic programming to find the optimal solution by saving the previous best like-time coefficient and its corresponding element sum.
2. If adding the current element to the previous best like-time coefficient and its corresponding element sum would increase the best like-time coefficient, then go ahead and add it. Otherwise, keep the previous best like-time coefficient.

## 示例

```
[-1,-8,0,5,-7]
[4,3,2]
[-1,-4,-5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
```

### C

```c
int maxSatisfaction(int* satisfaction, int satisfactionSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSatisfaction(int[] satisfaction) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    
};
```

### TypeScript

```typescript
function maxSatisfaction(satisfaction: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $satisfaction
     * @return Integer
     */
    function maxSatisfaction($satisfaction) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSatisfaction(_ satisfaction: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSatisfaction(satisfaction: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSatisfaction(List<int> satisfaction) {
    
  }
}
```

### Go

```golang
func maxSatisfaction(satisfaction []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} satisfaction
# @return {Integer}
def max_satisfaction(satisfaction)
    
end
```

### Scala

```scala
object Solution {
    def maxSatisfaction(satisfaction: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_satisfaction(satisfaction: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-satisfaction satisfaction)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_satisfaction(Satisfaction :: [integer()]) -> integer().
max_satisfaction(Satisfaction) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_satisfaction(satisfaction :: [integer]) :: integer
  def max_satisfaction(satisfaction) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSatisfaction(satisfaction: Array<Int64>): Int64 {

    }
}
```

