# 888. 公平的糖果交换

## 题目描述

<p>爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 <code>aliceSizes</code> 和 <code>bobSizes</code> ，<code>aliceSizes[i]</code> 是爱丽丝拥有的第 <code>i</code> 盒糖果中的糖果数量，<code>bobSizes[j]</code> 是鲍勃拥有的第 <code>j</code> 盒糖果中的糖果数量。</p>

<p>两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。</p>

<p>返回一个整数数组 <code>answer</code>，其中 <code>answer[0]</code> 是爱丽丝必须交换的糖果盒中的糖果的数目，<code>answer[1]</code> 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 <strong>任何一个</strong> 。题目测试用例保证存在与输入对应的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,1], bobSizes = [2,2]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,2], bobSizes = [2,3]
<strong>输出：</strong>[1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [2], bobSizes = [1,3]
<strong>输出：</strong>[2,3]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>aliceSizes = [1,2,5], bobSizes = [2,4]
<strong>输出：</strong>[5,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= aliceSizes.length, bobSizes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= aliceSizes[i], bobSizes[j] &lt;= 10<sup>5</sup></code></li>
	<li>爱丽丝和鲍勃的糖果总数量不同。</li>
	<li>题目数据保证对于给定的输入至少存在一个有效答案。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 二分查找
- 排序

## 示例

```
[1,1]
[2,2]
[1,2]
[2,3]
[2]
[1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fairCandySwap(int* aliceSizes, int aliceSizesSize, int* bobSizes, int bobSizesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FairCandySwap(int[] aliceSizes, int[] bobSizes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} aliceSizes
 * @param {number[]} bobSizes
 * @return {number[]}
 */
var fairCandySwap = function(aliceSizes, bobSizes) {
    
};
```

### TypeScript

```typescript
function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $aliceSizes
     * @param Integer[] $bobSizes
     * @return Integer[]
     */
    function fairCandySwap($aliceSizes, $bobSizes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fairCandySwap(_ aliceSizes: [Int], _ bobSizes: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fairCandySwap(aliceSizes: IntArray, bobSizes: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> fairCandySwap(List<int> aliceSizes, List<int> bobSizes) {
    
  }
}
```

### Go

```golang
func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} alice_sizes
# @param {Integer[]} bob_sizes
# @return {Integer[]}
def fair_candy_swap(alice_sizes, bob_sizes)
    
end
```

### Scala

```scala
object Solution {
    def fairCandySwap(aliceSizes: Array[Int], bobSizes: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn fair_candy_swap(alice_sizes: Vec<i32>, bob_sizes: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (fair-candy-swap aliceSizes bobSizes)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec fair_candy_swap(AliceSizes :: [integer()], BobSizes :: [integer()]) -> [integer()].
fair_candy_swap(AliceSizes, BobSizes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec fair_candy_swap(alice_sizes :: [integer], bob_sizes :: [integer]) :: [integer]
  def fair_candy_swap(alice_sizes, bob_sizes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fairCandySwap(aliceSizes: Array<Int64>, bobSizes: Array<Int64>): Array<Int64> {

    }
}
```

