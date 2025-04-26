# 115. 不同的子序列

## 题目描述

<p>给你两个字符串 <code>s</code><strong> </strong>和 <code>t</code> ，统计并返回在 <code>s</code> 的 <strong>子序列</strong> 中 <code>t</code> 出现的个数。</p>

<p>测试用例保证结果在 32 位有符号整数范围内。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>s = "rabbbit", t = "rabbit"<code>
<strong>输出</strong></code><strong>：</strong><code>3
</code><strong>解释：</strong>
如下所示, 有 3 种可以从 s 中得到 <code>"rabbit" 的方案</code>。
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code></pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>s = "babgbag", t = "bag"
<code><strong>输出</strong></code><strong>：</strong><code>5
</code><strong>解释：</strong>
如下所示, 有 5 种可以从 s 中得到 <code>"bag" 的方案</code>。 
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 示例

```
"rabbbit"
"rabbit"
"babgbag"
"bag"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int numDistinct(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
```

### C

```c
int numDistinct(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumDistinct(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    
};
```

### TypeScript

```typescript
function numDistinct(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function numDistinct($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numDistinct(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numDistinct(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numDistinct(String s, String t) {
    
  }
}
```

### Go

```golang
func numDistinct(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def num_distinct(s, t)
    
end
```

### Scala

```scala
object Solution {
    def numDistinct(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-distinct s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_distinct(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
num_distinct(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_distinct(s :: String.t, t :: String.t) :: integer
  def num_distinct(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numDistinct(s: String, t: String): Int64 {

    }
}
```

