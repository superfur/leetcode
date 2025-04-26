# 3492. 船上可以装载的最大集装箱数量

## 题目描述

<p>给你一个正整数 <code>n</code>，表示船上的一个 <code>n x n</code> 的货物甲板。甲板上的每个单元格可以装载一个重量<strong> 恰好 </strong>为 <code>w</code> 的集装箱。</p>

<p>然而，如果将所有集装箱装载到甲板上，其总重量不能超过船的最大承载重量 <code>maxWeight</code>。</p>

<p>请返回可以装载到船上的 <strong>最大 </strong>集装箱数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 2, w = 3, maxWeight = 15</span></p>

<p><strong>输出：</strong> 4</p>

<p><strong>解释：</strong></p>

<p>甲板有 4 个单元格，每个集装箱的重量为 3。将所有集装箱装载后，总重量为 12，未超过 <code>maxWeight</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 3, w = 5, maxWeight = 20</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>甲板有 9 个单元格，每个集装箱的重量为 5。可以装载的最大集装箱数量为 4，此时总重量不超过 <code>maxWeight</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= w &lt;= 1000</code></li>
	<li><code>1 &lt;= maxWeight &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. What are the limits on the number of containers?
2. We can load at most <code>min(n * n, maxWeight / w)</code> containers.

## 示例

```
2
3
15
3
5
20
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxContainers(int n, int w, int maxWeight) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        
```

### C

```c
int maxContainers(int n, int w, int maxWeight) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxContainers(int n, int w, int maxWeight) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} w
 * @param {number} maxWeight
 * @return {number}
 */
var maxContainers = function(n, w, maxWeight) {
    
};
```

### TypeScript

```typescript
function maxContainers(n: number, w: number, maxWeight: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $w
     * @param Integer $maxWeight
     * @return Integer
     */
    function maxContainers($n, $w, $maxWeight) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxContainers(_ n: Int, _ w: Int, _ maxWeight: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxContainers(n: Int, w: Int, maxWeight: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxContainers(int n, int w, int maxWeight) {
    
  }
}
```

### Go

```golang
func maxContainers(n int, w int, maxWeight int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} w
# @param {Integer} max_weight
# @return {Integer}
def max_containers(n, w, max_weight)
    
end
```

### Scala

```scala
object Solution {
    def maxContainers(n: Int, w: Int, maxWeight: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_containers(n: i32, w: i32, max_weight: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-containers n w maxWeight)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_containers(N :: integer(), W :: integer(), MaxWeight :: integer()) -> integer().
max_containers(N, W, MaxWeight) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_containers(n :: integer, w :: integer, max_weight :: integer) :: integer
  def max_containers(n, w, max_weight) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxContainers(n: Int64, w: Int64, maxWeight: Int64): Int64 {

    }
}
```

