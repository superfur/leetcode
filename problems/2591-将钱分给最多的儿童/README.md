# 2591. 将钱分给最多的儿童

## 题目描述

<p>给你一个整数&nbsp;<code>money</code>&nbsp;，表示你总共有的钱数（单位为美元）和另一个整数&nbsp;<code>children</code>&nbsp;，表示你要将钱分配给多少个儿童。</p>

<p>你需要按照如下规则分配：</p>

<ul>
	<li>所有的钱都必须被分配。</li>
	<li>每个儿童至少获得&nbsp;<code>1</code>&nbsp;美元。</li>
	<li>没有人获得 <code>4</code>&nbsp;美元。</li>
</ul>

<p>请你按照上述规则分配金钱，并返回 <strong>最多</strong>&nbsp;有多少个儿童获得 <strong>恰好</strong><em>&nbsp;</em><code>8</code>&nbsp;美元。如果没有任何分配方案，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>money = 20, children = 3
<b>输出：</b>1
<b>解释：</b>
最多获得 8 美元的儿童数为 1 。一种分配方案为：
- 给第一个儿童分配 8 美元。
- 给第二个儿童分配 9 美元。
- 给第三个儿童分配 3 美元。
没有分配方案能让获得 8 美元的儿童数超过 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>money = 16, children = 2
<b>输出：</b>2
<b>解释：</b>每个儿童都可以获得 8 美元。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= money &lt;= 200</code></li>
	<li><code>2 &lt;= children &lt;= 30</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学

## 提示

1. Can we distribute the money according to the rules if we give 'k' children exactly 8 dollars?
2. Brute force to find the largest possible value of k, or return -1 if there doesn’t exist any such k.

## 示例

```
20
3
16
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distMoney(int money, int children) {
        
    }
};
```

### Java

```java
class Solution {
    public int distMoney(int money, int children) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
```

### C

```c
int distMoney(int money, int children) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistMoney(int money, int children) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} money
 * @param {number} children
 * @return {number}
 */
var distMoney = function(money, children) {
    
};
```

### TypeScript

```typescript
function distMoney(money: number, children: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $money
     * @param Integer $children
     * @return Integer
     */
    function distMoney($money, $children) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distMoney(_ money: Int, _ children: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distMoney(money: Int, children: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distMoney(int money, int children) {
    
  }
}
```

### Go

```golang
func distMoney(money int, children int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} money
# @param {Integer} children
# @return {Integer}
def dist_money(money, children)
    
end
```

### Scala

```scala
object Solution {
    def distMoney(money: Int, children: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dist_money(money: i32, children: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (dist-money money children)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec dist_money(Money :: integer(), Children :: integer()) -> integer().
dist_money(Money, Children) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dist_money(money :: integer, children :: integer) :: integer
  def dist_money(money, children) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distMoney(money: Int64, children: Int64): Int64 {

    }
}
```

