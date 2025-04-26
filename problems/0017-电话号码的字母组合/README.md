# 17. 电话号码的字母组合

## 题目描述

<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。答案可以按 <strong>任意顺序</strong> 返回。</p>

<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-telephone-keypad2svg.png" style="width: 200px;" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = "23"
<strong>输出：</strong>["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = ""
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>digits = "2"
<strong>输出：</strong>["a","b","c"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> 是范围 <code>['2', '9']</code> 的一个数字。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 回溯

## 示例

```
"23"
""
"2"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> letterCombinations(String digits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCombinations(char* digits, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> LetterCombinations(string digits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    
};
```

### TypeScript

```typescript
function letterCombinations(digits: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $digits
     * @return String[]
     */
    function letterCombinations($digits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func letterCombinations(_ digits: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun letterCombinations(digits: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> letterCombinations(String digits) {
    
  }
}
```

### Go

```golang
func letterCombinations(digits string) []string {
    
}
```

### Ruby

```ruby
# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
    
end
```

### Scala

```scala
object Solution {
    def letterCombinations(digits: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (letter-combinations digits)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec letter_combinations(Digits :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
letter_combinations(Digits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec letter_combinations(digits :: String.t) :: [String.t]
  def letter_combinations(digits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func letterCombinations(digits: String): ArrayList<String> {

    }
}
```

