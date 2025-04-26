# 1835. 所有数对按位与结果的异或和

## 题目描述

<p>列表的 <strong>异或和</strong>（<strong>XOR sum</strong>）指对所有元素进行按位 <code>XOR</code> 运算的结果。如果列表中仅有一个元素，那么其 <strong>异或和</strong> 就等于该元素。</p>

<ul>
	<li>例如，<code>[1,2,3,4]</code> 的 <strong>异或和</strong> 等于 <code>1 XOR 2 XOR 3 XOR 4 = 4</code> ，而 <code>[3]</code> 的 <strong>异或和</strong> 等于 <code>3</code> 。</li>
</ul>

<p>给你两个下标 <strong>从 0 开始</strong> 计数的数组 <code>arr1</code> 和 <code>arr2</code> ，两数组均由非负整数组成。</p>

<p>根据每个 <code>(i, j)</code> 数对，构造一个由 <code>arr1[i] AND arr2[j]</code>（按位 <code>AND</code> 运算）结果组成的列表。其中 <code>0 &lt;= i &lt; arr1.length</code> 且 <code>0 &lt;= j &lt; arr2.length</code> 。</p>

<p>返回上述列表的 <strong>异或和</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr1 = [1,2,3], arr2 = [6,5]
<strong>输出：</strong>0
<strong>解释：</strong>列表 = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1] ，
异或和 = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr1 = [12], arr2 = [4]
<strong>输出：</strong>4
<strong>解释：</strong>列表 = [12 AND 4] = [4] ，异或和 = 4 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= arr1[i], arr2[j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学

## 提示

1. Think about (a&b) ^ (a&c). Can you simplify this expression?
2. It is equal to a&(b^c). Then, (arr1[i]&arr2[0])^(arr1[i]&arr2[1]).. = arr1[i]&(arr2[0]^arr2[1]^arr[2]...).
3. Let arr2XorSum = (arr2[0]^arr2[1]^arr2[2]...), arr1XorSum = (arr1[0]^arr1[1]^arr1[2]...) so the final answer is (arr2XorSum&arr1[0]) ^ (arr2XorSum&arr1[1]) ^ (arr2XorSum&arr1[2]) ^ ... = arr2XorSum & arr1XorSum.

## 示例

```
[1,2,3]
[6,5]
[12]
[4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
        
    }
};
```

### Java

```java
class Solution {
    public int getXORSum(int[] arr1, int[] arr2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
```

### C

```c
int getXORSum(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var getXORSum = function(arr1, arr2) {
    
};
```

### TypeScript

```typescript
function getXORSum(arr1: number[], arr2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function getXORSum($arr1, $arr2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getXORSum(_ arr1: [Int], _ arr2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getXORSum(arr1: IntArray, arr2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getXORSum(List<int> arr1, List<int> arr2) {
    
  }
}
```

### Go

```golang
func getXORSum(arr1 []int, arr2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def get_xor_sum(arr1, arr2)
    
end
```

### Scala

```scala
object Solution {
    def getXORSum(arr1: Array[Int], arr2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_xor_sum(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-xor-sum arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_xor_sum(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
get_xor_sum(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_xor_sum(arr1 :: [integer], arr2 :: [integer]) :: integer
  def get_xor_sum(arr1, arr2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getXORSum(arr1: Array<Int64>, arr2: Array<Int64>): Int64 {

    }
}
```

