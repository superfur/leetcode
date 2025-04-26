# 3106. 满足距离约束且字典序最小的字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> 。</p>

<p>定义函数 <code>distance(s<sub>1</sub>, s<sub>2</sub>)</code> ，用于衡量两个长度为 <code>n</code> 的字符串 <code>s<sub>1</sub></code> 和 <code>s<sub>2</sub></code> 之间的距离，即：</p>

<ul>
	<li>字符 <code>'a'</code> 到 <code>'z'</code> 按 <strong>循环 </strong>顺序排列，对于区间 <code>[0, n - 1]</code> 中的 <code>i</code> ，计算所有「 <code>s<sub>1</sub>[i]</code> 和 <code>s<sub>2</sub>[i]</code> 之间<strong> 最小距离</strong>」的 <strong>和 </strong>。</li>
</ul>

<p>例如，<code>distance("ab", "cd") == 4</code> ，且 <code>distance("a", "z") == 1</code> 。</p>

<p>你可以对字符串 <code>s</code> 执行<strong> 任意次 </strong>操作。在每次操作中，可以将 <code>s</code> 中的一个字母 <strong>改变 </strong>为<strong> 任意 </strong>其他小写英文字母。</p>

<p>返回一个字符串，表示在执行一些操作后你可以得到的 <strong>字典序最小</strong> 的字符串 <code>t</code> ，且满足 <code>distance(s, t) &lt;= k</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "zbbz", k = 3
<strong>输出：</strong>"aaaz"
<strong>解释：</strong>在这个例子中，可以执行以下操作：
将 s[0] 改为 'a' ，s 变为 "abbz" 。
将 s[1] 改为 'a' ，s 变为 "aabz" 。
将 s[2] 改为 'a' ，s 变为 "aaaz" 。
"zbbz" 和 "aaaz" 之间的距离等于 k = 3 。
可以证明 "aaaz" 是在任意次操作后能够得到的字典序最小的字符串。
因此，答案是 "aaaz" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "xaxcd", k = 4
<strong>输出：</strong>"aawcd"
<strong>解释：</strong>在这个例子中，可以执行以下操作：
将 s[0] 改为 'a' ，s 变为 "aaxcd" 。
将 s[2] 改为 'w' ，s 变为 "aawcd" 。
"xaxcd" 和 "aawcd" 之间的距离等于 k = 4 。
可以证明 "aawcd" 是在任意次操作后能够得到的字典序最小的字符串。
因此，答案是 "aawcd" 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "lol", k = 0
<strong>输出：</strong>"lol"
<strong>解释：</strong>在这个例子中，k = 0，更改任何字符都会使得距离大于 0 。
因此，答案是 "lol" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2000</code></li>
	<li><code>s</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. The problem can be approached greedily.
2. For each index in order from <code>0</code> to <code>n - 1</code>, we try all letters from <code>'a'</code> to <code>'z'</code>, selecting the first one as long as the current total distance accumulated is not larger than <code>k</code>.

## 示例

```
"zbbz"
3
"xaxcd"
4
"lol"
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getSmallestString(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String getSmallestString(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSmallestString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
```

### C

```c
char* getSmallestString(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetSmallestString(string s, int k) {
        
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
var getSmallestString = function(s, k) {
    
};
```

### TypeScript

```typescript
function getSmallestString(s: string, k: number): string {
    
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
    function getSmallestString($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSmallestString(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSmallestString(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getSmallestString(String s, int k) {
    
  }
}
```

### Go

```golang
func getSmallestString(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def get_smallest_string(s, k)
    
end
```

### Scala

```scala
object Solution {
    def getSmallestString(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_smallest_string(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-smallest-string s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec get_smallest_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
get_smallest_string(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(s :: String.t, k :: integer) :: String.t
  def get_smallest_string(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSmallestString(s: String, k: Int64): String {

    }
}
```

