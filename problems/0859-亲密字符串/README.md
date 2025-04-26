# 859. 亲密字符串

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>goal</code> ，只要我们可以通过交换 <code>s</code> 中的两个字母得到与 <code>goal</code> 相等的结果，就返回&nbsp;<code>true</code>&nbsp;；否则返回 <code>false</code> 。</p>

<p>交换字母的定义是：取两个下标 <code>i</code> 和 <code>j</code> （下标从 <code>0</code> 开始）且满足 <code>i != j</code> ，接着交换 <code>s[i]</code> 和 <code>s[j]</code> 处的字符。</p>

<ul>
	<li>例如，在 <code>"abcd"</code> 中交换下标 <code>0</code> 和下标 <code>2</code> 的元素可以生成 <code>"cbad"</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ab", goal = "ba"
<strong>输出：</strong>true
<strong>解释：</strong>你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ab", goal = "ab"
<strong>输出：</strong>false
<strong>解释：</strong>你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "aa", goal = "aa"
<strong>输出：</strong>true
<strong>解释：</strong>你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>s</code> 和 <code>goal</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 示例

```
"ab"
"ba"
"ab"
"ab"
"aa"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean buddyStrings(String s, String goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
```

### C

```c
bool buddyStrings(char* s, char* goal) {
    
}
```

### C#

```csharp
public class Solution {
    public bool BuddyStrings(string s, string goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
    
};
```

### TypeScript

```typescript
function buddyStrings(s: string, goal: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function buddyStrings($s, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func buddyStrings(_ s: String, _ goal: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun buddyStrings(s: String, goal: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool buddyStrings(String s, String goal) {
    
  }
}
```

### Go

```golang
func buddyStrings(s string, goal string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} goal
# @return {Boolean}
def buddy_strings(s, goal)
    
end
```

### Scala

```scala
object Solution {
    def buddyStrings(s: String, goal: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (buddy-strings s goal)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec buddy_strings(S :: unicode:unicode_binary(), Goal :: unicode:unicode_binary()) -> boolean().
buddy_strings(S, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec buddy_strings(s :: String.t, goal :: String.t) :: boolean
  def buddy_strings(s, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func buddyStrings(s: String, goal: String): Bool {

    }
}
```

