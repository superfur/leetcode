# 面试题 10.03. 搜索旋转数组

## 题目描述

<p>搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入：</strong>arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
<strong> 输出：</strong>8（元素5在该数组中的索引）
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
<strong> 输出</strong>：-1 （没有找到）
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>arr 长度范围在[1, 1000000]之间</li>
</ol>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. 你能为此改进二分查找吗？
2. 该算法的运行时间是什么？如果数组有重复，会发生什么？

## 示例

```
[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
5
[1,1,1,1,1,2,1,1,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int search(vector<int>& arr, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int search(int[] arr, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def search(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
```

### C

```c
int search(int* arr, int arrSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int Search(int[] arr, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var search = function(arr, target) {
    
};
```

### TypeScript

```typescript
function search(arr: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function search($arr, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func search(_ arr: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun search(arr: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int search(List<int> arr, int target) {
    
  }
}
```

### Go

```golang
func search(arr []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def search(arr, target)
    
end
```

### Scala

```scala
object Solution {
    def search(arr: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn search(arr: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (search arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec search(Arr :: [integer()], Target :: integer()) -> integer().
search(Arr, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec search(arr :: [integer], target :: integer) :: integer
  def search(arr, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func search(arr: Array<Int64>, target: Int64): Int64 {

    }
}
```

