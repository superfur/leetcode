# 916. 单词子集

## 题目描述

<p>给你两个字符串数组 <code>words1</code>&nbsp;和&nbsp;<code>words2</code>。</p>

<p>现在，如果&nbsp;<code>b</code> 中的每个字母都出现在 <code>a</code> 中，<strong>包括重复出现的字母</strong>，那么称字符串 <code>b</code> 是字符串 <code>a</code> 的 <strong>子集</strong> 。</p>

<ul>
	<li>例如，<code>"wrr"</code> 是 <code>"warrior"</code> 的子集，但不是 <code>"world"</code> 的子集。</li>
</ul>

<p>如果对 <code>words2</code> 中的每一个单词&nbsp;<code>b</code>，<code>b</code> 都是 <code>a</code> 的子集，那么我们称&nbsp;<code>words1</code> 中的单词 <code>a</code> 是<em> </em><strong>通用单词</strong><em> </em>。</p>

<p>以数组形式返回&nbsp;<code>words1</code> 中所有的 <strong>通用</strong> 单词。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]</span></p>

<p><span class="example-io"><b>输出：</b>["facebook","google","leetcode"]</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">["leetcode"]</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">["cccbb"]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words1.length, words2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words1[i].length, words2[i].length &lt;= 10</code></li>
	<li><code>words1[i]</code> 和 <code>words2[i]</code> 仅由小写英文字母组成</li>
	<li><code>words1</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["amazon","apple","facebook","google","leetcode"]
["e","o"]
["amazon","apple","facebook","google","leetcode"]
["lc","eo"]
["acaac","cccbb","aacbb","caacc","bcbbb"]
["c","cc","b"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** wordSubsets(char** words1, int words1Size, char** words2, int words2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> WordSubsets(string[] words1, string[] words2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {
    
};
```

### TypeScript

```typescript
function wordSubsets(words1: string[], words2: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words1
     * @param String[] $words2
     * @return String[]
     */
    function wordSubsets($words1, $words2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wordSubsets(_ words1: [String], _ words2: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wordSubsets(words1: Array<String>, words2: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> wordSubsets(List<String> words1, List<String> words2) {
    
  }
}
```

### Go

```golang
func wordSubsets(words1 []string, words2 []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words1
# @param {String[]} words2
# @return {String[]}
def word_subsets(words1, words2)
    
end
```

### Scala

```scala
object Solution {
    def wordSubsets(words1: Array[String], words2: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn word_subsets(words1: Vec<String>, words2: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (word-subsets words1 words2)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec word_subsets(Words1 :: [unicode:unicode_binary()], Words2 :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
word_subsets(Words1, Words2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec word_subsets(words1 :: [String.t], words2 :: [String.t]) :: [String.t]
  def word_subsets(words1, words2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wordSubsets(words1: Array<String>, words2: Array<String>): ArrayList<String> {

    }
}
```

