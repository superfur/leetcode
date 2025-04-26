# 483. 最小好进制

## 题目描述

<p>以字符串的形式给出 <code>n</code>&nbsp;, 以字符串的形式返回<em> <code>n</code> 的最小 <strong>好进制</strong> </em>&nbsp;。</p>

<p>如果 <code>n</code> 的 &nbsp;<code>k(k&gt;=2)</code>&nbsp;进制数的所有数位全为1，则称&nbsp;<code>k(k&gt;=2)</code>&nbsp;是 <code>n</code> 的一个&nbsp;<strong>好进制&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = "13"
<strong>输出：</strong>"3"
<strong>解释：</strong>13 的 3 进制是 111。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = "4681"
<strong>输出：</strong>"8"
<strong>解释：</strong>4681 的 8 进制是 11111。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = "1000000000000000000"
<strong>输出：</strong>"999999999999999999"
<strong>解释：</strong>1000000000000000000 的 999999999999999999 进制是 11。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n</code> 的取值范围是&nbsp;<code>[3, 10<sup>18</sup>]</code></li>
	<li><code>n</code> 没有前导 0</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 二分查找

## 示例

```
"13"
"4681"
"1000000000000000000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestGoodBase(string n) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestGoodBase(String n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        
```

### C

```c
char* smallestGoodBase(char* n) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestGoodBase(string n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} n
 * @return {string}
 */
var smallestGoodBase = function(n) {
    
};
```

### TypeScript

```typescript
function smallestGoodBase(n: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $n
     * @return String
     */
    function smallestGoodBase($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestGoodBase(_ n: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestGoodBase(n: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestGoodBase(String n) {
    
  }
}
```

### Go

```golang
func smallestGoodBase(n string) string {
    
}
```

### Ruby

```ruby
# @param {String} n
# @return {String}
def smallest_good_base(n)
    
end
```

### Scala

```scala
object Solution {
    def smallestGoodBase(n: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_good_base(n: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-good-base n)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec smallest_good_base(N :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_good_base(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_good_base(n :: String.t) :: String.t
  def smallest_good_base(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestGoodBase(n: String): String {

    }
}
```

