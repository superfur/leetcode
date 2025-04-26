# 551. 学生出勤记录 I

## 题目描述

<p>给你一个字符串 <code>s</code> 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：</p>

<ul>
	<li><code>'A'</code>：Absent，缺勤</li>
	<li><code>'L'</code>：Late，迟到</li>
	<li><code>'P'</code>：Present，到场</li>
</ul>

<p>如果学生能够 <strong>同时</strong> 满足下面两个条件，则可以获得出勤奖励：</p>

<ul>
	<li>按 <strong>总出勤</strong> 计，学生缺勤（<code>'A'</code>）<strong>严格</strong> 少于两天。</li>
	<li>学生 <strong>不会</strong> 存在 <strong>连续</strong> 3 天或 <strong>连续</strong> 3 天以上的迟到（<code>'L'</code>）记录。</li>
</ul>

<p>如果学生可以获得出勤奖励，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "PPALLP"
<strong>输出：</strong>true
<strong>解释：</strong>学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "PPALLL"
<strong>输出：</strong>false
<strong>解释：</strong>学生最后三天连续迟到，所以不满足出勤奖励的条件。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> 为 <code>'A'</code>、<code>'L'</code> 或 <code>'P'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 示例

```
"PPALLP"
"PPALLL"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkRecord(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkRecord(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkRecord(self, s: str) -> bool:
        
```

### C

```c
bool checkRecord(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckRecord(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    
};
```

### TypeScript

```typescript
function checkRecord(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkRecord($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkRecord(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkRecord(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkRecord(String s) {
    
  }
}
```

### Go

```golang
func checkRecord(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_record(s)
    
end
```

### Scala

```scala
object Solution {
    def checkRecord(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_record(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-record s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_record(S :: unicode:unicode_binary()) -> boolean().
check_record(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_record(s :: String.t) :: boolean
  def check_record(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkRecord(s: String): Bool {

    }
}
```

