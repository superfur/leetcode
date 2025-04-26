# 1745. 分割回文串 IV

## 题目描述

<p>给你一个字符串 <code>s</code> ，如果可以将它分割成三个 <strong>非空</strong> 回文子字符串，那么返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>当一个字符串正着读和反着读是一模一样的，就称其为 <strong>回文字符串</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "abcbdd"
<b>输出：</b>true
<strong>解释：</strong>"abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "bcbddxy"
<b>输出：</b>false
<strong>解释：</strong>s 没办法被分割成 3 个回文子字符串。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= s.length <= 2000</code></li>
	<li><code>s</code>​​​​​​ 只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Preprocess checking palindromes in O(1)
2. Note that one string is a prefix and another one is a suffix you can try brute forcing the rest

## 示例

```
"abcbdd"
"bcbddxy"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkPartitioning(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkPartitioning(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        
```

### C

```c
bool checkPartitioning(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckPartitioning(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkPartitioning = function(s) {
    
};
```

### TypeScript

```typescript
function checkPartitioning(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkPartitioning($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkPartitioning(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkPartitioning(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkPartitioning(String s) {
    
  }
}
```

### Go

```golang
func checkPartitioning(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_partitioning(s)
    
end
```

### Scala

```scala
object Solution {
    def checkPartitioning(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_partitioning(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-partitioning s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_partitioning(S :: unicode:unicode_binary()) -> boolean().
check_partitioning(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_partitioning(s :: String.t) :: boolean
  def check_partitioning(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkPartitioning(s: String): Bool {

    }
}
```

