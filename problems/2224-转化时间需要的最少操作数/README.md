# 2224. 转化时间需要的最少操作数

## 题目描述

<p>给你两个字符串 <code>current</code> 和 <code>correct</code> ，表示两个 <strong>24 小时制时间</strong> 。</p>

<p><strong>24 小时制时间</strong> 按 <code>"HH:MM"</code> 进行格式化，其中 <code>HH</code> 在 <code>00</code> 和 <code>23</code> 之间，而 <code>MM</code> 在 <code>00</code> 和 <code>59</code> 之间。最早的 24 小时制时间为 <code>00:00</code> ，最晚的是 <code>23:59</code> 。</p>

<p>在一步操作中，你可以将 <code>current</code> 这个时间增加 <code>1</code>、<code>5</code>、<code>15</code> 或 <code>60</code> 分钟。你可以执行这一操作 <strong>任意</strong> 次数。</p>

<p>返回将&nbsp;<code>current</code><em> </em>转化为<em> </em><code>correct</code> 需要的 <strong>最少操作数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>current = "02:30", correct = "04:35"
<strong>输出：</strong>3
<strong>解释：
</strong>可以按下述 3 步操作将 current 转换为 correct ：
- 为 current 加 60 分钟，current 变为 "03:30" 。
- 为 current 加 60 分钟，current 变为 "04:30" 。 
- 为 current 加 5 分钟，current 变为 "04:35" 。
可以证明，无法用少于 3 步操作将 current 转化为 correct 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>current = "11:00", correct = "11:01"
<strong>输出：</strong>1
<strong>解释：</strong>只需要为 current 加一分钟，所以最小操作数是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>current</code> 和 <code>correct</code> 都符合 <code>"HH:MM"</code> 格式</li>
	<li><code>current &lt;= correct</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串

## 提示

1. Convert the times to minutes.
2. Use the operation with the biggest value possible at each step.

## 示例

```
"02:30"
"04:35"
"11:00"
"11:01"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int convertTime(string current, string correct) {
        
    }
};
```

### Java

```java
class Solution {
    public int convertTime(String current, String correct) {
        
    }
}
```

### Python

```python
class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
```

### C

```c
int convertTime(char* current, char* correct) {
    
}
```

### C#

```csharp
public class Solution {
    public int ConvertTime(string current, string correct) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} current
 * @param {string} correct
 * @return {number}
 */
var convertTime = function(current, correct) {
    
};
```

### TypeScript

```typescript
function convertTime(current: string, correct: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $current
     * @param String $correct
     * @return Integer
     */
    function convertTime($current, $correct) {
        
    }
}
```

### Swift

```swift
class Solution {
    func convertTime(_ current: String, _ correct: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun convertTime(current: String, correct: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int convertTime(String current, String correct) {
    
  }
}
```

### Go

```golang
func convertTime(current string, correct string) int {
    
}
```

### Ruby

```ruby
# @param {String} current
# @param {String} correct
# @return {Integer}
def convert_time(current, correct)
    
end
```

### Scala

```scala
object Solution {
    def convertTime(current: String, correct: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn convert_time(current: String, correct: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (convert-time current correct)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec convert_time(Current :: unicode:unicode_binary(), Correct :: unicode:unicode_binary()) -> integer().
convert_time(Current, Correct) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec convert_time(current :: String.t, correct :: String.t) :: integer
  def convert_time(current, correct) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func convertTime(current: String, correct: String): Int64 {

    }
}
```

