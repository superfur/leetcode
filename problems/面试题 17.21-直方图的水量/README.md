# 面试题 17.21. 直方图的水量

## 题目描述

<p>给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" style="height: 161px; width: 412px;" /></p>

<p><small>上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。&nbsp;<strong>感谢 Marcos</strong> 贡献此图。</small></p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>[0,1,0,2,1,0,1,3,2,1,2,1]
<strong>输出：</strong>6</pre>


## 难度

Hard

## 标签

- 栈
- 数组
- 双指针
- 动态规划
- 单调栈

## 提示

1. 直方图中最高的长方形起什么作用?
2. 想象一下最高的长方形、左边第二高的长方形和右边第二高的长方形。水会填满它们之间的区域。你能计算出其面积吗？其余的面积怎么办？
3. 为了计算出整体上最高的长方形和左侧最高的长方形之间的面积，你只需遍历直方图并减去这两个长方形之间的任何长方形的面积。你可以在右侧做同样的事情。如何处理剩下的图表?
4. 你可以通过重复这个过程来处理图的其余部分：找到最高的长方形和第二高的长方形，然后减去它们之间的长方形的面积。
5. 怎样才能更快地找到两边的下一个最高的长方形?
6. 你能通过预计算来得出每边下一个最高的长方形是哪个么？
7. 作为另一种解决方案，请从每个长方形的角度来考虑。每个长方形上面都有水。每个长方形上面会有多少水？
8. 每个长方形的顶部都有水，水的高度应与左侧最高长方形和右侧最高长方形的较小值相匹配，也就是说，water_on_top[i] = min(tallest_ bar(0->i), tallest_bar(i, n))。
9. 你应该能在O(N)时间和O(N)空间中解出该题。

## 示例

```
[0,1,0,2,1,0,1,3,2,1,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        
    }
};
```

### Java

```java
class Solution {
    public int trap(int[] height) {
        
    }
}
```

### Python

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def trap(self, height: List[int]) -> int:
        
```

### C

```c
int trap(int* height, int heightSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Trap(int[] height) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    
};
```

### TypeScript

```typescript
function trap(height: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function trap($height) {
        
    }
}
```

### Swift

```swift
class Solution {
    func trap(_ height: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trap(height: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int trap(List<int> height) {
    
  }
}
```

### Go

```golang
func trap(height []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} height
# @return {Integer}
def trap(height)
    
end
```

### Scala

```scala
object Solution {
    def trap(height: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (trap height)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec trap(Height :: [integer()]) -> integer().
trap(Height) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec trap(height :: [integer]) :: integer
  def trap(height) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func trap(height: Array<Int64>): Int64 {

    }
}
```

