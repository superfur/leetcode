# 390. 消除游戏

## 题目描述

<p>列表 <code>arr</code> 由在范围 <code>[1, n]</code> 中的所有整数组成，并按严格递增排序。请你对 <code>arr</code> 应用下述算法：</p>

<div class="original__bRMd">
<div>
<ul>
	<li>从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。</li>
	<li>重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。</li>
	<li>不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。</li>
</ul>

<p>给你整数 <code>n</code> ，返回 <code>arr</code> 最后剩下的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 9
<strong>输出：</strong>6
<strong>解释：</strong>
arr = [<strong><em>1</em></strong>, 2, <em><strong>3</strong></em>, 4, <em><strong>5</strong></em>, 6, <em><strong>7</strong></em>, 8, <em><strong>9</strong></em>]
arr = [2, <em><strong>4</strong></em>, 6, <em><strong>8</strong></em>]
arr = [<em><strong>2</strong></em>, 6]
arr = [6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 递归
- 数学

## 示例

```
9
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lastRemaining(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int lastRemaining(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lastRemaining(self, n: int) -> int:
        
```

### C

```c
int lastRemaining(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int LastRemaining(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function(n) {
    
};
```

### TypeScript

```typescript
function lastRemaining(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function lastRemaining($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lastRemaining(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lastRemaining(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lastRemaining(int n) {
    
  }
}
```

### Go

```golang
func lastRemaining(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def last_remaining(n)
    
end
```

### Scala

```scala
object Solution {
    def lastRemaining(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn last_remaining(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (last-remaining n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec last_remaining(N :: integer()) -> integer().
last_remaining(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec last_remaining(n :: integer) :: integer
  def last_remaining(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lastRemaining(n: Int64): Int64 {

    }
}
```

