# 2109. 向字符串添加空格

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，以及一个下标从 <strong>0</strong> 开始的整数数组 <code>spaces</code> 。</p>

<p>数组 <code>spaces</code> 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 <strong>之前</strong> 。</p>

<ul>
	<li>例如，<code>s = "EnjoyYourCoffee"</code> 且 <code>spaces = [5, 9]</code> ，那么我们需要在 <code>'Y'</code> 和 <code>'C'</code> 之前添加空格，这两个字符分别位于下标 <code>5</code> 和下标 <code>9</code> 。因此，最终得到 <code>"Enjoy <em><strong>Y</strong></em>our <em><strong>C</strong></em>offee"</code> 。</li>
</ul>

<p>请你添加空格，并返回修改后的字符串<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
<strong>输出：</strong>"Leetcode Helps Me Learn"
<strong>解释：</strong>
下标 8、13 和 15 对应 "Leetcode<em><strong>H</strong></em>elps<em><strong>M</strong></em>e<em><strong>L</strong></em>earn" 中加粗斜体字符。
接着在这些字符前添加空格。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "icodeinpython", spaces = [1,5,7,9]
<strong>输出：</strong>"i code in py thon"
<strong>解释：</strong>
下标 1、5、7 和 9 对应 "i<em><strong>c</strong></em>ode<em><strong>i</strong></em>n<em><strong>p</strong></em>y<em><strong>t</strong></em>hon" 中加粗斜体字符。
接着在这些字符前添加空格。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "spacing", spaces = [0,1,2,3,4,5,6]
<strong>输出：</strong>" s p a c i n g"
<strong>解释：</strong>
字符串的第一个字符前可以添加空格。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由大小写英文字母组成</li>
	<li><code>1 &lt;= spaces.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= spaces[i] &lt;= s.length - 1</code></li>
	<li><code>spaces</code> 中的所有值 <strong>严格递增</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 字符串
- 模拟

## 提示

1. Create a new string, initially empty, as the modified string. Iterate through the original string and append each character of the original string to the new string. However, each time you reach a character that requires a space before it, append a space before appending the character.
2. Since the array of indices for the space locations is sorted, use a pointer to keep track of the next index to place a space. Only increment the pointer once a space has been appended.
3. Ensure that your append operation can be done in O(1).

## 示例

```
"LeetcodeHelpsMeLearn"
[8,13,15]
"icodeinpython"
[1,5,7,9]
"spacing"
[0,1,2,3,4,5,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        
    }
};
```

### Java

```java
class Solution {
    public String addSpaces(String s, int[] spaces) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
```

### C

```c
char* addSpaces(char* s, int* spaces, int spacesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string AddSpaces(string s, int[] spaces) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    
};
```

### TypeScript

```typescript
function addSpaces(s: string, spaces: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $spaces
     * @return String
     */
    function addSpaces($s, $spaces) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addSpaces(_ s: String, _ spaces: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addSpaces(s: String, spaces: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String addSpaces(String s, List<int> spaces) {
    
  }
}
```

### Go

```golang
func addSpaces(s string, spaces []int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} spaces
# @return {String}
def add_spaces(s, spaces)
    
end
```

### Scala

```scala
object Solution {
    def addSpaces(s: String, spaces: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_spaces(s: String, spaces: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (add-spaces s spaces)
  (-> string? (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec add_spaces(S :: unicode:unicode_binary(), Spaces :: [integer()]) -> unicode:unicode_binary().
add_spaces(S, Spaces) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_spaces(s :: String.t, spaces :: [integer]) :: String.t
  def add_spaces(s, spaces) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addSpaces(s: String, spaces: Array<Int64>): String {

    }
}
```

