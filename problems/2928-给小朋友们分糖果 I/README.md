# 2928. 给小朋友们分糖果 I

## 题目描述

<p>给你两个正整数&nbsp;<code>n</code> 和&nbsp;<code>limit</code>&nbsp;。</p>

<p>请你将 <code>n</code>&nbsp;颗糖果分给 <code>3</code>&nbsp;位小朋友，确保没有任何小朋友得到超过 <code>limit</code>&nbsp;颗糖果，请你返回满足此条件下的&nbsp;<strong>总方案数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 5, limit = 2
<b>输出：</b>3
<b>解释：</b>总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, limit = 3
<b>输出：</b>10
<b>解释：</b>总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= limit &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 组合数学
- 枚举

## 提示

1. Use three nested for loops to check all the triplets.

## 示例

```
5
2
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distributeCandies(int n, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int distributeCandies(int n, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
```

### C

```c
int distributeCandies(int n, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistributeCandies(int n, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function(n, limit) {
    
};
```

### TypeScript

```typescript
function distributeCandies(n: number, limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $limit
     * @return Integer
     */
    function distributeCandies($n, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distributeCandies(_ n: Int, _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distributeCandies(n: Int, limit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distributeCandies(int n, int limit) {
    
  }
}
```

### Go

```golang
func distributeCandies(n int, limit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
    
end
```

### Scala

```scala
object Solution {
    def distributeCandies(n: Int, limit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distribute-candies n limit)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distribute_candies(N :: integer(), Limit :: integer()) -> integer().
distribute_candies(N, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(n :: integer, limit :: integer) :: integer
  def distribute_candies(n, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distributeCandies(n: Int64, limit: Int64): Int64 {

    }
}
```

