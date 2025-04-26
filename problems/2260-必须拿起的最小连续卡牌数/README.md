# 2260. 必须拿起的最小连续卡牌数

## 题目描述

<p>给你一个整数数组 <code>cards</code> ，其中 <code>cards[i]</code> 表示第 <code>i</code> 张卡牌的 <strong>值</strong> 。如果两张卡牌的值相同，则认为这一对卡牌 <strong>匹配</strong> 。</p>

<p>返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cards = [3,4,2,3,4,7]
<strong>输出：</strong>4
<strong>解释：</strong>拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cards = [1,0,5,3]
<strong>输出：</strong>-1
<strong>解释：</strong>无法找出含一对匹配卡牌的一组连续卡牌。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cards.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= cards[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 提示

1. Iterate through the cards and store the location of the last occurrence of each number.
2. What data structure could you use to get the last occurrence of a number in O(1) or O(log n)?

## 示例

```
[3,4,2,3,4,7]
[1,0,5,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCardPickup(int[] cards) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
```

### C

```c
int minimumCardPickup(int* cards, int cardsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCardPickup(int[] cards) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cards
 * @return {number}
 */
var minimumCardPickup = function(cards) {
    
};
```

### TypeScript

```typescript
function minimumCardPickup(cards: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cards
     * @return Integer
     */
    function minimumCardPickup($cards) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCardPickup(_ cards: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCardPickup(cards: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCardPickup(List<int> cards) {
    
  }
}
```

### Go

```golang
func minimumCardPickup(cards []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cards
# @return {Integer}
def minimum_card_pickup(cards)
    
end
```

### Scala

```scala
object Solution {
    def minimumCardPickup(cards: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_card_pickup(cards: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-card-pickup cards)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_card_pickup(Cards :: [integer()]) -> integer().
minimum_card_pickup(Cards) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_card_pickup(cards :: [integer]) :: integer
  def minimum_card_pickup(cards) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCardPickup(cards: Array<Int64>): Int64 {

    }
}
```

