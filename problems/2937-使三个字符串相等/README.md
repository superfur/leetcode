# 2937. 使三个字符串相等

## 题目描述

<p>给你三个字符串 <code>s1</code>、<code>s2</code> 和 <code>s3</code>。 你可以根据需要对这三个字符串执行以下操作 <strong>任意次数</strong> <!-- notionvc: b5178de7-3318-4129-b7d9-726b47e90621 -->。</p>

<p>在每次操作中，你可以选择其中一个长度至少为 <code>2</code> 的字符串 <!-- notionvc: 3342ac46-33c8-4010-aacd-e58678ce31ef --> 并删除其 <strong>最右位置上</strong> 的字符。</p>

<p>如果存在某种方法能够使这三个字符串相等，请返回使它们相等所需的 <strong>最小</strong> 操作次数；否则，返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "abc"，s2 = "abb"，s3 = "ab"
<strong>输出：</strong>2
<strong>解释：</strong>对 s1 和 s2 进行一次操作后，可以得到三个相等的字符串。
可以证明，不可能用少于两次操作使它们相等。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "dac"，s2 = "bac"，s3 = "cac"
<strong>输出：</strong>-1
<strong>解释：</strong>因为 s1 和 s2 的最左位置上的字母<!-- notionvc: 47239f7c-eec1-49f8-af79-c206ec88cb07 -->不相等，所以无论进行多少次操作，它们都不可能相等。因此答案是 -1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length, s3.length &lt;= 100</code></li>
	<li><code>s1</code>、<code>s2</code> 和 <code>s3</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Calculate the length of the longest common prefix of the <code>3</code> strings.

## 示例

```
"abc"
"abb"
"ab"
"dac"
"bac"
"cac"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
```

### C

```c
int findMinimumOperations(char* s1, char* s2, char* s3) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinimumOperations(string s1, string s2, string s3) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {number}
 */
var findMinimumOperations = function(s1, s2, s3) {
    
};
```

### TypeScript

```typescript
function findMinimumOperations(s1: string, s2: string, s3: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Integer
     */
    function findMinimumOperations($s1, $s2, $s3) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinimumOperations(_ s1: String, _ s2: String, _ s3: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinimumOperations(s1: String, s2: String, s3: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinimumOperations(String s1, String s2, String s3) {
    
  }
}
```

### Go

```golang
func findMinimumOperations(s1 string, s2 string, s3 string) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @param {String} s3
# @return {Integer}
def find_minimum_operations(s1, s2, s3)
    
end
```

### Scala

```scala
object Solution {
    def findMinimumOperations(s1: String, s2: String, s3: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_minimum_operations(s1: String, s2: String, s3: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-minimum-operations s1 s2 s3)
  (-> string? string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_minimum_operations(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), S3 :: unicode:unicode_binary()) -> integer().
find_minimum_operations(S1, S2, S3) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_minimum_operations(s1 :: String.t, s2 :: String.t, s3 :: String.t) :: integer
  def find_minimum_operations(s1, s2, s3) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinimumOperations(s1: String, s2: String, s3: String): Int64 {

    }
}
```

