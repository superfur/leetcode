# 546. 移除盒子

## 题目描述

<p>给出一些不同颜色的盒子<meta charset="UTF-8" />&nbsp;<code>boxes</code>&nbsp;，盒子的颜色由不同的正数表示。</p>

<p>你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 <code>k</code> 个盒子（<code>k&nbsp;&gt;= 1</code>），这样一轮之后你将得到 <code>k * k</code> 个积分。</p>

<p>返回 <em>你能获得的最大积分和</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>boxes = [1,3,2,2,2,3,4,3,1]
<strong>输出：</strong>23
<strong>解释：</strong>
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----&gt; [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----&gt; [1, 3, 3, 3, 1] (1*1=1 分) 
----&gt; [1, 1] (3*3=9 分) 
----&gt; [] (2*2=4 分)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>boxes = [1,1,1]
<strong>输出：</strong>9
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>boxes = [1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= boxes.length &lt;= 100</code></li>
	<li><code>1 &lt;= boxes[i]&nbsp;&lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 动态规划

## 示例

```
[1,3,2,2,2,3,4,3,1]
[1,1,1]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removeBoxes(vector<int>& boxes) {
        
    }
};
```

### Java

```java
class Solution {
    public int removeBoxes(int[] boxes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
```

### C

```c
int removeBoxes(int* boxes, int boxesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemoveBoxes(int[] boxes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} boxes
 * @return {number}
 */
var removeBoxes = function(boxes) {
    
};
```

### TypeScript

```typescript
function removeBoxes(boxes: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $boxes
     * @return Integer
     */
    function removeBoxes($boxes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeBoxes(_ boxes: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeBoxes(boxes: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removeBoxes(List<int> boxes) {
    
  }
}
```

### Go

```golang
func removeBoxes(boxes []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} boxes
# @return {Integer}
def remove_boxes(boxes)
    
end
```

### Scala

```scala
object Solution {
    def removeBoxes(boxes: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_boxes(boxes: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (remove-boxes boxes)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec remove_boxes(Boxes :: [integer()]) -> integer().
remove_boxes(Boxes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_boxes(boxes :: [integer]) :: integer
  def remove_boxes(boxes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeBoxes(boxes: Array<Int64>): Int64 {

    }
}
```

