# LCR 005. 最大单词长度乘积

## 题目描述

<p>给定一个字符串数组&nbsp;<code>words</code>，请计算当两个字符串 <code>words[i]</code> 和 <code>words[j]</code> 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;fxyz&quot;,&quot;abcdef&quot;]
<strong>输出：</strong>16 
<strong>解释：</strong>这两个单词为<strong> </strong>&quot;abcw&quot;, &quot;fxyz&quot;。它们不包含相同字符，且长度的乘积最大。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]
<strong>输出：</strong>4 
<strong>解释：</strong>这两个单词为 &quot;ab&quot;, &quot;cd&quot;。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]
<strong>输出：</strong>0 
<strong>解释：</strong>不存在这样的两个单词。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code>&nbsp;仅包含小写字母</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 318&nbsp;题相同：<a href="https://leetcode-cn.com/problems/maximum-product-of-word-lengths/">https://leetcode-cn.com/problems/maximum-product-of-word-lengths/</a></p>


## 难度

Medium

## 标签

- 位运算
- 数组
- 字符串

## 示例

```
["abcw","baz","foo","bar","xtfn","abcdef"]
["a","ab","abc","d","cd","bcd","abcd"]
["a","aa","aaa","aaaa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProduct(vector<string>& words) {

    }
};
```

### Java

```java
class Solution {
    public int maxProduct(String[] words) {

    }
}
```

### Python

```python
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def maxProduct(self, words: List[str]) -> int:
```

### C

```c


int maxProduct(char ** words, int wordsSize){

}
```

### C#

```csharp
public class Solution {
    public int MaxProduct(string[] words) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {

};
```

### TypeScript

```typescript
function maxProduct(words: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maxProduct($words) {

    }
}
```

### Swift

```swift
class Solution {
    func maxProduct(_ words: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProduct(words: Array<String>): Int {

    }
}
```

### Go

```golang
func maxProduct(words []string) int {

}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def max_product(words)

end
```

### Scala

```scala
object Solution {
    def maxProduct(words: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (max-product words)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec max_product(Words :: [unicode:unicode_binary()]) -> integer().
max_product(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product(words :: [String.t]) :: integer
  def max_product(words) do

  end
end
```

