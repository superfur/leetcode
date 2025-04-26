# 1736. 替换隐藏数字得到的最晚时间

## 题目描述

<p>给你一个字符串 <code>time</code> ，格式为 <code> hh:mm</code>（小时：分钟），其中某几位数字被隐藏（用 <code>?</code> 表示）。</p>

<p>有效的时间为 <code>00:00</code> 到 <code>23:59</code> 之间的所有时间，包括 <code>00:00</code> 和 <code>23:59</code> 。</p>

<p>替换 <code>time</code> 中隐藏的数字，返回你可以得到的最晚有效时间。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>time = "2?:?0"
<strong>输出：</strong>"23:50"
<strong>解释：</strong>以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>time = "0?:3?"
<strong>输出：</strong>"09:39"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>time = "1?:22"
<strong>输出：</strong>"19:22"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>time</code> 的格式为 <code>hh:mm</code></li>
	<li>题目数据保证你可以由输入的字符串生成有效的时间</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串

## 提示

1. Trying out all possible solutions from biggest to smallest would fit in the time limit.
2. To check if the solution is okay, you need to find out if it's valid and matches every character

## 示例

```
"2?:?0"
"0?:3?"
"1?:22"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string maximumTime(string time) {
        
    }
};
```

### Java

```java
class Solution {
    public String maximumTime(String time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def maximumTime(self, time: str) -> str:
        
```

### C

```c
char* maximumTime(char* time) {
    
}
```

### C#

```csharp
public class Solution {
    public string MaximumTime(string time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} time
 * @return {string}
 */
var maximumTime = function(time) {
    
};
```

### TypeScript

```typescript
function maximumTime(time: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $time
     * @return String
     */
    function maximumTime($time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTime(_ time: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTime(time: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String maximumTime(String time) {
    
  }
}
```

### Go

```golang
func maximumTime(time string) string {
    
}
```

### Ruby

```ruby
# @param {String} time
# @return {String}
def maximum_time(time)
    
end
```

### Scala

```scala
object Solution {
    def maximumTime(time: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_time(time: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-time time)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec maximum_time(Time :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_time(Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_time(time :: String.t) :: String.t
  def maximum_time(time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTime(time: String): String {

    }
}
```

