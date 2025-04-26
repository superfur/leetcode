# 面试题 08.08. 有重复字符串的排列组合

## 题目描述

<p>有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：S = "qqe"
<strong> 输出</strong>：["eqq","qeq","qqe"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：S = "ab"
<strong> 输出</strong>：["ab", "ba"]
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>字符都是英文字母。</li>
	<li>字符串长度在[1, 9]之间。</li>
</ol>


## 难度

Medium

## 标签

- 字符串
- 回溯

## 提示

1. 你可以通过在打印之前检查是否有重复内容（或将它们添加到列表中）来处理此问题。你可以用散列表来做到这一点。在什么情况下，这样是可以的？在什么情况下，这可能不是一个很好的解法？
2. 如果你还没有解决8.7的问题，就先解决那个。
3. 试着获得每个字符的计数。例如，abcaac有3个a、2个c和1个b。
4. 要得到3个a、2个c和1个b的全排列，你首先需要选择一个起始字符：a、b或c。如果是a，那么你需要2个a、2个c和1个b的全排列。

## 示例

```
"qqe"
"ab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> permutation(string S) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] permutation(String S) {
        
    }
}
```

### Python

```python
class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def permutation(self, S: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** permutation(char* S, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] Permutation(string S) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} S
 * @return {string[]}
 */
var permutation = function(S) {
    
};
```

### TypeScript

```typescript
function permutation(S: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $S
     * @return String[]
     */
    function permutation($S) {
        
    }
}
```

### Swift

```swift
class Solution {
    func permutation(_ S: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun permutation(S: String): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> permutation(String S) {
    
  }
}
```

### Go

```golang
func permutation(S string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def permutation(s)
    
end
```

### Scala

```scala
object Solution {
    def permutation(S: String): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn permutation(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (permutation S)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec permutation(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
permutation(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec permutation(s :: String.t) :: [String.t]
  def permutation(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func permutation(S: String): Array<String> {

    }
}
```

