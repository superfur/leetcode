# 1739. 放置盒子

## 题目描述

<p>有一个立方体房间，其长度、宽度和高度都等于 <code>n</code> 个单位。请你在房间里放置 <code>n</code> 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下：</p>

<ul>
	<li>你可以把盒子放在地板上的任何地方。</li>
	<li>如果盒子 <code>x</code> 需要放置在盒子 <code>y</code> 的顶部，那么盒子 <code>y</code> 竖直的四个侧面都 <strong>必须</strong> 与另一个盒子或墙相邻。</li>
</ul>

<p>给你一个整数 <code>n</code> ，返回接触地面的盒子的 <strong>最少</strong> 可能数量<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/3-boxes.png" style="width: 135px; height: 143px;" /></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>3
<strong>解释：</strong>上图是 3 个盒子的摆放位置。
这些盒子放在房间的一角，对应左侧位置。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/4-boxes.png" style="width: 135px; height: 179px;" /></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>3
<strong>解释：</strong>上图是 3 个盒子的摆放位置。
这些盒子放在房间的一角，对应左侧位置。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/10-boxes.png" style="width: 271px; height: 257px;" /></p>

<pre>
<strong>输入：</strong>n = 10
<strong>输出：</strong>6
<strong>解释：</strong>上图是 10 个盒子的摆放位置。
这些盒子放在房间的一角，对应后方位置。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数学
- 二分查找

## 提示

1. Suppose We can put m boxes on the floor, within all the ways to put the boxes, what’s the maximum number of boxes we can put in?
2. The first box should always start in the corner

## 示例

```
3
4
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumBoxes(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumBoxes(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumBoxes(self, n: int) -> int:
        
```

### C

```c
int minimumBoxes(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumBoxes(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minimumBoxes = function(n) {
    
};
```

### TypeScript

```typescript
function minimumBoxes(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumBoxes($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumBoxes(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumBoxes(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumBoxes(int n) {
    
  }
}
```

### Go

```golang
func minimumBoxes(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def minimum_boxes(n)
    
end
```

### Scala

```scala
object Solution {
    def minimumBoxes(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_boxes(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-boxes n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_boxes(N :: integer()) -> integer().
minimum_boxes(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_boxes(n :: integer) :: integer
  def minimum_boxes(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumBoxes(n: Int64): Int64 {

    }
}
```

