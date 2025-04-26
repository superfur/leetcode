# 1138. 字母板上的路径

## 题目描述

<p>我们从一块字母板上的位置&nbsp;<code>(0, 0)</code>&nbsp;出发，该坐标对应的字符为&nbsp;<code>board[0][0]</code>。</p>

<p>在本题里，字母板为<code>board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]</code>，如下所示。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 300px;" /></p>

<p>我们可以按下面的指令规则行动：</p>

<ul>
	<li>如果方格存在，<code>'U'</code>&nbsp;意味着将我们的位置上移一行；</li>
	<li>如果方格存在，<code>'D'</code>&nbsp;意味着将我们的位置下移一行；</li>
	<li>如果方格存在，<code>'L'</code>&nbsp;意味着将我们的位置左移一列；</li>
	<li>如果方格存在，<code>'R'</code>&nbsp;意味着将我们的位置右移一列；</li>
	<li><code>'!'</code>&nbsp;会把在我们当前位置 <code>(r, c)</code> 的字符&nbsp;<code>board[r][c]</code>&nbsp;添加到答案中。</li>
</ul>

<p>（注意，字母板上只存在有字母的位置。）</p>

<p>返回指令序列，用最小的行动次数让答案和目标&nbsp;<code>target</code>&nbsp;相同。你可以返回任何达成目标的路径。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = "leet"
<strong>输出：</strong>"DDR!UURRR!!DDD!"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = "code"
<strong>输出：</strong>"RR!DDRR!UUL!R!"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>target</code>&nbsp;仅含有小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串

## 提示

1. Create a hashmap from letter to position on the board.
2. Now for each letter, try moving there in steps, where at each step you check if it is inside the boundaries of the board.

## 示例

```
"leet"
"code"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string alphabetBoardPath(string target) {
        
    }
};
```

### Java

```java
class Solution {
    public String alphabetBoardPath(String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
```

### C

```c
char* alphabetBoardPath(char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public string AlphabetBoardPath(string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} target
 * @return {string}
 */
var alphabetBoardPath = function(target) {
    
};
```

### TypeScript

```typescript
function alphabetBoardPath(target: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $target
     * @return String
     */
    function alphabetBoardPath($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func alphabetBoardPath(_ target: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun alphabetBoardPath(target: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String alphabetBoardPath(String target) {
    
  }
}
```

### Go

```golang
func alphabetBoardPath(target string) string {
    
}
```

### Ruby

```ruby
# @param {String} target
# @return {String}
def alphabet_board_path(target)
    
end
```

### Scala

```scala
object Solution {
    def alphabetBoardPath(target: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn alphabet_board_path(target: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (alphabet-board-path target)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec alphabet_board_path(Target :: unicode:unicode_binary()) -> unicode:unicode_binary().
alphabet_board_path(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec alphabet_board_path(target :: String.t) :: String.t
  def alphabet_board_path(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func alphabetBoardPath(target: String): String {

    }
}
```

