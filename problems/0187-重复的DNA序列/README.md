# 187. 重复的DNA序列

## 题目描述

<p><strong>DNA序列</strong>&nbsp;由一系列核苷酸组成，缩写为<meta charset="UTF-8" />&nbsp;<code>'A'</code>,&nbsp;<code>'C'</code>,&nbsp;<code>'G'</code>&nbsp;和<meta charset="UTF-8" />&nbsp;<code>'T'</code>.。</p>

<ul>
	<li>例如，<meta charset="UTF-8" /><code>"ACGAATTCCG"</code>&nbsp;是一个 <strong>DNA序列</strong> 。</li>
</ul>

<p>在研究 <strong>DNA</strong> 时，识别 DNA 中的重复序列非常有用。</p>

<p>给定一个表示 <strong>DNA序列</strong> 的字符串 <code>s</code> ，返回所有在 DNA 分子中出现不止一次的&nbsp;<strong>长度为&nbsp;<code>10</code></strong>&nbsp;的序列(子字符串)。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>输出：</strong>["AAAAACCCCC","CCCCCAAAAA"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "AAAAAAAAAAAAA"
<strong>输出：</strong>["AAAAAAAAAA"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code><code>==</code><code>'A'</code>、<code>'C'</code>、<code>'G'</code>&nbsp;or&nbsp;<code>'T'</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 滑动窗口
- 哈希函数
- 滚动哈希

## 示例

```
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
"AAAAAAAAAAAAA"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRepeatedDnaSequences(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    
};
```

### TypeScript

```typescript
function findRepeatedDnaSequences(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function findRepeatedDnaSequences($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRepeatedDnaSequences(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRepeatedDnaSequences(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findRepeatedDnaSequences(String s) {
    
  }
}
```

### Go

```golang
func findRepeatedDnaSequences(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def find_repeated_dna_sequences(s)
    
end
```

### Scala

```scala
object Solution {
    def findRepeatedDnaSequences(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-repeated-dna-sequences s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec find_repeated_dna_sequences(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
find_repeated_dna_sequences(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_repeated_dna_sequences(s :: String.t) :: [String.t]
  def find_repeated_dna_sequences(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRepeatedDnaSequences(s: String): ArrayList<String> {

    }
}
```

