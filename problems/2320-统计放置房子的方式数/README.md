# 2320. 统计放置房子的方式数

## 题目描述

<p>一条街道上共有 <code>n * 2</code> 个 <strong>地块</strong> ，街道的两侧各有 <code>n</code> 个地块。每一边的地块都按从 <code>1</code> 到 <code>n</code> 编号。每个地块上都可以放置一所房子。</p>

<p>现要求街道同一侧不能存在两所房子相邻的情况，请你计算并返回放置房屋的方式数目。由于答案可能很大，需要对 <code>10<sup>9</sup> + 7</code> 取余后再返回。</p>

<p>注意，如果一所房子放置在这条街某一侧上的第 <code>i</code> 个地块，不影响在另一侧的第 <code>i</code> 个地块放置房子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>4
<strong>解释：</strong>
可能的放置方式：
1. 所有地块都不放置房子。
2. 一所房子放在街道的某一侧。
3. 一所房子放在街道的另一侧。
4. 放置两所房子，街道两侧各放置一所。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/12/arrangements.png" style="width: 500px; height: 500px;">
<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>9
<strong>解释：</strong>如上图所示，共有 9 种可能的放置方式。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 提示

1. Try coming up with a DP solution for one side of the street.
2. The DP for one side of the street will bear resemblance to the Fibonacci sequence.
3. The number of different arrangements on both side of the street is the same.

## 示例

```
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countHousePlacements(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countHousePlacements(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countHousePlacements(self, n: int) -> int:
        
```

### C

```c
int countHousePlacements(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountHousePlacements(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countHousePlacements = function(n) {
    
};
```

### TypeScript

```typescript
function countHousePlacements(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countHousePlacements($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countHousePlacements(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countHousePlacements(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countHousePlacements(int n) {
    
  }
}
```

### Go

```golang
func countHousePlacements(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_house_placements(n)
    
end
```

### Scala

```scala
object Solution {
    def countHousePlacements(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_house_placements(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-house-placements n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_house_placements(N :: integer()) -> integer().
count_house_placements(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_house_placements(n :: integer) :: integer
  def count_house_placements(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countHousePlacements(n: Int64): Int64 {

    }
}
```

