# 1711. 大餐计数

## 题目描述

<p><strong>大餐</strong> 是指 <strong>恰好包含两道不同餐品</strong> 的一餐，其美味程度之和等于 2 的幂。</p>

<p>你可以搭配 <strong>任意</strong> 两道餐品做一顿大餐。</p>

<p>给你一个整数数组 <code>deliciousness</code> ，其中 <code>deliciousness[i]</code> 是第 <code>i<sup>​​​​​​</sup>​​​​</code>​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 <strong>大餐</strong> 的数量。结果需要对 <code>10<sup>9</sup> + 7</code> 取余。</p>

<p>注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>deliciousness = [1,3,5,7,9]
<strong>输出：</strong>4
<strong>解释：</strong>大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>deliciousness = [1,1,1,3,3,3,7]
<strong>输出：</strong>15
<strong>解释：</strong>大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= deliciousness.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= deliciousness[i] <= 2<sup>20</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 提示

1. Note that the number of powers of 2 is at most 21 so this turns the problem to a classic find the number of pairs that sum to a certain value but for 21 values
2. You need to use something fasters than the NlogN approach since there is already the log of iterating over the powers so one idea is two pointers

## 示例

```
[1,3,5,7,9]
[1,1,1,3,3,3,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPairs(int[] deliciousness) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
```

### C

```c
int countPairs(int* deliciousness, int deliciousnessSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPairs(int[] deliciousness) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} deliciousness
 * @return {number}
 */
var countPairs = function(deliciousness) {
    
};
```

### TypeScript

```typescript
function countPairs(deliciousness: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $deliciousness
     * @return Integer
     */
    function countPairs($deliciousness) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ deliciousness: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(deliciousness: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<int> deliciousness) {
    
  }
}
```

### Go

```golang
func countPairs(deliciousness []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} deliciousness
# @return {Integer}
def count_pairs(deliciousness)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(deliciousness: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(deliciousness: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs deliciousness)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Deliciousness :: [integer()]) -> integer().
count_pairs(Deliciousness) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(deliciousness :: [integer]) :: integer
  def count_pairs(deliciousness) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(deliciousness: Array<Int64>): Int64 {

    }
}
```

