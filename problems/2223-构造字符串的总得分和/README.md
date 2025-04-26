# 2223. 构造字符串的总得分和

## 题目描述

<p>你需要从空字符串开始&nbsp;<strong>构造</strong> 一个长度为 <code>n</code>&nbsp;的字符串 <code>s</code>&nbsp;，构造的过程为每次给当前字符串 <strong>前面</strong>&nbsp;添加 <strong>一个</strong> 字符。构造过程中得到的所有字符串编号为 <code>1</code>&nbsp;到 <code>n</code>&nbsp;，其中长度为 <code>i</code>&nbsp;的字符串编号为 <code>s<sub>i</sub></code>&nbsp;。</p>

<ul>
	<li>比方说，<code>s = "abaca"</code>&nbsp;，<code>s<sub>1</sub> == "a"</code>&nbsp;，<code>s<sub>2</sub> == "ca"</code>&nbsp;，<code>s<sub>3</sub> == "aca"</code>&nbsp;依次类推。</li>
</ul>

<p><code>s<sub>i</sub></code>&nbsp;的 <strong>得分</strong>&nbsp;为&nbsp;<code>s<sub>i</sub></code> 和&nbsp;<code>s<sub>n</sub></code>&nbsp;的 <strong>最长公共前缀</strong> 的长度（注意&nbsp;<code>s == s<sub>n</sub></code>&nbsp;）。</p>

<p>给你最终的字符串&nbsp;<code>s</code>&nbsp;，请你返回每一个<em>&nbsp;</em><code>s<sub>i</sub></code>&nbsp;的&nbsp;<strong>得分之和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "babab"
<b>输出：</b>9
<b>解释：</b>
s<sub>1</sub> == "b" ，最长公共前缀是 "b" ，得分为 1 。
s<sub>2</sub> == "ab" ，没有公共前缀，得分为 0 。
s<sub>3</sub> == "bab" ，最长公共前缀为 "bab" ，得分为 3 。
s<sub>4</sub> == "abab" ，没有公共前缀，得分为 0 。
s<sub>5</sub> == "babab" ，最长公共前缀为 "babab" ，得分为 5 。
得分和为 1 + 0 + 3 + 0 + 5 = 9 ，所以我们返回 9 。</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<b>输入：</b>s = "azbazbzaz"
<b>输出：</b>14
<b>解释：</b>
s<sub>2</sub> == "az" ，最长公共前缀为 "az" ，得分为 2 。
s<sub>6</sub> == "azbzaz" ，最长公共前缀为 "azb" ，得分为 3 。
s<sub>9</sub> == "azbazbzaz" ，最长公共前缀为 "azbazbzaz" ，得分为 9 。
其他 s<sub>i</sub> 得分均为 0 。
得分和为 2 + 3 + 9 = 14 ，所以我们返回 14 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 二分查找
- 字符串匹配
- 后缀数组
- 哈希函数
- 滚动哈希

## 提示

1. Each s_i is a suffix of the string s, so consider algorithms that can determine the longest prefix that is also a suffix.
2. Could you use the Z array from the Z algorithm to find the score of each s_i?

## 示例

```
"babab"
"azbazbzaz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long sumScores(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long sumScores(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumScores(self, s: str) -> int:
        
```

### C

```c
long long sumScores(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long SumScores(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var sumScores = function(s) {
    
};
```

### TypeScript

```typescript
function sumScores(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function sumScores($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumScores(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumScores(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumScores(String s) {
    
  }
}
```

### Go

```golang
func sumScores(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def sum_scores(s)
    
end
```

### Scala

```scala
object Solution {
    def sumScores(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_scores(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-scores s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_scores(S :: unicode:unicode_binary()) -> integer().
sum_scores(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_scores(s :: String.t) :: integer
  def sum_scores(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumScores(s: String): Int64 {

    }
}
```

