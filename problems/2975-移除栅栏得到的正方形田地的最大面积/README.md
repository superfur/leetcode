# 2975. 移除栅栏得到的正方形田地的最大面积

## 题目描述

<p>有一个大型的 <code>(m - 1) x (n - 1)</code> 矩形田地，其两个对角分别是 <code>(1, 1)</code> 和 <code>(m, n)</code> ，田地内部有一些水平栅栏和垂直栅栏，分别由数组 <code>hFences</code> 和 <code>vFences</code> 给出。</p>

<p>水平栅栏为坐标 <code>(hFences[i], 1)</code> 到 <code>(hFences[i], n)</code>，垂直栅栏为坐标 <code>(1, vFences[i])</code> 到 <code>(m, vFences[i])</code> 。</p>

<p>返回通过<strong> 移除 </strong>一些栅栏（<strong>可能不移除</strong>）所能形成的最大面积的<strong> 正方形 </strong>田地的面积，或者如果无法形成正方形田地则返回 <code>-1</code>。</p>

<p>由于答案可能很大，所以请返回结果对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后的值。</p>

<p><strong>注意：</strong>田地外围两个水平栅栏（坐标 <code>(1, 1)</code> 到 <code>(1, n)</code> 和坐标 <code>(m, 1)</code> 到 <code>(m, n)</code> ）以及两个垂直栅栏（坐标 <code>(1, 1)</code> 到 <code>(m, 1)</code> 和坐标 <code>(1, n)</code> 到 <code>(m, n)</code> ）所包围。这些栅栏<strong> 不能</strong> 被移除。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png" /></p>

<pre>
<strong>输入：</strong>m = 4, n = 3, hFences = [2,3], vFences = [2]
<strong>输出：</strong>4
<strong>解释：</strong>移除位于 2 的水平栅栏和位于 2 的垂直栅栏将得到一个面积为 4 的正方形田地。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/22/maxsquareareaexample1.png" style="width: 285px; height: 242px;" /></p>

<pre>
<strong>输入：</strong>m = 6, n = 7, hFences = [2], vFences = [4]
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明无法通过移除栅栏形成正方形田地。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= m, n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= hFences.length, vFences.length &lt;= 600</code></li>
	<li><code>1 &lt; hFences[i] &lt; m</code></li>
	<li><code>1 &lt; vFences[i] &lt; n</code></li>
	<li><code>hFences</code> 和 <code>vFences</code> 中的元素是唯一的。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 枚举

## 提示

1. Put <code>1</code> and <code>m</code> into <code>hFences</code>. The differences of any two values in the new <code>hFences</code> can be a horizontal edge of a rectangle.
2. Similarly put <code>1</code> and <code>n</code> into <code>vFences</code>. The differences of any two values in the new <code>vFences</code> can be a vertical edge of a rectangle.
3. Our goal is to find the maximum common value in both parts.

## 示例

```
4
3
[2,3]
[2]
6
7
[2]
[4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
```

### C

```c
int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} hFences
 * @param {number[]} vFences
 * @return {number}
 */
var maximizeSquareArea = function(m, n, hFences, vFences) {
    
};
```

### TypeScript

```typescript
function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[] $hFences
     * @param Integer[] $vFences
     * @return Integer
     */
    function maximizeSquareArea($m, $n, $hFences, $vFences) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences: [Int], _ vFences: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximizeSquareArea(m: Int, n: Int, hFences: IntArray, vFences: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximizeSquareArea(int m, int n, List<int> hFences, List<int> vFences) {
    
  }
}
```

### Go

```golang
func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} h_fences
# @param {Integer[]} v_fences
# @return {Integer}
def maximize_square_area(m, n, h_fences, v_fences)
    
end
```

### Scala

```scala
object Solution {
    def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximize-square-area m n hFences vFences)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximize_square_area(M :: integer(), N :: integer(), HFences :: [integer()], VFences :: [integer()]) -> integer().
maximize_square_area(M, N, HFences, VFences) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximize_square_area(m :: integer, n :: integer, h_fences :: [integer], v_fences :: [integer]) :: integer
  def maximize_square_area(m, n, h_fences, v_fences) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximizeSquareArea(m: Int64, n: Int64, hFences: Array<Int64>, vFences: Array<Int64>): Int64 {

    }
}
```

