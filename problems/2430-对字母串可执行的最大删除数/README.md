# 2430. 对字母串可执行的最大删除数

## 题目描述

<p>给你一个仅由小写英文字母组成的字符串 <code>s</code> 。在一步操作中，你可以：</p>

<ul>
	<li>删除 <strong>整个字符串</strong> <code>s</code> ，或者</li>
	<li>对于满足&nbsp;<code>1 &lt;= i &lt;= s.length / 2</code> 的任意 <code>i</code> ，如果 <code>s</code> 中的 <strong>前</strong> <code>i</code> 个字母和接下来的 <code>i</code> 个字母 <strong>相等</strong> ，删除 <strong>前</strong> <code>i</code> 个字母。</li>
</ul>

<p>例如，如果 <code>s = "ababc"</code> ，那么在一步操作中，你可以删除 <code>s</code> 的前两个字母得到 <code>"abc"</code> ，因为 <code>s</code> 的前两个字母和接下来的两个字母都等于 <code>"ab"</code> 。</p>

<p>返回删除 <code>s</code> 所需的最大操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcabcdabc"
<strong>输出：</strong>2
<strong>解释：</strong>
- 删除前 3 个字母（"abc"），因为它们和接下来 3 个字母相等。现在，s = "abcdabc"。
- 删除全部字母。
一共用了 2 步操作，所以返回 2 。可以证明 2 是所需的最大操作数。
注意，在第二步操作中无法再次删除 "abc" ，因为 "abc" 的下一次出现并不是位于接下来的 3 个字母。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabaab"
<strong>输出：</strong>4
<strong>解释：</strong>
- 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "aabaab"。
- 删除前 3 个字母（"aab"），因为它们和接下来 3 个字母相等。现在，s = "aab"。 
- 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "ab"。
- 删除全部字母。
一共用了 4 步操作，所以返回 4 。可以证明 4 是所需的最大操作数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "aaaaa"
<strong>输出：</strong>5
<strong>解释：</strong>在每一步操作中，都可以仅删除 s 的第一个字母。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. We can use dynamic programming to find the answer. Create a 0-indexed dp array where dp[i] represents the maximum number of moves needed to remove the first i + 1 letters from s.
2. What should we do if there is an i where it is impossible to remove the first i + 1 letters?
3. Use a sentinel value such as -1 to show that it is impossible.
4. How can we quickly determine if two substrings of s are equal? We can use hashing.

## 示例

```
"abcabcdabc"
"aaabaab"
"aaaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int deleteString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int deleteString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def deleteString(self, s: str) -> int:
        
```

### C

```c
int deleteString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int DeleteString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var deleteString = function(s) {
    
};
```

### TypeScript

```typescript
function deleteString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function deleteString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func deleteString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun deleteString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int deleteString(String s) {
    
  }
}
```

### Go

```golang
func deleteString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def delete_string(s)
    
end
```

### Scala

```scala
object Solution {
    def deleteString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn delete_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (delete-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec delete_string(S :: unicode:unicode_binary()) -> integer().
delete_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec delete_string(s :: String.t) :: integer
  def delete_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func deleteString(s: String): Int64 {

    }
}
```

