# 1046. 最后一块石头的重量

## 题目描述

<p>有一堆石头，每块石头的重量都是正整数。</p>

<p>每一回合，从中选出两块<strong> 最重的</strong> 石头，然后将它们一起粉碎。假设石头的重量分别为 <code>x</code> 和 <code>y</code>，且 <code>x <= y</code>。那么粉碎的可能结果如下：</p>

<ul>
	<li>如果 <code>x == y</code>，那么两块石头都会被完全粉碎；</li>
	<li>如果 <code>x != y</code>，那么重量为 <code>x</code> 的石头将会完全粉碎，而重量为 <code>y</code> 的石头新重量为 <code>y-x</code>。</li>
</ul>

<p>最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 <code>0</code>。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>[2,7,4,1,8,1]
<strong>输出：</strong>1
<strong>解释：</strong>
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= stones.length <= 30</code></li>
	<li><code>1 <= stones[i] <= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 堆（优先队列）

## 提示

1. Simulate the process.  We can do it with a heap, or by sorting some list of stones every time we take a turn.

## 示例

```
[2,7,4,1,8,1]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int lastStoneWeight(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
```

### C

```c
int lastStoneWeight(int* stones, int stonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LastStoneWeight(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    
};
```

### TypeScript

```typescript
function lastStoneWeight(stones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeight($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lastStoneWeight(_ stones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lastStoneWeight(stones: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lastStoneWeight(List<int> stones) {
    
  }
}
```

### Go

```golang
func lastStoneWeight(stones []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
    
end
```

### Scala

```scala
object Solution {
    def lastStoneWeight(stones: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (last-stone-weight stones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec last_stone_weight(Stones :: [integer()]) -> integer().
last_stone_weight(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec last_stone_weight(stones :: [integer]) :: integer
  def last_stone_weight(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lastStoneWeight(stones: Array<Int64>): Int64 {

    }
}
```

