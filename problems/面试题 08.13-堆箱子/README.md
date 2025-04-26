# 面试题 08.13. 堆箱子

## 题目描述

<p>堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最高的一堆箱子。箱堆的高度为每个箱子高度的总和。</p>

<p>输入使用数组<code>[wi, di, hi]</code>表示每个箱子。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
<strong> 输出</strong>：6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
<strong> 输出</strong>：10
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>箱子的数目不大于3000个。</li>
</ol>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. 排列箱子会有什么帮助吗？
2. 我们可以按任一维度对箱子从大到小进行排序。这样我们会有箱子某一维度的局部顺序，在数组中后面的箱子必须出现在数组中前面的箱子之前。
3. 试着把它分解成子问题。
4. 想想你必须做出的第一个决定。第一个决定是哪个箱子在底部。
5. 一旦我们选择了底部的箱子，就需要选择第二个箱子，然后是第三个。
6. 实现一个基本的递归算法之后，你要考虑是否可以优化它。其中有重复的子问题吗？
7. 或者，我们可以考虑重复的选择：第一个箱子要放上去吗？第二个箱子要放上去吗？如此反复。

## 示例

```
[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
[[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int pileBox(vector<vector<int>>& box) {
        
    }
};
```

### Java

```java
class Solution {
    public int pileBox(int[][] box) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pileBox(self, box):
        """
        :type box: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        
```

### C

```c
int pileBox(int** box, int boxSize, int* boxColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int PileBox(int[][] box) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} box
 * @return {number}
 */
var pileBox = function(box) {
    
};
```

### TypeScript

```typescript
function pileBox(box: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $box
     * @return Integer
     */
    function pileBox($box) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pileBox(_ box: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pileBox(box: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int pileBox(List<List<int>> box) {
    
  }
}
```

### Go

```golang
func pileBox(box [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} box
# @return {Integer}
def pile_box(box)
    
end
```

### Scala

```scala
object Solution {
    def pileBox(box: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pile_box(box: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (pile-box box)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec pile_box(Box :: [[integer()]]) -> integer().
pile_box(Box) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pile_box(box :: [[integer]]) :: integer
  def pile_box(box) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pileBox(box: Array<Array<Int64>>): Int64 {

    }
}
```

