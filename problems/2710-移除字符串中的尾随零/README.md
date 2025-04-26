# 2710. 移除字符串中的尾随零

## 题目描述

<p>给你一个用字符串表示的正整数 <code>num</code> ，请你以字符串形式返回不含尾随零的整数<em> </em><code>num</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = "51230100"
<strong>输出：</strong>"512301"
<strong>解释：</strong>整数 "51230100" 有 2 个尾随零，移除并返回整数 "512301" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = "123"
<strong>输出：</strong>"123"
<strong>解释：</strong>整数 "123" 不含尾随零，返回整数 "123" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 1000</code></li>
	<li><code>num</code> 仅由数字 <code>0</code> 到 <code>9</code> 组成</li>
	<li><code>num</code> 不含前导零</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Find the last non-zero digit in num.

## 示例

```
"51230100"
"123"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeTrailingZeros(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeTrailingZeros(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
```

### C

```c
char* removeTrailingZeros(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveTrailingZeros(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var removeTrailingZeros = function(num) {
    
};
```

### TypeScript

```typescript
function removeTrailingZeros(num: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function removeTrailingZeros($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeTrailingZeros(_ num: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeTrailingZeros(num: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeTrailingZeros(String num) {
    
  }
}
```

### Go

```golang
func removeTrailingZeros(num string) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {String}
def remove_trailing_zeros(num)
    
end
```

### Scala

```scala
object Solution {
    def removeTrailingZeros(num: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_trailing_zeros(num: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-trailing-zeros num)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec remove_trailing_zeros(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_trailing_zeros(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_trailing_zeros(num :: String.t) :: String.t
  def remove_trailing_zeros(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeTrailingZeros(num: String): String {

    }
}
```

