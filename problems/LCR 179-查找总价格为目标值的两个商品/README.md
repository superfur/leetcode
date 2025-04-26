# LCR 179. 查找总价格为目标值的两个商品

## 题目描述

<p>购物车内的商品价格按照升序记录于数组 <code>price</code>。请在购物车中找到两个商品的价格总和刚好是 <code>target</code>。若存在多种情况，返回任一结果即可。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>price = [3, 9, 12, 15], target = 18
<strong>输出：</strong>[3,15] 或者 [15,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>price = [8, 21, 27, 34, 52, 66], target = 61
<strong>输出：</strong>[27,34] 或者 [34,27]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= price.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= price[i] &lt;= 10^6</code></li>
	<li><code>1 &lt;= target &lt;= 2*10^6</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 二分查找

## 示例

```
[3, 9, 12, 15]
18
[8, 21, 27, 34, 52, 66]
61
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& price, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] twoSum(int[] price, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def twoSum(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* price, int priceSize, int target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] TwoSum(int[] price, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} price
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(price, target) {
    
};
```

### TypeScript

```typescript
function twoSum(price: number[], target: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $price
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($price, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func twoSum(_ price: [Int], _ target: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoSum(price: IntArray, target: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> twoSum(List<int> price, int target) {
    
  }
}
```

### Go

```golang
func twoSum(price []int, target int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} price
# @param {Integer} target
# @return {Integer[]}
def two_sum(price, target)
    
end
```

### Scala

```scala
object Solution {
    def twoSum(price: Array[Int], target: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_sum(price: Vec<i32>, target: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (two-sum price target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec two_sum(Price :: [integer()], Target :: integer()) -> [integer()].
two_sum(Price, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_sum(price :: [integer], target :: integer) :: [integer]
  def two_sum(price, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func twoSum(price: Array<Int64>, target: Int64): Array<Int64> {

    }
}
```

