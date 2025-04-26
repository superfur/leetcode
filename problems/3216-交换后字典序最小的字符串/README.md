# 3216. 交换后字典序最小的字符串

## 题目描述

<p>给你一个仅由数字组成的字符串 <code>s</code>，在最多交换一次 <strong>相邻 </strong>且具有相同 <strong>奇偶性 </strong>的数字后，返回可以得到的<span data-keyword="lexicographically-smaller-string">字典序最小的字符串</span>。</p>

<p>如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "45320"</span></p>

<p><strong>输出：</strong> <span class="example-io">"43520"</span></p>

<p><strong>解释：</strong></p>

<p><code>s[1] == '5'</code> 和 <code>s[2] == '3'</code> 都具有相同的奇偶性，交换它们可以得到字典序最小的字符串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "001"</span></p>

<p><strong>输出：</strong> <span class="example-io">"001"</span></p>

<p><strong>解释：</strong></p>

<p>无需进行交换，因为 <code>s</code> 已经是字典序最小的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由数字组成。</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串

## 提示

1. Try all possible swaps satisfying the constraints and find the one that results in the lexicographically smallest string.

## 示例

```
"45320"
"001"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getSmallestString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String getSmallestString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getSmallestString(self, s: str) -> str:
        
```

### C

```c
char* getSmallestString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetSmallestString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var getSmallestString = function(s) {
    
};
```

### TypeScript

```typescript
function getSmallestString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function getSmallestString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSmallestString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSmallestString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getSmallestString(String s) {
    
  }
}
```

### Go

```golang
func getSmallestString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def get_smallest_string(s)
    
end
```

### Scala

```scala
object Solution {
    def getSmallestString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-smallest-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec get_smallest_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
get_smallest_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(s :: String.t) :: String.t
  def get_smallest_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSmallestString(s: String): String {

    }
}
```

