# 402. 移掉 K 位数字

## 题目描述

<p>给你一个以字符串表示的非负整数 <code>num</code> 和一个整数 <code>k</code> ，移除这个数中的 <code>k</code><em> </em>位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。</p>
 

<p><strong>示例 1 ：</strong></p>

<pre>
<strong>输入：</strong>num = "1432219", k = 3
<strong>输出：</strong>"1219"
<strong>解释：</strong>移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<strong>输入：</strong>num = "10200", k = 1
<strong>输出：</strong>"200"
<strong>解释：</strong>移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
</pre>

<p><strong>示例 3 ：</strong></p>

<pre>
<strong>输入：</strong>num = "10", k = 2
<strong>输出：</strong>"0"
<strong>解释：</strong>从原数字移除所有的数字，剩余为空就是 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= num.length <= 10<sup>5</sup></code></li>
	<li><code>num</code> 仅由若干位数字（0 - 9）组成</li>
	<li>除了 <strong>0</strong> 本身之外，<code>num</code> 不含任何前导零</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串
- 单调栈

## 示例

```
"1432219"
3
"10200"
1
"10"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeKdigits(String num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
```

### C

```c
char* removeKdigits(char* num, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveKdigits(string num, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    
};
```

### TypeScript

```typescript
function removeKdigits(num: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function removeKdigits($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeKdigits(_ num: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeKdigits(num: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeKdigits(String num, int k) {
    
  }
}
```

### Go

```golang
func removeKdigits(num string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {Integer} k
# @return {String}
def remove_kdigits(num, k)
    
end
```

### Scala

```scala
object Solution {
    def removeKdigits(num: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-kdigits num k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec remove_kdigits(Num :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
remove_kdigits(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_kdigits(num :: String.t, k :: integer) :: String.t
  def remove_kdigits(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeKdigits(num: String, k: Int64): String {

    }
}
```

