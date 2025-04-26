# 657. 机器人能否返回原点

## 题目描述

<p>在二维平面上，有一个机器人从原点 <code>(0, 0)</code> 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在<strong>&nbsp;<code>(0, 0)</code> 处结束</strong>。</p>

<p>移动顺序由字符串&nbsp;<code>moves</code>&nbsp;表示。字符 <code>move[i]</code> 表示其第 <code>i</code> 次移动。机器人的有效动作有&nbsp;<code>R</code>（右），<code>L</code>（左），<code>U</code>（上）和 <code>D</code>（下）。</p>

<p>如果机器人在完成所有动作后返回原点，则返回 <code>true</code>。否则，返回 <code>false</code>。</p>

<p><strong>注意：</strong>机器人“面朝”的方向无关紧要。 <code>“R”</code> 将始终使机器人向右移动一次，<code>“L”</code> 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> moves = "UD"
<strong>输出:</strong> true
<strong>解释：</strong>机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> moves = "LL"
<strong>输出:</strong> false
<strong>解释：</strong>机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>moves</code>&nbsp;只包含字符&nbsp;<code>'U'</code>,&nbsp;<code>'D'</code>,&nbsp;<code>'L'</code>&nbsp;和&nbsp;<code>'R'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 示例

```
"UD"
"LL"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool judgeCircle(string moves) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean judgeCircle(String moves) {
        
    }
}
```

### Python

```python
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
```

### C

```c
bool judgeCircle(char* moves) {
    
}
```

### C#

```csharp
public class Solution {
    public bool JudgeCircle(string moves) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    
};
```

### TypeScript

```typescript
function judgeCircle(moves: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $moves
     * @return Boolean
     */
    function judgeCircle($moves) {
        
    }
}
```

### Swift

```swift
class Solution {
    func judgeCircle(_ moves: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun judgeCircle(moves: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool judgeCircle(String moves) {
    
  }
}
```

### Go

```golang
func judgeCircle(moves string) bool {
    
}
```

### Ruby

```ruby
# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
    
end
```

### Scala

```scala
object Solution {
    def judgeCircle(moves: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (judge-circle moves)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec judge_circle(Moves :: unicode:unicode_binary()) -> boolean().
judge_circle(Moves) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec judge_circle(moves :: String.t) :: boolean
  def judge_circle(moves) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func judgeCircle(moves: String): Bool {

    }
}
```

