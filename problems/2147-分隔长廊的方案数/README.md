# 2147. 分隔长廊的方案数

## 题目描述

<p>在一个图书馆的长廊里，有一些座位和装饰植物排成一列。给你一个下标从 <strong>0</strong>&nbsp;开始，长度为 <code>n</code>&nbsp;的字符串&nbsp;<code>corridor</code>&nbsp;，它包含字母&nbsp;<code>'S'</code> 和&nbsp;<code>'P'</code>&nbsp;，其中每个&nbsp;<code>'S'</code>&nbsp;表示一个座位，每个&nbsp;<code>'P'</code>&nbsp;表示一株植物。</p>

<p>在下标 <code>0</code>&nbsp;的左边和下标 <code>n - 1</code>&nbsp;的右边 <strong>已经</strong>&nbsp;分别各放了一个屏风。你还需要额外放置一些屏风。每一个位置&nbsp;<code>i - 1</code> 和&nbsp;<code>i</code>&nbsp;之间（<code>1 &lt;= i &lt;= n - 1</code>），至多能放一个屏风。</p>

<p>请你将走廊用屏风划分为若干段，且每一段内都 <strong>恰好有两个座位</strong>&nbsp;，而每一段内植物的数目没有要求。可能有多种划分方案，如果两个方案中有任何一个屏风的位置不同，那么它们被视为 <strong>不同</strong> 方案。</p>

<p>请你返回划分走廊的方案数。由于答案可能很大，请你返回它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;的结果。如果没有任何方案，请返回&nbsp;<code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/1.png" style="width: 410px; height: 199px;"></p>

<pre><b>输入：</b>corridor = "SSPPSPS"
<b>输出：</b>3
<b>解释：</b>总共有 3 种不同分隔走廊的方案。
上图中黑色的竖线表示已经放置好的屏风。
上图每种方案中，每一段都恰好有 <strong>两个</strong>&nbsp;座位。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/2.png" style="width: 357px; height: 68px;"></p>

<pre><b>输入：</b>corridor = "PPSPSP"
<b>输出：</b>1
<b>解释：</b>只有 1 种分隔走廊的方案，就是不放置任何屏风。
放置任何的屏风都会导致有一段无法恰好有 2 个座位。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/12/3.png" style="width: 115px; height: 68px;"></p>

<pre><b>输入：</b>corridor = "S"
<b>输出：</b>0
<b>解释：</b>没有任何方案，因为总是有一段无法恰好有 2 个座位。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == corridor.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>corridor[i]</code>&nbsp;要么是&nbsp;<code>'S'</code>&nbsp;，要么是&nbsp;<code>'P'</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 动态规划

## 提示

1. Divide the corridor into segments. Each segment has two seats, starts precisely with one seat, and ends precisely with the other seat.
2. How many dividers can you install between two adjacent segments? You must install precisely one. Otherwise, you would have created a section with not exactly two seats.
3. If there are k plants between two adjacent segments, there are k + 1 positions (ways) you could install the divider you must install.
4. The problem now becomes: Find the product of all possible positions between every two adjacent segments.

## 示例

```
"SSPPSPS"
"PPSPSP"
"S"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfWays(string corridor) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfWays(String corridor) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
```

### C

```c
int numberOfWays(char* corridor) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfWays(string corridor) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function(corridor) {
    
};
```

### TypeScript

```typescript
function numberOfWays(corridor: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $corridor
     * @return Integer
     */
    function numberOfWays($corridor) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWays(_ corridor: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWays(corridor: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWays(String corridor) {
    
  }
}
```

### Go

```golang
func numberOfWays(corridor string) int {
    
}
```

### Ruby

```ruby
# @param {String} corridor
# @return {Integer}
def number_of_ways(corridor)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWays(corridor: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-ways corridor)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_ways(Corridor :: unicode:unicode_binary()) -> integer().
number_of_ways(Corridor) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(corridor :: String.t) :: integer
  def number_of_ways(corridor) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWays(corridor: String): Int64 {

    }
}
```

