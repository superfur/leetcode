# 2347. 最好的扑克手牌

## 题目描述

<p>给你一个整数数组&nbsp;<code>ranks</code>&nbsp;和一个字符数组&nbsp;<code>suit</code>&nbsp;。你有&nbsp;<code>5</code>&nbsp;张扑克牌，第&nbsp;<code>i</code>&nbsp;张牌大小为&nbsp;<code>ranks[i]</code>&nbsp;，花色为&nbsp;<code>suits[i]</code>&nbsp;。</p>

<p>下述是从好到坏你可能持有的 <strong>手牌类型&nbsp;</strong>：</p>

<ol>
	<li><code>"Flush"</code>：同花，五张相同花色的扑克牌。</li>
	<li><code>"Three of a Kind"</code>：三条，有 3 张大小相同的扑克牌。</li>
	<li><code>"Pair"</code>：对子，两张大小一样的扑克牌。</li>
	<li><code>"High Card"</code>：高牌，五张大小互不相同的扑克牌。</li>
</ol>

<p>请你返回一个字符串，表示给定的 5 张牌中，你能组成的 <strong>最好手牌类型</strong>&nbsp;。</p>

<p><strong>注意：</strong>返回的字符串&nbsp;<strong>大小写</strong>&nbsp;需与题目描述相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
<b>输出：</b>"Flush"
<b>解释：</b>5 张扑克牌的花色相同，所以返回 "Flush" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
<b>输出：</b>"Three of a Kind"
<b>解释：</b>第一、二和四张牌组成三张相同大小的扑克牌，所以得到 "Three of a Kind" 。
注意我们也可以得到 "Pair" ，但是 "Three of a Kind" 是更好的手牌类型。
有其他的 3 张牌也可以组成 "Three of a Kind" 手牌类型。</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
<b>输出：</b>"Pair"
<b>解释：</b>第一和第二张牌大小相同，所以得到 "Pair" 。
我们无法得到 "Flush" 或者 "Three of a Kind" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>ranks.length == suits.length == 5</code></li>
	<li><code>1 &lt;= ranks[i] &lt;= 13</code></li>
	<li><code>'a' &lt;= suits[i] &lt;= 'd'</code></li>
	<li>任意两张扑克牌不会同时有相同的大小和花色。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Sequentially check the conditions 1 through 4, and return the outcome corresponding to the first met condition.

## 示例

```
[13,2,3,1,9]
["a","a","a","a","a"]
[4,4,2,4,4]
["d","a","a","b","c"]
[10,10,2,12,9]
["a","b","c","a","d"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        
    }
};
```

### Java

```java
class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
```

### C

```c
char* bestHand(int* ranks, int ranksSize, char* suits, int suitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string BestHand(int[] ranks, char[] suits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} ranks
 * @param {character[]} suits
 * @return {string}
 */
var bestHand = function(ranks, suits) {
    
};
```

### TypeScript

```typescript
function bestHand(ranks: number[], suits: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $ranks
     * @param String[] $suits
     * @return String
     */
    function bestHand($ranks, $suits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestHand(_ ranks: [Int], _ suits: [Character]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestHand(ranks: IntArray, suits: CharArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String bestHand(List<int> ranks, List<String> suits) {
    
  }
}
```

### Go

```golang
func bestHand(ranks []int, suits []byte) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} ranks
# @param {Character[]} suits
# @return {String}
def best_hand(ranks, suits)
    
end
```

### Scala

```scala
object Solution {
    def bestHand(ranks: Array[Int], suits: Array[Char]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_hand(ranks: Vec<i32>, suits: Vec<char>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (best-hand ranks suits)
  (-> (listof exact-integer?) (listof char?) string?)
  )
```

### Erlang

```erlang
-spec best_hand(Ranks :: [integer()], Suits :: [char()]) -> unicode:unicode_binary().
best_hand(Ranks, Suits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_hand(ranks :: [integer], suits :: [char]) :: String.t
  def best_hand(ranks, suits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestHand(ranks: Array<Int64>, suits: Array<Rune>): String {

    }
}
```

