# LCR 183. 望远镜中最高的海拔

## 题目描述

<p>科技馆内有一台虚拟观景望远镜，它可以用来观测特定纬度地区的地形情况。该纬度的海拔数据记于数组 <code>heights</code> ，其中 <code>heights[i]</code> 表示对应位置的海拔高度。请找出并返回望远镜视野范围 <code>limit</code> 内，可以观测到的最高海拔值。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>heights = [14,2,27,-5,28,13,39], limit = 3
<strong>输出：</strong>[27,27,28,28,39]
<strong>解释：</strong>
  滑动窗口的位置                最大值
---------------               -----
[14 2 27] -5 28 13 39          27
14 [2 27 -5] 28 13 39          27
14 2 [27 -5 28] 13 39          28
14 2 27 [-5 28 13] 39          28
14 2 27 -5 [28 13 39]          39</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p>你可以假设输入总是有效的，在输入数组不为空的情况下：</p>

<ul>
	<li><code>1 &lt;= limit &lt;= heights.length</code></li>
	<li><code>-10000 &lt;= heights[i] &lt;= 10000</code></li>
</ul>

<p>注意：本题与主站 239 题相同：<a href="https://leetcode-cn.com/problems/sliding-window-maximum/">https://leetcode-cn.com/problems/sliding-window-maximum/</a></p>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 队列
- 数组
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 示例

```
[14,2,27,-5,28,13,39]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxAltitude(vector<int>& heights, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maxAltitude(int[] heights, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAltitude(self, heights, limit):
        """
        :type heights: List[int]
        :type limit: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxAltitude(int* heights, int heightsSize, int limit, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaxAltitude(int[] heights, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} heights
 * @param {number} limit
 * @return {number[]}
 */
var maxAltitude = function(heights, limit) {
    
};
```

### TypeScript

```typescript
function maxAltitude(heights: number[], limit: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @param Integer $limit
     * @return Integer[]
     */
    function maxAltitude($heights, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAltitude(_ heights: [Int], _ limit: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAltitude(heights: IntArray, limit: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxAltitude(List<int> heights, int limit) {
    
  }
}
```

### Go

```golang
func maxAltitude(heights []int, limit int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} heights
# @param {Integer} limit
# @return {Integer[]}
def max_altitude(heights, limit)
    
end
```

### Scala

```scala
object Solution {
    def maxAltitude(heights: Array[Int], limit: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_altitude(heights: Vec<i32>, limit: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-altitude heights limit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_altitude(Heights :: [integer()], Limit :: integer()) -> [integer()].
max_altitude(Heights, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_altitude(heights :: [integer], limit :: integer) :: [integer]
  def max_altitude(heights, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAltitude(heights: Array<Int64>, limit: Int64): Array<Int64> {

    }
}
```

