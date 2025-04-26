# 3324. 出现在屏幕上的字符串序列

## 题目描述

<p>给你一个字符串 <code>target</code>。</p>

<p>Alice 将会使用一种特殊的键盘在她的电脑上输入 <code>target</code>，这个键盘<strong> 只有两个 </strong>按键：</p>

<ul>
	<li>按键 1：在屏幕上的字符串后追加字符 <code>'a'</code>。</li>
	<li>按键 2：将屏幕上字符串的 <strong>最后一个 </strong>字符更改为英文字母表中的 <strong>下一个</strong> 字符。例如，<code>'c'</code> 变为 <code>'d'</code>，<code>'z'</code> 变为 <code>'a'</code>。</li>
</ul>

<p><strong>注意</strong>，最初屏幕上是一个<em>空</em>字符串 <code>""</code>，所以她<strong> 只能</strong> 按按键 1。</p>

<p>请你考虑按键次数 <strong>最少</strong> 的情况，按字符串出现顺序，返回 Alice 输入 <code>target</code> 时屏幕上出现的所有字符串列表。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">target = "abc"</span></p>

<p><strong>输出：</strong> <span class="example-io">["a","aa","ab","aba","abb","abc"]</span></p>

<p><strong>解释：</strong></p>

<p>Alice 按键的顺序如下：</p>

<ul>
	<li>按下按键 1，屏幕上的字符串变为 <code>"a"</code>。</li>
	<li>按下按键 1，屏幕上的字符串变为 <code>"aa"</code>。</li>
	<li>按下按键 2，屏幕上的字符串变为 <code>"ab"</code>。</li>
	<li>按下按键 1，屏幕上的字符串变为 <code>"aba"</code>。</li>
	<li>按下按键 2，屏幕上的字符串变为 <code>"abb"</code>。</li>
	<li>按下按键 2，屏幕上的字符串变为 <code>"abc"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">target = "he"</span></p>

<p><strong>输出：</strong> <span class="example-io">["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 400</code></li>
	<li><code>target</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 模拟

## 提示

1. Append the character <code>'a'</code> using key 1.
2. Convert it to the required character using key 2.

## 示例

```
"abc"
"he"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> stringSequence(string target) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> stringSequence(String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** stringSequence(char* target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> StringSequence(string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} target
 * @return {string[]}
 */
var stringSequence = function(target) {
    
};
```

### TypeScript

```typescript
function stringSequence(target: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $target
     * @return String[]
     */
    function stringSequence($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stringSequence(_ target: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stringSequence(target: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> stringSequence(String target) {
    
  }
}
```

### Go

```golang
func stringSequence(target string) []string {
    
}
```

### Ruby

```ruby
# @param {String} target
# @return {String[]}
def string_sequence(target)
    
end
```

### Scala

```scala
object Solution {
    def stringSequence(target: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn string_sequence(target: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (string-sequence target)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec string_sequence(Target :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
string_sequence(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec string_sequence(target :: String.t) :: [String.t]
  def string_sequence(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stringSequence(target: String): ArrayList<String> {

    }
}
```

