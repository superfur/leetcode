# 843. 猜猜这个单词

## 题目描述

<p>给你一个由 <strong>不同</strong> 字符串组成的单词列表&nbsp;<code>words</code> ，其中 <code>words[i]</code>&nbsp;长度均为&nbsp;<code>6</code> 。<code>words</code> 中的一个单词将被选作秘密单词 <code>secret</code>&nbsp;。</p>

<p>另给你一个辅助对象&nbsp;<code>Master</code> ，你可以调用&nbsp;<code>Master.guess(word)</code> 来猜单词，其中参数 <code>word</code> 长度为 6 且必须是 <code>words</code> 中的字符串。</p>

<p><code>Master.guess(word)</code> 将会返回如下结果：</p>

<ul>
	<li>如果 <code>word</code> 不是 <code>words</code> 中的字符串，返回 <code>-1</code> ，或者</li>
	<li>一个整数，表示你所猜测的单词 <code>word</code> 与 <strong>秘密单词</strong>&nbsp;<code>secret</code>&nbsp;的准确匹配（值和位置同时匹配）的数目。</li>
</ul>

<p>每组测试用例都会包含一个参数 <code>allowedGuesses</code> ，其中 <code>allowedGuesses</code> 是你可以调用 <code>Master.guess(word)</code> 的最大次数。</p>

<p>对于每组测试用例，在不超过允许猜测的次数的前提下，你应该调用 <code>Master.guess</code> 来猜出秘密单词。最终，你将会得到以下结果：</p>

<ul>
	<li>如果你调用 <code>Master.guess</code> 的次数大于 <code>allowedGuesses</code> 所限定的次数或者你没有用 <code>Master.guess</code> 猜到秘密单词，则得到 <strong><code>"Either you took too many guesses, or you did not find the secret word."</code> 。</strong></li>
	<li>如果你调用 <code>Master.guess</code> 猜到秘密单词，且调用 <code>Master.guess</code> 的次数小于或等于 <code>allowedGuesses</code> ，则得到 <strong><code>"You guessed the secret word correctly."</code> 。</strong></li>
</ul>

<p>生成的测试用例保证你可以利用某种合理的策略（而不是暴力）猜到秘密单词。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
<strong>输出：</strong>You guessed the secret word correctly.
<strong>解释：</strong>
master.guess("aaaaaa") 返回 -1 ，因为 "aaaaaa" 不在 words 中。
master.guess("acckzz") 返回 6 ，因为 "acckzz" 是秘密单词 secret ，共有 6 个字母匹配。
master.guess("ccbazz") 返回 3 ，因为 "ccbazz" 共有 3 个字母匹配。
master.guess("eiowzz") 返回 2 ，因为 "eiowzz" 共有 2 个字母匹配。
master.guess("abcczz") 返回 4 ，因为 "abcczz" 共有 4 个字母匹配。
一共调用 5 次 master.guess ，其中一个为秘密单词，所以通过测试用例。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
<strong>输出：</strong>You guessed the secret word correctly.
<strong>解释：</strong>共有 2 个单词，且其中一个为秘密单词，可以通过测试用例。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>words[i].length == 6</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>words</code> 中所有字符串 <strong>互不相同</strong></li>
	<li><code>secret</code> 存在于 <code>words</code> 中</li>
	<li><code>10 &lt;= allowedGuesses &lt;= 30</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 字符串
- 博弈
- 交互

## 示例

```
"acckzz"
["acckzz","ccbazz","eiowzz","abcczz"]
10
"hamada"
["hamada","khaled"]
10
```

## 示例代码

### C++

```cpp
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    void findSecretWord(vector<string>& words, Master& master) {
        
    }
};
```

### Java

```java
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */
class Solution {
    public void findSecretWord(String[] words, Master master) {
        
    }
}
```

### Python

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        
```

### Python3

```python3
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
```

### C

```c
/**
 * *********************************************************************
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * int guess(Master *, char *word);
 */
void findSecretWord(char** words, int wordsSize, Master* master) {
    
}
```

### C#

```csharp
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public int Guess(string word);
 * }
 */
class Solution {
    public void FindSecretWord(string[] words, Master master) {
        
    }
}
```

### JavaScript

```javascript
/**
 * // This is the master's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Master() {
 *
 *     @param {string} word
 *     @return {integer}
 *     this.guess = function(word) {
 *         ...
 *     };
 * };
 */
/**
 * @param {string[]} words
 * @param {Master} master
 * @return {void}
 */
var findSecretWord = function(words, master) {
    
};
```

### TypeScript

```typescript
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *      guess(word: string): number {}
 * }
 */

function findSecretWord(words: string[], master: Master) {

};
```

### PHP

```php
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     function guess($word) {}
 * }
 */

class Solution {
    /**
     * @param String[] $words
     * @param Master $master
     * @return 
     */
    function findSecretWord($words, $master) {
        
    }
}
```

### Swift

```swift
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public func guess(word: String) -> Int {}
 * }
 */
class Solution {
    func findSecretWord(_ words: [String], _ master: Master) {
        
    }
}
```

### Kotlin

```kotlin
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     fun guess(word: String): Int {}
 * }
 */
class Solution {
    fun findSecretWord(words: Array<String>, master: Master) {
        
    }
}
```

### Go

```golang
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * type Master struct {
 * }
 *
 * func (this *Master) Guess(word string) int {}
 */
func findSecretWord(words []string, master *Master) {
    
}
```

### Ruby

```ruby
#    This is Master's API interface.
#    You should not implement it, or speculate about its implementation
#
# class Master
# =begin
#     :type word: String
#     :rtype: Integer
# =end
#     def guess(word)
#         ...
#     end
# end
#

# @param {String[]} words
# @param {Master} master
# @return {Void}
def find_secret_word(words, master)
    
end
```

### Scala

```scala
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *
 *   def guess(word: String): Int = {}
 *
 * }
 */
object Solution {
    def findSecretWord(words: Array[String], master: Master): Unit = {
        
    }
}
```

### Rust

```rust
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * struct Master;
 * impl Master {
 *     fn guess(word:String)->int;
 * };
 */

impl Solution {
    pub fn find_secret_word(words: Vec<String>, master: &Master) {
        
    }
}
```

