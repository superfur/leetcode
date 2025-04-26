# 3457. 吃披萨

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组 <code>pizzas</code>，其中 <code>pizzas[i]</code> 表示第 <code>i</code>&nbsp;个披萨的重量。每天你会吃&nbsp;<strong>恰好</strong> 4 个披萨。由于你的新陈代谢能力惊人，当你吃重量为 <code>W</code>、<code>X</code>、<code>Y</code> 和 <code>Z</code> 的披萨（其中 <code>W &lt;= X &lt;= Y &lt;= Z</code>）时，你只会增加 1 个披萨的重量！体重增加规则如下：</p>

<ul>
	<li>在&nbsp;<strong><span style="box-sizing: border-box; margin: 0px; padding: 0px;">奇数天</span></strong>（按 <strong>1 开始计数</strong>）你会增加 <code>Z</code> 的重量。</li>
	<li>在&nbsp;<strong>偶数天</strong>，你会增加 <code>Y</code> 的重量。</li>
</ul>

<p>请你设计吃掉&nbsp;<strong>所有&nbsp;</strong>披萨的最优方案，并计算你可以增加的&nbsp;<strong>最大&nbsp;</strong>总重量。</p>

<p><strong>注意：</strong>保证 <code>n</code> 是 4 的倍数，并且每个披萨只吃一次。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">pizzas = [1,2,3,4,5,6,7,8]</span></p>

<p><strong>输出：</strong> <span class="example-io">14</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 1 天，你吃掉下标为 <code>[1, 2, 4, 7] = [2, 3, 5, 8]</code> 的披萨。你增加的重量为 8。</li>
	<li>第 2 天，你吃掉下标为 <code>[0, 3, 5, 6] = [1, 4, 6, 7]</code> 的披萨。你增加的重量为 6。</li>
</ul>

<p>吃掉所有披萨后，你增加的总重量为 <code>8 + 6 = 14</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">pizzas = [2,1,1,1,1,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 1 天，你吃掉下标为 <code>[4, 5, 6, 0] = [1, 1, 1, 2]</code> 的披萨。你增加的重量为 2。</li>
	<li>第 2 天，你吃掉下标为 <code>[1, 2, 3, 7] = [1, 1, 1, 1]</code> 的披萨。你增加的重量为 1。</li>
</ul>

<p>吃掉所有披萨后，你增加的总重量为 <code>2 + 1 = 3</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= n == pizzas.length &lt;= 2 * 10<sup><span style="font-size: 10.8333px;">5</span></sup></code></li>
	<li><code>1 &lt;= pizzas[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 是 4 的倍数。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. On odd-numbered days, it is optimal to pair the smallest three and the largest one.
2. On even-numbered days, it is optimal to pair the smallest two and the largest two.
3. There will be ceil((n / 4) / 2) odd-numbered days. Select pizzas for all odd-numbered days first.
4. Select the remaining pizzas for the even-numbered days.

## 示例

```
[1,2,3,4,5,6,7,8]
[2,1,1,1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxWeight(int[] pizzas) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        
```

### C

```c
long long maxWeight(int* pizzas, int pizzasSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxWeight(int[] pizzas) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} pizzas
 * @return {number}
 */
var maxWeight = function(pizzas) {
    
};
```

### TypeScript

```typescript
function maxWeight(pizzas: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $pizzas
     * @return Integer
     */
    function maxWeight($pizzas) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxWeight(_ pizzas: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxWeight(pizzas: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxWeight(List<int> pizzas) {
    
  }
}
```

### Go

```golang
func maxWeight(pizzas []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} pizzas
# @return {Integer}
def max_weight(pizzas)
    
end
```

### Scala

```scala
object Solution {
    def maxWeight(pizzas: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_weight(pizzas: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-weight pizzas)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_weight(Pizzas :: [integer()]) -> integer().
max_weight(Pizzas) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_weight(pizzas :: [integer]) :: integer
  def max_weight(pizzas) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxWeight(pizzas: Array<Int64>): Int64 {

    }
}
```

