# 1374. 生成每种字符都是奇数个的字符串

## 题目描述

<p>给你一个整数 <code>n</code>，请你返回一个含<em> <code>n</code> </em>个字符的字符串，其中每种字符在该字符串中都恰好出现 <strong>奇数次</strong> <em><strong>。</strong></em></p>

<p>返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>&quot;pppz&quot;
<strong>解释：</strong>&quot;pppz&quot; 是一个满足题目要求的字符串，因为 &#39;p&#39; 出现 3 次，且 &#39;z&#39; 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如：&quot;ohhh&quot; 和 &quot;love&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>&quot;xy&quot;
<strong>解释：</strong>&quot;xy&quot; 是一个满足题目要求的字符串，因为 &#39;x&#39; 和 &#39;y&#39; 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如：&quot;ag&quot; 和 &quot;ur&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 7
<strong>输出：</strong>&quot;holasss&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. If n is odd, return a string of size n formed only by 'a', else return string formed with n-1 'a' and 1 'b''.

## 示例

```
4
2
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string generateTheString(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public String generateTheString(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def generateTheString(self, n: int) -> str:
        
```

### C

```c
char* generateTheString(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public string GenerateTheString(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    
};
```

### TypeScript

```typescript
function generateTheString(n: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function generateTheString($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func generateTheString(_ n: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun generateTheString(n: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String generateTheString(int n) {
    
  }
}
```

### Go

```golang
func generateTheString(n int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String}
def generate_the_string(n)
    
end
```

### Scala

```scala
object Solution {
    def generateTheString(n: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn generate_the_string(n: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (generate-the-string n)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec generate_the_string(N :: integer()) -> unicode:unicode_binary().
generate_the_string(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec generate_the_string(n :: integer) :: String.t
  def generate_the_string(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func generateTheString(n: Int64): String {

    }
}
```

