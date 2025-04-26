# 2138. 将字符串拆分为若干长度为 k 的组

## 题目描述

<p>字符串 <code>s</code> 可以按下述步骤划分为若干长度为 <code>k</code> 的组：</p>

<ul>
	<li>第一组由字符串中的前 <code>k</code> 个字符组成，第二组由接下来的 <code>k</code> 个字符串组成，依此类推。每个字符都能够成为 <strong>某一个</strong> 组的一部分。</li>
	<li>对于最后一组，如果字符串剩下的字符 <strong>不足</strong> <code>k</code> 个，需使用字符 <code>fill</code> 来补全这一组字符。</li>
</ul>

<p>注意，在去除最后一个组的填充字符 <code>fill</code>（如果存在的话）并按顺序连接所有的组后，所得到的字符串应该是 <code>s</code> 。</p>

<p>给你一个字符串 <code>s</code> ，以及每组的长度 <code>k</code> 和一个用于填充的字符 <code>fill</code> ，按上述步骤处理之后，返回一个字符串数组，该数组表示 <code>s</code> 分组后 <strong>每个组的组成情况</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "abcdefghi", k = 3, fill = "x"
<strong>输出：</strong>["abc","def","ghi"]
<strong>解释：</strong>
前 3 个字符是 "abc" ，形成第一组。
接下来 3 个字符是 "def" ，形成第二组。
最后 3 个字符是 "ghi" ，形成第三组。
由于所有组都可以由字符串中的字符完全填充，所以不需要使用填充字符。
因此，形成 3 组，分别是 "abc"、"def" 和 "ghi" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "abcdefghij", k = 3, fill = "x"
<strong>输出：</strong>["abc","def","ghi","jxx"]
<strong>解释：</strong>
与前一个例子类似，形成前三组 "abc"、"def" 和 "ghi" 。
对于最后一组，字符串中仅剩下字符 'j' 可以用。为了补全这一组，使用填充字符 'x' 两次。
因此，形成 4 组，分别是 "abc"、"def"、"ghi" 和 "jxx" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>fill</code> 是一个小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. Using the length of the string and k, can you count the number of groups the string can be divided into?
2. Try completing each group using characters from the string. If there aren’t enough characters for the last group, use the fill character to complete the group.

## 示例

```
"abcdefghi"
3
"x"
"abcdefghij"
3
"x"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] divideString(String s, int k, char fill) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** divideString(char* s, int k, char fill, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] DivideString(string s, int k, char fill) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function(s, k, fill) {
    
};
```

### TypeScript

```typescript
function divideString(s: string, k: number, fill: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param String $fill
     * @return String[]
     */
    function divideString($s, $k, $fill) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divideString(_ s: String, _ k: Int, _ fill: Character) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divideString(s: String, k: Int, fill: Char): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> divideString(String s, int k, String fill) {
    
  }
}
```

### Go

```golang
func divideString(s string, k int, fill byte) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @param {Character} fill
# @return {String[]}
def divide_string(s, k, fill)
    
end
```

### Scala

```scala
object Solution {
    def divideString(s: String, k: Int, fill: Char): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (divide-string s k fill)
  (-> string? exact-integer? char? (listof string?))
  )
```

### Erlang

```erlang
-spec divide_string(S :: unicode:unicode_binary(), K :: integer(), Fill :: char()) -> [unicode:unicode_binary()].
divide_string(S, K, Fill) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide_string(s :: String.t, k :: integer, fill :: char) :: [String.t]
  def divide_string(s, k, fill) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divideString(s: String, k: Int64, fill: Rune): Array<String> {

    }
}
```

