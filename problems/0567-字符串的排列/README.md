# 567. 字符串的排列

## 题目描述

<p>给你两个字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code> ，写一个函数来判断 <code>s2</code> 是否包含 <code>s1</code><strong>&nbsp;</strong>的 <span data-keyword="permutation-string">排列</span>。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>换句话说，<code>s1</code> 的排列之一是 <code>s2</code> 的 <strong>子串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "ab" s2 = "eidbaooo"
<strong>输出：</strong>true
<strong>解释：</strong>s2 包含 s1 的排列之一 ("ba").
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1= "ab" s2 = "eidboaoo"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> 和 <code>s2</code> 仅包含小写字母</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 双指针
- 字符串
- 滑动窗口

## 提示

1. Obviously, brute force will result in TLE. Think of something else.
2. How will you check whether one string is a permutation of another string?
3. One way is to sort the string and then compare. But, Is there a better way?
4. If one string is a permutation of another string then they must have one common metric. What is that?
5. Both strings must have same character frequencies, if  one is permutation of another. Which data structure should be used to store frequencies?
6. What about hash table?  An array of size 26?

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
bool checkInclusion(char* s1, char* s2) {
    
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

### Dart

```dart
class Solution {
  bool checkInclusion(String s1, String s2) {
    
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

### Cangjie

```cangjie
class Solution {
    func checkInclusion(s1: String, s2: String): Bool {

    }
}
```

