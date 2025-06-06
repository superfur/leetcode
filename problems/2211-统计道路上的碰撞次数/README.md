# 2211. 统计道路上的碰撞次数

## 题目描述

<p>在一条无限长的公路上有 <code>n</code> 辆汽车正在行驶。汽车按从左到右的顺序按从 <code>0</code> 到 <code>n - 1</code> 编号，每辆车都在一个 <strong>独特的</strong> 位置。</p>

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>directions</code> ，长度为 <code>n</code> 。<code>directions[i]</code> 可以是 <code>'L'</code>、<code>'R'</code> 或 <code>'S'</code> 分别表示第 <code>i</code> 辆车是向 <strong>左</strong> 、向 <strong>右</strong> 或者 <strong>停留</strong> 在当前位置。每辆车移动时 <strong>速度相同</strong> 。</p>

<p>碰撞次数可以按下述方式计算：</p>

<ul>
	<li>当两辆移动方向&nbsp;<strong>相反</strong>&nbsp;的车相撞时，碰撞次数加 <code>2</code> 。</li>
	<li>当一辆移动的车和一辆静止的车相撞时，碰撞次数加 <code>1</code> 。</li>
</ul>

<p>碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。</p>

<p>返回在这条道路上发生的 <strong>碰撞总次数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>directions = "RLRSLL"
<strong>输出：</strong>5
<strong>解释：</strong>
将会在道路上发生的碰撞列出如下：
- 车 0 和车 1 会互相碰撞。由于它们按相反方向移动，碰撞数量变为 0 + 2 = 2 。
- 车 2 和车 3 会互相碰撞。由于 3 是静止的，碰撞数量变为 2 + 1 = 3 。
- 车 3 和车 4 会互相碰撞。由于 3 是静止的，碰撞数量变为 3 + 1 = 4 。
- 车 4 和车 5 会互相碰撞。在车 4 和车 3 碰撞之后，车 4 会待在碰撞位置，接着和车 5 碰撞。碰撞数量变为 4 + 1 = 5 。
因此，将会在道路上发生的碰撞总次数是 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>directions = "LLRR"
<strong>输出：</strong>0
<strong>解释：</strong>
不存在会发生碰撞的车辆。因此，将会在道路上发生的碰撞总次数是 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= directions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>directions[i]</code> 的值为 <code>'L'</code>、<code>'R'</code> 或 <code>'S'</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串
- 模拟

## 提示

1. In what circumstances does a moving car not collide with another car?
2. If we disregard the moving cars that do not collide with another car, what does each moving car contribute to the answer?
3. Will stationary cars contribute towards the answer?

## 示例

```
"RLRSLL"
"LLRR"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCollisions(string directions) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCollisions(String directions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCollisions(self, directions: str) -> int:
        
```

### C

```c
int countCollisions(char* directions) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCollisions(string directions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} directions
 * @return {number}
 */
var countCollisions = function(directions) {
    
};
```

### TypeScript

```typescript
function countCollisions(directions: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $directions
     * @return Integer
     */
    function countCollisions($directions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCollisions(_ directions: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCollisions(directions: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCollisions(String directions) {
    
  }
}
```

### Go

```golang
func countCollisions(directions string) int {
    
}
```

### Ruby

```ruby
# @param {String} directions
# @return {Integer}
def count_collisions(directions)
    
end
```

### Scala

```scala
object Solution {
    def countCollisions(directions: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-collisions directions)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_collisions(Directions :: unicode:unicode_binary()) -> integer().
count_collisions(Directions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_collisions(directions :: String.t) :: integer
  def count_collisions(directions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCollisions(directions: String): Int64 {

    }
}
```

