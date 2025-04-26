# LCR 166. 珠宝的最高价值

## 题目描述

<p>现有一个记作二维矩阵 <code>frame</code> 的珠宝架，其中 <code>frame[i][j]</code> 为该位置珠宝的价值。拿取珠宝的规则为：</p>

<ul>
	<li>只能从架子的左上角开始拿珠宝</li>
	<li>每次可以移动到右侧或下侧的相邻位置</li>
	<li>到达珠宝架子的右下角时，停止拿取</li>
</ul>

<p>注意：珠宝的价值都是大于 0 的。除非这个架子上没有任何珠宝，比如 <code>frame = [[0]]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>frame = [[1,3,1],[1,5,1],[4,2,1]]
<strong>输出：</strong><code>12
</code><strong>解释：</strong>路径 1→3→5→2→1 可以拿到最高价值的珠宝</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt; frame.length &lt;= 200</code></li>
	<li><code>0 &lt; frame[0].length &lt;= 200</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 示例

```
[[1,3,1],[1,5,1],[4,2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int jewelleryValue(vector<vector<int>>& frame) {
        
    }
};
```

### Java

```java
class Solution {
    public int jewelleryValue(int[][] frame) {
        
    }
}
```

### Python

```python
class Solution(object):
    def jewelleryValue(self, frame):
        """
        :type frame: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        
```

### C

```c
int jewelleryValue(int** frame, int frameSize, int* frameColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int JewelleryValue(int[][] frame) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} frame
 * @return {number}
 */
var jewelleryValue = function(frame) {
    
};
```

### TypeScript

```typescript
function jewelleryValue(frame: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $frame
     * @return Integer
     */
    function jewelleryValue($frame) {
        
    }
}
```

### Swift

```swift
class Solution {
    func jewelleryValue(_ frame: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun jewelleryValue(frame: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int jewelleryValue(List<List<int>> frame) {
    
  }
}
```

### Go

```golang
func jewelleryValue(frame [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} frame
# @return {Integer}
def jewellery_value(frame)
    
end
```

### Scala

```scala
object Solution {
    def jewelleryValue(frame: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn jewellery_value(frame: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (jewellery-value frame)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec jewellery_value(Frame :: [[integer()]]) -> integer().
jewellery_value(Frame) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec jewellery_value(frame :: [[integer]]) :: integer
  def jewellery_value(frame) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func jewelleryValue(frame: Array<Array<Int64>>): Int64 {

    }
}
```

