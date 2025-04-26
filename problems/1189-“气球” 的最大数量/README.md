# 1189. “气球” 的最大数量

## 题目描述

<p>给你一个字符串&nbsp;<code>text</code>，你需要使用 <code>text</code> 中的字母来拼凑尽可能多的单词&nbsp;<strong>"balloon"（气球）</strong>。</p>

<p>字符串&nbsp;<code>text</code> 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词&nbsp;<strong>"balloon"</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/14/1536_ex1_upd.jpeg" style="height: 35px; width: 154px;" /></strong></p>

<pre>
<strong>输入：</strong>text = "nlaebolko"
<strong>输出：</strong>1
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/14/1536_ex2_upd.jpeg" style="height: 35px; width: 233px;" /></strong></p>

<pre>
<strong>输入：</strong>text = "loonbalxballpoon"
<strong>输出：</strong>2
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>text = "leetcode"
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code>&nbsp;全部由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/rearrange-characters-to-make-target-string/">2287. 重排字符形成目标字符串</a>&nbsp;相同。</p>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Count the frequency of letters in the given string.
2. Find the letter than can make the minimum number of instances of the word "balloon".

## 示例

```
"nlaebolko"
"loonbalxballpoon"
"leetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNumberOfBalloons(String text) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
```

### C

```c
int maxNumberOfBalloons(char* text) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNumberOfBalloons(string text) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    
};
```

### TypeScript

```typescript
function maxNumberOfBalloons(text: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function maxNumberOfBalloons($text) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumberOfBalloons(_ text: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNumberOfBalloons(String text) {
    
  }
}
```

### Go

```golang
func maxNumberOfBalloons(text string) int {
    
}
```

### Ruby

```ruby
# @param {String} text
# @return {Integer}
def max_number_of_balloons(text)
    
end
```

### Scala

```scala
object Solution {
    def maxNumberOfBalloons(text: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-number-of-balloons text)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_number_of_balloons(Text :: unicode:unicode_binary()) -> integer().
max_number_of_balloons(Text) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_number_of_balloons(text :: String.t) :: integer
  def max_number_of_balloons(text) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumberOfBalloons(text: String): Int64 {

    }
}
```

