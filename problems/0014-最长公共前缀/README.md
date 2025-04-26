# 14. 最长公共前缀

## 题目描述

<p>编写一个函数来查找字符串数组中的最长公共前缀。</p>

<p>如果不存在公共前缀，返回空字符串&nbsp;<code>""</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["flower","flow","flight"]
<strong>输出：</strong>"fl"
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["dog","racecar","car"]
<strong>输出：</strong>""
<strong>解释：</strong>输入不存在公共前缀。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code>&nbsp;如果非空，则仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 字典树
- 字符串

## 示例

```
["flower","flow","flight"]
["dog","racecar","car"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
```

### C

```c
char* longestCommonPrefix(char** strs, int strsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
};
```

### TypeScript

```typescript
function longestCommonPrefix(strs: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestCommonPrefix(List<String> strs) {
    
  }
}
```

### Go

```golang
func longestCommonPrefix(strs []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    
end
```

### Scala

```scala
object Solution {
    def longestCommonPrefix(strs: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-common-prefix strs)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec longest_common_prefix(Strs :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
longest_common_prefix(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(strs :: [String.t]) :: String.t
  def longest_common_prefix(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestCommonPrefix(strs: Array<String>): String {

    }
}
```

