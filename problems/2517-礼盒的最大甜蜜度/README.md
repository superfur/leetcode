# 2517. 礼盒的最大甜蜜度

## 题目描述

<p>给你一个正整数数组 <code>price</code> ，其中 <code>price[i]</code> 表示第 <code>i</code> 类糖果的价格，另给你一个正整数 <code>k</code> 。</p>

<p>商店组合 <code>k</code> 类 <strong>不同</strong> 糖果打包成礼盒出售。礼盒的 <strong>甜蜜度</strong> 是礼盒中任意两种糖果 <strong>价格</strong> 绝对差的最小值。</p>

<p>返回礼盒的 <strong>最大 </strong>甜蜜度<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>price = [13,5,1,8,21,2], k = 3
<strong>输出：</strong>8
<strong>解释：</strong>选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>price = [1,3,1], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>选出价格分别为 [1,3] 的两类糖果。 
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>price = [7,7,7,7], k = 2
<strong>输出：</strong>0
<strong>解释：</strong>从现有的糖果中任选两类糖果，甜蜜度都会是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= price.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= price[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找
- 排序

## 提示

1. The answer is binary searchable.
2. For some x, we can use a greedy strategy to check if it is possible to pick k distinct candies with tastiness being at least x.
3. Sort prices and iterate from left to right. For some price[i] check if the price difference between the last taken candy and price[i] is at least x. If so, add the candy i to the basket.
4. So, a candy basket with tastiness x can be achieved if the basket size is bigger than or equal to k.

## 示例

```
[13,5,1,8,21,2]
3
[1,3,1]
2
[7,7,7,7]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumTastiness(vector<int>& price, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumTastiness(int[] price, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
```

### C

```c
int maximumTastiness(int* price, int priceSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumTastiness(int[] price, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} price
 * @param {number} k
 * @return {number}
 */
var maximumTastiness = function(price, k) {
    
};
```

### TypeScript

```typescript
function maximumTastiness(price: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $price
     * @param Integer $k
     * @return Integer
     */
    function maximumTastiness($price, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTastiness(_ price: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTastiness(price: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTastiness(List<int> price, int k) {
    
  }
}
```

### Go

```golang
func maximumTastiness(price []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} price
# @param {Integer} k
# @return {Integer}
def maximum_tastiness(price, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumTastiness(price: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_tastiness(price: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-tastiness price k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_tastiness(Price :: [integer()], K :: integer()) -> integer().
maximum_tastiness(Price, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_tastiness(price :: [integer], k :: integer) :: integer
  def maximum_tastiness(price, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTastiness(price: Array<Int64>, k: Int64): Int64 {

    }
}
```

