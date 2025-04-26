# 365. 水壶问题

## 题目描述

<p>有两个水壶，容量分别为&nbsp;<code>x</code>&nbsp;和 <code>y</code> 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到&nbsp;<code>target</code>&nbsp;升。</p>

<p>你可以：</p>

<ul>
	<li>装满任意一个水壶</li>
	<li>清空任意一个水壶</li>
	<li>将水从一个水壶倒入另一个水壶，直到接水壶已满，或倒水壶已空。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1:</strong>&nbsp;</p>

<pre>
<strong>输入:</strong> x = 3,y = 5,target = 4
<strong>输出:</strong> true
<strong>解释：
</strong>按照以下步骤操作，以达到总共 4 升水：
1. 装满 5 升的水壶(0, 5)。
2. 把 5 升的水壶倒进 3 升的水壶，留下 2 升(3, 2)。
3. 倒空 3 升的水壶(0, 2)。
4. 把 2 升水从 5 升的水壶转移到 3 升的水壶(2, 0)。
5. 再次加满 5 升的水壶(2, 5)。
6. 从 5 升的水壶向 3 升的水壶倒水直到 3 升的水壶倒满。5 升的水壶里留下了 4 升水(3, 4)。
7. 倒空 3 升的水壶。现在，5 升的水壶里正好有 4 升水(0, 4)。
参考：来自著名的&nbsp;<a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg"><em>"Die Hard"</em></a></pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> x = 2, y = 6, target = 5
<strong>输出:</strong> false
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> x = 1, y = 2, target = 3
<strong>输出:</strong> true
<b>解释：</b>同时倒满两个水壶。现在两个水壶中水的总量等于 3。</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= x, y, target &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数学

## 示例

```
3
5
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
```

### C

```c
bool canMeasureWater(int x, int y, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanMeasureWater(int x, int y, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} target
 * @return {boolean}
 */
var canMeasureWater = function(x, y, target) {
    
};
```

### TypeScript

```typescript
function canMeasureWater(x: number, y: number, target: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $target
     * @return Boolean
     */
    function canMeasureWater($x, $y, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMeasureWater(_ x: Int, _ y: Int, _ target: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMeasureWater(x: Int, y: Int, target: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canMeasureWater(int x, int y, int target) {
    
  }
}
```

### Go

```golang
func canMeasureWater(x int, y int, target int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @param {Integer} target
# @return {Boolean}
def can_measure_water(x, y, target)
    
end
```

### Scala

```scala
object Solution {
    def canMeasureWater(x: Int, y: Int, target: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_measure_water(x: i32, y: i32, target: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-measure-water x y target)
  (-> exact-integer? exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_measure_water(X :: integer(), Y :: integer(), Target :: integer()) -> boolean().
can_measure_water(X, Y, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_measure_water(x :: integer, y :: integer, target :: integer) :: boolean
  def can_measure_water(x, y, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMeasureWater(x: Int64, y: Int64, target: Int64): Bool {

    }
}
```

