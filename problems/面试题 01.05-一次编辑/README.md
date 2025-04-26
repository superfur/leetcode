# 面试题 01.05. 一次编辑

## 题目描述

<p>字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
first = "pale"
second = "ple"
<strong>输出：</strong>True</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
first = "pales"
second = "pal"
<strong>输出：</strong>False
</pre>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. 从容易的事情开始。你能分别检查一下每一个条件吗？
2. “插入字符”选项和“删除字符”选项之间是何关系？这些需要分开检查吗？
3. 你能一次完成三次检查吗？

## 示例

```
"horse"
"ros"
"intention"
"execution"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool oneEditAway(string first, string second) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean oneEditAway(String first, String second) {
        
    }
}
```

### Python

```python
class Solution(object):
    def oneEditAway(self, first, second):
        """
        :type first: str
        :type second: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        
```

### C

```c
bool oneEditAway(char* first, char* second) {
    
}
```

### C#

```csharp
public class Solution {
    public bool OneEditAway(string first, string second) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} first
 * @param {string} second
 * @return {boolean}
 */
var oneEditAway = function(first, second) {
    
};
```

### TypeScript

```typescript
function oneEditAway(first: string, second: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $first
     * @param String $second
     * @return Boolean
     */
    function oneEditAway($first, $second) {
        
    }
}
```

### Swift

```swift
class Solution {
    func oneEditAway(_ first: String, _ second: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun oneEditAway(first: String, second: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool oneEditAway(String first, String second) {
    
  }
}
```

### Go

```golang
func oneEditAway(first string, second string) bool {
    
}
```

### Ruby

```ruby
# @param {String} first
# @param {String} second
# @return {Boolean}
def one_edit_away(first, second)
    
end
```

### Scala

```scala
object Solution {
    def oneEditAway(first: String, second: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn one_edit_away(first: String, second: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (one-edit-away first second)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec one_edit_away(First :: unicode:unicode_binary(), Second :: unicode:unicode_binary()) -> boolean().
one_edit_away(First, Second) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec one_edit_away(first :: String.t, second :: String.t) :: boolean
  def one_edit_away(first, second) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func oneEditAway(first: String, second: String): Bool {

    }
}
```

