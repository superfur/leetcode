# 77. 组合

## 题目描述

<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回范围 <code>[1, n]</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 2
<strong>输出：</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>[[1]]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= n</code></li>
</ul>


## 难度

Medium

## 标签

- 回溯

## 示例

```
4
2
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> Combine(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    
};
```

### TypeScript

```typescript
function combine(n: number, k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[][]
     */
    function combine($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> combine(int n, int k) {
    
  }
}
```

### Go

```golang
func combine(n int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[][]}
def combine(n, k)
    
end
```

### Scala

```scala
object Solution {
    def combine(n: Int, k: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (combine n k)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec combine(N :: integer(), K :: integer()) -> [[integer()]].
combine(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combine(n :: integer, k :: integer) :: [[integer]]
  def combine(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func combine(n: Int64, k: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

