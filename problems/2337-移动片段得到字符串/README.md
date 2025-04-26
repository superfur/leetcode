# 2337. 移动片段得到字符串

## 题目描述

<p>给你两个字符串 <code>start</code> 和 <code>target</code> ，长度均为 <code>n</code> 。每个字符串 <strong>仅</strong> 由字符 <code>'L'</code>、<code>'R'</code> 和 <code>'_'</code> 组成，其中：</p>

<ul>
	<li>字符 <code>'L'</code> 和 <code>'R'</code> 表示片段，其中片段 <code>'L'</code> 只有在其左侧直接存在一个 <strong>空位</strong> 时才能向 <strong>左</strong> 移动，而片段 <code>'R'</code> 只有在其右侧直接存在一个 <strong>空位</strong> 时才能向 <strong>右</strong> 移动。</li>
	<li>字符 <code>'_'</code> 表示可以被 <strong>任意</strong> <code>'L'</code> 或 <code>'R'</code> 片段占据的空位。</li>
</ul>

<p>如果在移动字符串 <code>start</code> 中的片段任意次之后可以得到字符串 <code>target</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "_L__R__R_", target = "L______RR"
<strong>输出：</strong>true
<strong>解释：</strong>可以从字符串 start 获得 target ，需要进行下面的移动：
- 将第一个片段向左移动一步，字符串现在变为 "<strong>L</strong>___R__R_" 。
- 将最后一个片段向右移动一步，字符串现在变为 "L___R___<strong>R</strong>" 。
- 将第二个片段向右移动三步，字符串现在变为 "L______<strong>R</strong>R" 。
可以从字符串 start 得到 target ，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "R_L_", target = "__LR"
<strong>输出：</strong>false
<strong>解释：</strong>字符串 start 中的 'R' 片段可以向右移动一步得到 "_<strong>R</strong>L_" 。
但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>start = "_R", target = "R_"
<strong>输出：</strong>false
<strong>解释：</strong>字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == start.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>start</code> 和 <code>target</code> 由字符 <code>'L'</code>、<code>'R'</code> 和 <code>'_'</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. After some sequence of moves, can the order of the pieces change?
2. Try to match each piece in s with a piece in e.

## 示例

```
"_L__R__R_"
"L______RR"
"R_L_"
"__LR"
"_R"
"R_"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canChange(string start, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canChange(String start, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
```

### C

```c
bool canChange(char* start, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanChange(string start, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} start
 * @param {string} target
 * @return {boolean}
 */
var canChange = function(start, target) {
    
};
```

### TypeScript

```typescript
function canChange(start: string, target: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $start
     * @param String $target
     * @return Boolean
     */
    function canChange($start, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canChange(_ start: String, _ target: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canChange(start: String, target: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canChange(String start, String target) {
    
  }
}
```

### Go

```golang
func canChange(start string, target string) bool {
    
}
```

### Ruby

```ruby
# @param {String} start
# @param {String} target
# @return {Boolean}
def can_change(start, target)
    
end
```

### Scala

```scala
object Solution {
    def canChange(start: String, target: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_change(start: String, target: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-change start target)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_change(Start :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> boolean().
can_change(Start, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_change(start :: String.t, target :: String.t) :: boolean
  def can_change(start, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canChange(start: String, target: String): Bool {

    }
}
```

