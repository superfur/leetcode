# 2437. 有效时间的数目

## 题目描述

<p>给你一个长度为&nbsp;<code>5</code>&nbsp;的字符串&nbsp;<code>time</code>&nbsp;，表示一个电子时钟当前的时间，格式为&nbsp;<code>"hh:mm"</code>&nbsp;。<strong>最早</strong>&nbsp;可能的时间是&nbsp;<code>"00:00"</code>&nbsp;，<strong>最晚</strong>&nbsp;可能的时间是&nbsp;<code>"23:59"</code>&nbsp;。</p>

<p>在字符串&nbsp;<code>time</code>&nbsp;中，被字符&nbsp;<code>?</code>&nbsp;替换掉的数位是 <strong>未知的</strong>&nbsp;，被替换的数字可能是&nbsp;<code>0</code>&nbsp;到&nbsp;<code>9</code>&nbsp;中的任何一个。</p>

<p>请你返回一个整数<em>&nbsp;</em><code>answer</code>&nbsp;，将每一个 <code>?</code>&nbsp;都用<em>&nbsp;</em><code>0</code>&nbsp;到<em>&nbsp;</em><code>9</code>&nbsp;中一个数字替换后，可以得到的有效时间的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>time = "?5:00"
<b>输出：</b>2
<b>解释：</b>我们可以将 ? 替换成 0 或 1 ，得到 "05:00" 或者 "15:00" 。注意我们不能替换成 2 ，因为时间 "25:00" 是无效时间。所以我们有两个选择。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>time = "0?:0?"
<b>输出：</b>100
<b>解释：</b>两个 ? 都可以被 0 到 9 之间的任意数字替换，所以我们总共有 100 种选择。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>time = "??:??"
<b>输出：</b>1440
<b>解释：</b>小时总共有 24 种选择，分钟总共有 60 种选择。所以总共有 24 * 60 = 1440 种选择。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>time</code>&nbsp;是一个长度为 <code>5</code>&nbsp;的有效字符串，格式为&nbsp;<code>"hh:mm"</code>&nbsp;。</li>
	<li><code>"00" &lt;= hh &lt;= "23"</code></li>
	<li><code>"00" &lt;= mm &lt;= "59"</code></li>
	<li>字符串中有的数位是&nbsp;<code>'?'</code>&nbsp;，需要用&nbsp;<code>0</code>&nbsp;到&nbsp;<code>9</code>&nbsp;之间的数字替换。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 枚举

## 提示

1. Brute force all possible clock times.
2. Checking if a clock time is valid can be done with Regex.

## 示例

```
"?5:00"
"0?:0?"
"??:??"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTime(string time) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTime(String time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTime(self, time: str) -> int:
        
```

### C

```c
int countTime(char* time) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTime(string time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} time
 * @return {number}
 */
var countTime = function(time) {
    
};
```

### TypeScript

```typescript
function countTime(time: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $time
     * @return Integer
     */
    function countTime($time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTime(_ time: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTime(time: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTime(String time) {
    
  }
}
```

### Go

```golang
func countTime(time string) int {
    
}
```

### Ruby

```ruby
# @param {String} time
# @return {Integer}
def count_time(time)
    
end
```

### Scala

```scala
object Solution {
    def countTime(time: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_time(time: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-time time)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_time(Time :: unicode:unicode_binary()) -> integer().
count_time(Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_time(time :: String.t) :: integer
  def count_time(time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTime(time: String): Int64 {

    }
}
```

