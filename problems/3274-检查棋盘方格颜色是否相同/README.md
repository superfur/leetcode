# 3274. 检查棋盘方格颜色是否相同

## 题目描述

<p>给你两个字符串 <code>coordinate1</code> 和 <code>coordinate2</code>，代表 <code>8 x 8</code> 国际象棋棋盘上的两个方格的坐标。</p>

<p>以下是棋盘的参考图。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/17/screenshot-2021-02-20-at-22159-pm.png" style="width: 400px; height: 396px;" /></p>

<p>如果这两个方格颜色相同，返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>坐标总是表示有效的棋盘方格。坐标的格式总是先字母（表示列），再数字（表示行）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coordinate1 = "a1", coordinate2 = "c3"</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>两个方格均为黑色。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coordinate1 = "a1", coordinate2 = "h3"</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>方格 <code>"a1"</code> 是黑色，而 <code>"h3"</code> 是白色。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>coordinate1.length == coordinate2.length == 2</code></li>
	<li><code>'a' &lt;= coordinate1[0], coordinate2[0] &lt;= 'h'</code></li>
	<li><code>'1' &lt;= coordinate1[1], coordinate2[1] &lt;= '8'</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 提示

1. The color of the chessboard is black the sum of row coordinates and column coordinates is even. Otherwise, it's white.

## 示例

```
"a1"
"c3"
"a1"
"h3"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
```

### C

```c
bool checkTwoChessboards(char* coordinate1, char* coordinate2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckTwoChessboards(string coordinate1, string coordinate2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} coordinate1
 * @param {string} coordinate2
 * @return {boolean}
 */
var checkTwoChessboards = function(coordinate1, coordinate2) {
    
};
```

### TypeScript

```typescript
function checkTwoChessboards(coordinate1: string, coordinate2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $coordinate1
     * @param String $coordinate2
     * @return Boolean
     */
    function checkTwoChessboards($coordinate1, $coordinate2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkTwoChessboards(_ coordinate1: String, _ coordinate2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkTwoChessboards(String coordinate1, String coordinate2) {
    
  }
}
```

### Go

```golang
func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} coordinate1
# @param {String} coordinate2
# @return {Boolean}
def check_two_chessboards(coordinate1, coordinate2)
    
end
```

### Scala

```scala
object Solution {
    def checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-two-chessboards coordinate1 coordinate2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_two_chessboards(Coordinate1 :: unicode:unicode_binary(), Coordinate2 :: unicode:unicode_binary()) -> boolean().
check_two_chessboards(Coordinate1, Coordinate2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_two_chessboards(coordinate1 :: String.t, coordinate2 :: String.t) :: boolean
  def check_two_chessboards(coordinate1, coordinate2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkTwoChessboards(coordinate1: String, coordinate2: String): Bool {

    }
}
```

