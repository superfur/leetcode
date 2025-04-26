# 1561. 你可以获得的最大硬币数目

## 题目描述

<p>有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：</p>

<ul>
	<li>每一轮中，你将会选出 <strong>任意</strong> 3 堆硬币（不一定连续）。</li>
	<li>Alice 将会取走硬币数量最多的那一堆。</li>
	<li>你将会取走硬币数量第二多的那一堆。</li>
	<li>Bob 将会取走最后一堆。</li>
	<li>重复这个过程，直到没有更多硬币。</li>
</ul>

<p>给你一个整数数组 <code>piles</code> ，其中 <code>piles[i]</code> 是第 <code>i</code> 堆中硬币的数目。</p>

<p>返回你可以获得的最大硬币数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>piles = [2,4,1,2,7,8]
<strong>输出：</strong>9
<strong>解释：</strong>选出 (2, 7, 8) ，Alice 取走 8 枚硬币的那堆，你取走 <strong>7</strong> 枚硬币的那堆，Bob 取走最后一堆。
选出 (1, 2, 4) , Alice 取走 4 枚硬币的那堆，你取走 <strong>2</strong> 枚硬币的那堆，Bob 取走最后一堆。
你可以获得的最大硬币数目：7 + 2 = 9.
考虑另外一种情况，如果选出的是 (1, <strong>2</strong>, 8) 和 (2, <strong>4</strong>, 7) ，你就只能得到 2 + 4 = 6 枚硬币，这不是最优解。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>piles = [2,4,5]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>piles = [9,8,7,6,5,1,2,3,4]
<strong>输出：</strong>18
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= piles.length &lt;= 10^5</code></li>
	<li><code>piles.length % 3 == 0</code></li>
	<li><code>1 &lt;= piles[i] &lt;= 10^4</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 博弈
- 排序

## 提示

1. Which pile of coins will you never be able to pick up?
2. Bob is forced to take the last pile of coins, no matter what it is. Which pile should you give to him?

## 示例

```
[2,4,1,2,7,8]
[2,4,5]
[9,8,7,6,5,1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCoins(vector<int>& piles) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCoins(int[] piles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
```

### C

```c
int maxCoins(int* piles, int pilesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCoins(int[] piles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    
};
```

### TypeScript

```typescript
function maxCoins(piles: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function maxCoins($piles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCoins(_ piles: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCoins(piles: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCoins(List<int> piles) {
    
  }
}
```

### Go

```golang
func maxCoins(piles []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} piles
# @return {Integer}
def max_coins(piles)
    
end
```

### Scala

```scala
object Solution {
    def maxCoins(piles: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_coins(piles: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-coins piles)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_coins(Piles :: [integer()]) -> integer().
max_coins(Piles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_coins(piles :: [integer]) :: integer
  def max_coins(piles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCoins(piles: Array<Int64>): Int64 {

    }
}
```

