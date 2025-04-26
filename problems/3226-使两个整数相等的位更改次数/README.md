# 3226. 使两个整数相等的位更改次数

## 题目描述

<p>给你两个正整数 <code>n</code> 和 <code>k</code>。</p>

<p>你可以选择 <code>n</code> 的 <strong>二进制表示</strong> 中任意一个值为 1 的位，并将其改为 0。</p>

<p>返回使得 <code>n</code> 等于 <code>k</code> 所需要的更改次数。如果无法实现，返回 -1。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 13, k = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong><br />
最初，<code>n</code> 和 <code>k</code> 的二进制表示分别为 <code>n = (1101)<sub>2</sub></code> 和 <code>k = (0100)<sub>2</sub></code>，</p>

<p>我们可以改变 <code>n</code> 的第一位和第四位。结果整数为 <code>n = (<u><strong>0</strong></u>10<u><strong>0</strong></u>)<sub>2</sub> = k</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 21, k = 21</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong><br />
<code>n</code> 和 <code>k</code> 已经相等，因此不需要更改。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 14, k = 13</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong><br />
无法使 <code>n</code> 等于 <code>k</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 位运算

## 提示

1. Find the binary representations of <code>n</code> and <code>k</code>.
2. Any bit that is equal to 1 in <code>n</code> and equal to 0 in <code>k</code> needs to be changed.

## 示例

```
13
4
21
21
14
13
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minChanges(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minChanges(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
```

### C

```c
int minChanges(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinChanges(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var minChanges = function(n, k) {
    
};
```

### TypeScript

```typescript
function minChanges(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function minChanges($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minChanges(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minChanges(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minChanges(int n, int k) {
    
  }
}
```

### Go

```golang
func minChanges(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def min_changes(n, k)
    
end
```

### Scala

```scala
object Solution {
    def minChanges(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_changes(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-changes n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_changes(N :: integer(), K :: integer()) -> integer().
min_changes(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_changes(n :: integer, k :: integer) :: integer
  def min_changes(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minChanges(n: Int64, k: Int64): Int64 {

    }
}
```

