# 899. 有序队列

## 题目描述

<p>给定一个字符串 <code>s</code> 和一个整数 <code>k</code>&nbsp;。你可以从 <code>s</code> 的前 <code>k</code> 个字母中选择一个，并把它加到字符串的末尾。</p>

<p>返回 <em>在应用上述步骤的任意数量的移动后，字典序最小的字符串&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "cba", k = 1
<strong>输出：</strong>"acb"
<strong>解释：</strong>
在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "baaca", k = 3
<strong>输出：</strong>"aaabc"
<strong>解释：
</strong>在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k&nbsp;&lt;= S.length&nbsp;&lt;= 1000</code></li>
	<li><code>s</code>&nbsp;只由小写字母组成。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 排序

## 示例

```
"cba"
1
"baaca"
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string orderlyQueue(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String orderlyQueue(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
```

### C

```c
char* orderlyQueue(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string OrderlyQueue(string s, int k) {
        
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
var orderlyQueue = function(s, k) {
    
};
```

### TypeScript

```typescript
function orderlyQueue(s: string, k: number): string {
    
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
    function orderlyQueue($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func orderlyQueue(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun orderlyQueue(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String orderlyQueue(String s, int k) {
    
  }
}
```

### Go

```golang
func orderlyQueue(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def orderly_queue(s, k)
    
end
```

### Scala

```scala
object Solution {
    def orderlyQueue(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (orderly-queue s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec orderly_queue(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
orderly_queue(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec orderly_queue(s :: String.t, k :: integer) :: String.t
  def orderly_queue(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func orderlyQueue(s: String, k: Int64): String {

    }
}
```

