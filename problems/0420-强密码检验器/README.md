# 420. 强密码检验器

## 题目描述

<p>满足以下条件的密码被认为是强密码：</p>

<ul>
	<li>由至少 <code>6</code> 个，至多 <code>20</code> 个字符组成。</li>
	<li>包含至少 <strong>一个小写 </strong>字母，至少&nbsp;<strong>一个大写</strong> 字母，和至少&nbsp;<strong>一个数字</strong> 。</li>
	<li>不包含连续三个重复字符 (比如 <code>"B<em><strong>aaa</strong></em>bb0"</code> 是弱密码, 但是&nbsp;<code>"B<em><strong>aa</strong></em>b<em><strong>a</strong></em>0"</code> 是强密码)。</li>
</ul>

<p>给你一个字符串 <code>password</code> ，返回&nbsp;<em>将 <code>password</code> 修改到满足强密码条件需要的最少修改步数。如果 <code>password</code> 已经是强密码，则返回 <code>0</code> 。</em></p>

<p>在一步修改操作中，你可以：</p>

<ul>
	<li>插入一个字符到 <code>password</code> ，</li>
	<li>从 <code>password</code> 中删除一个字符，或</li>
	<li>用另一个字符来替换 <code>password</code> 中的某个字符。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>password = "a"
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>password = "aA1"
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>password = "1337C0d3"
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= password.length &lt;= 50</code></li>
	<li><code>password</code> 由字母、数字、点 <code>'.'</code> 或者感叹号 <code>'!'</code> 组成</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 字符串
- 堆（优先队列）

## 示例

```
"a"
"aA1"
"1337C0d3"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int strongPasswordChecker(string password) {
        
    }
};
```

### Java

```java
class Solution {
    public int strongPasswordChecker(String password) {
        
    }
}
```

### Python

```python
class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
```

### C

```c
int strongPasswordChecker(char* password) {
    
}
```

### C#

```csharp
public class Solution {
    public int StrongPasswordChecker(string password) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} password
 * @return {number}
 */
var strongPasswordChecker = function(password) {
    
};
```

### TypeScript

```typescript
function strongPasswordChecker(password: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $password
     * @return Integer
     */
    function strongPasswordChecker($password) {
        
    }
}
```

### Swift

```swift
class Solution {
    func strongPasswordChecker(_ password: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun strongPasswordChecker(password: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int strongPasswordChecker(String password) {
    
  }
}
```

### Go

```golang
func strongPasswordChecker(password string) int {
    
}
```

### Ruby

```ruby
# @param {String} password
# @return {Integer}
def strong_password_checker(password)
    
end
```

### Scala

```scala
object Solution {
    def strongPasswordChecker(password: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn strong_password_checker(password: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (strong-password-checker password)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec strong_password_checker(Password :: unicode:unicode_binary()) -> integer().
strong_password_checker(Password) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec strong_password_checker(password :: String.t) :: integer
  def strong_password_checker(password) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func strongPasswordChecker(password: String): Int64 {

    }
}
```

