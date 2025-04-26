# 2381. 字母移位 II

## 题目描述

<p>给你一个小写英文字母组成的字符串&nbsp;<code>s</code>&nbsp;和一个二维整数数组&nbsp;<code>shifts</code>&nbsp;，其中&nbsp;<code>shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]</code>&nbsp;。对于每个&nbsp;<code>i</code>&nbsp;，将&nbsp;<code>s</code>&nbsp;中从下标&nbsp;<code>start<sub>i</sub></code>&nbsp;到下标&nbsp;<code>end<sub>i</sub></code>&nbsp;（两者都包含）所有字符都进行移位运算，如果&nbsp;<code>direction<sub>i</sub> = 1</code>&nbsp;将字符向后移位，如果&nbsp;<code>direction<sub>i</sub> = 0</code>&nbsp;将字符向前移位。</p>

<p>将一个字符 <strong>向后</strong>&nbsp;移位的意思是将这个字符用字母表中 <strong>下一个</strong>&nbsp;字母替换（字母表视为环绕的，所以&nbsp;<code>'z'</code>&nbsp;变成&nbsp;<code>'a'</code>）。类似的，将一个字符 <strong>向前</strong>&nbsp;移位的意思是将这个字符用字母表中 <strong>前一个</strong>&nbsp;字母替换（字母表是环绕的，所以&nbsp;<code>'a'</code>&nbsp;变成&nbsp;<code>'z'</code>&nbsp;）。</p>

<p>请你返回对 <code>s</code>&nbsp;进行所有移位操作以后得到的最终字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
<b>输出：</b>"ace"
<b>解释：</b>首先，将下标从 0 到 1 的字母向前移位，得到 s = "zac" 。
然后，将下标从 1 到 2 的字母向后移位，得到 s = "zbd" 。
最后，将下标从 0 到 2 的字符向后移位，得到 s = "ace" 。</pre>

<p><strong>示例 2:</strong></p>

<pre><b>输入：</b>s = "dztz", shifts = [[0,0,0],[1,1,1]]
<b>输出：</b>"catz"
<b>解释：</b>首先，将下标从 0 到 0 的字母向前移位，得到 s = "cztz" 。
最后，将下标从 1 到 1 的字符向后移位，得到 s = "catz" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, shifts.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>shifts[i].length == 3</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; s.length</code></li>
	<li><code>0 &lt;= direction<sub>i</sub> &lt;= 1</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 前缀和

## 提示

1. Instead of shifting every character in each shift, could you keep track of which characters are shifted and by how much across all shifts?
2. Try marking the start and ends of each shift, then perform a prefix sum of the shifts.

## 示例

```
"abc"
[[0,1,0],[1,2,1],[0,2,1]]
"dztz"
[[0,0,0],[1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        
    }
};
```

### Java

```java
class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
```

### C

```c
char* shiftingLetters(char* s, int** shifts, int shiftsSize, int* shiftsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShiftingLetters(string s, int[][] shifts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[][]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    
};
```

### TypeScript

```typescript
function shiftingLetters(s: string, shifts: number[][]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shiftingLetters(_ s: String, _ shifts: [[Int]]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shiftingLetters(s: String, shifts: Array<IntArray>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shiftingLetters(String s, List<List<int>> shifts) {
    
  }
}
```

### Go

```golang
func shiftingLetters(s string, shifts [][]int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} shifts
# @return {String}
def shifting_letters(s, shifts)
    
end
```

### Scala

```scala
object Solution {
    def shiftingLetters(s: String, shifts: Array[Array[Int]]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<Vec<i32>>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shifting-letters s shifts)
  (-> string? (listof (listof exact-integer?)) string?)
  )
```

### Erlang

```erlang
-spec shifting_letters(S :: unicode:unicode_binary(), Shifts :: [[integer()]]) -> unicode:unicode_binary().
shifting_letters(S, Shifts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shifting_letters(s :: String.t, shifts :: [[integer]]) :: String.t
  def shifting_letters(s, shifts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shiftingLetters(s: String, shifts: Array<Array<Int64>>): String {

    }
}
```

