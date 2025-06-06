# 935. 骑士拨号器

## 题目描述

<p>象棋骑士有一个<strong>独特的移动方式</strong>，它可以垂直移动两个方格，水平移动一个方格，或者水平移动两个方格，垂直移动一个方格(两者都形成一个&nbsp;<strong>L&nbsp;</strong>的形状)。</p>

<p>象棋骑士可能的移动方式如下图所示:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="height: 200px; width: 200px;" /></p>

<p>我们有一个象棋骑士和一个电话垫，如下所示，骑士<strong>只能站在一个数字单元格上</strong>(即蓝色单元格)。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="height: 200px; width: 150px;" /></p>

<p>给定一个整数 n，返回我们可以拨多少个长度为 n 的不同电话号码。</p>

<p>你可以将骑士放置在<strong>任何数字单元格</strong>上，然后你应该执行 n - 1 次移动来获得长度为 n 的号码。所有的跳跃应该是<strong>有效</strong>的骑士跳跃。</p>

<p>因为答案可能很大，<strong>所以输出答案模&nbsp;</strong><code>10<sup>9</sup>&nbsp;+ 7</code>.</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>10
<strong>解释：</strong>我们需要拨一个长度为1的数字，所以把骑士放在10个单元格中的任何一个数字单元格上都能满足条件。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>20
<strong>解释：</strong>我们可以拨打的所有有效号码为[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3131
<strong>输出：</strong>136006598
<strong>解释：</strong>注意取模
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 示例

```
1
2
3131
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int knightDialer(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int knightDialer(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def knightDialer(self, n: int) -> int:
        
```

### C

```c
int knightDialer(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int KnightDialer(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var knightDialer = function(n) {
    
};
```

### TypeScript

```typescript
function knightDialer(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function knightDialer($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func knightDialer(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun knightDialer(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int knightDialer(int n) {
    
  }
}
```

### Go

```golang
func knightDialer(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def knight_dialer(n)
    
end
```

### Scala

```scala
object Solution {
    def knightDialer(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn knight_dialer(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (knight-dialer n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec knight_dialer(N :: integer()) -> integer().
knight_dialer(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec knight_dialer(n :: integer) :: integer
  def knight_dialer(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func knightDialer(n: Int64): Int64 {

    }
}
```

