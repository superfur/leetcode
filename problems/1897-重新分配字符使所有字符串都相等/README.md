# 1897. 重新分配字符使所有字符串都相等

## 题目描述

<p>给你一个字符串数组 <code>words</code>（下标 <strong>从 0 开始</strong> 计数）。</p>

<p>在一步操作中，需先选出两个 <strong>不同</strong> 下标 <code>i</code> 和 <code>j</code>，其中 <code>words[i]</code> 是一个非空字符串，接着将 <code>words[i]</code> 中的 <strong>任一</strong> 字符移动到 <code>words[j]</code> 中的 <strong>任一</strong> 位置上。</p>

<p>如果执行任意步操作可以使 <code>words</code> 中的每个字符串都相等，返回 <code>true</code><em> </em>；否则，返回<em> </em><code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["abc","aabc","bc"]
<strong>输出：</strong>true
<strong>解释：</strong>将 <code>words[1] 中的第一个</code> 'a' 移动到<code> words[2] 的最前面。
使 </code><code>words[1]</code> = "abc" 且 words[2] = "abc" 。
所有字符串都等于 "abc" ，所以返回 <code>true</code> 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["ab","a"]
<strong>输出：</strong>false
<strong>解释：</strong>执行操作无法使所有字符串都相等。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Characters are independent—only the frequency of characters matters.
2. It is possible to distribute characters if all characters can be divided equally among all strings.

## 示例

```
["abc","aabc","bc"]
["ab","a"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean makeEqual(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
```

### C

```c
bool makeEqual(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool MakeEqual(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {
    
};
```

### TypeScript

```typescript
function makeEqual(words: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Boolean
     */
    function makeEqual($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeEqual(_ words: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeEqual(words: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool makeEqual(List<String> words) {
    
  }
}
```

### Go

```golang
func makeEqual(words []string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Boolean}
def make_equal(words)
    
end
```

### Scala

```scala
object Solution {
    def makeEqual(words: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (make-equal words)
  (-> (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec make_equal(Words :: [unicode:unicode_binary()]) -> boolean().
make_equal(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_equal(words :: [String.t]) :: boolean
  def make_equal(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeEqual(words: Array<String>): Bool {

    }
}
```

