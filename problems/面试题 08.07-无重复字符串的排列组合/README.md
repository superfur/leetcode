# 面试题 08.07. 无重复字符串的排列组合

## 题目描述

<p>无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：S = "qwe"
<strong> 输出</strong>：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：S = "ab"
<strong> 输出</strong>：["ab", "ba"]
</pre>

<p><strong>提示：</strong></p>

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

1. 方法1：假设你有abc的所有排列。你怎么用它来得到abcd的所有排列？
2. 方法1：abc的排列组合表示abc的所有组合方式。现在，我们要创建abcd的所有组合方式。选择abcd的特定组合，如bdca。这个bdca字符串也代表abc的一种排列方式：删除d，你会得到bca。那么给定字符串bca，你是否可以创建包含d 的所有“相关”排列组合？
3. 方法1：给定一个字符串，比如bca，可以通过将d 插入到每个可能的位置：dbca、bdca、bcda、bcad，来创建abcd（其中abc顺序一定）的所有排列组合。给定abc的所有排列，你可以创建所有abcd的排列吗？
4. 方法1：你可以通过计算abc的所有排列，然后在每个可能的位置插入d，从而创建abcd的所有排列。
5. 方法2：如果你拥有两个字符所有排列的子串，可以生成三个字符全排列的子串吗？
6. 方法2：生成一个abcd的全排列，需要选择一个初始字符。它可以是a、b、c或d。然后你可以排列其余的字符。如何使用这种方法生成完整字符串的所有排列？
7. 方法 2：要生成abcd的所有排列组合，请选择每个字符（a、b、c、d）作为首字符。排列剩余的字符并追加首字符。如何排列剩余的字符？使用遵循相同逻辑的递归过程。
8. 方法 2：你可以通过让递归函数返回字符串列表来实现该方法，然后在它上面追加首字符。或者，你可以将前缀下推到递归调用中。

## 示例

```
"qwe"
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

