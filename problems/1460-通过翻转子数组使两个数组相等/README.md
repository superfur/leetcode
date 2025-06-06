# 1460. 通过翻转子数组使两个数组相等

## 题目描述

<p>给你两个长度相同的整数数组&nbsp;<code>target</code>&nbsp;和&nbsp;<code>arr</code>&nbsp;。每一步中，你可以选择&nbsp;<code>arr</code>&nbsp;的任意 <strong>非空子数组</strong>&nbsp;并将它翻转。你可以执行此过程任意次。</p>

<p><em>如果你能让 <code>arr</code>&nbsp;变得与 <code>target</code>&nbsp;相同，返回 True；否则，返回 False 。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = [1,2,3,4], arr = [2,4,1,3]
<strong>输出：</strong>true
<strong>解释：</strong>你可以按照如下步骤使 arr 变成 target：
1- 翻转子数组 [2,4,1] ，arr 变成 [1,4,2,3]
2- 翻转子数组 [4,2] ，arr 变成 [1,2,4,3]
3- 翻转子数组 [4,3] ，arr 变成 [1,2,3,4]
上述方法并不是唯一的，还存在多种将 arr 变成 target 的方法。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = [7], arr = [7]
<strong>输出：</strong>true
<strong>解释：</strong>arr 不需要做任何翻转已经与 target 相等。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = [3,7,9], arr = [3,7,11]
<strong>输出：</strong>false
<strong>解释：</strong>arr 没有数字 9 ，所以无论如何也无法变成 target 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>target.length == arr.length</code></li>
	<li><code>1 &lt;= target.length &lt;= 1000</code></li>
	<li><code>1 &lt;= target[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. Each element of target should have a corresponding element in arr, and if it doesn't have a corresponding element, return false.
2. To solve it easiely you can sort the two arrays and check if they are equal.

## 示例

```
[1,2,3,4]
[2,4,1,3]
[7]
[7]
[3,7,9]
[3,7,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
```

### C

```c
bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanBeEqual(int[] target, int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    
};
```

### TypeScript

```typescript
function canBeEqual(target: number[], arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Boolean
     */
    function canBeEqual($target, $arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canBeEqual(_ target: [Int], _ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canBeEqual(List<int> target, List<int> arr) {
    
  }
}
```

### Go

```golang
func canBeEqual(target []int, arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} target
# @param {Integer[]} arr
# @return {Boolean}
def can_be_equal(target, arr)
    
end
```

### Scala

```scala
object Solution {
    def canBeEqual(target: Array[Int], arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-be-equal target arr)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_be_equal(Target :: [integer()], Arr :: [integer()]) -> boolean().
can_be_equal(Target, Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_be_equal(target :: [integer], arr :: [integer]) :: boolean
  def can_be_equal(target, arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canBeEqual(target: Array<Int64>, arr: Array<Int64>): Bool {

    }
}
```

