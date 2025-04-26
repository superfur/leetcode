# 面试题 17.25. 单词矩阵

## 题目描述

<p>给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。</p>

<p>如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>["this", "real", "hard", "trh", "hea", "iar", "sld"]</code>
<strong>输出：
</strong><code>[
&nbsp;  "this",
&nbsp;  "real",
&nbsp;  "hard"</code>
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>["aa"]</code>
<strong>输出：</strong>["aa","aa"]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>words.length &lt;= 1000</code></li>
	<li><code>words[i].length &lt;= 100</code></li>
	<li>数据保证单词足够随机</li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 数组
- 字符串
- 回溯

## 提示

1. 首先根据单词长度对字典进行分组，因为你知道每一列的长度必须相同，每一行的长度也必须相同。
2. 你能找到一个特定长宽的单词矩阵吗？如果尝试了所有的选项会怎样？
3. 当矩形看起来无效时，可以使用trie提前终止吗？

## 示例

```
["this", "real", "hard", "trh", "hea", "iar", "sld"]
["aa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> maxRectangle(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] maxRectangle(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRectangle(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** maxRectangle(char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] MaxRectangle(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var maxRectangle = function(words) {
    
};
```

### TypeScript

```typescript
function maxRectangle(words: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String[]
     */
    function maxRectangle($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRectangle(_ words: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRectangle(words: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> maxRectangle(List<String> words) {
    
  }
}
```

### Go

```golang
func maxRectangle(words []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String[]}
def max_rectangle(words)
    
end
```

### Scala

```scala
object Solution {
    def maxRectangle(words: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_rectangle(words: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (max-rectangle words)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec max_rectangle(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
max_rectangle(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_rectangle(words :: [String.t]) :: [String.t]
  def max_rectangle(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRectangle(words: Array<String>): Array<String> {

    }
}
```

