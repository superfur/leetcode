# 804. 唯一摩尔斯密码词

## 题目描述

<p>国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串，&nbsp;比如:</p>

<ul>
	<li><code>'a'</code> 对应 <code>".-"</code> ，</li>
	<li><code>'b'</code> 对应 <code>"-..."</code> ，</li>
	<li><code>'c'</code> 对应 <code>"-.-."</code> ，以此类推。</li>
</ul>

<p>为了方便，所有 <code>26</code> 个英文字母的摩尔斯密码表如下：</p>

<pre>
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]</pre>

<p>给你一个字符串数组 <code>words</code> ，每个单词可以写成每个字母对应摩尔斯密码的组合。</p>

<ul>
	<li>例如，<code>"cab"</code> 可以写成 <code>"-.-..--..."</code> ，(即 <code>"-.-."</code> + <code>".-"</code> + <code>"-..."</code> 字符串的结合)。我们将这样一个连接过程称作 <strong>单词翻译</strong> 。</li>
</ul>

<p>对<strong> </strong><code>words</code> 中所有单词进行单词翻译，返回不同 <strong>单词翻译</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> words = ["gin", "zen", "gig", "msg"]
<strong>输出:</strong> 2
<strong>解释: </strong>
各单词翻译如下:
"gin" -&gt; "--...-."
"zen" -&gt; "--...-."
"gig" -&gt; "--...--."
"msg" -&gt; "--...--."

共有 2 种不同翻译, "--...-." 和 "--...--.".
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["a"]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 12</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["gin","zen","gig","msg"]
["a"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
```

### C

```c
int uniqueMorseRepresentations(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UniqueMorseRepresentations(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    
};
```

### TypeScript

```typescript
function uniqueMorseRepresentations(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function uniqueMorseRepresentations($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int uniqueMorseRepresentations(List<String> words) {
    
  }
}
```

### Go

```golang
func uniqueMorseRepresentations(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def unique_morse_representations(words)
    
end
```

### Scala

```scala
object Solution {
    def uniqueMorseRepresentations(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unique-morse-representations words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec unique_morse_representations(Words :: [unicode:unicode_binary()]) -> integer().
unique_morse_representations(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_morse_representations(words :: [String.t]) :: integer
  def unique_morse_representations(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniqueMorseRepresentations(words: Array<String>): Int64 {

    }
}
```

