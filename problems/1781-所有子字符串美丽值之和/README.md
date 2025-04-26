# 1781. 所有子字符串美丽值之和

## 题目描述

<p>一个字符串的 <strong>美丽值</strong> 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。</p>

<ul>
	<li>比方说，<code>"abaacc"</code> 的美丽值为 <code>3 - 1 = 2</code> 。</li>
</ul>

<p>给你一个字符串 <code>s</code> ，请你返回它所有子字符串的 <strong>美丽值</strong> 之和。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "aabcb"
<b>输出：</b>5
<strong>解释：</strong>美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "aabcbaa"
<b>输出：</b>17
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <=<sup> </sup>500</code></li>
	<li><code>s</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Maintain a prefix sum for the frequencies of characters.
2. You can iterate over all substring then iterate over the alphabet and find which character appears most and which appears least using the prefix sum array

## 示例

```
"aabcb"
"aabcbaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautySum(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int beautySum(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def beautySum(self, s: str) -> int:
        
```

### C

```c
int beautySum(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int BeautySum(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var beautySum = function(s) {
    
};
```

### TypeScript

```typescript
function beautySum(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function beautySum($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautySum(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautySum(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int beautySum(String s) {
    
  }
}
```

### Go

```golang
func beautySum(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def beauty_sum(s)
    
end
```

### Scala

```scala
object Solution {
    def beautySum(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beauty_sum(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (beauty-sum s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec beauty_sum(S :: unicode:unicode_binary()) -> integer().
beauty_sum(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beauty_sum(s :: String.t) :: integer
  def beauty_sum(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautySum(s: String): Int64 {

    }
}
```

