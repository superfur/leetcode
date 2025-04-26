# 72. 编辑距离

## 题目描述

<p>给你两个单词&nbsp;<code>word1</code> 和&nbsp;<code>word2</code>， <em>请返回将&nbsp;<code>word1</code>&nbsp;转换成&nbsp;<code>word2</code> 所使用的最少操作数</em> &nbsp;。</p>

<p>你可以对一个单词进行如下三种操作：</p>

<ul>
	<li>插入一个字符</li>
	<li>删除一个字符</li>
	<li>替换一个字符</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>word1 = "horse", word2 = "ros"
<strong>输出：</strong>3
<strong>解释：</strong>
horse -&gt; rorse (将 'h' 替换为 'r')
rorse -&gt; rose (删除 'r')
rose -&gt; ros (删除 'e')
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>word1 = "intention", word2 = "execution"
<strong>输出：</strong>5
<strong>解释：</strong>
intention -&gt; inention (删除 't')
inention -&gt; enention (将 'i' 替换为 'e')
enention -&gt; exention (将 'n' 替换为 'x')
exention -&gt; exection (将 'n' 替换为 'c')
exection -&gt; execution (插入 'u')
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= word1.length, word2.length &lt;= 500</code></li>
	<li><code>word1</code> 和 <code>word2</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"horse"
"ros"
"intention"
"execution"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDistance(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
```

### C

```c
int minDistance(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDistance(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function minDistance(word1: string, word2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function minDistance($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDistance(word1: String, word2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDistance(String word1, String word2) {
    
  }
}
```

### Go

```golang
func minDistance(word1 string, word2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def minDistance(word1: String, word2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-distance word1 word2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_distance(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
min_distance(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_distance(word1 :: String.t, word2 :: String.t) :: integer
  def min_distance(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDistance(word1: String, word2: String): Int64 {

    }
}
```

