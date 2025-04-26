# 2135. 统计追加字母可以获得的单词数

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的字符串数组 <code>startWords</code> 和 <code>targetWords</code> 。每个字符串都仅由 <strong>小写英文字母</strong> 组成。</p>

<p>对于 <code>targetWords</code> 中的每个字符串，检查是否能够从 <code>startWords</code> 中选出一个字符串，执行一次 <strong>转换操作</strong>&nbsp;，得到的结果与当前&nbsp;<code>targetWords</code> 字符串相等。</p>

<p><strong>转换操作</strong> 如下面两步所述：</p>

<ol>
	<li><strong>追加</strong> 任何 <strong>不存在</strong> 于当前字符串的任一小写字母到当前字符串的末尾。

	<ul>
		<li>例如，如果字符串为 <code>"abc"</code> ，那么字母 <code>'d'</code>、<code>'e'</code> 或 <code>'y'</code> 都可以加到该字符串末尾，但 <code>'a'</code> 就不行。如果追加的是 <code>'d'</code> ，那么结果字符串为 <code>"abcd"</code> 。</li>
	</ul>
	</li>
	<li><strong>重排</strong> 新字符串中的字母，可以按 <strong>任意</strong> 顺序重新排布字母。
	<ul>
		<li>例如，<code>"abcd"</code> 可以重排为 <code>"acbd"</code>、<code>"bacd"</code>、<code>"cbda"</code>，以此类推。注意，它也可以重排为 <code>"abcd"</code> 自身。</li>
	</ul>
	</li>
</ol>

<p>找出 <code>targetWords</code> 中有多少字符串能够由&nbsp;<code>startWords</code> 中的 <strong>任一</strong> 字符串执行上述转换操作获得。返回<em> </em><code>targetWords</code><em> </em>中这类 <strong>字符串的数目</strong> 。</p>

<p><strong>注意：</strong>你仅能验证 <code>targetWords</code> 中的字符串是否可以由 <code>startWords</code> 中的某个字符串经执行操作获得。<code>startWords</code>&nbsp; 中的字符串在这一过程中 <strong>不</strong> 发生实际变更。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
<strong>输出：</strong>2
<strong>解释：</strong>
- 为了形成 targetWords[0] = "tack" ，可以选用 startWords[1] = "act" ，追加字母 'k' ，并重排 "actk" 为 "tack" 。
- startWords 中不存在可以用于获得 targetWords[1] = "act" 的字符串。
  注意 "act" 确实存在于 startWords ，但是 <strong>必须</strong> 在重排前给这个字符串追加一个字母。
- 为了形成 targetWords[2] = "acti" ，可以选用 startWords[1] = "act" ，追加字母 'i' ，并重排 "acti" 为 "acti" 自身。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>startWords = ["ab","a"], targetWords = ["abc","abcd"]
<strong>输出：</strong>1
<strong>解释：</strong>
- 为了形成 targetWords[0] = "abc" ，可以选用 startWords[0] = "ab" ，追加字母 'c' ，并重排为 "abc" 。
- startWords 中不存在可以用于获得 targetWords[1] = "abcd" 的字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= startWords.length, targetWords.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= startWords[i].length, targetWords[j].length &lt;= 26</code></li>
	<li><code>startWords</code> 和 <code>targetWords</code> 中的每个字符串都仅由小写英文字母组成</li>
	<li>在 <code>startWords</code> 或 <code>targetWords</code> 的任一字符串中，每个字母至多出现一次</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Which data structure can be used to efficiently check if a string exists in startWords?
2. After appending a letter, all letters of a string can be rearranged in any possible way. How can we use this to reduce our search space while checking if a string in targetWords can be obtained from a string in startWords?

## 示例

```
["ant","act","tack"]
["tack","act","acti"]
["ab","a"]
["abc","abcd"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        
    }
};
```

### Java

```java
class Solution {
    public int wordCount(String[] startWords, String[] targetWords) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
```

### C

```c
int wordCount(char** startWords, int startWordsSize, char** targetWords, int targetWordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WordCount(string[] startWords, string[] targetWords) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} startWords
 * @param {string[]} targetWords
 * @return {number}
 */
var wordCount = function(startWords, targetWords) {
    
};
```

### TypeScript

```typescript
function wordCount(startWords: string[], targetWords: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $startWords
     * @param String[] $targetWords
     * @return Integer
     */
    function wordCount($startWords, $targetWords) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordCount(_ startWords: [String], _ targetWords: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordCount(startWords: Array<String>, targetWords: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int wordCount(List<String> startWords, List<String> targetWords) {
    
  }
}
```

### Go

```golang
func wordCount(startWords []string, targetWords []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} start_words
# @param {String[]} target_words
# @return {Integer}
def word_count(start_words, target_words)
    
end
```

### Scala

```scala
object Solution {
    def wordCount(startWords: Array[String], targetWords: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_count(start_words: Vec<String>, target_words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (word-count startWords targetWords)
  (-> (listof string?) (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec word_count(StartWords :: [unicode:unicode_binary()], TargetWords :: [unicode:unicode_binary()]) -> integer().
word_count(StartWords, TargetWords) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_count(start_words :: [String.t], target_words :: [String.t]) :: integer
  def word_count(start_words, target_words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordCount(startWords: Array<String>, targetWords: Array<String>): Int64 {

    }
}
```

