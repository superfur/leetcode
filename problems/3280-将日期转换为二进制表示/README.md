# 3280. 将日期转换为二进制表示

## 题目描述

<p>给你一个字符串 <code>date</code>，它的格式为 <code>yyyy-mm-dd</code>，表示一个公历日期。</p>

<p><code>date</code> 可以重写为二进制表示，只需要将年、月、日分别转换为对应的二进制表示（不带前导零）并遵循 <code>year-month-day</code> 的格式。</p>

<p>返回 <code>date</code> 的 <strong>二进制</strong> 表示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">date = "2080-02-29"</span></p>

<p><strong>输出：</strong> <span class="example-io">"100000100000-10-11101"</span></p>

<p><strong>解释：</strong></p>

<p><span class="example-io">100000100000, 10 和 11101 分别是 2080, 02 和 29 的二进制表示。</span></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">date = "1900-01-01"</span></p>

<p><strong>输出：</strong> <span class="example-io">"11101101100-1-1"</span></p>

<p><strong>解释：</strong></p>

<p><span class="example-io">11101101100, 1 和 1 分别是 1900, 1 和 1 的二进制表示。</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>date.length == 10</code></li>
	<li><code>date[4] == date[7] == '-'</code>，其余的 <code>date[i]</code> 都是数字。</li>
	<li>输入保证 <code>date</code> 代表一个有效的公历日期，日期范围从 1900 年 1 月 1 日到 2100 年 12 月 31 日（包括这两天）。</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 示例

```
"2080-02-29"
"1900-01-01"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string convertDateToBinary(string date) {
        
    }
};
```

### Java

```java
class Solution {
    public String convertDateToBinary(String date) {
        
    }
}
```

### Python

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
```

### C

```c
char* convertDateToBinary(char* date) {
    
}
```

### C#

```csharp
public class Solution {
    public string ConvertDateToBinary(string date) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} date
 * @return {string}
 */
var convertDateToBinary = function(date) {
    
};
```

### TypeScript

```typescript
function convertDateToBinary(date: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $date
     * @return String
     */
    function convertDateToBinary($date) {
        
    }
}
```

### Swift

```swift
class Solution {
    func convertDateToBinary(_ date: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun convertDateToBinary(date: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String convertDateToBinary(String date) {
    
  }
}
```

### Go

```golang
func convertDateToBinary(date string) string {
    
}
```

### Ruby

```ruby
# @param {String} date
# @return {String}
def convert_date_to_binary(date)
    
end
```

### Scala

```scala
object Solution {
    def convertDateToBinary(date: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn convert_date_to_binary(date: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (convert-date-to-binary date)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec convert_date_to_binary(Date :: unicode:unicode_binary()) -> unicode:unicode_binary().
convert_date_to_binary(Date) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec convert_date_to_binary(date :: String.t) :: String.t
  def convert_date_to_binary(date) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func convertDateToBinary(date: String): String {

    }
}
```

