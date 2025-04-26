# 2446. 判断两个事件是否存在冲突

## 题目描述

<p>给你两个字符串数组 <code>event1</code> 和&nbsp;<code>event2</code>&nbsp;，表示发生在同一天的两个闭区间时间段事件，其中：</p>

<ul>
	<li><code>event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]</code> 且</li>
	<li><code>event2 = [startTime<sub>2</sub>, endTime<sub>2</sub>]</code></li>
</ul>

<p>事件的时间为有效的 24 小时制且按&nbsp;<code>HH:MM</code>&nbsp;格式给出。</p>

<p>当两个事件存在某个非空的交集时（即，某些时刻是两个事件都包含的），则认为出现 <strong>冲突</strong>&nbsp;。</p>

<p>如果两个事件之间存在冲突，返回&nbsp;<code>true</code><em>&nbsp;</em>；否则，返回<em>&nbsp;</em><code>false</code> 。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<b>输入：</b>event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
<b>输出：</b>true
<b>解释：</b>两个事件在 2:00 出现交集。
</pre>

<p><b>示例 2：</b></p>

<pre>
<b>输入：</b>event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
<b>输出：</b>true
<b>解释：</b>两个事件的交集从 01:20 开始，到 02:00 结束。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
<b>输出：</b>false
<b>解释：</b>两个事件不存在交集。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>event1.length == event2.length == 2</code></li>
	<li><code>event1[i].length == event2[i].length == 5</code></li>
	<li><code>startTime<sub>1</sub> &lt;= endTime<sub>1</sub></code></li>
	<li><code>startTime<sub>2</sub> &lt;= endTime<sub>2</sub></code></li>
	<li>所有事件的时间都按照&nbsp;<code>HH:MM</code>&nbsp;格式给出</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Parse time format to some integer interval first
2. How would you determine if two intervals overlap?

## 示例

```
["01:15","02:00"]
["02:00","03:00"]
["01:00","02:00"]
["01:20","03:00"]
["10:00","11:00"]
["14:00","15:00"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
```

### C

```c
bool haveConflict(char** event1, int event1Size, char** event2, int event2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HaveConflict(string[] event1, string[] event2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} event1
 * @param {string[]} event2
 * @return {boolean}
 */
var haveConflict = function(event1, event2) {
    
};
```

### TypeScript

```typescript
function haveConflict(event1: string[], event2: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $event1
     * @param String[] $event2
     * @return Boolean
     */
    function haveConflict($event1, $event2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func haveConflict(_ event1: [String], _ event2: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun haveConflict(event1: Array<String>, event2: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool haveConflict(List<String> event1, List<String> event2) {
    
  }
}
```

### Go

```golang
func haveConflict(event1 []string, event2 []string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} event1
# @param {String[]} event2
# @return {Boolean}
def have_conflict(event1, event2)
    
end
```

### Scala

```scala
object Solution {
    def haveConflict(event1: Array[String], event2: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn have_conflict(event1: Vec<String>, event2: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (have-conflict event1 event2)
  (-> (listof string?) (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec have_conflict(Event1 :: [unicode:unicode_binary()], Event2 :: [unicode:unicode_binary()]) -> boolean().
have_conflict(Event1, Event2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec have_conflict(event1 :: [String.t], event2 :: [String.t]) :: boolean
  def have_conflict(event1, event2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func haveConflict(event1: Array<String>, event2: Array<String>): Bool {

    }
}
```

