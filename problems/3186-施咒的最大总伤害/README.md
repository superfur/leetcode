# 3186. 施咒的最大总伤害

## 题目描述

<p>一个魔法师有许多不同的咒语。</p>

<p>给你一个数组&nbsp;<code>power</code>&nbsp;，其中每个元素表示一个咒语的伤害值，可能会有多个咒语有相同的伤害值。</p>

<p>已知魔法师使用伤害值为&nbsp;<code>power[i]</code>&nbsp;的咒语时，他们就&nbsp;<strong>不能</strong>&nbsp;使用伤害为&nbsp;<code>power[i] - 2</code>&nbsp;，<code>power[i] - 1</code>&nbsp;，<code>power[i] + 1</code>&nbsp;或者&nbsp;<code>power[i] + 2</code>&nbsp;的咒语。</p>

<p>每个咒语最多只能被使用 <strong>一次</strong>&nbsp;。</p>

<p>请你返回这个魔法师可以达到的伤害值之和的 <strong>最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>power = [1,1,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><strong>解释：</strong></p>

<p>可以使用咒语 0，1，3，伤害值分别为 1，1，4，总伤害值为 6 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>power = [7,1,6,6]</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><strong>解释：</strong></p>

<p>可以使用咒语 1，2，3，伤害值分别为 1，6，6，总伤害值为 13 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= power.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= power[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 二分查找
- 动态规划
- 计数
- 排序

## 提示

1. If we ever decide to use some spell with power <code>x</code>, then we will use all spells with power <code>x</code>.
2. Think of dynamic programming.
3. <code>dp[i][j]</code> represents the maximum damage considering up to the <code>i</code>-th unique spell and <code>j</code> represents the number of spells skipped (up to 3 as per constraints).

## 示例

```
[1,1,3,4]
[7,1,6,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumTotalDamage(int[] power) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
```

### C

```c
long long maximumTotalDamage(int* power, int powerSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumTotalDamage(int[] power) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} power
 * @return {number}
 */
var maximumTotalDamage = function(power) {
    
};
```

### TypeScript

```typescript
function maximumTotalDamage(power: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $power
     * @return Integer
     */
    function maximumTotalDamage($power) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTotalDamage(_ power: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTotalDamage(power: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTotalDamage(List<int> power) {
    
  }
}
```

### Go

```golang
func maximumTotalDamage(power []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} power
# @return {Integer}
def maximum_total_damage(power)
    
end
```

### Scala

```scala
object Solution {
    def maximumTotalDamage(power: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_total_damage(power: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-total-damage power)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_total_damage(Power :: [integer()]) -> integer().
maximum_total_damage(Power) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_total_damage(power :: [integer]) :: integer
  def maximum_total_damage(power) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTotalDamage(power: Array<Int64>): Int64 {

    }
}
```

