# 2582. 递枕头

## 题目描述

<p><code>n</code> 个人站成一排，按从 <code>1</code> 到 <code>n</code> 编号。最初，排在队首的第一个人拿着一个枕头。每秒钟，拿着枕头的人会将枕头传递给队伍中的下一个人。一旦枕头到达队首或队尾，传递方向就会改变，队伍会继续沿相反方向传递枕头。</p>

<ul>
	<li>例如，当枕头到达第 <code>n</code> 个人时，TA 会将枕头传递给第 <code>n - 1</code> 个人，然后传递给第 <code>n - 2</code> 个人，依此类推。</li>
</ul>

<p>给你两个正整数 <code>n</code> 和 <code>time</code> ，返回 <code>time</code> 秒后拿着枕头的人的编号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, time = 5
<strong>输出：</strong>2
<strong>解释：</strong>队伍中枕头的传递情况为：1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 3 -&gt; 2 。
5 秒后，枕头传递到第 2 个人手中。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, time = 2
<strong>输出：</strong>3
<strong>解释：</strong>队伍中枕头的传递情况为：1 -&gt; 2 -&gt; 3 。
2 秒后，枕头传递到第 3 个人手中。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= time &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><b>注意：</b>本题与 <a href="https://leetcode.cn/problems/find-the-child-who-has-the-ball-after-k-seconds/">3178.找出 K 秒后拿着球的孩子</a>&nbsp;一致。</p>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Maintain two integer variables, direction and i, where direction denotes the current direction in which the pillow should pass, and i denotes an index of the person holding the pillow.
2. While time is positive, update the current index with the current direction. If the index reaches the end of the line, multiply direction by - 1.

## 示例

```
4
5
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int passThePillow(int n, int time) {
        
    }
};
```

### Java

```java
class Solution {
    public int passThePillow(int n, int time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
```

### C

```c
int passThePillow(int n, int time) {
    
}
```

### C#

```csharp
public class Solution {
    public int PassThePillow(int n, int time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} time
 * @return {number}
 */
var passThePillow = function(n, time) {
    
};
```

### TypeScript

```typescript
function passThePillow(n: number, time: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $time
     * @return Integer
     */
    function passThePillow($n, $time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func passThePillow(_ n: Int, _ time: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun passThePillow(n: Int, time: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int passThePillow(int n, int time) {
    
  }
}
```

### Go

```golang
func passThePillow(n int, time int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} time
# @return {Integer}
def pass_the_pillow(n, time)
    
end
```

### Scala

```scala
object Solution {
    def passThePillow(n: Int, time: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (pass-the-pillow n time)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec pass_the_pillow(N :: integer(), Time :: integer()) -> integer().
pass_the_pillow(N, Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pass_the_pillow(n :: integer, time :: integer) :: integer
  def pass_the_pillow(n, time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func passThePillow(n: Int64, time: Int64): Int64 {

    }
}
```

