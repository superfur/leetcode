# 3438. 找到字符串中合法的相邻数字

## 题目描述

<p>给你一个只包含数字的字符串&nbsp;<code>s</code>&nbsp;。如果 <code>s</code>&nbsp;中两个 <strong>相邻</strong>&nbsp;的数字满足以下条件，我们称它们是 <strong>合法的</strong>&nbsp;：</p>

<ul>
	<li>前面的数字 <strong>不等于</strong> 第二个数字。</li>
	<li>两个数字在 <code>s</code>&nbsp;中出现的次数 <strong>恰好</strong>&nbsp;分别等于这个数字本身。</li>
</ul>

<p>请你从左到右遍历字符串 <code>s</code>&nbsp;，并返回最先找到的 <strong>合法</strong>&nbsp;相邻数字。如果这样的相邻数字不存在，请你返回一个空字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "2523533"</span></p>

<p><span class="example-io"><b>输出：</b>"23"</span></p>

<p><strong>解释：</strong></p>

<p>数字&nbsp;<code>'2'</code>&nbsp;出现 2 次，数字&nbsp;<code>'3'</code>&nbsp;出现 3 次。<code>"23"</code>&nbsp;中每个数字在 <code>s</code>&nbsp;中出现的次数都恰好分别等于数字本身。所以输出&nbsp;<code>"23"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "221"</span></p>

<p><span class="example-io"><b>输出：</b>"21"</span></p>

<p><strong>解释：</strong></p>

<p>数字&nbsp;<code>'2'</code>&nbsp;出现 2 次，数字&nbsp;<code>'1'</code>&nbsp;出现 1 次。所以输出&nbsp;<code>"21"</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "22"</span></p>

<p><span class="example-io"><b>输出：</b>""</span></p>

<p><strong>解释：</strong></p>

<p>没有合法的相邻数字。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;只包含&nbsp;<code>'1'</code> 到&nbsp;<code>'9'</code> 的数字。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Use a HashMap to count the frequency of each digit.

## 示例

```
"2523533"
"221"
"22"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findValidPair(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String findValidPair(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findValidPair(self, s: str) -> str:
        
```

### C

```c
char* findValidPair(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindValidPair(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var findValidPair = function(s) {
    
};
```

### TypeScript

```typescript
function findValidPair(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function findValidPair($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findValidPair(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findValidPair(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findValidPair(String s) {
    
  }
}
```

### Go

```golang
func findValidPair(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def find_valid_pair(s)
    
end
```

### Scala

```scala
object Solution {
    def findValidPair(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_valid_pair(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-valid-pair s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec find_valid_pair(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
find_valid_pair(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_valid_pair(s :: String.t) :: String.t
  def find_valid_pair(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findValidPair(s: String): String {

    }
}
```

