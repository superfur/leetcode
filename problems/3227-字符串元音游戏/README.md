# 3227. 字符串元音游戏

## 题目描述

<p>小红和小明在玩一个字符串元音游戏。</p>

<p>给你一个字符串 <code>s</code>，小红和小明将轮流参与游戏，小红<strong> 先 </strong>开始：</p>

<ul>
	<li>在小红的回合，她必须移除 <code>s</code> 中包含 <strong>奇数 </strong>个元音的任意 <strong>非空</strong> <span data-keyword="substring">子字符串</span>。</li>
	<li>在小明的回合，他必须移除 <code>s</code> 中包含 <strong>偶数 </strong>个元音的任意 <strong>非空</strong> <span data-keyword="substring">子字符串</span>。</li>
</ul>

<p>第一个无法在其回合内进行移除操作的玩家输掉游戏。假设小红和小明都采取 <strong>最优策略 </strong>。</p>

<p>如果小红赢得游戏，返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>英文元音字母包括：<code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, 和 <code>u</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "leetcoder"</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong><br />
小红可以执行如下移除操作来赢得游戏：</p>

<ul>
	<li>小红先手，她可以移除加下划线的子字符串 <code>s = "<u><strong>leetco</strong></u>der"</code>，其中包含 3 个元音。结果字符串为 <code>s = "der"</code>。</li>
	<li>小明接着，他可以移除加下划线的子字符串 <code>s = "<u><strong>d</strong></u>er"</code>，其中包含 0 个元音。结果字符串为 <code>s = "er"</code>。</li>
	<li>小红再次操作，她可以移除整个字符串 <code>s = "<strong><u>er</u></strong>"</code>，其中包含 1 个元音。</li>
	<li>又轮到小明，由于字符串为空，无法执行移除操作，因此小红赢得游戏。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "bbcd"</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong><br />
小红在她的第一回合无法执行移除操作，因此小红输掉了游戏。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数学
- 字符串
- 博弈

## 提示

1. If there are no vowels in the initial string, then Bob wins.
2. If the number of vowels in the initial string is odd, then Alice can remove the whole string on her first turn and win.
3. What if the number of vowels in the initial string is even? What’s the optimal play for Alice’s first turn?

## 示例

```
"leetcoder"
"bbcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool doesAliceWin(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean doesAliceWin(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
```

### C

```c
bool doesAliceWin(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool DoesAliceWin(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var doesAliceWin = function(s) {
    
};
```

### TypeScript

```typescript
function doesAliceWin(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function doesAliceWin($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func doesAliceWin(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun doesAliceWin(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool doesAliceWin(String s) {
    
  }
}
```

### Go

```golang
func doesAliceWin(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def does_alice_win(s)
    
end
```

### Scala

```scala
object Solution {
    def doesAliceWin(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn does_alice_win(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (does-alice-win s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec does_alice_win(S :: unicode:unicode_binary()) -> boolean().
does_alice_win(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec does_alice_win(s :: String.t) :: boolean
  def does_alice_win(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func doesAliceWin(s: String): Bool {

    }
}
```

