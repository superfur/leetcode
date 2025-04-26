# LCR 014. 字符串的排列

## 题目描述

<p>给定两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>，写一个函数来判断 <code>s2</code> 是否包含 <code>s1</code><strong>&nbsp;</strong>的某个变位词。</p>

<p>换句话说，第一个字符串的排列之一是第二个字符串的 <strong>子串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<strong>输出: </strong>True
<strong>解释:</strong> s2 包含 s1 的排列之一 (&quot;ba&quot;).
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> 和 <code>s2</code> 仅包含小写字母</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 567&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/permutation-in-string/">https://leetcode-cn.com/problems/permutation-in-string/</a></p>


## 难度

Medium

## 标签

- 哈希表
- 双指针
- 字符串
- 滑动窗口

## 示例

```
"ab"
"eidbaooo"
"ab"
"eidboaoo"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {

    }
};
```

### Java

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {

    }
}
```

### Python

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
```

### C

```c


bool checkInclusion(char * s1, char * s2){

}
```

### C#

```csharp
public class Solution {
    public bool CheckInclusion(string s1, string s2) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {

};
```

### TypeScript

```typescript
function checkInclusion(s1: string, s2: string): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkInclusion($s1, $s2) {

    }
}
```

### Swift

```swift
class Solution {
    func checkInclusion(_ s1: String, _ s2: String) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {

    }
}
```

### Go

```golang
func checkInclusion(s1 string, s2 string) bool {

}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_inclusion(s1, s2)

end
```

### Scala

```scala
object Solution {
    def checkInclusion(s1: String, s2: String): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {

    }
}
```

### Racket

```racket
(define/contract (check-inclusion s1 s2)
  (-> string? string? boolean?)

  )
```

### Erlang

```erlang
-spec check_inclusion(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_inclusion(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_inclusion(s1 :: String.t, s2 :: String.t) :: boolean
  def check_inclusion(s1, s2) do

  end
end
```

