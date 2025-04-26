# 735. 小行星碰撞

## 题目描述

<p>给定一个整数数组 <code>asteroids</code>，表示在同一行的小行星。数组中小行星的索引表示它们在空间中的相对位置。</p>

<p>对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。</p>

<p>找出碰撞后剩下的所有小行星。碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。如果两颗小行星大小相同，则两颗小行星都会爆炸。两颗移动方向相同的小行星，永远不会发生碰撞。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [5,10,-5]
<strong>输出：</strong>[5,10]
<b>解释：</b>10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [8,-8]
<strong>输出：</strong>[]
<b>解释：</b>8 和 -8 碰撞后，两者都发生爆炸。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [10,2,-5]
<strong>输出：</strong>[10]
<b>解释：</b>2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= asteroids.length&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
	<li><code>asteroids[i] != 0</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 模拟

## 提示

1. Say a row of asteroids is stable.  What happens when a new asteroid is added on the right?

## 示例

```
[5,10,-5]
[8,-8]
[10,2,-5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        
    }
}
```

### Python

```python
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    
};
```

### TypeScript

```typescript
function asteroidCollision(asteroids: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $asteroids
     * @return Integer[]
     */
    function asteroidCollision($asteroids) {
        
    }
}
```

### Swift

```swift
class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> asteroidCollision(List<int> asteroids) {
    
  }
}
```

### Go

```golang
func asteroidCollision(asteroids []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} asteroids
# @return {Integer[]}
def asteroid_collision(asteroids)
    
end
```

### Scala

```scala
object Solution {
    def asteroidCollision(asteroids: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (asteroid-collision asteroids)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec asteroid_collision(Asteroids :: [integer()]) -> [integer()].
asteroid_collision(Asteroids) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec asteroid_collision(asteroids :: [integer]) :: [integer]
  def asteroid_collision(asteroids) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func asteroidCollision(asteroids: Array<Int64>): Array<Int64> {

    }
}
```

