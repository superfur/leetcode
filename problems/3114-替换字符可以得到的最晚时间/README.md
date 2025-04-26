# 3114. 替换字符可以得到的最晚时间

## 题目描述

<p>给你一个字符串 <code>s</code>，表示一个 12 小时制的时间格式，其中一些数字（可能没有）被 <code>"?"</code> 替换。</p>

<p>12 小时制时间格式为 <code>"HH:MM"</code> ，其中 <code>HH</code> 的取值范围为 <code>00</code> 至 <code>11</code>，<code>MM</code> 的取值范围为 <code>00</code> 至 <code>59</code>。最早的时间为 <code>00:00</code>，最晚的时间为 <code>11:59</code>。</p>

<p>你需要将 <code>s</code> 中的<strong> 所有</strong> <code>"?"</code> 字符替换为数字，使得结果字符串代表的时间是一个<strong> 有效 </strong>的 12 小时制时间，并且是可能的 <strong>最晚 </strong>时间。</p>

<p>返回结果字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "1?:?4"</span></p>

<p><strong>输出：</strong> <span class="example-io">"11:54"</span></p>

<p><strong>解释：</strong> 通过替换 <code>"?"</code> 字符，可以得到的最晚12小时制时间是 <code>"11:54"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "0?:5?"</span></p>

<p><strong>输出：</strong> <span class="example-io">"09:59"</span></p>

<p><strong>解释：</strong> 通过替换 <code>"?"</code> 字符，可以得到的最晚12小时制时间是 <code>"09:59"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s.length == 5</code></li>
	<li><code>s[2]</code> 是字符 <code>":"</code></li>
	<li>除 <code>s[2]</code> 外，其他字符都是数字或 <code>"?"</code></li>
	<li>输入保证在替换 <code>"?"</code> 字符后至少存在一个介于 <code>"00:00"</code> 和 <code>"11:59"</code> 之间的时间。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 枚举

## 提示

1. Try using a brute force approach.
2. Iterate over all possible times that can be generated from the string and find the latest one.

## 示例

```
"1?:?4"
"0?:5?"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findLatestTime(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String findLatestTime(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findLatestTime(self, s: str) -> str:
        
```

### C

```c
char* findLatestTime(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindLatestTime(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var findLatestTime = function(s) {
    
};
```

### TypeScript

```typescript
function findLatestTime(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function findLatestTime($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLatestTime(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLatestTime(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findLatestTime(String s) {
    
  }
}
```

### Go

```golang
func findLatestTime(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def find_latest_time(s)
    
end
```

### Scala

```scala
object Solution {
    def findLatestTime(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_latest_time(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-latest-time s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec find_latest_time(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
find_latest_time(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_latest_time(s :: String.t) :: String.t
  def find_latest_time(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLatestTime(s: String): String {

    }
}
```

