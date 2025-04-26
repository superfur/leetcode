# 面试题 01.02. 判定是否互为字符重排

## 题目描述

<p>给定两个由小写字母组成的字符串 <code>s1</code> 和 <code>s2</code>，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> <code>s1</code> = "abc", <code>s2</code> = "bca"
<strong>输出:</strong> true 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> <code>s1</code> = "abc", <code>s2</code> = "bad"
<strong>输出:</strong> false
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>0 &lt;= len(s1) &lt;= 100 </code></li>
	<li><code>0 &lt;= len(s2) &lt;= 100 </code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 排序

## 提示

1. 描述两个字符串是否互为字符重排的含义。现在，看看你提供的定义，你能否根据这个定义检查字符串
2. 有一种解法需要O(NlogN)的时间。另一种解法需要使用一些空间，但需要运行时间为O(N)
3. 散列表有用吗
4. 两个重排的字符串应该具有相同的字符，但顺序不同。你可以让它们的顺序一样吗？

## 示例

```
"abc"
"bca"
"abc"
"bad"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool CheckPermutation(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean CheckPermutation(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool CheckPermutation(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckPermutation(string s1, string s2) {
        
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
var CheckPermutation = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function CheckPermutation(s1: string, s2: string): boolean {
    
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
    function CheckPermutation($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func CheckPermutation(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun CheckPermutation(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool CheckPermutation(String s1, String s2) {
    
  }
}
```

### Go

```golang
func CheckPermutation(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_permutation(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def CheckPermutation(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_permutation(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-permutation s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec check_permutation(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_permutation(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_permutation(s1 :: String.t, s2 :: String.t) :: boolean
  def check_permutation(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func CheckPermutation(s1: String, s2: String): Bool {

    }
}
```

