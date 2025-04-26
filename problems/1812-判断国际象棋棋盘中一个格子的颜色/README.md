# 1812. 判断国际象棋棋盘中一个格子的颜色

## 题目描述

<p>给你一个坐标 <code>coordinates</code> ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/03/chessboard.png" style="width: 400px; height: 396px;" /></p>

<p>如果所给格子的颜色是白色，请你返回 <code>true</code>，如果是黑色，请返回 <code>false</code> 。</p>

<p>给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>coordinates = "a1"
<b>输出：</b>false
<b>解释：</b>如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>coordinates = "h3"
<b>输出：</b>true
<b>解释：</b>如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>coordinates = "c7"
<b>输出：</b>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>coordinates.length == 2</code></li>
	<li><code>'a' <= coordinates[0] <= 'h'</code></li>
	<li><code>'1' <= coordinates[1] <= '8'</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 提示

1. Convert the coordinates to (x, y) - that is, "a1" is (1, 1), "d7" is (4, 7).
2. Try add the numbers together and look for a pattern.

## 示例

```
"a1"
"h3"
"c7"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool squareIsWhite(string coordinates) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean squareIsWhite(String coordinates) {
        
    }
}
```

### Python

```python
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
```

### C

```c
bool squareIsWhite(char* coordinates) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SquareIsWhite(string coordinates) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} coordinates
 * @return {boolean}
 */
var squareIsWhite = function(coordinates) {
    
};
```

### TypeScript

```typescript
function squareIsWhite(coordinates: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $coordinates
     * @return Boolean
     */
    function squareIsWhite($coordinates) {
        
    }
}
```

### Swift

```swift
class Solution {
    func squareIsWhite(_ coordinates: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun squareIsWhite(coordinates: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool squareIsWhite(String coordinates) {
    
  }
}
```

### Go

```golang
func squareIsWhite(coordinates string) bool {
    
}
```

### Ruby

```ruby
# @param {String} coordinates
# @return {Boolean}
def square_is_white(coordinates)
    
end
```

### Scala

```scala
object Solution {
    def squareIsWhite(coordinates: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (square-is-white coordinates)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec square_is_white(Coordinates :: unicode:unicode_binary()) -> boolean().
square_is_white(Coordinates) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec square_is_white(coordinates :: String.t) :: boolean
  def square_is_white(coordinates) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func squareIsWhite(coordinates: String): Bool {

    }
}
```

