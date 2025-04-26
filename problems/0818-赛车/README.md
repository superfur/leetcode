# 818. 赛车

## 题目描述

你的赛车可以从位置 <code>0</code> 开始，并且速度为 <code>+1</code> ，在一条无限长的数轴上行驶。赛车也可以向负方向行驶。赛车可以按照由加速指令 <code>'A'</code> 和倒车指令 <code>'R'</code> 组成的指令序列自动行驶。
<ul>
	<li>当收到指令 <code>'A'</code> 时，赛车这样行驶：
	<ul>
		<li><code>position += speed</code></li>
		<li><code>speed *= 2</code></li>
	</ul>
	</li>
	<li>当收到指令 <code>'R'</code> 时，赛车这样行驶：
	<ul>
		<li>如果速度为正数，那么<code>speed = -1</code></li>
		<li>否则 <code>speed = 1</code></li>
	</ul>
	当前所处位置不变。</li>
</ul>

<p>例如，在执行指令 <code>"AAR"</code> 后，赛车位置变化为 <code>0 --&gt; 1 --&gt; 3 --&gt; 3</code> ，速度变化为 <code>1 --&gt; 2 --&gt; 4 --&gt; -1</code> 。</p>

<p>给你一个目标位置 <code>target</code> ，返回能到达目标位置的最短指令序列的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = 3
<strong>输出：</strong>2
<strong>解释：</strong>
最短指令序列是 "AA" 。
位置变化 0 --&gt; 1 --&gt; 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = 6
<strong>输出：</strong>5
<strong>解释：</strong>
最短指令序列是 "AAARA" 。
位置变化 0 --&gt; 1 --&gt; 3 --&gt; 7 --&gt; 7 --&gt; 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 示例

```
3
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int racecar(int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int racecar(int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def racecar(self, target: int) -> int:
        
```

### C

```c
int racecar(int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int Racecar(int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @return {number}
 */
var racecar = function(target) {
    
};
```

### TypeScript

```typescript
function racecar(target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @return Integer
     */
    function racecar($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func racecar(_ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun racecar(target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int racecar(int target) {
    
  }
}
```

### Go

```golang
func racecar(target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @return {Integer}
def racecar(target)
    
end
```

### Scala

```scala
object Solution {
    def racecar(target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn racecar(target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (racecar target)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec racecar(Target :: integer()) -> integer().
racecar(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec racecar(target :: integer) :: integer
  def racecar(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func racecar(target: Int64): Int64 {

    }
}
```

