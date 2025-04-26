# 面试题 16.11. 跳水板

## 题目描述

<p>你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为<code>shorter</code>，长度较长的木板长度为<code>longer</code>。你必须正好使用<code>k</code>块木板。编写一个方法，生成跳水板所有可能的长度。</p>

<p>返回的长度需要从小到大排列。</p>

<p><strong>示例 1：</strong></p>

<pre>
<code><strong>输入：</strong>
shorter = 1
longer = 2
k = 3
<strong>输出：</strong>[3,4,5,6]
<strong>解释：</strong>
可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。</code></pre>

<p><strong>提示：</strong></p>

<ul>
	<li>0 &lt; shorter &lt;= longer</li>
	<li>0 &lt;= k &lt;= 100000</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. 考虑制作一个跳水板。你的选择是什么？
2. 考虑递归解法。
3. 一旦有了递归算法，就考虑一下时间复杂度。能快点吗？如何进行？
4.  考虑使用缓存来优化时间复杂度。仔细想想你到底需要缓存什么。时间复杂度是什么？时间复杂度与表的最大尺寸密切相关。
5. 有一个替代的、聪明的（而且非常快速的）解决方案。实际上你可以在线性时间内不用递归求解。如何进行？
6. 这样想：你选择K块木板，其有两种不同的类型。对于第一种木板选择10个、第二种木板选择4个的所有方案，它们的和都是相同的。你能遍历所有可能的选择吗？

## 示例

```
1
1
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> divingBoard(int shorter, int longer, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] divingBoard(int shorter, int longer, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* divingBoard(int shorter, int longer, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] DivingBoard(int shorter, int longer, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} shorter
 * @param {number} longer
 * @param {number} k
 * @return {number[]}
 */
var divingBoard = function(shorter, longer, k) {
    
};
```

### TypeScript

```typescript
function divingBoard(shorter: number, longer: number, k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $shorter
     * @param Integer $longer
     * @param Integer $k
     * @return Integer[]
     */
    function divingBoard($shorter, $longer, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divingBoard(_ shorter: Int, _ longer: Int, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divingBoard(shorter: Int, longer: Int, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> divingBoard(int shorter, int longer, int k) {
    
  }
}
```

### Go

```golang
func divingBoard(shorter int, longer int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} shorter
# @param {Integer} longer
# @param {Integer} k
# @return {Integer[]}
def diving_board(shorter, longer, k)
    
end
```

### Scala

```scala
object Solution {
    def divingBoard(shorter: Int, longer: Int, k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn diving_board(shorter: i32, longer: i32, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (diving-board shorter longer k)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec diving_board(Shorter :: integer(), Longer :: integer(), K :: integer()) -> [integer()].
diving_board(Shorter, Longer, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec diving_board(shorter :: integer, longer :: integer, k :: integer) :: [integer]
  def diving_board(shorter, longer, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divingBoard(shorter: Int64, longer: Int64, k: Int64): Array<Int64> {

    }
}
```

