# 401. 二进制手表

## 题目描述

<p>二进制手表顶部有 4 个 LED 代表<strong> 小时（0-11）</strong>，底部的 6 个 LED 代表<strong> 分钟（0-59）</strong>。每个 LED 代表一个 0 或 1，最低位在右侧。</p>

<ul>
	<li>例如，下面的二进制手表读取 <code>"4:51"</code> 。</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" style="height: 300px; width" /></p>

<p>给你一个整数 <code>turnedOn</code> ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p>小时不会以零开头：</p>

<ul>
	<li>例如，<code>"01:00"</code> 是无效的时间，正确的写法应该是 <code>"1:00"</code> 。</li>
</ul>

<p>分钟必须由两位数组成，可能会以零开头：</p>

<ul>
	<li>例如，<code>"10:2"</code> 是无效的时间，正确的写法应该是 <code>"10:02"</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>turnedOn = 1
<strong>输出：</strong>["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>turnedOn = 9
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= turnedOn &lt;= 10</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 回溯

## 提示

1. Simplify by seeking for solutions that involve comparing bit counts.
2. Consider calculating all possible times for comparison purposes.

## 示例

```
1
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        
    }
}
```

### Python

```python
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** readBinaryWatch(int turnedOn, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> ReadBinaryWatch(int turnedOn) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} turnedOn
 * @return {string[]}
 */
var readBinaryWatch = function(turnedOn) {
    
};
```

### TypeScript

```typescript
function readBinaryWatch(turnedOn: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $turnedOn
     * @return String[]
     */
    function readBinaryWatch($turnedOn) {
        
    }
}
```

### Swift

```swift
class Solution {
    func readBinaryWatch(_ turnedOn: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun readBinaryWatch(turnedOn: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> readBinaryWatch(int turnedOn) {
    
  }
}
```

### Go

```golang
func readBinaryWatch(turnedOn int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer} turned_on
# @return {String[]}
def read_binary_watch(turned_on)
    
end
```

### Scala

```scala
object Solution {
    def readBinaryWatch(turnedOn: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (read-binary-watch turnedOn)
  (-> exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec read_binary_watch(TurnedOn :: integer()) -> [unicode:unicode_binary()].
read_binary_watch(TurnedOn) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec read_binary_watch(turned_on :: integer) :: [String.t]
  def read_binary_watch(turned_on) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func readBinaryWatch(turnedOn: Int64): ArrayList<String> {

    }
}
```

