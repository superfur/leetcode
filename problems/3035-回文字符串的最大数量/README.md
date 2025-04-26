# 3035. 回文字符串的最大数量

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> ，数组的长度为 <code>n</code> ，且包含下标从 <strong>0</strong> 开始的若干字符串。</p>

<p>你可以执行以下操作 <strong>任意 </strong>次数（<strong>包括零次</strong>）：</p>

<ul>
	<li>选择整数<code>i</code>、<code>j</code>、<code>x</code>和<code>y</code>，满足<code>0 &lt;= i, j &lt; n</code>，<code>0 &lt;= x &lt; words[i].length</code>，<code>0 &lt;= y &lt; words[j].length</code>，<strong>交换 </strong>字符 <code>words[i][x]</code> 和 <code>words[j][y]</code> 。</li>
</ul>

<p>返回一个整数，表示在执行一些操作后，<code>words</code> 中可以包含的<span data-keyword="palindrome-string">回文串</span>的 <strong>最大 </strong>数量。</p>

<p><strong>注意：</strong>在操作过程中，<code>i</code> 和 <code>j</code> 可以相等。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["abbb","ba","aa"]
<strong>输出：</strong>3
<strong>解释：</strong>在这个例子中，获得最多回文字符串的一种方式是：
选择 i = 0, j = 1, x = 0, y = 0，交换 words[0][0] 和 words[1][0] 。words 变成了 ["bbbb","aa","aa"] 。
words 中的所有字符串都是回文。
因此，可实现的回文字符串的最大数量是 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["abc","ab"]
<strong>输出：</strong>2
<strong>解释：</strong>在这个例子中，获得最多回文字符串的一种方式是： 
选择 i = 0, j = 1, x = 1, y = 0，交换 words[0][1] 和 words[1][0] 。words 变成了 ["aac","bb"] 。
选择 i = 0, j = 0, x = 1, y = 2，交换 words[0][1] 和 words[0][2] 。words 变成了 ["aca","bb"] 。
两个字符串都是回文 。
因此，可实现的回文字符串的最大数量是 2。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["cd","ef","a"]
<strong>输出：</strong>1
<strong>解释：</strong>在这个例子中，没有必要执行任何操作。
words 中有一个回文 "a" 。
可以证明，在执行任何次数操作后，无法得到更多回文。
因此，答案是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 字符串
- 计数
- 排序

## 提示

1. We can redistribute all the letters freely among the words.
2. Calculate the frequency of each letter and total the number of matching letter pairs that can be formed from the letters, i.e., <code>total = sum(freq[ch] / 2)</code> for all <code>'a' <= ch <= 'z'</code>.
3. We can greedily try making palindromes from <code>words[i]</code> with the smallest length to <code>words[i]</code> with the longest length.
4. For the current index, <code>i</code>, we try to make <code>words[i]</code> a palindrome. We need <code>len(words[i]) / 2</code> matching character pairs, and the letter in the middle (if it exists) can be freely chosen afterward.
5. We can check if we have enough pairs for index <code>i</code>; if we do, we increase the number of palindromes we can make and decrease the number of pairs we have. Otherwise, we end the loop at this index.
6. The answer is the number of palindromes we were able to make in the end.

## 示例

```
["abbb","ba","aa"]
["abc","ab"]
["cd","ef","a"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPalindromesAfterOperations(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPalindromesAfterOperations(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPalindromesAfterOperations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        
```

### C

```c
int maxPalindromesAfterOperations(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPalindromesAfterOperations(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maxPalindromesAfterOperations = function(words) {
    
};
```

### TypeScript

```typescript
function maxPalindromesAfterOperations(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maxPalindromesAfterOperations($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPalindromesAfterOperations(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPalindromesAfterOperations(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPalindromesAfterOperations(List<String> words) {
    
  }
}
```

### Go

```golang
func maxPalindromesAfterOperations(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def max_palindromes_after_operations(words)
    
end
```

### Scala

```scala
object Solution {
    def maxPalindromesAfterOperations(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_palindromes_after_operations(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-palindromes-after-operations words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_palindromes_after_operations(Words :: [unicode:unicode_binary()]) -> integer().
max_palindromes_after_operations(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_palindromes_after_operations(words :: [String.t]) :: integer
  def max_palindromes_after_operations(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPalindromesAfterOperations(words: Array<String>): Int64 {

    }
}
```

