# 672. 灯泡开关 Ⅱ

## 题目描述

<p>房间中有 <code>n</code>&nbsp;只已经打开的灯泡，编号从 <code>1</code> 到 <code>n</code> 。墙上挂着 <strong>4 个开关</strong> 。</p>

<p>这 4 个开关各自都具有不同的功能，其中：</p>

<ul>
	<li><strong>开关 1 ：</strong>反转当前所有灯的状态（即开变为关，关变为开）</li>
	<li><strong>开关 2 ：</strong>反转编号为偶数的灯的状态（即 <code>0, 2, 4, ...</code>）</li>
	<li><strong>开关 3 ：</strong>反转编号为奇数的灯的状态（即 <code>1, 3, ...</code>）</li>
	<li><strong>开关 4 ：</strong>反转编号为 <code>j = 3k + 1</code> 的灯的状态，其中 <code>k = 0, 1, 2, ...</code>（即 <code>1, 4, 7, 10, ...</code>）</li>
</ul>

<p>你必须 <strong>恰好</strong> 按压开关 <code>presses</code> 次。每次按压，你都需要从 4 个开关中选出一个来执行按压操作。</p>

<p>给你两个整数 <code>n</code> 和 <code>presses</code> ，执行完所有按压之后，返回 <strong>不同可能状态</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1, presses = 1
<strong>输出：</strong>2
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关]
- 按压开关 2 ，[开]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, presses = 1
<strong>输出：</strong>3
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关, 关]
- 按压开关 2 ，[开, 关]
- 按压开关 3 ，[关, 开]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3, presses = 1
<strong>输出：</strong>4
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关, 关, 关]
- 按压开关 2 ，[关, 开, 关]
- 按压开关 3 ，[开, 关, 开]
- 按压开关 4 ，[关, 开, 开]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= presses &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 深度优先搜索
- 广度优先搜索
- 数学

## 示例

```
1
1
2
1
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int flipLights(int n, int presses) {
        
    }
};
```

### Java

```java
class Solution {
    public int flipLights(int n, int presses) {
        
    }
}
```

### Python

```python
class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        
```

### C

```c
int flipLights(int n, int presses) {
    
}
```

### C#

```csharp
public class Solution {
    public int FlipLights(int n, int presses) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} presses
 * @return {number}
 */
var flipLights = function(n, presses) {
    
};
```

### TypeScript

```typescript
function flipLights(n: number, presses: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $presses
     * @return Integer
     */
    function flipLights($n, $presses) {
        
    }
}
```

### Swift

```swift
class Solution {
    func flipLights(_ n: Int, _ presses: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun flipLights(n: Int, presses: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int flipLights(int n, int presses) {
    
  }
}
```

### Go

```golang
func flipLights(n int, presses int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} presses
# @return {Integer}
def flip_lights(n, presses)
    
end
```

### Scala

```scala
object Solution {
    def flipLights(n: Int, presses: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn flip_lights(n: i32, presses: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (flip-lights n presses)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec flip_lights(N :: integer(), Presses :: integer()) -> integer().
flip_lights(N, Presses) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec flip_lights(n :: integer, presses :: integer) :: integer
  def flip_lights(n, presses) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func flipLights(n: Int64, presses: Int64): Int64 {

    }
}
```

