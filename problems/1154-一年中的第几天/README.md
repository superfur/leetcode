# 1154. 一年中的第几天

## 题目描述

<p>给你一个字符串&nbsp;<code>date</code> ，按 <code>YYYY-MM-DD</code> 格式表示一个 <a href="https://baike.baidu.com/item/公元/17855" target="_blank">现行公元纪年法</a> 日期。返回该日期是当年的第几天。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>date = "2019-01-09"
<strong>输出：</strong>9
<strong>解释：</strong>给定日期是2019年的第九天。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>date = "2019-02-10"
<strong>输出：</strong>41
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>date.length == 10</code></li>
	<li><code>date[4] == date[7] == '-'</code>，其他的&nbsp;<code>date[i]</code>&nbsp;都是数字</li>
	<li><code>date</code> 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 提示

1. Have a integer array of how many days there are per month.  February gets one extra day if its a leap year.  Then, we can manually count the ordinal as day + (number of days in months before this one).

## 示例

```
"2019-01-09"
"2019-02-10"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int dayOfYear(string date) {
        
    }
};
```

### Java

```java
class Solution {
    public int dayOfYear(String date) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def dayOfYear(self, date: str) -> int:
        
```

### C

```c
int dayOfYear(char* date) {
    
}
```

### C#

```csharp
public class Solution {
    public int DayOfYear(string date) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    
};
```

### TypeScript

```typescript
function dayOfYear(date: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $date
     * @return Integer
     */
    function dayOfYear($date) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dayOfYear(_ date: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dayOfYear(date: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int dayOfYear(String date) {
    
  }
}
```

### Go

```golang
func dayOfYear(date string) int {
    
}
```

### Ruby

```ruby
# @param {String} date
# @return {Integer}
def day_of_year(date)
    
end
```

### Scala

```scala
object Solution {
    def dayOfYear(date: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn day_of_year(date: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (day-of-year date)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec day_of_year(Date :: unicode:unicode_binary()) -> integer().
day_of_year(Date) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec day_of_year(date :: String.t) :: integer
  def day_of_year(date) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dayOfYear(date: String): Int64 {

    }
}
```

