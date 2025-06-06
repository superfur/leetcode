# 806. 写字符串需要的行数

## 题目描述

<p>我们要把给定的字符串 <code>S</code>&nbsp;从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组&nbsp;<code>widths</code>&nbsp;，这个数组&nbsp;widths[0] 代表 &#39;a&#39; 需要的单位，&nbsp;widths[1] 代表 &#39;b&#39; 需要的单位，...，&nbsp;widths[25] 代表 &#39;z&#39; 需要的单位。</p>

<p>现在回答两个问题：至少多少行能放下<code>S</code>，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = &quot;abcdefghijklmnopqrstuvwxyz&quot;
<strong>输出:</strong> [3, 60]
<strong>解释: 
</strong>所有的字符拥有相同的占用单位10。所以书写所有的26个字母，
我们需要2个整行和占用60个单位的一行。
</pre>

<pre>
<strong>示例 2:</strong>
<strong>输入:</strong> 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = &quot;bbbcccdddaaa&quot;
<strong>输出:</strong> [2, 4]
<strong>解释: 
</strong>除去字母&#39;a&#39;所有的字符都是相同的单位10，并且字符串 &quot;bbbcccdddaa&quot; 将会覆盖 9 * 10 + 2 * 4 = 98 个单位.
最后一个字母 &#39;a&#39; 将会被写到第二行，因为第一行只剩下2个单位了。
所以，这个答案是2行，第二行有4个单位宽度。
</pre>

<p>&nbsp;</p>

<p><strong>注:</strong></p>

<ul>
	<li>字符串&nbsp;<code>S</code> 的长度在&nbsp;[1, 1000] 的范围。</li>
	<li><code>S</code> 只包含小写字母。</li>
	<li><code>widths</code> 是长度为&nbsp;<code>26</code>的数组。</li>
	<li><code>widths[i]</code>&nbsp;值的范围在&nbsp;<code>[2, 10]</code>。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 示例

```
[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
"abcdefghijklmnopqrstuvwxyz"
[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
"bbbcccdddaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* widths, int widthsSize, char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumberOfLines(int[] widths, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function(widths, s) {
    
};
```

### TypeScript

```typescript
function numberOfLines(widths: number[], s: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $widths
     * @param String $s
     * @return Integer[]
     */
    function numberOfLines($widths, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfLines(_ widths: [Int], _ s: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfLines(widths: IntArray, s: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numberOfLines(List<int> widths, String s) {
    
  }
}
```

### Go

```golang
func numberOfLines(widths []int, s string) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} widths
# @param {String} s
# @return {Integer[]}
def number_of_lines(widths, s)
    
end
```

### Scala

```scala
object Solution {
    def numberOfLines(widths: Array[Int], s: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_lines(widths: Vec<i32>, s: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-lines widths s)
  (-> (listof exact-integer?) string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec number_of_lines(Widths :: [integer()], S :: unicode:unicode_binary()) -> [integer()].
number_of_lines(Widths, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_lines(widths :: [integer], s :: String.t) :: [integer]
  def number_of_lines(widths, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfLines(widths: Array<Int64>, s: String): Array<Int64> {

    }
}
```

