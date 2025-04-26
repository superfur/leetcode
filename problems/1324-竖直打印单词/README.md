# 1324. 竖直打印单词

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>。请你按照单词在 <code>s</code> 中的出现顺序将它们全部竖直返回。<br>
单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。<br>
每个单词只能放在一列上，每一列中也只能有一个单词。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;HOW ARE YOU&quot;
<strong>输出：</strong>[&quot;HAY&quot;,&quot;ORO&quot;,&quot;WEU&quot;]
<strong>解释：</strong>每个单词都应该竖直打印。 
 &quot;HAY&quot;
&nbsp;&quot;ORO&quot;
&nbsp;&quot;WEU&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;TO BE OR NOT TO BE&quot;
<strong>输出：</strong>[&quot;TBONTB&quot;,&quot;OEROOE&quot;,&quot;   T&quot;]
<strong>解释：</strong>题目允许使用空格补位，但不允许输出末尾出现空格。
&quot;TBONTB&quot;
&quot;OEROOE&quot;
&quot;   T&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;CONTEST IS COMING&quot;
<strong>输出：</strong>[&quot;CIC&quot;,&quot;OSO&quot;,&quot;N M&quot;,&quot;T I&quot;,&quot;E N&quot;,&quot;S G&quot;,&quot;T&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code>&nbsp;仅含大写英文字母。</li>
	<li>题目数据保证两个单词之间只有一个空格。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 模拟

## 提示

1. Use the maximum length of words to determine the length of the returned answer. However, don't forget to remove trailing spaces.

## 示例

```
"HOW ARE YOU"
"TO BE OR NOT TO BE"
"CONTEST IS COMING"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> printVertically(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> printVertically(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def printVertically(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** printVertically(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> PrintVertically(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    
};
```

### TypeScript

```typescript
function printVertically(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function printVertically($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func printVertically(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun printVertically(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> printVertically(String s) {
    
  }
}
```

### Go

```golang
func printVertically(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def print_vertically(s)
    
end
```

### Scala

```scala
object Solution {
    def printVertically(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn print_vertically(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (print-vertically s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec print_vertically(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
print_vertically(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec print_vertically(s :: String.t) :: [String.t]
  def print_vertically(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func printVertically(s: String): ArrayList<String> {

    }
}
```

