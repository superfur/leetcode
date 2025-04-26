# 216. 组合总和 III

## 题目描述

<p>找出所有相加之和为&nbsp;<code>n</code><em> </em>的&nbsp;<code>k</code><strong>&nbsp;</strong>个数的组合，且满足下列条件：</p>

<ul>
	<li>只使用数字1到9</li>
	<li>每个数字&nbsp;<strong>最多使用一次</strong>&nbsp;</li>
</ul>

<p>返回 <em>所有可能的有效组合的列表</em> 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 7
<strong>输出:</strong> [[1,2,4]]
<strong>解释:</strong>
1 + 2 + 4 = 7
没有其他符合的组合了。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 9
<strong>输出:</strong> [[1,2,6], [1,3,5], [2,3,4]]
<strong>解释:
</strong>1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> k = 4, n = 1
<strong>输出:</strong> []
<strong>解释:</strong> 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 &gt; 1，没有有效的组合。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 回溯

## 示例

```
3
7
3
9
4
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    
};
```

### TypeScript

```typescript
function combinationSum3(k: number, n: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer[][]
     */
    function combinationSum3($k, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> combinationSum3(int k, int n) {
    
  }
}
```

### Go

```golang
func combinationSum3(k int, n int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
def combination_sum3(k, n)
    
end
```

### Scala

```scala
object Solution {
    def combinationSum3(k: Int, n: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (combination-sum3 k n)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec combination_sum3(K :: integer(), N :: integer()) -> [[integer()]].
combination_sum3(K, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combination_sum3(k :: integer, n :: integer) :: [[integer]]
  def combination_sum3(k, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func combinationSum3(k: Int64, n: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

