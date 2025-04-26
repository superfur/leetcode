# 1299. 将每个元素替换为右侧最大元素

## 题目描述

<p>给你一个数组 <code>arr</code> ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 <code>-1</code> 替换。</p>

<p>完成所有替换操作后，请你返回这个数组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [17,18,5,4,6,1]
<strong>输出：</strong>[18,6,6,6,1,-1]
<strong>解释：</strong>
- 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
- 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
- 下标 5 的元素 --> 右侧没有其他元素，替换为 -1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [400]
<strong>输出：</strong>[-1]
<strong>解释：</strong>下标<strong> </strong>0 的元素右侧没有其他元素。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= arr.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= arr[i] <= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Loop through the array starting from the end.
2. Keep the maximum value seen so far.

## 示例

```
[17,18,5,4,6,1]
[400]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] replaceElements(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ReplaceElements(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    
};
```

### TypeScript

```typescript
function replaceElements(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function replaceElements($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func replaceElements(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> replaceElements(List<int> arr) {
    
  }
}
```

### Go

```golang
func replaceElements(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def replace_elements(arr)
    
end
```

### Scala

```scala
object Solution {
    def replaceElements(arr: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (replace-elements arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec replace_elements(Arr :: [integer()]) -> [integer()].
replace_elements(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec replace_elements(arr :: [integer]) :: [integer]
  def replace_elements(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func replaceElements(arr: Array<Int64>): Array<Int64> {

    }
}
```

