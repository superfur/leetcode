# 1974. 使用特殊打字机键入单词的最少时间

## 题目描述

<p>有一个特殊打字机，它由一个 <strong>圆盘</strong> 和一个 <strong>指针</strong>&nbsp;组成， 圆盘上标有小写英文字母&nbsp;<code>'a'</code> 到&nbsp;<code>'z'</code>。<strong>只有</strong>&nbsp;当指针指向某个字母时，它才能被键入。指针 <strong>初始时</strong>&nbsp;指向字符 <code>'a'</code>&nbsp;。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/31/chart.jpg" style="width: 530px; height: 410px;" />
<p>每一秒钟，你可以执行以下操作之一：</p>

<ul>
	<li>将指针 <strong>顺时针</strong>&nbsp;或者 <b>逆时针</b>&nbsp;移动一个字符。</li>
	<li>键入指针 <strong>当前</strong>&nbsp;指向的字符。</li>
</ul>

<p>给你一个字符串&nbsp;<code>word</code>&nbsp;，请你返回键入&nbsp;<code>word</code>&nbsp;所表示单词的 <b>最少</b>&nbsp;秒数&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>word = "abc"
<b>输出：</b>5
<strong>解释：
</strong>单词按如下操作键入：
- 花 1 秒键入字符 'a' in 1 ，因为指针初始指向 'a' ，故不需移动指针。
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 1 秒将指针顺时针移到 'c' 。
- 花 1 秒键入字符 'c' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>word = "bza"
<b>输出：</b>7
<strong>解释：
</strong>单词按如下操作键入：
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 2 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 1 秒将指针顺时针移到 'a' 。
- 花 1 秒键入字符 'a' 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>word = "zjpc"
<b>输出：</b>34
<strong>解释：</strong>
单词按如下操作键入：
- 花 1 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 10 秒将指针顺时针移到 'j' 。
- 花 1 秒键入字符 'j' 。
- 花 6 秒将指针顺时针移到 'p' 。
- 花 1 秒键入字符 'p' 。
- 花 13 秒将指针逆时针移到 'c' 。
- 花 1 秒键入字符 'c' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串

## 提示

1. There are only two possible directions you can go when you move to the next letter.
2. When moving to the next letter, you will always go in the direction that takes the least amount of time.

## 示例

```
"abc"
"bza"
"zjpc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minTimeToType(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int minTimeToType(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minTimeToType(self, word: str) -> int:
        
```

### C

```c
int minTimeToType(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinTimeToType(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minTimeToType = function(word) {
    
};
```

### TypeScript

```typescript
function minTimeToType(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minTimeToType($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minTimeToType(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minTimeToType(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minTimeToType(String word) {
    
  }
}
```

### Go

```golang
func minTimeToType(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def min_time_to_type(word)
    
end
```

### Scala

```scala
object Solution {
    def minTimeToType(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_time_to_type(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-time-to-type word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_time_to_type(Word :: unicode:unicode_binary()) -> integer().
min_time_to_type(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_time_to_type(word :: String.t) :: integer
  def min_time_to_type(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minTimeToType(word: String): Int64 {

    }
}
```

