# 464. 我能赢吗

## 题目描述

<p>在 "100 game" 这个游戏中，两名玩家轮流选择从 <code>1</code> 到 <code>10</code> 的任意整数，累计整数和，先使得累计整数和 <strong>达到或超过</strong>&nbsp; 100 的玩家，即为胜者。</p>

<p>如果我们将游戏规则改为 “玩家 <strong>不能</strong> 重复使用整数” 呢？</p>

<p>例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 &gt;= 100。</p>

<p>给定两个整数&nbsp;<code>maxChoosableInteger</code>&nbsp;（整数池中可选择的最大数）和&nbsp;<code>desiredTotal</code>（累计和），若先出手的玩家能稳赢则返回 <code>true</code>&nbsp;，否则返回 <code>false</code> 。假设两位玩家游戏时都表现 <strong>最佳</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>maxChoosableInteger = 10, desiredTotal = 11
<strong>输出：</strong>false
<strong>解释：
</strong>无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 &gt;= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>maxChoosableInteger = 10, desiredTotal = 0
<b>输出：</b>true
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入：</strong>maxChoosableInteger = 10, desiredTotal = 1
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= maxChoosableInteger &lt;= 20</code></li>
	<li><code>0 &lt;= desiredTotal &lt;= 300</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 记忆化搜索
- 数学
- 动态规划
- 状态压缩
- 博弈

## 示例

```
10
11
10
0
10
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
```

### C

```c
bool canIWin(int maxChoosableInteger, int desiredTotal) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanIWin(int maxChoosableInteger, int desiredTotal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} maxChoosableInteger
 * @param {number} desiredTotal
 * @return {boolean}
 */
var canIWin = function(maxChoosableInteger, desiredTotal) {
    
};
```

### TypeScript

```typescript
function canIWin(maxChoosableInteger: number, desiredTotal: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $maxChoosableInteger
     * @param Integer $desiredTotal
     * @return Boolean
     */
    function canIWin($maxChoosableInteger, $desiredTotal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canIWin(int maxChoosableInteger, int desiredTotal) {
    
  }
}
```

### Go

```golang
func canIWin(maxChoosableInteger int, desiredTotal int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} max_choosable_integer
# @param {Integer} desired_total
# @return {Boolean}
def can_i_win(max_choosable_integer, desired_total)
    
end
```

### Scala

```scala
object Solution {
    def canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_i_win(max_choosable_integer: i32, desired_total: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-i-win maxChoosableInteger desiredTotal)
  (-> exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_i_win(MaxChoosableInteger :: integer(), DesiredTotal :: integer()) -> boolean().
can_i_win(MaxChoosableInteger, DesiredTotal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_i_win(max_choosable_integer :: integer, desired_total :: integer) :: boolean
  def can_i_win(max_choosable_integer, desired_total) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canIWin(maxChoosableInteger: Int64, desiredTotal: Int64): Bool {

    }
}
```

