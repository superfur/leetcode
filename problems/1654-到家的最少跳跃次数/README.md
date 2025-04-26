# 1654. 到家的最少跳跃次数

## 题目描述

<p>有一只跳蚤的家在数轴上的位置 <code>x</code> 处。请你帮助它从位置 <code>0</code> 出发，到达它的家。</p>

<p>跳蚤跳跃的规则如下：</p>

<ul>
	<li>它可以 <strong>往前</strong> 跳恰好 <code>a</code> 个位置（即往右跳）。</li>
	<li>它可以 <strong>往后</strong> 跳恰好 <code>b</code> 个位置（即往左跳）。</li>
	<li>它不能 <strong>连续</strong> 往后跳 <code>2</code> 次。</li>
	<li>它不能跳到任何 <code>forbidden</code> 数组中的位置。</li>
</ul>

<p>跳蚤可以往前跳 <strong>超过</strong> 它的家的位置，但是它 <strong>不能跳到负整数</strong> 的位置。</p>

<p>给你一个整数数组 <code>forbidden</code> ，其中 <code>forbidden[i]</code> 是跳蚤不能跳到的位置，同时给你整数 <code>a</code>， <code>b</code> 和 <code>x</code> ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 <code>x</code> 的可行方案，请你返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
<b>输出：</b>3
<b>解释：</b>往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
<b>输出：</b>-1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
<b>输出：</b>2
<b>解释：</b>往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= forbidden.length <= 1000</code></li>
	<li><code>1 <= a, b, forbidden[i] <= 2000</code></li>
	<li><code>0 <= x <= 2000</code></li>
	<li><code>forbidden</code> 中所有位置互不相同。</li>
	<li>位置 <code>x</code> 不在 <code>forbidden</code> 中。</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 动态规划

## 提示

1. Think of the line as a graph
2. to handle the no double back jumps condition you can handle it by holding the state of your previous jump

## 示例

```
[14,4,18,1,15]
3
15
9
[8,3,16,6,12,20]
15
13
11
[1,6,2,14,5,17,4]
16
9
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
```

### C

```c
int minimumJumps(int* forbidden, int forbiddenSize, int a, int b, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumJumps(int[] forbidden, int a, int b, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} forbidden
 * @param {number} a
 * @param {number} b
 * @param {number} x
 * @return {number}
 */
var minimumJumps = function(forbidden, a, b, x) {
    
};
```

### TypeScript

```typescript
function minimumJumps(forbidden: number[], a: number, b: number, x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $forbidden
     * @param Integer $a
     * @param Integer $b
     * @param Integer $x
     * @return Integer
     */
    function minimumJumps($forbidden, $a, $b, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumJumps(_ forbidden: [Int], _ a: Int, _ b: Int, _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumJumps(forbidden: IntArray, a: Int, b: Int, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumJumps(List<int> forbidden, int a, int b, int x) {
    
  }
}
```

### Go

```golang
func minimumJumps(forbidden []int, a int, b int, x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} forbidden
# @param {Integer} a
# @param {Integer} b
# @param {Integer} x
# @return {Integer}
def minimum_jumps(forbidden, a, b, x)
    
end
```

### Scala

```scala
object Solution {
    def minimumJumps(forbidden: Array[Int], a: Int, b: Int, x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_jumps(forbidden: Vec<i32>, a: i32, b: i32, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-jumps forbidden a b x)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_jumps(Forbidden :: [integer()], A :: integer(), B :: integer(), X :: integer()) -> integer().
minimum_jumps(Forbidden, A, B, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_jumps(forbidden :: [integer], a :: integer, b :: integer, x :: integer) :: integer
  def minimum_jumps(forbidden, a, b, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumJumps(forbidden: Array<Int64>, a: Int64, b: Int64, x: Int64): Int64 {

    }
}
```

