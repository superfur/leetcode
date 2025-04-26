# LCR 182. 动态口令

## 题目描述

<p>某公司门禁密码使用动态口令技术。初始密码为字符串 <code>password</code>，密码更新均遵循以下步骤：</p>

<ul>
	<li>设定一个正整数目标值 <code>target</code></li>
	<li>将 <code>password</code> 前 <code>target</code> 个字符按原顺序移动至字符串末尾</li>
</ul>

<p>请返回更新后的密码字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> password = "s3cur1tyC0d3", target = 4
<strong>输出:</strong> "r1tyC0d3s3cu"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> password = "lrloseumgh", target = 6
<strong>输出:&nbsp;</strong>"umghlrlose"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target&nbsp;&lt; password.length &lt;= 10000</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数学
- 双指针
- 字符串

## 示例

```
"s3cur1tyC0d3"
4
"vbzkgsaoiu"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string dynamicPassword(string password, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public String dynamicPassword(String password, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        
```

### C

```c
char* dynamicPassword(char* password, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public string DynamicPassword(string password, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} password
 * @param {number} target
 * @return {string}
 */
var dynamicPassword = function(password, target) {
    
};
```

### TypeScript

```typescript
function dynamicPassword(password: string, target: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $password
     * @param Integer $target
     * @return String
     */
    function dynamicPassword($password, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dynamicPassword(_ password: String, _ target: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dynamicPassword(password: String, target: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String dynamicPassword(String password, int target) {
    
  }
}
```

### Go

```golang
func dynamicPassword(password string, target int) string {
    
}
```

### Ruby

```ruby
# @param {String} password
# @param {Integer} target
# @return {String}
def dynamic_password(password, target)
    
end
```

### Scala

```scala
object Solution {
    def dynamicPassword(password: String, target: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dynamic_password(password: String, target: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (dynamic-password password target)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec dynamic_password(Password :: unicode:unicode_binary(), Target :: integer()) -> unicode:unicode_binary().
dynamic_password(Password, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dynamic_password(password :: String.t, target :: integer) :: String.t
  def dynamic_password(password, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dynamicPassword(password: String, target: Int64): String {

    }
}
```

