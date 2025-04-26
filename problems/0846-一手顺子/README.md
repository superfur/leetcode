# 846. 一手顺子

## 题目描述

<p>Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 <code>groupSize</code> ，并且由 <code>groupSize</code> 张连续的牌组成。</p>

<p>给你一个整数数组 <code>hand</code> 其中 <code>hand[i]</code> 是写在第 <code>i</code> 张牌上的<strong>数值</strong>。如果她可能重新排列这些牌，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>输出：</strong>true
<strong>解释：</strong>Alice 手中的牌可以被重新排列为 <code>[1,2,3]，[2,3,4]，[6,7,8]</code>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>hand = [1,2,3,4,5], groupSize = 4
<strong>输出：</strong>false
<strong>解释：</strong>Alice 手中的牌无法被重新排列成几个大小为 4 的组。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>此题目与 1296 重复：<a href="https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 排序

## 示例

```
[1,2,3,6,2,3,4,7,8]
3
[1,2,3,4,5]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
```

### C

```c
bool isNStraightHand(int* hand, int handSize, int groupSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function(hand, groupSize) {
    
};
```

### TypeScript

```typescript
function isNStraightHand(hand: number[], groupSize: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $hand
     * @param Integer $groupSize
     * @return Boolean
     */
    function isNStraightHand($hand, $groupSize) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isNStraightHand(hand: IntArray, groupSize: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isNStraightHand(List<int> hand, int groupSize) {
    
  }
}
```

### Go

```golang
func isNStraightHand(hand []int, groupSize int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} hand
# @param {Integer} group_size
# @return {Boolean}
def is_n_straight_hand(hand, group_size)
    
end
```

### Scala

```scala
object Solution {
    def isNStraightHand(hand: Array[Int], groupSize: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-n-straight-hand hand groupSize)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_n_straight_hand(Hand :: [integer()], GroupSize :: integer()) -> boolean().
is_n_straight_hand(Hand, GroupSize) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_n_straight_hand(hand :: [integer], group_size :: integer) :: boolean
  def is_n_straight_hand(hand, group_size) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isNStraightHand(hand: Array<Int64>, groupSize: Int64): Bool {

    }
}
```

