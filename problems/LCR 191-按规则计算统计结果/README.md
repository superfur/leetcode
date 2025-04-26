# LCR 191. 按规则计算统计结果

## 题目描述

<p>为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 <code>arrayA</code> 记录了各个生物群体数量数据，其中 <code>arrayA[i]</code> 表示第 <code>i</code> 个生物群体的数量。请返回一个数组 <code>arrayB</code>，该数组为基于数组 <code>arrayA</code> 中的数据计算得出的结果，其中 <code>arrayB[i]</code> 表示将第 <code>i</code> 个生物群体的数量从总体中排除后的其他数量的乘积。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arrayA = [2, 4, 6, 8, 10]
<strong>输出：</strong>[1920, 960, 640, 480, 384]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>所有元素乘积之和不会溢出 32 位整数</li>
	<li><code>arrayA.length &lt;= 100000</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 示例

```
[2,4,6,8,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> statisticalResult(vector<int>& arrayA) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] statisticalResult(int[] arrayA) {
        
    }
}
```

### Python

```python
class Solution(object):
    def statisticalResult(self, arrayA):
        """
        :type arrayA: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* statisticalResult(int* arrayA, int arrayASize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] StatisticalResult(int[] arrayA) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arrayA
 * @return {number[]}
 */
var statisticalResult = function(arrayA) {
    
};
```

### TypeScript

```typescript
function statisticalResult(arrayA: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arrayA
     * @return Integer[]
     */
    function statisticalResult($arrayA) {
        
    }
}
```

### Swift

```swift
class Solution {
    func statisticalResult(_ arrayA: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun statisticalResult(arrayA: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> statisticalResult(List<int> arrayA) {
    
  }
}
```

### Go

```golang
func statisticalResult(arrayA []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} array_a
# @return {Integer[]}
def statistical_result(array_a)
    
end
```

### Scala

```scala
object Solution {
    def statisticalResult(arrayA: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn statistical_result(array_a: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (statistical-result arrayA)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec statistical_result(ArrayA :: [integer()]) -> [integer()].
statistical_result(ArrayA) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec statistical_result(array_a :: [integer]) :: [integer]
  def statistical_result(array_a) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func statisticalResult(arrayA: Array<Int64>): Array<Int64> {

    }
}
```

