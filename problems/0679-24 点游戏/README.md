# 679. 24 点游戏

## 题目描述

<p>给定一个长度为4的整数数组&nbsp;<code>cards</code>&nbsp;。你有 <code>4</code> 张卡片，每张卡片上都包含一个范围在 <code>[1,9]</code> 的数字。您应该使用运算符&nbsp;<code>['+', '-', '*', '/']</code>&nbsp;和括号&nbsp;<code>'('</code>&nbsp;和&nbsp;<code>')'</code>&nbsp;将这些卡片上的数字排列成数学表达式，以获得值24。</p>

<p>你须遵守以下规则:</p>

<ul>
	<li>除法运算符 <code>'/'</code> 表示实数除法，而不是整数除法。

	<ul>
		<li>例如，&nbsp;<code>4 /(1 - 2 / 3)= 4 /(1 / 3)= 12</code>&nbsp;。</li>
	</ul>
	</li>
	<li>每个运算都在两个数字之间。特别是，不能使用 <code>“-”</code> 作为一元运算符。
	<ul>
		<li>例如，如果 <code>cards =[1,1,1,1]</code> ，则表达式 <code>“-1 -1 -1 -1”</code> 是 <strong>不允许</strong> 的。</li>
	</ul>
	</li>
	<li>你不能把数字串在一起
	<ul>
		<li>例如，如果 <code>cards =[1,2,1,2]</code> ，则表达式 <code>“12 + 12”</code> 无效。</li>
	</ul>
	</li>
</ul>

<p>如果可以得到这样的表达式，其计算结果为 <code>24</code> ，则返回 <code>true </code>，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> cards = [4, 1, 8, 7]
<strong>输出:</strong> true
<strong>解释:</strong> (8-4) * (7-1) = 24
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> cards = [1, 2, 1, 2]
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>cards.length == 4</code></li>
	<li><code>1 &lt;= cards[i] &lt;= 9</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 回溯

## 示例

```
[4,1,8,7]
[1,2,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean judgePoint24(int[] cards) {
        
    }
}
```

### Python

```python
class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
```

### C

```c
bool judgePoint24(int* cards, int cardsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool JudgePoint24(int[] cards) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cards
 * @return {boolean}
 */
var judgePoint24 = function(cards) {
    
};
```

### TypeScript

```typescript
function judgePoint24(cards: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cards
     * @return Boolean
     */
    function judgePoint24($cards) {
        
    }
}
```

### Swift

```swift
class Solution {
    func judgePoint24(_ cards: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun judgePoint24(cards: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool judgePoint24(List<int> cards) {
    
  }
}
```

### Go

```golang
func judgePoint24(cards []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cards
# @return {Boolean}
def judge_point24(cards)
    
end
```

### Scala

```scala
object Solution {
    def judgePoint24(cards: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn judge_point24(cards: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (judge-point24 cards)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec judge_point24(Cards :: [integer()]) -> boolean().
judge_point24(Cards) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec judge_point24(cards :: [integer]) :: boolean
  def judge_point24(cards) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func judgePoint24(cards: Array<Int64>): Bool {

    }
}
```

