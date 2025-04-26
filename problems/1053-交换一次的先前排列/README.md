# 1053. 交换一次的先前排列

## 题目描述

<p>给你一个正整数数组 <code>arr</code>（可能存在重复的元素），请你返回可在&nbsp;<strong>一次交换</strong>（交换两数字 <code>arr[i]</code> 和 <code>arr[j]</code> 的位置）后得到的、按<span data-keyword="lexicographically-smaller-string-alien">字典序</span>排列小于 <code>arr</code> 的最大排列。</p>

<p>如果无法这么操作，就请返回原数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,2,1]
<strong>输出：</strong>[3,1,2]
<strong>解释：</strong>交换 2 和 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,5]
<strong>输出：</strong>[1,1,5]
<strong>解释：</strong>已经是最小排列
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,9,4,6,7]
<strong>输出：</strong>[1,7,4,6,9]
<strong>解释：</strong>交换 9 和 7
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. You need to swap two values, one larger than the other.  Where is the larger one located?

## 示例

```
[3,2,1]
[1,1,5]
[1,9,4,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> prevPermOpt1(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] prevPermOpt1(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prevPermOpt1(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] PrevPermOpt1(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var prevPermOpt1 = function(arr) {
    
};
```

### TypeScript

```typescript
function prevPermOpt1(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function prevPermOpt1($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func prevPermOpt1(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun prevPermOpt1(arr: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> prevPermOpt1(List<int> arr) {
    
  }
}
```

### Go

```golang
func prevPermOpt1(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def prev_perm_opt1(arr)
    
end
```

### Scala

```scala
object Solution {
    def prevPermOpt1(arr: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn prev_perm_opt1(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (prev-perm-opt1 arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec prev_perm_opt1(Arr :: [integer()]) -> [integer()].
prev_perm_opt1(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec prev_perm_opt1(arr :: [integer]) :: [integer]
  def prev_perm_opt1(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func prevPermOpt1(arr: Array<Int64>): Array<Int64> {

    }
}
```

