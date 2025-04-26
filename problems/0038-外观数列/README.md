# 38. 外观数列

## 题目描述

<p>「外观数列」是一个数位字符串序列，由递归公式定义：</p>

<ul>
	<li><code>countAndSay(1) = "1"</code></li>
	<li><code>countAndSay(n)</code> 是&nbsp;<code>countAndSay(n-1)</code> 的行程长度编码。</li>
</ul>

<p>&nbsp;</p>

<ul>
</ul>

<p><a href="https://baike.baidu.com/item/%E8%A1%8C%E7%A8%8B%E9%95%BF%E5%BA%A6%E7%BC%96%E7%A0%81/2931940">行程长度编码</a>（RLE）是一种字符串压缩方法，其工作原理是通过将连续相同字符（重复两次或更多次）替换为字符重复次数（运行长度）和字符的串联。例如，要压缩字符串&nbsp;<code>"3322251"</code>&nbsp;，我们将&nbsp;<code>"33"</code>&nbsp;用&nbsp;<code>"23"</code>&nbsp;替换，将&nbsp;<code>"222"</code>&nbsp;用&nbsp;<code>"32"</code>&nbsp;替换，将&nbsp;<code>"5"</code>&nbsp;用&nbsp;<code>"15"</code>&nbsp;替换并将&nbsp;<code>"1"</code>&nbsp;用&nbsp;<code>"11"</code>&nbsp;替换。因此压缩后字符串变为 <code>"23321511"</code>。</p>

<p>给定一个整数&nbsp;<code>n</code>&nbsp;，返回&nbsp;<strong>外观数列</strong>&nbsp;的第&nbsp;<code>n</code>&nbsp;个元素。</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>n = 4</p>

<p><strong>输出：</strong>"1211"</p>

<p><strong>解释：</strong></p>

<p>countAndSay(1) = "1"</p>

<p>countAndSay(2) = "1" 的行程长度编码 = "11"</p>

<p>countAndSay(3) = "11" 的行程长度编码 = "21"</p>

<p>countAndSay(4) = "21" 的行程长度编码 = "1211"</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 1</span></p>

<p><strong>输出：</strong><span class="example-io">"1"</span></p>

<p><strong>解释：</strong></p>

<p>这是基本情况。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 30</code></li>
</ul>

<p>&nbsp;</p>
<strong>进阶：</strong>你能迭代解决该问题吗？

## 难度

Medium

## 标签

- 字符串

## 提示

1. Create a helper function that maps an integer to pairs of its digits and their frequencies. For example, if you call this function with "223314444411", then it maps it to an array of pairs [[2,2], [3,2], [1,1], [4,5], [1, 2]].
2. Create another helper function that takes the array of pairs and creates a new integer. For example, if you call this function with [[2,2], [3,2], [1,1], [4,5], [1, 2]], it should create "22"+"23"+"11"+"54"+"21" = "2223115421".
3. Now, with the two helper functions, you can start with "1" and call the two functions alternatively n-1 times. The answer is the last integer you will obtain.

## 示例

```
1
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string countAndSay(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public String countAndSay(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def countAndSay(self, n: int) -> str:
        
```

### C

```c
char* countAndSay(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public string CountAndSay(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    
};
```

### TypeScript

```typescript
function countAndSay(n: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function countAndSay($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countAndSay(_ n: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countAndSay(n: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String countAndSay(int n) {
    
  }
}
```

### Go

```golang
func countAndSay(n int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String}
def count_and_say(n)
    
end
```

### Scala

```scala
object Solution {
    def countAndSay(n: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_and_say(n: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (count-and-say n)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec count_and_say(N :: integer()) -> unicode:unicode_binary().
count_and_say(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_and_say(n :: integer) :: String.t
  def count_and_say(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countAndSay(n: Int64): String {

    }
}
```

