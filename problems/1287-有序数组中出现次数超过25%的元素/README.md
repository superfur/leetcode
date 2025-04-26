# 1287. 有序数组中出现次数超过25%的元素

## 题目描述

<p>给你一个非递减的&nbsp;<strong>有序&nbsp;</strong>整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。</p>

<p>请你找到并返回这个整数</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,2,6,6,6,6,7,10]
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^4</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10^5</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]
2. The answer should be in one of the ends of the intervals.
3. In order to check which is element is the answer we can count the frequency with binarySearch.

## 示例

```
[1,2,2,6,6,6,6,7,10]
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int findSpecialInteger(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
```

### C

```c
int findSpecialInteger(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindSpecialInteger(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    
};
```

### TypeScript

```typescript
function findSpecialInteger(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findSpecialInteger($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSpecialInteger(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSpecialInteger(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findSpecialInteger(List<int> arr) {
    
  }
}
```

### Go

```golang
func findSpecialInteger(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def find_special_integer(arr)
    
end
```

### Scala

```scala
object Solution {
    def findSpecialInteger(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-special-integer arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_special_integer(Arr :: [integer()]) -> integer().
find_special_integer(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_special_integer(arr :: [integer]) :: integer
  def find_special_integer(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSpecialInteger(arr: Array<Int64>): Int64 {

    }
}
```

