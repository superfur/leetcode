# 168. Excel 表列名称

## 题目描述

<p>给你一个整数 <code>columnNumber</code> ，返回它在 Excel 表中相对应的列名称。</p>

<p>例如：</p>

<pre>
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
</pre>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>columnNumber = 1
<strong>输出：</strong>"A"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>columnNumber = 28
<strong>输出：</strong>"AB"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>columnNumber = 701
<strong>输出：</strong>"ZY"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>columnNumber = 2147483647
<strong>输出：</strong>"FXSHRXW"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= columnNumber <= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 示例

```
1
28
701
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string convertToTitle(int columnNumber) {
        
    }
};
```

### Java

```java
class Solution {
    public String convertToTitle(int columnNumber) {
        
    }
}
```

### Python

```python
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
```

### C

```c
char* convertToTitle(int columnNumber) {
    
}
```

### C#

```csharp
public class Solution {
    public string ConvertToTitle(int columnNumber) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    
};
```

### TypeScript

```typescript
function convertToTitle(columnNumber: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $columnNumber
     * @return String
     */
    function convertToTitle($columnNumber) {
        
    }
}
```

### Swift

```swift
class Solution {
    func convertToTitle(_ columnNumber: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun convertToTitle(columnNumber: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String convertToTitle(int columnNumber) {
    
  }
}
```

### Go

```golang
func convertToTitle(columnNumber int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} column_number
# @return {String}
def convert_to_title(column_number)
    
end
```

### Scala

```scala
object Solution {
    def convertToTitle(columnNumber: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (convert-to-title columnNumber)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec convert_to_title(ColumnNumber :: integer()) -> unicode:unicode_binary().
convert_to_title(ColumnNumber) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec convert_to_title(column_number :: integer) :: String.t
  def convert_to_title(column_number) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func convertToTitle(columnNumber: Int64): String {

    }
}
```

