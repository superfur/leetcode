# 319. 灯泡开关

## 题目描述

<p>初始时有&nbsp;<code>n</code><em> </em>个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭第二个。</p>

<p>第三轮，你每三个灯泡就切换第三个灯泡的开关（即，打开变关闭，关闭变打开）。第 <code>i</code> 轮，你每 <code>i</code> 个灯泡就切换第 <code>i</code> 个灯泡的开关。直到第 <code>n</code> 轮，你只需要切换最后一个灯泡的开关。</p>

<p>找出并返回 <code>n</code><em>&nbsp;</em>轮后有多少个亮着的灯泡。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg" style="width: 421px; height: 321px;" /></p>

<pre>
<strong>输入：</strong>n =<strong> </strong>3
<strong>输出：</strong>1 
<strong>解释：</strong>
初始时, 灯泡状态 <strong>[关闭, 关闭, 关闭]</strong>.
第一轮后, 灯泡状态 <strong>[开启, 开启, 开启]</strong>.
第二轮后, 灯泡状态 <strong>[开启, 关闭, 开启]</strong>.
第三轮后, 灯泡状态 <strong>[开启, 关闭, 关闭]</strong>. 

你应该返回 1，因为只有一个灯泡还亮着。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 0
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数学

## 示例

```
3
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bulbSwitch(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int bulbSwitch(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bulbSwitch(self, n: int) -> int:
        
```

### C

```c
int bulbSwitch(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int BulbSwitch(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    
};
```

### TypeScript

```typescript
function bulbSwitch(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function bulbSwitch($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bulbSwitch(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bulbSwitch(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bulbSwitch(int n) {
    
  }
}
```

### Go

```golang
func bulbSwitch(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def bulb_switch(n)
    
end
```

### Scala

```scala
object Solution {
    def bulbSwitch(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn bulb_switch(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (bulb-switch n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec bulb_switch(N :: integer()) -> integer().
bulb_switch(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec bulb_switch(n :: integer) :: integer
  def bulb_switch(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bulbSwitch(n: Int64): Int64 {

    }
}
```

