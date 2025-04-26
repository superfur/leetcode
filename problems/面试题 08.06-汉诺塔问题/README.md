# 面试题 08.06. 汉诺塔问题

## 题目描述

<p>在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:<br />
(1) 每次只能移动一个盘子;<br />
(2) 盘子只能从柱子顶端滑出移到下一根柱子;<br />
(3) 盘子只能叠在比它大的盘子上。</p>

<p>请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。</p>

<p>你需要原地修改栈。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：A = [2, 1, 0], B = [], C = []
<strong> 输出</strong>：C = [2, 1, 0]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：A = [1, 0], B = [], C = []
<strong> 输出</strong>：C = [1, 0]
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>A 中盘子的数目不大于 14 个。</li>
</ol>


## 难度

Easy

## 标签

- 递归
- 数组

## 提示

1. 尝试简单构建法。
2. 你可以很容易地把最小的圆盘从一根柱子移到另一根柱子。把最小的两个圆盘从一根柱子移到另一根柱子也是小菜一碟。你能移动最小的三个圆盘吗？
3. 考虑将最小的圆盘从柱X = 0 移动到柱Y = 2，使用柱Z = 1作为临时保留点，作为f(1, X = 0, Y = 2, Z = 1)的解题方案。移动最小的两个圆盘来表示f(2, X = 0, Y = 2, Z = 1)。给定你f(1, X = 0, Y = 2, Z = 1)和f(2, X = 0, Y = 2, Z = 1)的题目解法，你能解出f(3, X = 0, Y = 2, Z = 1)吗？
4. 请注意，哪根柱子是源、目的地或暂存点并不重要。你可以通过f(2, X = 0, Y = 2, Z = 1)来计算f(2, X = 0, Y = 1, Z = 2)（将两个盘子从柱0移动到柱1，以柱2作为暂存点），然后将盘子3从柱0移动到柱2，计算f(2, X = 1, Y = 2, Z = 0)（将两个盘子从柱1移动到柱2，以柱0作为暂存点）。这个过程是怎样重复的？
5. 如果你在递归方面遇到困难，请尝试更多地相信递归过程。一旦弄清如何将前2个盘子从柱0移至柱2，就可以相信你完成了这项工作。当需要移动3个盘子时，请相信你可以将2个盘子从一根柱子移动到另一根柱子。现在，你已经移动了2个盘子。那么要如何处理第三个盘子呢？

## 示例

```
[0]
[]
[]
[1, 0]
[]
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
        
    }
};
```

### Java

```java
class Solution {
    public void hanota(List<Integer> A, List<Integer> B, List<Integer> C) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        
```

### C

```c
void hanota(int* A, int ASize, int* B, int BSize, int** C, int *CSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void Hanota(IList<int> A, IList<int> B, IList<int> C) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @return {void} Do not return anything, modify C in-place instead.
 */
var hanota = function(A, B, C) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify C in-place instead.
 */
function hanota(A: number[], B: number[], C: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $A
     * @param Integer[] $B
     * @param Integer[] $C
     * @return NULL
     */
    function hanota($A, $B, $C) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hanota(_ A: inout [Int], _ B: inout [Int], _ C: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hanota(A: List<Int>, B: List<Int>, C: List<Int>): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void hanota(List<int> A, List<int> B, List<int> C) {
    
  }
}
```

### Go

```golang
func hanota(A []int, B []int, C []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} a
# @param {Integer[]} b
# @param {Integer[]} c
# @return {Void} Do not return anything, modify C in-place instead.
def hanota(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def hanota(A: List[Int], B: List[Int], C: List[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn hanota(a: &mut Vec<i32>, b: &mut Vec<i32>, c: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func hanota(A: ArrayList<Int64>, B: ArrayList<Int64>, C: ArrayList<Int64>): Unit {

    }
}
```

