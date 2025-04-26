# 2126. 摧毁小行星

## 题目描述

<p>给你一个整数&nbsp;<code>mass</code>&nbsp;，它表示一颗行星的初始质量。再给你一个整数数组&nbsp;<code>asteroids</code>&nbsp;，其中&nbsp;<code>asteroids[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;颗小行星的质量。</p>

<p>你可以按 <strong>任意顺序</strong>&nbsp;重新安排小行星的顺序，然后让行星跟它们发生碰撞。如果行星碰撞时的质量 <strong>大于等于</strong>&nbsp;小行星的质量，那么小行星被 <strong>摧毁</strong>&nbsp;，并且行星会 <strong>获得</strong>&nbsp;这颗小行星的质量。否则，行星将被摧毁。</p>

<p>如果所有小行星 <strong>都</strong>&nbsp;能被摧毁，请返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>mass = 10, asteroids = [3,9,19,5,21]
<b>输出：</b>true
<b>解释：</b>一种安排小行星的方式为 [9,19,5,3,21] ：
- 行星与质量为 9 的小行星碰撞。新的行星质量为：10 + 9 = 19
- 行星与质量为 19 的小行星碰撞。新的行星质量为：19 + 19 = 38
- 行星与质量为 5 的小行星碰撞。新的行星质量为：38 + 5 = 43
- 行星与质量为 3 的小行星碰撞。新的行星质量为：43 + 3 = 46
- 行星与质量为 21 的小行星碰撞。新的行星质量为：46 + 21 = 67
所有小行星都被摧毁。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>mass = 5, asteroids = [4,9,23,4]
<b>输出：</b>false
<b>解释：</b>
行星无论如何没法获得足够质量去摧毁质量为 23 的小行星。
行星把别的小行星摧毁后，质量为 5 + 4 + 9 + 4 = 22 。
它比 23 小，所以无法摧毁最后一颗小行星。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= mass &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= asteroids.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= asteroids[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Choosing the asteroid to collide with can be done greedily.
2. If an asteroid will destroy the planet, then every bigger asteroid will also destroy the planet.
3. You only need to check the smallest asteroid at each collision. If it will destroy the planet, then every other asteroid will also destroy the planet.
4. Sort the asteroids in non-decreasing order by mass, then greedily try to collide with the asteroids in that order.

## 示例

```
10
[3,9,19,5,21]
5
[4,9,23,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        
    }
}
```

### Python

```python
class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
```

### C

```c
bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */
var asteroidsDestroyed = function(mass, asteroids) {
    
};
```

### TypeScript

```typescript
function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $mass
     * @param Integer[] $asteroids
     * @return Boolean
     */
    function asteroidsDestroyed($mass, $asteroids) {
        
    }
}
```

### Swift

```swift
class Solution {
    func asteroidsDestroyed(_ mass: Int, _ asteroids: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun asteroidsDestroyed(mass: Int, asteroids: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool asteroidsDestroyed(int mass, List<int> asteroids) {
    
  }
}
```

### Go

```golang
func asteroidsDestroyed(mass int, asteroids []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} mass
# @param {Integer[]} asteroids
# @return {Boolean}
def asteroids_destroyed(mass, asteroids)
    
end
```

### Scala

```scala
object Solution {
    def asteroidsDestroyed(mass: Int, asteroids: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (asteroids-destroyed mass asteroids)
  (-> exact-integer? (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec asteroids_destroyed(Mass :: integer(), Asteroids :: [integer()]) -> boolean().
asteroids_destroyed(Mass, Asteroids) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec asteroids_destroyed(mass :: integer, asteroids :: [integer]) :: boolean
  def asteroids_destroyed(mass, asteroids) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func asteroidsDestroyed(mass: Int64, asteroids: Array<Int64>): Bool {

    }
}
```

