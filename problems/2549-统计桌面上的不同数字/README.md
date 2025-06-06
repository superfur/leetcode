# 2549. 统计桌面上的不同数字

## 题目描述

<p>给你一个正整数 <code>n</code> ，开始时，它放在桌面上。在 <code>10<sup>9</sup></code> 天内，每天都要执行下述步骤：</p>

<ul>
	<li>对于出现在桌面上的每个数字 <code>x</code> ，找出符合 <code>1 &lt;= i &lt;= n</code> 且满足 <code>x % i == 1</code> 的所有数字 <code>i</code> 。</li>
	<li>然后，将这些数字放在桌面上。</li>
</ul>

<p>返回在 <code>10<sup>9</sup></code> 天之后，出现在桌面上的 <strong>不同</strong> 整数的数目。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>一旦数字放在桌面上，则会一直保留直到结束。</li>
	<li><code>%</code> 表示取余运算。例如，<code>14 % 3</code> 等于 <code>2</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>4
<strong>解释：</strong>最开始，5 在桌面上。 
第二天，2 和 4 也出现在桌面上，因为 5 % 2 == 1 且 5 % 4 == 1 。 
再过一天 3 也出现在桌面上，因为 4 % 3 == 1 。 
在十亿天结束时，桌面上的不同数字有 2 、3 、4 、5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3 
<strong>输出：</strong>2
<strong>解释：</strong> 
因为 3 % 2 == 1 ，2 也出现在桌面上。 
在十亿天结束时，桌面上的不同数字只有两个：2 和 3 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 数学
- 模拟

## 提示

1. For n > 2, n % (n - 1) == 1 thus n - 1 will be added on the board the next day.
2. As the operations are performed for so long time, all the numbers lesser than n except 1 will be added to the board.
3. What will happen if n == 1?

## 示例

```
5
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distinctIntegers(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int distinctIntegers(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distinctIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distinctIntegers(self, n: int) -> int:
        
```

### C

```c
int distinctIntegers(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistinctIntegers(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var distinctIntegers = function(n) {
    
};
```

### TypeScript

```typescript
function distinctIntegers(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function distinctIntegers($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distinctIntegers(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distinctIntegers(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distinctIntegers(int n) {
    
  }
}
```

### Go

```golang
func distinctIntegers(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def distinct_integers(n)
    
end
```

### Scala

```scala
object Solution {
    def distinctIntegers(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distinct_integers(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distinct-integers n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distinct_integers(N :: integer()) -> integer().
distinct_integers(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distinct_integers(n :: integer) :: integer
  def distinct_integers(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distinctIntegers(n: Int64): Int64 {

    }
}
```

