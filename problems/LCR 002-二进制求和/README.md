# LCR 002. 二进制求和

## 题目描述

<p>给定两个 01 字符串&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>&nbsp;，请计算它们的和，并以二进制字符串的形式输出。</p>

<p>输入为 <strong>非空 </strong>字符串且只包含数字&nbsp;<code>1</code>&nbsp;和&nbsp;<code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> a = &quot;11&quot;, b = &quot;10&quot;
<strong>输出:</strong> &quot;101&quot;</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> a = &quot;1010&quot;, b = &quot;1011&quot;
<strong>输出:</strong> &quot;10101&quot;</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个字符串仅由字符 <code>&#39;0&#39;</code> 或 <code>&#39;1&#39;</code> 组成。</li>
	<li><code>1 &lt;= a.length, b.length &lt;= 10^4</code></li>
	<li>字符串如果不是 <code>&quot;0&quot;</code> ，就都不含前导零。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 67&nbsp;题相同：<a href="https://leetcode-cn.com/problems/add-binary/">https://leetcode-cn.com/problems/add-binary/</a></p>


## 难度

Easy

## 标签

- 位运算
- 数学
- 字符串
- 模拟

## 示例

```
"11"
"10"
"1010"
"1011"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string addBinary(string a, string b) {

    }
};
```

### Java

```java
class Solution {
    public String addBinary(String a, String b) {

    }
}
```

### Python

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
```

### Python3

```python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
```

### C

```c


char * addBinary(char * a, char * b){

}
```

### C#

```csharp
public class Solution {
    public string AddBinary(string a, string b) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {

};
```

### TypeScript

```typescript
function addBinary(a: string, b: string): string {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return String
     */
    function addBinary($a, $b) {

    }
}
```

### Swift

```swift
class Solution {
    func addBinary(_ a: String, _ b: String) -> String {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addBinary(a: String, b: String): String {

    }
}
```

### Go

```golang
func addBinary(a string, b string) string {

}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)

end
```

### Scala

```scala
object Solution {
    def addBinary(a: String, b: String): String = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {

    }
}
```

### Racket

```racket
(define/contract (add-binary a b)
  (-> string? string? string?)

  )
```

### Erlang

```erlang
-spec add_binary(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> unicode:unicode_binary().
add_binary(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_binary(a :: String.t, b :: String.t) :: String.t
  def add_binary(a, b) do

  end
end
```

