# 2416. 字符串的前缀分数和

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>words</code> ，该数组由 <strong>非空</strong> 字符串组成。</p>

<p>定义字符串 <code>term</code> 的 <strong>分数</strong> 等于以 <code>term</code> 作为 <strong>前缀</strong> 的 <code>words[i]</code> 的数目。</p>

<ul>
	<li>例如，如果 <code>words = ["a", "ab", "abc", "cab"]</code> ，那么 <code>"ab"</code> 的分数是 <code>2</code> ，因为 <code>"ab"</code> 是 <code>"ab"</code> 和 <code>"abc"</code> 的一个前缀。</li>
</ul>

<p>返回一个长度为<em> </em><code>n</code> 的数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer[i]</code><em> </em>是<em>&nbsp;</em><code>words[i]</code> 的每个非空前缀的分数 <strong>总和</strong> <em>。</em></p>

<p><strong>注意：</strong>字符串视作它自身的一个前缀。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["abc","ab","bc","b"]
<strong>输出：</strong>[5,4,3,2]
<strong>解释：</strong>对应每个字符串的答案如下：
- "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。
总计 answer[0] = 2 + 2 + 1 = 5 。
- "ab" 有 2 个前缀："a" 和 "ab" 。
- 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。
总计 answer[1] = 2 + 2 = 4 。
- "bc" 有 2 个前缀："b" 和 "bc" 。
- 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。 
总计 answer[2] = 2 + 1 = 3 。
- "b" 有 1 个前缀："b"。
- 2 个字符串的前缀为 "b" 。
总计 answer[3] = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["abcd"]
<strong>输出：</strong>[4]
<strong>解释：</strong>
"abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。
每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 数组
- 字符串
- 计数

## 提示

1. What data structure will allow you to efficiently keep track of the score of each prefix?
2. Use a Trie. Insert all the words into it, and keep a counter at each node that will tell you how many times we have visited each prefix.

## 示例

```
["abc","ab","bc","b"]
["abcd"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sumPrefixScores(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumPrefixScores(char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SumPrefixScores(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    
};
```

### TypeScript

```typescript
function sumPrefixScores(words: string[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[]
     */
    function sumPrefixScores($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumPrefixScores(_ words: [String]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumPrefixScores(words: Array<String>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sumPrefixScores(List<String> words) {
    
  }
}
```

### Go

```golang
func sumPrefixScores(words []string) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer[]}
def sum_prefix_scores(words)
    
end
```

### Scala

```scala
object Solution {
    def sumPrefixScores(words: Array[String]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sum-prefix-scores words)
  (-> (listof string?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sum_prefix_scores(Words :: [unicode:unicode_binary()]) -> [integer()].
sum_prefix_scores(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_prefix_scores(words :: [String.t]) :: [integer]
  def sum_prefix_scores(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumPrefixScores(words: Array<String>): Array<Int64> {

    }
}
```

