# 面试题 16.20. T9键盘

## 题目描述

<p>在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png" style="width: 200px;" /></p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "8733", words = ["tree", "used"]
<strong>输出：</strong>["tree", "used"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "2", words = ["a", "b", "c", "d"]
<strong>输出：</strong>["a", "b", "c"]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>num.length &lt;= 1000</code></li>
	<li><code>words.length &lt;= 500</code></li>
	<li><code>words[i].length == num.length</code></li>
	<li><code>num</code>中不会出现 0, 1 这两个数字</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. 想想递归。
2. 你能递归地尝试所有的可能性吗？
3. 在现实世界中，我们应该知道一些前缀/子字符串是行不通的。例如，考虑数字33835676368。虽然3383确实对应于fftf，但是没有以fftf开头的单词。有没有什么办法对于这样的情况做特殊处理？
4. trie可以帮助我们。如果将整个单词列表存储在trie中会怎样？
5. 我们可能会多次运行这个算法。如果做更多的预处理，这里有办法优化吗？
6. 通过预处理，实际上可以将查找时间降低到O(1)。

## 示例

```
"8733"
["tree", "used"]
"2"
["a", "b", "c", "d"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> getValidT9Words(string num, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> getValidT9Words(String num, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getValidT9Words(self, num, words):
        """
        :type num: str
        :type words: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getValidT9Words(char* num, char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> GetValidT9Words(string num, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {string[]} words
 * @return {string[]}
 */
var getValidT9Words = function(num, words) {
    
};
```

### TypeScript

```typescript
function getValidT9Words(num: string, words: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param String[] $words
     * @return String[]
     */
    function getValidT9Words($num, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getValidT9Words(_ num: String, _ words: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getValidT9Words(num: String, words: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> getValidT9Words(String num, List<String> words) {
    
  }
}
```

### Go

```golang
func getValidT9Words(num string, words []string) []string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {String[]} words
# @return {String[]}
def get_valid_t9_words(num, words)
    
end
```

### Scala

```scala
object Solution {
    def getValidT9Words(num: String, words: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_valid_t9_words(num: String, words: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (get-valid-t9-words num words)
  (-> string? (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec get_valid_t9_words(Num :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
get_valid_t9_words(Num, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_valid_t9_words(num :: String.t, words :: [String.t]) :: [String.t]
  def get_valid_t9_words(num, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getValidT9Words(num: String, words: Array<String>): ArrayList<String> {

    }
}
```

