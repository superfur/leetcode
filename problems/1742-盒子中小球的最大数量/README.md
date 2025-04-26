# 1742. 盒子中小球的最大数量

## 题目描述

<p>你在一家生产小球的玩具厂工作，有 <code>n</code> 个小球，编号从 <code>lowLimit</code> 开始，到 <code>highLimit</code> 结束（包括 <code>lowLimit</code> 和 <code>highLimit</code> ，即 <code>n == highLimit - lowLimit + 1</code>）。另有无限数量的盒子，编号从 <code>1</code> 到 <code>infinity</code> 。</p>

<p>你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 <code>321</code> 的小球应当放入编号 <code>3 + 2 + 1 = 6</code> 的盒子，而编号 <code>10</code> 的小球应当放入编号 <code>1 + 0 = 1</code> 的盒子。</p>

<p>给你两个整数 <code>lowLimit</code> 和 <code>highLimit</code> ，返回放有最多小球的盒子中的小球数量<em>。</em>如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>lowLimit = 1, highLimit = 10
<strong>输出：</strong>2
<strong>解释：</strong>
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
编号 1 的盒子放有最多小球，小球数量为 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>lowLimit = 5, highLimit = 15
<strong>输出：</strong>2
<strong>解释：</strong>
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>lowLimit = 19, highLimit = 28
<strong>输出：</strong>2
<strong>解释：</strong>
盒子编号：1 2 3 4 5 6 7 8 9 10 11 12 ...
小球数量：0 1 1 1 1 1 1 1 1 2  0  0  ...
编号 10 的盒子放有最多小球，小球数量为 2 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= lowLimit <= highLimit <= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 数学
- 计数

## 提示

1. Note that both lowLimit and highLimit are of small constraints so you can iterate on all number between them
2. You can simulate the boxes by counting for each box the number of balls with digit sum equal to that box number

## 示例

```
1
10
5
15
19
28
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        
    }
};
```

### Java

```java
class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
```

### C

```c
int countBalls(int lowLimit, int highLimit) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountBalls(int lowLimit, int highLimit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} lowLimit
 * @param {number} highLimit
 * @return {number}
 */
var countBalls = function(lowLimit, highLimit) {
    
};
```

### TypeScript

```typescript
function countBalls(lowLimit: number, highLimit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $lowLimit
     * @param Integer $highLimit
     * @return Integer
     */
    function countBalls($lowLimit, $highLimit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBalls(_ lowLimit: Int, _ highLimit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBalls(lowLimit: Int, highLimit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countBalls(int lowLimit, int highLimit) {
    
  }
}
```

### Go

```golang
func countBalls(lowLimit int, highLimit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} low_limit
# @param {Integer} high_limit
# @return {Integer}
def count_balls(low_limit, high_limit)
    
end
```

### Scala

```scala
object Solution {
    def countBalls(lowLimit: Int, highLimit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_balls(low_limit: i32, high_limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-balls lowLimit highLimit)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_balls(LowLimit :: integer(), HighLimit :: integer()) -> integer().
count_balls(LowLimit, HighLimit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_balls(low_limit :: integer, high_limit :: integer) :: integer
  def count_balls(low_limit, high_limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBalls(lowLimit: Int64, highLimit: Int64): Int64 {

    }
}
```

