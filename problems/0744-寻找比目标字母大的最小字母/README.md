# 744. 寻找比目标字母大的最小字母

## 题目描述

<p>给你一个字符数组 <code>letters</code>，该数组按<strong>非递减顺序</strong>排序，以及一个字符 <code>target</code>。<code>letters</code>&nbsp;里<strong>至少有两个不同</strong>的字符。</p>

<p>返回&nbsp;<code>letters</code>&nbsp;中大于 <code>target</code> 的最小的字符。如果不存在这样的字符，则返回&nbsp;<code>letters</code> 的第一个字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>letters = ["c", "f", "j"]，target = "a"
<strong>输出:</strong> "c"
<strong>解释：</strong>letters 中字典上比 'a' 大的最小字符是 'c'。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> letters = ["c","f","j"], target = "c"
<strong>输出:</strong> "f"
<strong>解释：</strong>letters 中字典顺序上大于 'c' 的最小字符是 'f'。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> letters = ["x","x","y","y"], target = "z"
<strong>输出:</strong> "x"
<strong>解释：</strong>letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code>&nbsp;是一个小写字母</li>
	<li><code>letters</code> 按<strong>非递减顺序</strong>排序</li>
	<li><code>letters</code> 最少包含两个不同的字母</li>
	<li><code>target</code> 是一个小写字母</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 提示

1. Try to find whether each of 26 next letters are in the given string array.

## 示例

```
["c","f","j"]
"a"
["c","f","j"]
"c"
["x","x","y","y"]
"z"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        
    }
};
```

### Java

```java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
```

### C

```c
char nextGreatestLetter(char* letters, int lettersSize, char target) {
    
}
```

### C#

```csharp
public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    
};
```

### TypeScript

```typescript
function nextGreatestLetter(letters: string[], target: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $letters
     * @param String $target
     * @return String
     */
    function nextGreatestLetter($letters, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nextGreatestLetter(_ letters: [Character], _ target: Character) -> Character {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        
    }
}
```

### Dart

```dart
class Solution {
  String nextGreatestLetter(List<String> letters, String target) {
    
  }
}
```

### Go

```golang
func nextGreatestLetter(letters []byte, target byte) byte {
    
}
```

### Ruby

```ruby
# @param {Character[]} letters
# @param {Character} target
# @return {Character}
def next_greatest_letter(letters, target)
    
end
```

### Scala

```scala
object Solution {
    def nextGreatestLetter(letters: Array[Char], target: Char): Char = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        
    }
}
```

### Racket

```racket
(define/contract (next-greatest-letter letters target)
  (-> (listof char?) char? char?)
  )
```

### Erlang

```erlang
-spec next_greatest_letter(Letters :: [char()], Target :: char()) -> char().
next_greatest_letter(Letters, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec next_greatest_letter(letters :: [char], target :: char) :: char
  def next_greatest_letter(letters, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nextGreatestLetter(letters: Array<Rune>, target: Rune): Rune {

    }
}
```

