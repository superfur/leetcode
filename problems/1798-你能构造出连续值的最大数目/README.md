# 1798. 你能构造出连续值的最大数目

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>coins</code> ，它代表你拥有的 <code>n</code> 个硬币。第 <code>i</code> 个硬币的值为 <code>coins[i]</code> 。如果你从这些硬币中选出一部分硬币，它们的和为 <code>x</code> ，那么称，你可以 <strong>构造</strong> 出 <code>x</code> 。</p>

<p>请返回从 <code>0</code> 开始（<strong>包括</strong> <code>0</code> ），你最多能 <strong>构造</strong> 出多少个连续整数。</p>

<p>你可能有多个相同值的硬币。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>coins = [1,3]
<b>输出：</b>2
<strong>解释：</strong>你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
从 0 开始，你可以构造出 2 个连续整数。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>coins = [1,1,1,4]
<b>输出：</b>8
<strong>解释：</strong>你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
- 2：取 [1,1]
- 3：取 [1,1,1]
- 4：取 [4]
- 5：取 [4,1]
- 6：取 [4,1,1]
- 7：取 [4,1,1,1]
从 0 开始，你可以构造出 8 个连续整数。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,10,3,1]
<b>输出：</b>20</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>coins.length == n</code></li>
	<li><code>1 <= n <= 4 * 10<sup>4</sup></code></li>
	<li><code>1 <= coins[i] <= 4 * 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. If you can make the first x values and you have a value v, then you can make all the values <var>≤ v + x</var>
2. Sort the array of coins. You can always make the value 0 so you can start with x = 0.
3. Process the values starting from the smallest and stop when there is a value that cannot be achieved with the current x.

## 示例

```
[1,3]
[1,1,1,4]
[1,4,10,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaximumConsecutive(int[] coins) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
```

### C

```c
int getMaximumConsecutive(int* coins, int coinsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaximumConsecutive(int[] coins) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} coins
 * @return {number}
 */
var getMaximumConsecutive = function(coins) {
    
};
```

### TypeScript

```typescript
function getMaximumConsecutive(coins: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @return Integer
     */
    function getMaximumConsecutive($coins) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaximumConsecutive(_ coins: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaximumConsecutive(coins: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaximumConsecutive(List<int> coins) {
    
  }
}
```

### Go

```golang
func getMaximumConsecutive(coins []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} coins
# @return {Integer}
def get_maximum_consecutive(coins)
    
end
```

### Scala

```scala
object Solution {
    def getMaximumConsecutive(coins: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_maximum_consecutive(coins: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-maximum-consecutive coins)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_maximum_consecutive(Coins :: [integer()]) -> integer().
get_maximum_consecutive(Coins) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_maximum_consecutive(coins :: [integer]) :: integer
  def get_maximum_consecutive(coins) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaximumConsecutive(coins: Array<Int64>): Int64 {

    }
}
```

