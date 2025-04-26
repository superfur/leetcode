# 473. 火柴拼正方形

## 题目描述

<p>你将得到一个整数数组 <code>matchsticks</code> ，其中 <code>matchsticks[i]</code> 是第 <code>i</code>&nbsp;个火柴棒的长度。你要用 <strong>所有的火柴棍</strong>&nbsp;拼成一个正方形。你 <strong>不能折断</strong> 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 <strong>使用一次</strong> 。</p>

<p>如果你能使这个正方形，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg" /></p>

<pre>
<strong>输入:</strong> matchsticks = [1,1,2,2,2]
<strong>输出:</strong> true
<strong>解释:</strong> 能拼成一个边长为2的正方形，每边两根火柴。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> matchsticks = [3,3,3,3,4]
<strong>输出:</strong> false
<strong>解释:</strong> 不能用所有火柴拼成一个正方形。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= matchsticks.length &lt;= 15</code></li>
	<li><code>1 &lt;= matchsticks[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. Treat the matchsticks as an array. Can we split the array into 4 equal parts?
2. Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
3. For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use of recursion for this.
4. We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need to keep track of the <b>length</b> of each of the 4 sides.
5. When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a square on our hands!

## 示例

```
[1,1,2,2,2]
[3,3,3,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean makesquare(int[] matchsticks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
```

### C

```c
bool makesquare(int* matchsticks, int matchsticksSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool Makesquare(int[] matchsticks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function(matchsticks) {
    
};
```

### TypeScript

```typescript
function makesquare(matchsticks: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $matchsticks
     * @return Boolean
     */
    function makesquare($matchsticks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makesquare(_ matchsticks: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makesquare(matchsticks: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool makesquare(List<int> matchsticks) {
    
  }
}
```

### Go

```golang
func makesquare(matchsticks []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} matchsticks
# @return {Boolean}
def makesquare(matchsticks)
    
end
```

### Scala

```scala
object Solution {
    def makesquare(matchsticks: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn makesquare(matchsticks: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (makesquare matchsticks)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec makesquare(Matchsticks :: [integer()]) -> boolean().
makesquare(Matchsticks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec makesquare(matchsticks :: [integer]) :: boolean
  def makesquare(matchsticks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makesquare(matchsticks: Array<Int64>): Bool {

    }
}
```

