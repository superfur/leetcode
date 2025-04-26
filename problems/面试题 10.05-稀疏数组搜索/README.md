# 面试题 10.05. 稀疏数组搜索

## 题目描述

<p>稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入：</strong>words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
<strong> 输出：</strong>-1
<strong> 说明：</strong>不存在返回-1。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
<strong> 输出</strong>：4
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>words的长度在[1, 1000000]之间</li>
</ol>


## 难度

Easy

## 标签

- 数组
- 字符串
- 二分查找

## 提示

1. 尝试修改二分查找来处理这个问题。

## 示例

```
["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
"ta"
["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
"ball"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findString(vector<string>& words, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int findString(String[] words, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        
```

### C

```c
int findString(char** words, int wordsSize, char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindString(string[] words, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} s
 * @return {number}
 */
var findString = function(words, s) {
    
};
```

### TypeScript

```typescript
function findString(words: string[], s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $s
     * @return Integer
     */
    function findString($words, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findString(_ words: [String], _ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findString(words: Array<String>, s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findString(List<String> words, String s) {
    
  }
}
```

### Go

```golang
func findString(words []string, s string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} s
# @return {Integer}
def find_string(words, s)
    
end
```

### Scala

```scala
object Solution {
    def findString(words: Array[String], s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_string(words: Vec<String>, s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-string words s)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_string(Words :: [unicode:unicode_binary()], S :: unicode:unicode_binary()) -> integer().
find_string(Words, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_string(words :: [String.t], s :: String.t) :: integer
  def find_string(words, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findString(words: Array<String>, s: String): Int64 {

    }
}
```

