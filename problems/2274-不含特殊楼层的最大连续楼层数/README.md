# 2274. 不含特殊楼层的最大连续楼层数

## 题目描述

<p>Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 <strong>特殊楼层</strong> ，仅用于放松。</p>

<p>给你两个整数 <code>bottom</code> 和 <code>top</code> ，表示 Alice 租用了从 <code>bottom</code> 到 <code>top</code>（含 <code>bottom</code> 和 <code>top</code> 在内）的所有楼层。另给你一个整数数组 <code>special</code> ，其中 <code>special[i]</code> 表示&nbsp; Alice 指定用于放松的特殊楼层。</p>

<p>返回不含特殊楼层的 <strong>最大</strong> 连续楼层数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>bottom = 2, top = 9, special = [4,6]
<strong>输出：</strong>3
<strong>解释：</strong>下面列出的是不含特殊楼层的连续楼层范围：
- (2, 3) ，楼层数为 2 。
- (5, 5) ，楼层数为 1 。
- (7, 9) ，楼层数为 3 。
因此，返回最大连续楼层数 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>bottom = 6, top = 8, special = [7,6,8]
<strong>输出：</strong>0
<strong>解释：</strong>每层楼都被规划为特殊楼层，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示</strong></p>

<ul>
	<li><code>1 &lt;= special.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= bottom &lt;= special[i] &lt;= top &lt;= 10<sup>9</sup></code></li>
	<li><code>special</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 提示

1. Say we have a pair of special floors (x, y) with no other special floors in between. There are x - y - 1 consecutive floors in between them without a special floor.
2. Say there are n special floors. After sorting special, we have answer = max(answer, special[i] – special[i – 1] – 1) for all 0 < i < n.
3. However, there are two special cases left to consider: the floors before special[0] and after special[n-1].
4. To consider these cases, we have answer = max(answer, special[0] – bottom, top – special[n-1]).

## 示例

```
2
9
[4,6]
6
8
[7,6,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
```

### C

```c
int maxConsecutive(int bottom, int top, int* special, int specialSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxConsecutive(int bottom, int top, int[] special) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} bottom
 * @param {number} top
 * @param {number[]} special
 * @return {number}
 */
var maxConsecutive = function(bottom, top, special) {
    
};
```

### TypeScript

```typescript
function maxConsecutive(bottom: number, top: number, special: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $bottom
     * @param Integer $top
     * @param Integer[] $special
     * @return Integer
     */
    function maxConsecutive($bottom, $top, $special) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxConsecutive(_ bottom: Int, _ top: Int, _ special: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxConsecutive(bottom: Int, top: Int, special: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxConsecutive(int bottom, int top, List<int> special) {
    
  }
}
```

### Go

```golang
func maxConsecutive(bottom int, top int, special []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} bottom
# @param {Integer} top
# @param {Integer[]} special
# @return {Integer}
def max_consecutive(bottom, top, special)
    
end
```

### Scala

```scala
object Solution {
    def maxConsecutive(bottom: Int, top: Int, special: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_consecutive(bottom: i32, top: i32, special: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-consecutive bottom top special)
  (-> exact-integer? exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_consecutive(Bottom :: integer(), Top :: integer(), Special :: [integer()]) -> integer().
max_consecutive(Bottom, Top, Special) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_consecutive(bottom :: integer, top :: integer, special :: [integer]) :: integer
  def max_consecutive(bottom, top, special) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxConsecutive(bottom: Int64, top: Int64, special: Array<Int64>): Int64 {

    }
}
```

