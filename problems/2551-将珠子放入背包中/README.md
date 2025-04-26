# 2551. 将珠子放入背包中

## 题目描述

<p>你有&nbsp;<code>k</code>&nbsp;个背包。给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>weights</code>&nbsp;，其中&nbsp;<code>weights[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个珠子的重量。同时给你整数 <code>k</code>&nbsp;。</p>

<p>请你按照如下规则将所有的珠子放进&nbsp;<code>k</code>&nbsp;个背包。</p>

<ul>
	<li>没有背包是空的。</li>
	<li>如果第&nbsp;<code>i</code>&nbsp;个珠子和第&nbsp;<code>j</code>&nbsp;个珠子在同一个背包里，那么下标在&nbsp;<code>i</code>&nbsp;到&nbsp;<code>j</code>&nbsp;之间的所有珠子都必须在这同一个背包中。</li>
	<li>如果一个背包有下标从&nbsp;<code>i</code>&nbsp;到&nbsp;<code>j</code>&nbsp;的所有珠子，那么这个背包的价格是&nbsp;<code>weights[i] + weights[j]</code>&nbsp;。</li>
</ul>

<p>一个珠子分配方案的 <strong>分数</strong>&nbsp;是所有 <code>k</code>&nbsp;个背包的价格之和。</p>

<p>请你返回所有分配方案中，<strong>最大分数</strong>&nbsp;与 <strong>最小分数</strong>&nbsp;的 <strong>差值</strong>&nbsp;为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>weights = [1,3,5,1], k = 2
<b>输出：</b>4
<b>解释：</b>
分配方案 [1],[3,5,1] 得到最小得分 (1+1) + (3+1) = 6 。
分配方案 [1,3],[5,1] 得到最大得分 (1+3) + (5+1) = 10 。
所以差值为 10 - 6 = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>weights = [1, 3], k = 2
<b>输出：</b>0
<b>解释：</b>唯一的分配方案为 [1],[3] 。
最大最小得分相等，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= weights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= weights[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. Each bag will contain a subarray, and only the endpoints of these subarrays matter.
2. Each subarray only contributes two numbers to the sum. Use this property to choose the subarrays optimally.
3. Try to use a priority queue.

## 示例

```
[1,3,5,1]
2
[1,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long putMarbles(int[] weights, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
```

### C

```c
long long putMarbles(int* weights, int weightsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long PutMarbles(int[] weights, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} weights
 * @param {number} k
 * @return {number}
 */
var putMarbles = function(weights, k) {
    
};
```

### TypeScript

```typescript
function putMarbles(weights: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $weights
     * @param Integer $k
     * @return Integer
     */
    function putMarbles($weights, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func putMarbles(_ weights: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun putMarbles(weights: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int putMarbles(List<int> weights, int k) {
    
  }
}
```

### Go

```golang
func putMarbles(weights []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} weights
# @param {Integer} k
# @return {Integer}
def put_marbles(weights, k)
    
end
```

### Scala

```scala
object Solution {
    def putMarbles(weights: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (put-marbles weights k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec put_marbles(Weights :: [integer()], K :: integer()) -> integer().
put_marbles(Weights, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec put_marbles(weights :: [integer], k :: integer) :: integer
  def put_marbles(weights, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func putMarbles(weights: Array<Int64>, k: Int64): Int64 {

    }
}
```

