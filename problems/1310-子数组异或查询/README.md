# 1310. 子数组异或查询

## 题目描述

<p>有一个正整数数组 <code>arr</code>，现给你一个对应的查询数组 <code>queries</code>，其中 <code>queries[i] = [L<sub>i, </sub>R<sub>i</sub>]</code>。</p>

<p>对于每个查询 <code>i</code>，请你计算从 <code>L<sub>i</sub></code> 到 <code>R<sub>i</sub></code> 的 <strong>XOR</strong> 值（即 <code>arr[L<sub>i</sub>] <strong>xor</strong> arr[L<sub>i</sub>+1] <strong>xor</strong> ... <strong>xor</strong> arr[R<sub>i</sub>]</code>）作为本次查询的结果。</p>

<p>并返回一个包含给定查询 <code>queries</code> 所有结果的数组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
<strong>输出：</strong>[2,7,14,8] 
<strong>解释：</strong>
数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
<strong>输出：</strong>[8,0,4,4]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= arr.length <= 3 * 10^4</code></li>
	<li><code>1 <= arr[i] <= 10^9</code></li>
	<li><code>1 <= queries.length <= 3 * 10^4</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 <= queries[i][0] <= queries[i][1] < arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 前缀和

## 提示

1. What is the result of x ^ y ^ x ?
2. Compute the prefix sum for XOR.
3. Process the queries with the prefix sum values.

## 示例

```
[1,3,4,8]
[[0,1],[1,2],[0,3],[3,3]]
[4,8,2,10]
[[2,3],[1,3],[0,0],[0,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] XorQueries(int[] arr, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function(arr, queries) {
    
};
```

### TypeScript

```typescript
function xorQueries(arr: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function xorQueries($arr, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func xorQueries(_ arr: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun xorQueries(arr: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> xorQueries(List<int> arr, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func xorQueries(arr []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer[][]} queries
# @return {Integer[]}
def xor_queries(arr, queries)
    
end
```

### Scala

```scala
object Solution {
    def xorQueries(arr: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (xor-queries arr queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec xor_queries(Arr :: [integer()], Queries :: [[integer()]]) -> [integer()].
xor_queries(Arr, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec xor_queries(arr :: [integer], queries :: [[integer]]) :: [integer]
  def xor_queries(arr, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func xorQueries(arr: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

