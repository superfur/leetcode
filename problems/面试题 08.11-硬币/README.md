# 面试题 08.11. 硬币

## 题目描述

<p>硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入：</strong>n = 5
<strong> 输出：</strong>2
<strong> 解释：</strong>有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入：</strong>n = 10
<strong> 输出</strong>：4
<strong> 解释：</strong>有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
</pre>

<p><strong>说明：</strong></p>

<p>注意:</p>

<p>你可以假设：</p>

<ul>
	<li>0 &lt;= n (总金额) &lt;= 1000000</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划

## 提示

1. 试着把它分解成子问题。如果你在做改变，第一选择是什么？
2. 如果你正在进行换零操作，不妨从决定需要多少个币值为25分的硬币开始。
3. 一旦你决定用两个25分兑换98分，就需要弄清楚用5分、10分和1分兑换 48分有多少种方式。
4. 分析你的算法。有重复性的工作吗？你能优化它吗？
5. 试试制表法。

## 示例

```
5
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToChange(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToChange(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToChange(self, n: int) -> int:
        
```

### C

```c
int waysToChange(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToChange(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var waysToChange = function(n) {
    
};
```

### TypeScript

```typescript
function waysToChange(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function waysToChange($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToChange(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToChange(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToChange(int n) {
    
  }
}
```

### Go

```golang
func waysToChange(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def ways_to_change(n)
    
end
```

### Scala

```scala
object Solution {
    def waysToChange(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_change(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-change n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_change(N :: integer()) -> integer().
ways_to_change(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_change(n :: integer) :: integer
  def ways_to_change(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToChange(n: Int64): Int64 {

    }
}
```

