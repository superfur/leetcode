# LCR 167. 招式拆解 I

## 题目描述

<p>某套连招动作记作序列 <code>arr</code>，其中 <code>arr[i]</code> 为第 <code>i</code> 个招式的名字。请返回 <code>arr</code> 中最多可以出连续不重复的多少个招式。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = "dbascDdad"
<strong>输出：</strong>6
<strong>解释：</strong>因为连续且最长的招式序列是 "dbascD" 或 "bascDd"，所以其长度为 6。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = "KKK"
<strong>输出：</strong>1
<strong>解释：</strong>因为无重复字符的最长子串是 <code>"K"</code>，所以其长度为 1。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = "pwwkew"
<strong>输出：</strong>3
<strong>解释：</strong>因为连续且最长的招式序列是 "wke"，所以其长度为 3。&nbsp;    
请注意区分 <strong>子串</strong> 与 <strong>子序列</strong> 的概念：你的答案必须是 <strong>连续招式</strong> 的长度，也就是 <strong>子串</strong>。而 "pwke" 是一个非连续的 <strong>子序列</strong>，不是 <strong>子串</strong>。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 40000</code></li>
	<li><code>arr</code> 由英文字母、数字、符号和空格组成。</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 3 题相同：<a href="https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/">https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/</a></p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 示例

```
"dbascDdad"
"KKK"
"pwwkew"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int dismantlingAction(string arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int dismantlingAction(String arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dismantlingAction(self, arr):
        """
        :type arr: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def dismantlingAction(self, arr: str) -> int:
        
```

### C

```c
int dismantlingAction(char* arr) {
    
}
```

### C#

```csharp
public class Solution {
    public int DismantlingAction(string arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} arr
 * @return {number}
 */
var dismantlingAction = function(arr) {
    
};
```

### TypeScript

```typescript
function dismantlingAction(arr: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $arr
     * @return Integer
     */
    function dismantlingAction($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dismantlingAction(_ arr: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dismantlingAction(arr: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int dismantlingAction(String arr) {
    
  }
}
```

### Go

```golang
func dismantlingAction(arr string) int {
    
}
```

### Ruby

```ruby
# @param {String} arr
# @return {Integer}
def dismantling_action(arr)
    
end
```

### Scala

```scala
object Solution {
    def dismantlingAction(arr: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dismantling_action(arr: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (dismantling-action arr)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec dismantling_action(Arr :: unicode:unicode_binary()) -> integer().
dismantling_action(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dismantling_action(arr :: String.t) :: integer
  def dismantling_action(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dismantlingAction(arr: String): Int64 {

    }
}
```

