# LCR 164. 破解闯关密码

## 题目描述

<p>闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：</p>

<ul>
	<li>一个拥有密码所有元素的非负整数数组 <code>password</code></li>
	<li>密码是 <code>password</code> 中所有元素拼接后得到的最小的一个数</li>
</ul>

<p>请编写一个程序返回这个密码。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>password = [15, 8, 7]
<strong>输出：</strong>"1578"</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>password = [0, 3, 30, 34, 5, 9]
<strong>输出：</strong>"03033459"</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt; password.length &lt;= 100</code></li>
</ul>

<p><strong>说明: </strong></p>

<ul>
	<li>输出结果可能非常大，所以你需要返回一个字符串而不是整数</li>
	<li>拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 排序

## 示例

```
[15,8,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string crackPassword(vector<int>& password) {
        
    }
};
```

### Java

```java
class Solution {
    public String crackPassword(int[] password) {
        
    }
}
```

### Python

```python
class Solution(object):
    def crackPassword(self, password):
        """
        :type password: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def crackPassword(self, password: List[int]) -> str:
        
```

### C

```c
char* crackPassword(int* password, int passwordSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string CrackPassword(int[] password) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} password
 * @return {string}
 */
var crackPassword = function(password) {
    
};
```

### TypeScript

```typescript
function crackPassword(password: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $password
     * @return String
     */
    function crackPassword($password) {
        
    }
}
```

### Swift

```swift
class Solution {
    func crackPassword(_ password: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun crackPassword(password: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String crackPassword(List<int> password) {
    
  }
}
```

### Go

```golang
func crackPassword(password []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} password
# @return {String}
def crack_password(password)
    
end
```

### Scala

```scala
object Solution {
    def crackPassword(password: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn crack_password(password: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (crack-password password)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec crack_password(Password :: [integer()]) -> unicode:unicode_binary().
crack_password(Password) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec crack_password(password :: [integer]) :: String.t
  def crack_password(password) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func crackPassword(password: Array<Int64>): String {

    }
}
```

