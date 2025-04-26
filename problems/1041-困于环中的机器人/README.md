# 1041. 困于环中的机器人

## 题目描述

<p>在无限的平面上，机器人最初位于&nbsp;<code>(0, 0)</code>&nbsp;处，面朝北方。注意:</p>

<ul>
	<li><strong>北方向</strong> 是y轴的正方向。</li>
	<li><strong>南方向</strong> 是y轴的负方向。</li>
	<li><strong>东方向</strong> 是x轴的正方向。</li>
	<li><strong>西方向</strong> 是x轴的负方向。</li>
</ul>

<p>机器人可以接受下列三条指令之一：</p>

<ul>
	<li><code>"G"</code>：直走 1 个单位</li>
	<li><code>"L"</code>：左转 90 度</li>
	<li><code>"R"</code>：右转 90 度</li>
</ul>

<p>机器人按顺序执行指令&nbsp;<code>instructions</code>，并一直重复它们。</p>

<p>只有在平面中存在环使得机器人永远无法离开时，返回&nbsp;<code>true</code>。否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>instructions = "GGLLGG"
<strong>输出：</strong>true
<strong>解释：</strong>机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
“L”:逆时针旋转90度。位置:(0,2).方向:西。
“L”:逆时针旋转90度。位置:(0,2)方向:南。
“G”:移动一步。位置:(0,1)方向:南。
“G”:移动一步。位置:(0,0)方向:南。
重复指令，机器人进入循环:(0,0)——&gt;(0,1)——&gt;(0,2)——&gt;(0,1)——&gt;(0,0)。
在此基础上，我们返回true。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>instructions = "GG"
<strong>输出：</strong>false
<strong>解释：</strong>机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“G”:移动一步。位置:(0,2).方向:北。
重复这些指示，继续朝北前进，不会进入循环。
在此基础上，返回false。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>instructions = "GL"
<strong>输出：</strong>true
<strong>解释：</strong>机器人最初在(0,0)处，面向北方。
“G”:移动一步。位置:(0,1)方向:北。
“L”:逆时针旋转90度。位置:(0,1).方向:西。
“G”:移动一步。位置:(- 1,1)方向:西。
“L”:逆时针旋转90度。位置:(- 1,1)方向:南。
“G”:移动一步。位置:(- 1,0)方向:南。
“L”:逆时针旋转90度。位置:(- 1,0)方向:东方。
“G”:移动一步。位置:(0,0)方向:东方。
“L”:逆时针旋转90度。位置:(0,0)方向:北。
重复指令，机器人进入循环:(0,0)——&gt;(0,1)——&gt;(- 1,1)——&gt;(- 1,0)——&gt;(0,0)。
在此基础上，我们返回true。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= instructions.length &lt;= 100</code></li>
	<li><code>instructions[i]</code>&nbsp;仅包含&nbsp;<code>'G', 'L', 'R'</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 模拟

## 提示

1. Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.
2. The robot stays in the circle if and only if (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.

## 示例

```
"GGLLGG"
"GG"
"GL"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isRobotBounded(string instructions) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isRobotBounded(String instructions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
```

### C

```c
bool isRobotBounded(char* instructions) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsRobotBounded(string instructions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} instructions
 * @return {boolean}
 */
var isRobotBounded = function(instructions) {
    
};
```

### TypeScript

```typescript
function isRobotBounded(instructions: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $instructions
     * @return Boolean
     */
    function isRobotBounded($instructions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isRobotBounded(_ instructions: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isRobotBounded(instructions: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isRobotBounded(String instructions) {
    
  }
}
```

### Go

```golang
func isRobotBounded(instructions string) bool {
    
}
```

### Ruby

```ruby
# @param {String} instructions
# @return {Boolean}
def is_robot_bounded(instructions)
    
end
```

### Scala

```scala
object Solution {
    def isRobotBounded(instructions: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_robot_bounded(instructions: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-robot-bounded instructions)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_robot_bounded(Instructions :: unicode:unicode_binary()) -> boolean().
is_robot_bounded(Instructions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_robot_bounded(instructions :: String.t) :: boolean
  def is_robot_bounded(instructions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isRobotBounded(instructions: String): Bool {

    }
}
```

