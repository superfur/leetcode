# 2930. 重新排列后包含指定子字符串的字符串数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;。</p>

<p>如果一个字符串&nbsp;<code>s</code>&nbsp;只包含小写英文字母，<strong>且</strong>&nbsp;将 <code>s</code>&nbsp;的字符重新排列后，新字符串包含&nbsp;<strong>子字符串</strong>&nbsp;<code>"leet"</code> ，那么我们称字符串 <code>s</code>&nbsp;是一个 <strong>好</strong>&nbsp;字符串。</p>

<p>比方说：</p>

<ul>
	<li>字符串&nbsp;<code>"lteer"</code>&nbsp;是好字符串，因为重新排列后可以得到&nbsp;<code>"leetr"</code>&nbsp;。</li>
	<li><code>"letl"</code>&nbsp;不是好字符串，因为无法重新排列并得到子字符串&nbsp;<code>"leet"</code>&nbsp;。</li>
</ul>

<p>请你返回长度为 <code>n</code>&nbsp;的好字符串 <strong>总</strong>&nbsp;数目。</p>

<p>由于答案可能很大，将答案对<strong>&nbsp;</strong><code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p><strong>子字符串</strong>&nbsp;是一个字符串中一段连续的字符序列。</p>

<div class="notranslate" style="all: initial;">&nbsp;</div>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 4
<b>输出：</b>12
<b>解释：</b>总共有 12 个字符串重新排列后包含子字符串 "leet" ："eelt" ，"eetl" ，"elet" ，"elte" ，"etel" ，"etle" ，"leet" ，"lete" ，"ltee" ，"teel" ，"tele" 和 "tlee" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 10
<b>输出：</b>83943898
<b>解释：</b>长度为 10 的字符串重新排列后包含子字符串 "leet" 的方案数为 526083947580 。所以答案为 526083947580 % (10<sup>9</sup> + 7) = 83943898 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. A good string must contain at least one <code>l</code>, one <code>t</code>, and two <code>e</code>.
2. Divide the problem into subproblems and use Dynamic Programming.

## 示例

```
4
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stringCount(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int stringCount(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stringCount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stringCount(self, n: int) -> int:
        
```

### C

```c
int stringCount(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int StringCount(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var stringCount = function(n) {
    
};
```

### TypeScript

```typescript
function stringCount(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function stringCount($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stringCount(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stringCount(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stringCount(int n) {
    
  }
}
```

### Go

```golang
func stringCount(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def string_count(n)
    
end
```

### Scala

```scala
object Solution {
    def stringCount(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn string_count(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (string-count n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec string_count(N :: integer()) -> integer().
string_count(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec string_count(n :: integer) :: integer
  def string_count(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stringCount(n: Int64): Int64 {

    }
}
```

