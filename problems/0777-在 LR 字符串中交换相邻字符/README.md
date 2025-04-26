# 777. 在 LR 字符串中交换相邻字符

## 题目描述

<p>在一个由 <code>'L'</code> , <code>'R'</code> 和 <code>'X'</code> 三个字符组成的字符串（例如<code>"RXXLRXRXL"</code>）中进行移动操作。一次移动操作指用一个&nbsp;<code>"LX"</code>&nbsp;替换一个&nbsp;<code>"XL"</code>，或者用一个&nbsp;<code>"XR"</code>&nbsp;替换一个&nbsp;<code>"RX"</code>。现给定起始字符串&nbsp;<code>start</code>&nbsp;和结束字符串&nbsp;<code>result</code>，请编写代码，当且仅当存在一系列移动操作使得&nbsp;<code>start</code>&nbsp;可以转换成&nbsp;<code>result</code>&nbsp;时， 返回&nbsp;<code>True</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "RXXLRXRXL", result = "XRLXXRRLX"
<strong>输出：</strong>true
<strong>解释：</strong>通过以下步骤我们可以将 start 转化为 result：
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "X", result = "L"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= start.length&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>start.length == result.length</code></li>
	<li><code>start</code> 和&nbsp;<code>result</code>&nbsp;都只包含&nbsp;<code>'L'</code>, <code>'R'</code>&nbsp;或&nbsp;<code>'X'</code>。</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. Think of the L and R's as people on a horizontal line, where X is a space.  The people can't cross each other, and also you can't go from XRX to RXX.

## 示例

```
"RXXLRXRXL"
"XRLXXRRLX"
"X"
"L"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canTransform(string start, string result) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canTransform(String start, String result) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
```

### C

```c
bool canTransform(char* start, char* result) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanTransform(string start, string result) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} start
 * @param {string} result
 * @return {boolean}
 */
var canTransform = function(start, result) {
    
};
```

### TypeScript

```typescript
function canTransform(start: string, result: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $start
     * @param String $result
     * @return Boolean
     */
    function canTransform($start, $result) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canTransform(_ start: String, _ result: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canTransform(start: String, result: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canTransform(String start, String result) {
    
  }
}
```

### Go

```golang
func canTransform(start string, result string) bool {
    
}
```

### Ruby

```ruby
# @param {String} start
# @param {String} result
# @return {Boolean}
def can_transform(start, result)
    
end
```

### Scala

```scala
object Solution {
    def canTransform(start: String, result: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_transform(start: String, result: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-transform start result)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_transform(Start :: unicode:unicode_binary(), Result :: unicode:unicode_binary()) -> boolean().
can_transform(Start, Result) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_transform(start :: String.t, result :: String.t) :: boolean
  def can_transform(start, result) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canTransform(start: String, result: String): Bool {

    }
}
```

