# 1089. 复写零

## 题目描述

<p>给你一个长度固定的整数数组&nbsp;<code>arr</code> ，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。</p>

<p>注意：请不要在超过该数组长度的位置写入元素。请对输入的数组&nbsp;<strong>就地&nbsp;</strong>进行上述修改，不要从函数返回任何东西。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,0,2,3,0,4,5,0]
<strong>输出：</strong>[1,0,0,2,3,0,0,4]
<strong>解释：</strong>调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3]
<strong>输出：</strong>[1,2,3]
<strong>解释：</strong>调用函数后，输入的数组将被修改为：[1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针

## 提示

1. This is a great introductory problem for understanding and working with the concept of in-place operations. The problem statement clearly states that we are to modify the array in-place. That does not mean we cannot use another array. We just don't have to return anything.
2. A better way to solve this would be without using additional space. The only reason the problem statement allows you to make modifications in place is that it hints at avoiding any additional memory.
3. The main problem with not using additional memory is that we might override elements due to the zero duplication requirement of the problem statement. How do we get around that?
4. If we had enough space available, we would be able to accommodate all the elements properly. The new length would be the original length of the array plus the number of zeros. Can we use this information somehow to solve the problem?

## 示例

```
[1,0,2,3,0,4,5,0]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public void duplicateZeros(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
```

### C

```c
void duplicateZeros(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void DuplicateZeros(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify arr in-place instead.
 */
function duplicateZeros(arr: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return NULL
     */
    function duplicateZeros(&$arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func duplicateZeros(_ arr: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun duplicateZeros(arr: IntArray): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void duplicateZeros(List<int> arr) {
    
  }
}
```

### Go

```golang
func duplicateZeros(arr []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Void} Do not return anything, modify arr in-place instead.
def duplicate_zeros(arr)
    
end
```

### Scala

```scala
object Solution {
    def duplicateZeros(arr: Array[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn duplicate_zeros(arr: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func duplicateZeros(arr: Array<Int64>): Unit {

    }
}
```

