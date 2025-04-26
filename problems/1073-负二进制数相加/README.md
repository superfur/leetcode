# 1073. 负二进制数相加

## 题目描述

<p>给出基数为 <strong>-2</strong>&nbsp;的两个数&nbsp;<code>arr1</code> 和&nbsp;<code>arr2</code>，返回两数相加的结果。</p>

<p>数字以&nbsp;<em>数组形式</em><strong>&nbsp;</strong>给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，<code>arr&nbsp;= [1,1,0,1]</code>&nbsp;表示数字&nbsp;<code>(-2)^3&nbsp;+ (-2)^2 + (-2)^0 = -3</code>。<em>数组形式</em>&nbsp;中的数字 <code>arr</code> 也同样不含前导零：即&nbsp;<code>arr == [0]</code>&nbsp;或&nbsp;<code>arr[0] == 1</code>。</p>

<p>返回相同表示形式的 <code>arr1</code> 和 <code>arr2</code> 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,1,1,1,1], arr2 = [1,0,1]
<strong>输出：</strong>[1,0,0,0,0]
<strong>解释：</strong>arr1 表示 11，arr2 表示 5，输出表示 16 。
</pre>

<p><meta charset="UTF-8" /></p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [0], arr2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [0], arr2 = [1]
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= arr1.length,&nbsp;arr2.length &lt;= 1000</code></li>
	<li><code>arr1[i]</code>&nbsp;和&nbsp;<code>arr2[i]</code>&nbsp;都是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
	<li><code>arr1</code>&nbsp;和&nbsp;<code>arr2</code>&nbsp;都没有前导0</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. We can try to determine the last digit of the answer, then divide everything by 2 and repeat.

## 示例

```
[1,1,1,1,1]
[1,0,1]
[0]
[0]
[0]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> addNegabinary(vector<int>& arr1, vector<int>& arr2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addNegabinary(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AddNegabinary(int[] arr1, int[] arr2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var addNegabinary = function(arr1, arr2) {
    
};
```

### TypeScript

```typescript
function addNegabinary(arr1: number[], arr2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function addNegabinary($arr1, $arr2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addNegabinary(_ arr1: [Int], _ arr2: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addNegabinary(arr1: IntArray, arr2: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> addNegabinary(List<int> arr1, List<int> arr2) {
    
  }
}
```

### Go

```golang
func addNegabinary(arr1 []int, arr2 []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def add_negabinary(arr1, arr2)
    
end
```

### Scala

```scala
object Solution {
    def addNegabinary(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_negabinary(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (add-negabinary arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec add_negabinary(Arr1 :: [integer()], Arr2 :: [integer()]) -> [integer()].
add_negabinary(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_negabinary(arr1 :: [integer], arr2 :: [integer]) :: [integer]
  def add_negabinary(arr1, arr2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addNegabinary(arr1: Array<Int64>, arr2: Array<Int64>): Array<Int64> {

    }
}
```

