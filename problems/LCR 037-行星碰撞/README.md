# LCR 037. 行星碰撞

## 题目描述

<p>给定一个整数数组 <code>asteroids</code>，表示在同一行的小行星。</p>

<p>对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。</p>

<p>找出碰撞后剩下的所有小行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [5,10,-5]
<strong>输出：</strong>[5,10]
<strong>解释：</strong>10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [8,-8]
<strong>输出：</strong>[]
<strong>解释：</strong>8 和 -8 碰撞后，两者都发生爆炸。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [10,2,-5]
<strong>输出：</strong>[10]
<strong>解释：</strong>2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>asteroids = [-2,-1,1,2]
<strong>输出：</strong>[-2,-1,1,2]
<strong>解释：</strong>-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。 </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= asteroids.length&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
	<li><code>asteroids[i] != 0</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 735&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/asteroid-collision/">https://leetcode-cn.com/problems/asteroid-collision/</a></p>


## 难度

Medium

## 标签

- 栈
- 数组
- 模拟

## 示例

```
[5,10,-5]
[8,-8]
[10,2,-5]
[-2,-1,1,2]
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
int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize){

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

