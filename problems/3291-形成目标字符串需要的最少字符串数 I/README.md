# 3291. 形成目标字符串需要的最少字符串数 I

## 题目描述

<p>给你一个字符串数组 <code>words</code> 和一个字符串 <code>target</code>。</p>

<p>如果字符串 <code>x</code> 是 <code>words</code> 中<strong> 任意 </strong>字符串的 <span data-keyword="string-prefix">前缀</span>，则认为 <code>x</code> 是一个 <strong>有效</strong> 字符串。</p>

<p>现计划通过 <strong>连接 </strong>有效字符串形成 <code>target</code> ，请你计算并返回需要连接的 <strong>最少 </strong>字符串数量。如果无法通过这种方式形成 <code>target</code>，则返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["abc","aaaaa","bcdef"], target = "aabcdabc"</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>target 字符串可以通过连接以下有效字符串形成：</p>

<ul>
	<li><code>words[1]</code> 的长度为 2 的前缀，即 <code>"aa"</code>。</li>
	<li><code>words[2]</code> 的长度为 3 的前缀，即 <code>"bcd"</code>。</li>
	<li><code>words[0]</code> 的长度为 3 的前缀，即 <code>"abc"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["abababab","ab"], target = "ababaababa"</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>target 字符串可以通过连接以下有效字符串形成：</p>

<ul>
	<li><code>words[0]</code> 的长度为 5 的前缀，即 <code>"ababa"</code>。</li>
	<li><code>words[0]</code> 的长度为 5 的前缀，即 <code>"ababa"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["abcdef"], target = "xyz"</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 5 * 10<sup>3</sup></code></li>
	<li>输入确保 <code>sum(words[i].length) &lt;= 10<sup>5</sup></code>。</li>
	<li><code>words[i]</code> 只包含小写英文字母。</li>
	<li><code>1 &lt;= target.length &lt;= 5 * 10<sup>3</sup></code></li>
	<li><code>target</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 线段树
- 数组
- 字符串
- 二分查找
- 动态规划
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. Let <code>dp[i]</code> be the minimum cost to form the prefix of length <code>i</code> of <code>target</code>.
2. If <code>target[(i + 1)..j]</code> matches any prefix, update the range <code>dp[(i + 1)..j]</code> to minimum between original value and <code>dp[i] + 1</code>.
3. Use a Trie to check prefix matching.

## 示例

```
["abc","aaaaa","bcdef"]
"aabcdabc"
["abababab","ab"]
"ababaababa"
["abcdef"]
"xyz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minValidStrings(String[] words, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        
```

### C

```c
int minValidStrings(char** words, int wordsSize, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinValidStrings(string[] words, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var minValidStrings = function(words, target) {
    
};
```

### TypeScript

```typescript
function minValidStrings(words: string[], target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $target
     * @return Integer
     */
    function minValidStrings($words, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minValidStrings(_ words: [String], _ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minValidStrings(words: Array<String>, target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minValidStrings(List<String> words, String target) {
    
  }
}
```

### Go

```golang
func minValidStrings(words []string, target string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} target
# @return {Integer}
def min_valid_strings(words, target)
    
end
```

### Scala

```scala
object Solution {
    def minValidStrings(words: Array[String], target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_valid_strings(words: Vec<String>, target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-valid-strings words target)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_valid_strings(Words :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
min_valid_strings(Words, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_valid_strings(words :: [String.t], target :: String.t) :: integer
  def min_valid_strings(words, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minValidStrings(words: Array<String>, target: String): Int64 {

    }
}
```

