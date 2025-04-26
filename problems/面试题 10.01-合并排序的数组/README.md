# 面试题 10.01. 合并排序的数组

## 题目描述

<p>给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。</p>

<p>初始化&nbsp;A 和 B 的元素数量分别为&nbsp;<em>m</em> 和 <em>n</em>。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

<strong>输出：</strong>&nbsp;[1,2,2,3,5,6]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>A.length == n + m</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 排序

## 提示

1. 尝试从数组的末端向前端移动。

## 示例

```
[1,2,3,0,0,0]
3
[2,5,6]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public void merge(int[] A, int m, int[] B, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        
```

### C

```c
void merge(int* A, int ASize, int m, int* B, int BSize, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public void Merge(int[] A, int m, int[] B, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} A
 * @param {number} m
 * @param {number[]} B
 * @param {number} n
 * @return {void} Do not return anything, modify A in-place instead.
 */
var merge = function(A, m, B, n) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify A in-place instead.
 */
function merge(A: number[], m: number, B: number[], n: number): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $A
     * @param Integer $m
     * @param Integer[] $B
     * @param Integer $n
     * @return NULL
     */
    function merge(&$A, $m, $B, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func merge(_ A: inout [Int], _ m: Int, _ B: [Int], _ n: Int) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun merge(A: IntArray, m: Int, B: IntArray, n: Int): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void merge(List<int> A, int m, List<int> B, int n) {
    
  }
}
```

### Go

```golang
func merge(A []int, m int, B []int, n int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} a
# @param {Integer} m
# @param {Integer[]} b
# @param {Integer} n
# @return {Void} Do not return anything, modify A in-place instead.
def merge(a, m, b, n)
    
end
```

### Scala

```scala
object Solution {
    def merge(A: Array[Int], m: Int, B: Array[Int], n: Int): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge(a: &mut Vec<i32>, m: i32, b: &mut Vec<i32>, n: i32) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func merge(A: Array<Int64>, m: Int64, B: Array<Int64>, n: Int64): Unit {

    }
}
```

