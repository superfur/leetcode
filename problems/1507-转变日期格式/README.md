# 1507. 转变日期格式

## 题目描述

<p>给你一个字符串&nbsp;<code>date</code>&nbsp;，它的格式为&nbsp;<code>Day Month Year</code>&nbsp;，其中：</p>

<ul>
	<li><code>Day</code>&nbsp;是集合&nbsp;<code>{&quot;1st&quot;, &quot;2nd&quot;, &quot;3rd&quot;, &quot;4th&quot;, ..., &quot;30th&quot;, &quot;31st&quot;}</code>&nbsp;中的一个元素。</li>
	<li><code>Month</code>&nbsp;是集合&nbsp;<code>{&quot;Jan&quot;, &quot;Feb&quot;, &quot;Mar&quot;, &quot;Apr&quot;, &quot;May&quot;, &quot;Jun&quot;, &quot;Jul&quot;, &quot;Aug&quot;, &quot;Sep&quot;, &quot;Oct&quot;, &quot;Nov&quot;, &quot;Dec&quot;}</code>&nbsp;中的一个元素。</li>
	<li><code>Year</code>&nbsp;的范围在 ​<code>[1900, 2100]</code>&nbsp;之间。</li>
</ul>

<p>请你将字符串转变为&nbsp;<code>YYYY-MM-DD</code>&nbsp;的格式，其中：</p>

<ul>
	<li><code>YYYY</code>&nbsp;表示 4 位的年份。</li>
	<li><code>MM</code>&nbsp;表示 2 位的月份。</li>
	<li><code>DD</code>&nbsp;表示 2 位的天数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>date = &quot;20th Oct 2052&quot;
<strong>输出：</strong>&quot;2052-10-20&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>date = &quot;6th Jun 1933&quot;
<strong>输出：</strong>&quot;1933-06-06&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>date = &quot;26th May 1960&quot;
<strong>输出：</strong>&quot;1960-05-26&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给定日期保证是合法的，所以不需要处理异常输入。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Handle the conversions of day, month and year separately.
2. Notice that days always have a two-word ending, so if you erase the last two characters of this days you'll get the number.

## 示例

```
"20th Oct 2052"
"6th Jun 1933"
"26th May 1960"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reformatDate(string date) {
        
    }
};
```

### Java

```java
class Solution {
    public String reformatDate(String date) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reformatDate(self, date: str) -> str:
        
```

### C

```c
char* reformatDate(char* date) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReformatDate(string date) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} date
 * @return {string}
 */
var reformatDate = function(date) {
    
};
```

### TypeScript

```typescript
function reformatDate(date: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $date
     * @return String
     */
    function reformatDate($date) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reformatDate(_ date: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reformatDate(date: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reformatDate(String date) {
    
  }
}
```

### Go

```golang
func reformatDate(date string) string {
    
}
```

### Ruby

```ruby
# @param {String} date
# @return {String}
def reformat_date(date)
    
end
```

### Scala

```scala
object Solution {
    def reformatDate(date: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reformat_date(date: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reformat-date date)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reformat_date(Date :: unicode:unicode_binary()) -> unicode:unicode_binary().
reformat_date(Date) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reformat_date(date :: String.t) :: String.t
  def reformat_date(date) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reformatDate(date: String): String {

    }
}
```

