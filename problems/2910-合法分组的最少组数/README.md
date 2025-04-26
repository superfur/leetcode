# 2910. 合法分组的最少组数

## 题目描述

<p>给你一组带编号的&nbsp;<code>balls</code> 并要求将它们分类到盒子里，以便均衡地分配。你必须遵守两条规则：</p>

<ul>
	<li>同一个盒子里的球必须具有相同的编号。但是，如果你有多个相同编号的球，你可以把它们放在不同的盒子里。</li>
	<li>最大的盒子只能比最小的盒子多一个球。</li>
</ul>

<p>返回遵循上述规则排列这些球所需要的盒子的最小数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>balls = [3,2,3,2,3]
<b>输出：</b>2
<b>解释：</b>一个得到 2 个分组的方案如下，中括号内的数字都是下标：
我们可以如下排列 balls 到盒子里：
- [3,3,3]
- [2,2]
两个盒子之间的大小差没有超过 1。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>balls = [10,10,10,3,1,1]
<b>输出：</b>4
<b>解释：</b>我们可以如下排列 balls 到盒子里：
- [10]
- [10,10]
- [3]
- [1,1]
无法得到一个遵循上述规则且小于 4 盒的答案。例如，把所有三个编号为 10 的球都放在一个盒子里，就会打破盒子之间最大尺寸差异的规则。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= balls.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= balls[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. Calculate the frequency of each number.
2. For each <code>x</code> in the range <code>[1, minimum_frequency]</code>, try to create groups with either <code>x</code> or <code>x + 1</code> indices assigned to them while minimizing the total number of groups.
3. For each distinct number, using its frequency, check that all its occurrences can be assigned to groups of size <code>x</code> or <code>x + 1</code> while minimizing the number of groups used.
4. To get the minimum number of groups needed for a number having frequency <code>f</code> to be assigned to groups of size <code>x</code> or <code>x + 1</code>, let <code>a = f / (x + 1)</code> and <code>b = f % (x + 1)</code>. <ul> <li>If <code>b == 0</code>, then we can simply create <code>a</code> groups of size <code>x + 1</code>.</li> <li>If <code>x - b <= a</code>, we can have <code>a - (x - b)</code> groups of size <code>x + 1</code> and <code>x - b + 1</code> groups of size <code>x</code>. So, in total, we have <code>a + 1</code> groups.</li> <li>Otherwise, it's impossible.</li> </ul>
5. The minimum number of groups needed for some <code>x</code> is the total minimized number of groups needed for each distinct number.
6. The answer is the minimum number of groups needed for each <code>x</code> in the range <code>[1, minimum_frequency]</code>.

## 示例

```
[3,2,3,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minGroupsForValidAssignment(vector<int>& balls) {
        
    }
};
```

### Java

```java
class Solution {
    public int minGroupsForValidAssignment(int[] balls) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minGroupsForValidAssignment(self, balls):
        """
        :type balls: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        
```

### C

```c
int minGroupsForValidAssignment(int* balls, int ballsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinGroupsForValidAssignment(int[] balls) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} balls
 * @return {number}
 */
var minGroupsForValidAssignment = function(balls) {
    
};
```

### TypeScript

```typescript
function minGroupsForValidAssignment(balls: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $balls
     * @return Integer
     */
    function minGroupsForValidAssignment($balls) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minGroupsForValidAssignment(_ balls: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minGroupsForValidAssignment(balls: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minGroupsForValidAssignment(List<int> balls) {
    
  }
}
```

### Go

```golang
func minGroupsForValidAssignment(balls []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} balls
# @return {Integer}
def min_groups_for_valid_assignment(balls)
    
end
```

### Scala

```scala
object Solution {
    def minGroupsForValidAssignment(balls: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_groups_for_valid_assignment(balls: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-groups-for-valid-assignment balls)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_groups_for_valid_assignment(Balls :: [integer()]) -> integer().
min_groups_for_valid_assignment(Balls) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_groups_for_valid_assignment(balls :: [integer]) :: integer
  def min_groups_for_valid_assignment(balls) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minGroupsForValidAssignment(balls: Array<Int64>): Int64 {

    }
}
```

