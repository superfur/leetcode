# 2707. 字符串中的额外字符

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;和一个单词字典&nbsp;<code>dictionary</code>&nbsp;。你需要将&nbsp;<code>s</code>&nbsp;分割成若干个 <strong>互不重叠</strong>&nbsp;的子字符串，每个子字符串都在&nbsp;<code>dictionary</code>&nbsp;中出现过。<code>s</code>&nbsp;中可能会有一些&nbsp;<strong>额外的字符</strong>&nbsp;不在任何子字符串中。</p>

<p>请你采取最优策略分割 <code>s</code>&nbsp;，使剩下的字符 <strong>最少</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "leetscode", dictionary = ["leet","code","leetcode"]
<b>输出：</b>1
<b>解释：</b>将 s 分成两个子字符串：下标从 0 到 3 的 "leet" 和下标从 5 到 8 的 "code" 。只有 1 个字符没有使用（下标为 4），所以我们返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "sayhelloworld", dictionary = ["hello","world"]
<b>输出：</b>3
<b>解释：</b>将 s 分成两个子字符串：下标从 3 到 7 的 "hello" 和下标从 8 到 12 的 "world" 。下标为 0 ，1 和 2 的字符没有使用，所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 50</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 50</code></li>
	<li><code>dictionary[i]</code>&nbsp;和&nbsp;<code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>dictionary</code>&nbsp;中的单词互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 动态规划

## 提示

1. Can we use Dynamic Programming here?
2. Define DP[i] as the min extra character if breaking up s[0:i] optimally.

## 示例

```
"leetscode"
["leet","code","leetcode"]
"sayhelloworld"
["hello","world"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        
    }
};
```

### Java

```java
class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
```

### C

```c
int minExtraChar(char* s, char** dictionary, int dictionarySize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinExtraChar(string s, string[] dictionary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {number}
 */
var minExtraChar = function(s, dictionary) {
    
};
```

### TypeScript

```typescript
function minExtraChar(s: string, dictionary: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $dictionary
     * @return Integer
     */
    function minExtraChar($s, $dictionary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minExtraChar(_ s: String, _ dictionary: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minExtraChar(s: String, dictionary: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minExtraChar(String s, List<String> dictionary) {
    
  }
}
```

### Go

```golang
func minExtraChar(s string, dictionary []string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String[]} dictionary
# @return {Integer}
def min_extra_char(s, dictionary)
    
end
```

### Scala

```scala
object Solution {
    def minExtraChar(s: String, dictionary: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-extra-char s dictionary)
  (-> string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_extra_char(S :: unicode:unicode_binary(), Dictionary :: [unicode:unicode_binary()]) -> integer().
min_extra_char(S, Dictionary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_extra_char(s :: String.t, dictionary :: [String.t]) :: integer
  def min_extra_char(s, dictionary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minExtraChar(s: String, dictionary: Array<String>): Int64 {

    }
}
```

