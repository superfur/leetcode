# 1716. 计算力扣银行的钱

## 题目描述

<p>Hercy 想要为购买第一辆车存钱。他 <strong>每天</strong> 都往力扣银行里存钱。</p>

<p>最开始，他在周一的时候存入 <code>1</code> 块钱。从周二到周日，他每天都比前一天多存入 <code>1</code> 块钱。在接下来每一个周一，他都会比 <strong>前一个周一</strong> 多存入 <code>1</code> 块钱。<span style=""> </span></p>

<p>给你 <code>n</code> ，请你返回在第 <code>n</code> 天结束的时候他在力扣银行总共存了多少块钱。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 4
<b>输出：</b>10
<b>解释：</b>第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 10
<b>输出：</b>37
<b>解释：</b>第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>n = 20
<b>输出：</b>96
<b>解释：</b>第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Simulate the process by keeping track of how much money Hercy is putting in and which day of the week it is, and use this information to deduce how much money Hercy will put in the next day.

## 示例

```
4
10
20
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalMoney(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalMoney(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalMoney(self, n: int) -> int:
        
```

### C

```c
int totalMoney(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalMoney(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    
};
```

### TypeScript

```typescript
function totalMoney(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalMoney(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalMoney(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalMoney(int n) {
    
  }
}
```

### Go

```golang
func totalMoney(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def total_money(n)
    
end
```

### Scala

```scala
object Solution {
    def totalMoney(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_money(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-money n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec total_money(N :: integer()) -> integer().
total_money(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_money(n :: integer) :: integer
  def total_money(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalMoney(n: Int64): Int64 {

    }
}
```

