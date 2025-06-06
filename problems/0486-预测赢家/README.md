# 486. 预测赢家

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。</p>

<p>玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 <code>0</code> 。每一回合，玩家从数组的任意一端取一个数字（即，<code>nums[0]</code> 或 <code>nums[nums.length - 1]</code>），取到的数字将会从数组中移除（数组长度减 <code>1</code> ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。</p>

<p>如果玩家 1 能成为赢家，返回 <code>true</code> 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 <code>true</code> 。你可以假设每个玩家的玩法都会使他的分数最大化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,2]
<strong>输出：</strong>false
<strong>解释：</strong>一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。 
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 false 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,233,7]
<strong>输出：</strong>true
<strong>解释：</strong>玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 递归
- 数组
- 数学
- 动态规划
- 博弈

## 示例

```
[1,5,2]
[1,5,233,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean predictTheWinner(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
```

### C

```c
bool predictTheWinner(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PredictTheWinner(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var predictTheWinner = function(nums) {
    
};
```

### TypeScript

```typescript
function predictTheWinner(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function predictTheWinner($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func predictTheWinner(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun predictTheWinner(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool predictTheWinner(List<int> nums) {
    
  }
}
```

### Go

```golang
func predictTheWinner(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def predict_the_winner(nums)
    
end
```

### Scala

```scala
object Solution {
    def predictTheWinner(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (predict-the-winner nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec predict_the_winner(Nums :: [integer()]) -> boolean().
predict_the_winner(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec predict_the_winner(nums :: [integer]) :: boolean
  def predict_the_winner(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func predictTheWinner(nums: Array<Int64>): Bool {

    }
}
```

