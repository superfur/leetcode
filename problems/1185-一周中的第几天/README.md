# 1185. 一周中的第几天

## 题目描述

<p>给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。</p>

<p>输入为三个整数：<code>day</code>、<code>month</code> 和&nbsp;<code>year</code>，分别表示日、月、年。</p>

<p>您返回的结果必须是这几个值中的一个&nbsp;<code>{&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>day = 31, month = 8, year = 2019
<strong>输出：</strong>&quot;Saturday&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>day = 18, month = 7, year = 1999
<strong>输出：</strong>&quot;Sunday&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>day = 15, month = 8, year = 1993
<strong>输出：</strong>&quot;Sunday&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给出的日期一定是在&nbsp;<code>1971</code> 到&nbsp;<code>2100</code>&nbsp;年之间的有效日期。</li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Sum up the number of days for the years before the given year.
2. Handle the case of a leap year.
3. Find the number of days for each month of the given year.

## 示例

```
31
8
2019
18
7
1999
15
8
1993
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        
    }
};
```

### Java

```java
class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
```

### C

```c
char* dayOfTheWeek(int day, int month, int year) {
    
}
```

### C#

```csharp
public class Solution {
    public string DayOfTheWeek(int day, int month, int year) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    
};
```

### TypeScript

```typescript
function dayOfTheWeek(day: number, month: number, year: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $day
     * @param Integer $month
     * @param Integer $year
     * @return String
     */
    function dayOfTheWeek($day, $month, $year) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dayOfTheWeek(_ day: Int, _ month: Int, _ year: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dayOfTheWeek(day: Int, month: Int, year: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String dayOfTheWeek(int day, int month, int year) {
    
  }
}
```

### Go

```golang
func dayOfTheWeek(day int, month int, year int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} day
# @param {Integer} month
# @param {Integer} year
# @return {String}
def day_of_the_week(day, month, year)
    
end
```

### Scala

```scala
object Solution {
    def dayOfTheWeek(day: Int, month: Int, year: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn day_of_the_week(day: i32, month: i32, year: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (day-of-the-week day month year)
  (-> exact-integer? exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec day_of_the_week(Day :: integer(), Month :: integer(), Year :: integer()) -> unicode:unicode_binary().
day_of_the_week(Day, Month, Year) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec day_of_the_week(day :: integer, month :: integer, year :: integer) :: String.t
  def day_of_the_week(day, month, year) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dayOfTheWeek(day: Int64, month: Int64, year: Int64): String {

    }
}
```

