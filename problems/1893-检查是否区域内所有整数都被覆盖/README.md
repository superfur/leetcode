# 1893. 检查是否区域内所有整数都被覆盖

## 题目描述

<p>给你一个二维整数数组 <code>ranges</code> 和两个整数 <code>left</code> 和 <code>right</code> 。每个 <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示一个从 <code>start<sub>i</sub></code> 到 <code>end<sub>i</sub></code> 的 <strong>闭区间</strong> 。</p>

<p>如果闭区间 <code>[left, right]</code> 内每个整数都被 <code>ranges</code> 中 <strong>至少一个</strong> 区间覆盖，那么请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>已知区间 <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，如果整数 <code>x</code> 满足 <code>start<sub>i</sub> <= x <= end<sub>i</sub></code> ，那么我们称整数<code>x</code> 被覆盖了。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
<b>输出：</b>true
<b>解释：</b>2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>ranges = [[1,10],[10,20]], left = 21, right = 21
<b>输出：</b>false
<b>解释：</b>21 没有被任何一个区间覆盖。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= ranges.length <= 50</code></li>
	<li><code>1 <= start<sub>i</sub> <= end<sub>i</sub> <= 50</code></li>
	<li><code>1 <= left <= right <= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Iterate over every integer point in the range [left, right].
2. For each of these points check if it is included in one of the ranges.

## 示例

```
[[1,2],[3,4],[5,6]]
2
5
[[1,10],[10,20]]
21
21
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
```

### C

```c
bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsCovered(int[][] ranges, int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} ranges
 * @param {number} left
 * @param {number} right
 * @return {boolean}
 */
var isCovered = function(ranges, left, right) {
    
};
```

### TypeScript

```typescript
function isCovered(ranges: number[][], left: number, right: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $ranges
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function isCovered($ranges, $left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isCovered(_ ranges: [[Int]], _ left: Int, _ right: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isCovered(ranges: Array<IntArray>, left: Int, right: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isCovered(List<List<int>> ranges, int left, int right) {
    
  }
}
```

### Go

```golang
func isCovered(ranges [][]int, left int, right int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} ranges
# @param {Integer} left
# @param {Integer} right
# @return {Boolean}
def is_covered(ranges, left, right)
    
end
```

### Scala

```scala
object Solution {
    def isCovered(ranges: Array[Array[Int]], left: Int, right: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_covered(ranges: Vec<Vec<i32>>, left: i32, right: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-covered ranges left right)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_covered(Ranges :: [[integer()]], Left :: integer(), Right :: integer()) -> boolean().
is_covered(Ranges, Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_covered(ranges :: [[integer]], left :: integer, right :: integer) :: boolean
  def is_covered(ranges, left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isCovered(ranges: Array<Array<Int64>>, left: Int64, right: Int64): Bool {

    }
}
```

