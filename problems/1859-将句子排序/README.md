# 1859. 将句子排序

## 题目描述

<p>一个 <strong>句子</strong> 指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。</p>

<p>我们可以给一个句子添加 <strong>从 1 开始的单词位置索引 </strong>，并且将句子中所有单词 <strong>打乱顺序</strong> 。</p>

<ul>
	<li>比方说，句子 <code>"This is a sentence"</code> 可以被打乱顺序得到 <code>"sentence4 a3 is2 This1"</code> 或者 <code>"is2 sentence4 This1 a3"</code> 。</li>
</ul>

<p>给你一个 <strong>打乱顺序</strong> 的句子 <code>s</code> ，它包含的单词不超过 <code>9</code> 个，请你重新构造并得到原本顺序的句子。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "is2 sentence4 This1 a3"
<b>输出：</b>"This is a sentence"
<b>解释：</b>将 s 中的单词按照初始位置排序，得到 "This1 is2 a3 sentence4" ，然后删除数字。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "Myself2 Me1 I4 and3"
<b>输出：</b>"Me Myself and I"
<b>解释：</b>将 s 中的单词按照初始位置排序，得到 "Me1 Myself2 and3 I4" ，然后删除数字。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= s.length <= 200</code></li>
	<li><code>s</code> 只包含小写和大写英文字母、空格以及从 <code>1</code> 到 <code>9</code> 的数字。</li>
	<li><code>s</code> 中单词数目为 <code>1</code> 到 <code>9</code> 个。</li>
	<li><code>s</code> 中的单词由单个空格分隔。</li>
	<li><code>s</code> 不包含任何前导或者后缀空格。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 排序

## 提示

1. Divide the string into the words as an array of strings
2. Sort the words by removing the last character from each word and sorting according to it

## 示例

```
"is2 sentence4 This1 a3"
"Myself2 Me1 I4 and3"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string sortSentence(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String sortSentence(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def sortSentence(self, s: str) -> str:
        
```

### C

```c


char * sortSentence(char * s){

}
```

### C#

```csharp
public class Solution {
    public string SortSentence(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    
};
```

### TypeScript

```typescript
function sortSentence(s: string): string {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortSentence($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortSentence(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortSentence(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String sortSentence(String s) {
    
  }
}
```

### Go

```golang
func sortSentence(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def sort_sentence(s)
    
end
```

### Scala

```scala
object Solution {
    def sortSentence(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_sentence(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (sort-sentence s)
  (-> string? string?)

  )
```

### Erlang

```erlang
-spec sort_sentence(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
sort_sentence(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_sentence(s :: String.t) :: String.t
  def sort_sentence(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortSentence(s: String): String {

    }
}
```

