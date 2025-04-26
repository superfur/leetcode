# 171. Excel 表列序号

## 题目描述

<p>给你一个字符串&nbsp;<code>columnTitle</code> ，表示 Excel 表格中的列名称。返回 <em>该列名称对应的列序号</em>&nbsp;。</p>

<p>例如：</p>

<pre>
A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...</pre>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> columnTitle = "A"
<strong>输出:</strong> 1
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入: </strong>columnTitle = "AB"
<strong>输出:</strong> 28
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入: </strong>columnTitle = "ZY"
<strong>输出:</strong> 701</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= columnTitle.length &lt;= 7</code></li>
	<li><code>columnTitle</code> 仅由大写英文组成</li>
	<li><code>columnTitle</code> 在范围 <code>["A", "FXSHRXW"]</code> 内</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 示例

```
"A"
"AB"
"ZY"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int titleToNumber(string columnTitle) {
        
    }
};
```

### Java

```java
class Solution {
    public int titleToNumber(String columnTitle) {
        
    }
}
```

### Python

```python
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
```

### C

```c
int titleToNumber(char* columnTitle) {
    
}
```

### C#

```csharp
public class Solution {
    public int TitleToNumber(string columnTitle) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    
};
```

### TypeScript

```typescript
function titleToNumber(columnTitle: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $columnTitle
     * @return Integer
     */
    function titleToNumber($columnTitle) {
        
    }
}
```

### Swift

```swift
class Solution {
    func titleToNumber(_ columnTitle: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun titleToNumber(columnTitle: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int titleToNumber(String columnTitle) {
    
  }
}
```

### Go

```golang
func titleToNumber(columnTitle string) int {
    
}
```

### Ruby

```ruby
# @param {String} column_title
# @return {Integer}
def title_to_number(column_title)
    
end
```

### Scala

```scala
object Solution {
    def titleToNumber(columnTitle: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (title-to-number columnTitle)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec title_to_number(ColumnTitle :: unicode:unicode_binary()) -> integer().
title_to_number(ColumnTitle) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec title_to_number(column_title :: String.t) :: integer
  def title_to_number(column_title) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func titleToNumber(columnTitle: String): Int64 {

    }
}
```

