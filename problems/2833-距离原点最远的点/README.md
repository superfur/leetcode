# 2833. 距离原点最远的点

## 题目描述

<p>给你一个长度为 <code>n</code> 的字符串 <code>moves</code> ，该字符串仅由字符 <code>'L'</code>、<code>'R'</code> 和 <code>'_'</code> 组成。字符串表示你在一条原点为 <code>0</code> 的数轴上的若干次移动。</p>

<p>你的初始位置就在原点（<code>0</code>），第 <code>i</code> 次移动过程中，你可以根据对应字符选择移动方向：</p>

<ul>
	<li>如果 <code>moves[i] = 'L'</code> 或 <code>moves[i] = '_'</code> ，可以选择向左移动一个单位距离</li>
	<li>如果 <code>moves[i] = 'R'</code> 或 <code>moves[i] = '_'</code> ，可以选择向右移动一个单位距离</li>
</ul>

<p>移动 <code>n</code> 次之后，请你找出可以到达的距离原点 <strong>最远</strong> 的点，并返回 <strong>从原点到这一点的距离</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>moves = "L_RL__R"
<strong>输出：</strong>3
<strong>解释：</strong>可以到达的距离原点 0 最远的点是 -3 ，移动的序列为 "LLRLLLR" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>moves = "_R__LL_"
<strong>输出：</strong>5
<strong>解释：</strong>可以到达的距离原点 0 最远的点是 -5 ，移动的序列为 "LRLLLLL" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>moves = "_______"
<strong>输出：</strong>7
<strong>解释：</strong>可以到达的距离原点 0 最远的点是 7 ，移动的序列为 "RRRRRRR" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= moves.length == n &lt;= 50</code></li>
	<li><code>moves</code> 仅由字符 <code>'L'</code>、<code>'R'</code> 和 <code>'_'</code> 组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 计数

## 提示

1. <div class="_1l1MA">In an optimal answer, all occurrences of <code>'_’</code> will be replaced with the <strong>same</strong> character.</div>
2. <div class="_1l1MA">Replace all characters of <code>'_’</code> with the character that occurs the most. </div>

## 示例

```
"L_RL__R"
"_R__LL_"
"_______"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        
    }
};
```

### Java

```java
class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        
    }
}
```

### Python

```python
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
```

### C

```c
int furthestDistanceFromOrigin(char* moves) {
    
}
```

### C#

```csharp
public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    
};
```

### TypeScript

```typescript
function furthestDistanceFromOrigin(moves: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $moves
     * @return Integer
     */
    function furthestDistanceFromOrigin($moves) {
        
    }
}
```

### Swift

```swift
class Solution {
    func furthestDistanceFromOrigin(_ moves: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun furthestDistanceFromOrigin(moves: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int furthestDistanceFromOrigin(String moves) {
    
  }
}
```

### Go

```golang
func furthestDistanceFromOrigin(moves string) int {
    
}
```

### Ruby

```ruby
# @param {String} moves
# @return {Integer}
def furthest_distance_from_origin(moves)
    
end
```

### Scala

```scala
object Solution {
    def furthestDistanceFromOrigin(moves: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (furthest-distance-from-origin moves)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec furthest_distance_from_origin(Moves :: unicode:unicode_binary()) -> integer().
furthest_distance_from_origin(Moves) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec furthest_distance_from_origin(moves :: String.t) :: integer
  def furthest_distance_from_origin(moves) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func furthestDistanceFromOrigin(moves: String): Int64 {

    }
}
```

