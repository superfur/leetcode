# 1688. 比赛中的配对次数

## 题目描述

<p>给你一个整数 <code>n</code> ，表示比赛中的队伍数。比赛遵循一种独特的赛制：</p>

<ul>
	<li>如果当前队伍数是 <strong>偶数</strong> ，那么每支队伍都会与另一支队伍配对。总共进行 <code>n / 2</code> 场比赛，且产生 <code>n / 2</code> 支队伍进入下一轮。</li>
	<li>如果当前队伍数为 <strong>奇数</strong> ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 <code>(n - 1) / 2</code> 场比赛，且产生 <code>(n - 1) / 2 + 1</code> 支队伍进入下一轮。</li>
</ul>

<p>返回在比赛中进行的配对次数，直到决出获胜队伍为止。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 7
<strong>输出：</strong>6
<strong>解释：</strong>比赛详情：
- 第 1 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。
- 第 2 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
- 第 3 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
总配对次数 = 3 + 2 + 1 = 6
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 14
<strong>输出：</strong>13
<strong>解释：</strong>比赛详情：
- 第 1 轮：队伍数 = 14 ，配对次数 = 7 ，7 支队伍晋级。
- 第 2 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。 
- 第 3 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
- 第 4 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
总配对次数 = 7 + 3 + 2 + 1 = 13
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 200</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Simulate the tournament as given in the statement.
2. Be careful when handling odd integers.

## 示例

```
7
14
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfMatches(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfMatches(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfMatches(self, n: int) -> int:
        
```

### C

```c
int numberOfMatches(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfMatches(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numberOfMatches = function(n) {
    
};
```

### TypeScript

```typescript
function numberOfMatches(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numberOfMatches($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfMatches(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfMatches(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfMatches(int n) {
    
  }
}
```

### Go

```golang
func numberOfMatches(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def number_of_matches(n)
    
end
```

### Scala

```scala
object Solution {
    def numberOfMatches(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_matches(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-matches n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_matches(N :: integer()) -> integer().
number_of_matches(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_matches(n :: integer) :: integer
  def number_of_matches(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfMatches(n: Int64): Int64 {

    }
}
```

