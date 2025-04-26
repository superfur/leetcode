# 1209. 删除字符串中的所有相邻重复项 II

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，「<code>k</code> 倍重复项删除操作」将会从 <code>s</code>&nbsp;中选择&nbsp;<code>k</code>&nbsp;个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。</p>

<p>你需要对&nbsp;<code>s</code>&nbsp;重复进行无限次这样的删除操作，直到无法继续为止。</p>

<p>在执行完所有删除操作后，返回最终得到的字符串。</p>

<p>本题答案保证唯一。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcd&quot;, k = 2
<strong>输出：</strong>&quot;abcd&quot;
<strong>解释：</strong>没有要删除的内容。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;deeedbbcccbdaa&quot;, k = 3
<strong>输出：</strong>&quot;aa&quot;
<strong>解释： 
</strong>先删除 &quot;eee&quot; 和 &quot;ccc&quot;，得到 &quot;ddbbbdaa&quot;
再删除 &quot;bbb&quot;，得到 &quot;dddaa&quot;
最后删除 &quot;ddd&quot;，得到 &quot;aa&quot;</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;pbbcggttciiippooaais&quot;, k = 2
<strong>输出：</strong>&quot;ps&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>2 &lt;= k &lt;= 10^4</code></li>
	<li><code>s</code>&nbsp;中只含有小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 提示

1. Use a stack to store the characters, when there are k same characters, delete them.
2. To make it more efficient, use a pair to store the value and the count of each character.

## 示例

```
"abcd"
2
"deeedbbcccbdaa"
3
"pbbcggttciiippooaais"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeDuplicates(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeDuplicates(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
```

### C

```c
char* removeDuplicates(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveDuplicates(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function(s, k) {
    
};
```

### TypeScript

```typescript
function removeDuplicates(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function removeDuplicates($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeDuplicates(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeDuplicates(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeDuplicates(String s, int k) {
    
  }
}
```

### Go

```golang
func removeDuplicates(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def remove_duplicates(s, k)
    
end
```

### Scala

```scala
object Solution {
    def removeDuplicates(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_duplicates(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-duplicates s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec remove_duplicates(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
remove_duplicates(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_duplicates(s :: String.t, k :: integer) :: String.t
  def remove_duplicates(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeDuplicates(s: String, k: Int64): String {

    }
}
```

