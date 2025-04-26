# 1409. 查询带键的排列

## 题目描述

<p>给定一个正整数数组&nbsp;<code>queries</code> ，其取值范围在&nbsp;<code>1</code> 到 <code>m</code> 之间。 请你根据以下规则按顺序处理所有&nbsp;<code>queries[i]</code>（从 <code>i=0</code> 到 <code>i=queries.length-1</code>）：</p>

<ul>
	<li>首先，你有一个排列&nbsp;<code>P=[1,2,3,...,m]</code>。</li>
	<li>对于当前的 <code>i</code> ，找到&nbsp;<code>queries[i]</code> 在排列 <code>P</code> 中的位置（<b>从 0 开始索引</b>），然后将它移到排列&nbsp;<code>P</code> 的开头（即下标为 0 处）。注意， <code>queries[i]</code>&nbsp;的查询结果是 <code>queries[i]</code> 在 <code>P</code> 中移动前的位置。</li>
</ul>

<p>返回一个数组，包含从给定 &nbsp;<code>queries</code>&nbsp;中查询到的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>queries = [3,1,2,1], m = 5
<strong>输出：</strong>[2,1,2,1] 
<strong>解释：处理</strong> queries 的过程如下：
对于 i=0: queries[i]=3, P=[1,2,3,4,5], 3 在 P 中的位置是 <strong>2</strong>，然后我们把 3 移动到 P 的开头，得到 P=[3,1,2,4,5] 。
对于 i=1: queries[i]=1, P=[3,1,2,4,5], 1 在 P 中的位置是 <strong>1</strong>，然后我们把 1 移动到 P 的开头，得到 P=[1,3,2,4,5] 。 
对于 i=2: queries[i]=2, P=[1,3,2,4,5], 2 在 P 中的位置是 <strong>2</strong>，然后我们把 2 移动到 P 的开头，得到 P=[2,1,3,4,5] 。
对于 i=3: queries[i]=1, P=[2,1,3,4,5], 1 在 P 中的位置是 <strong>1</strong>，然后我们把 1 移动到 P 的开头，得到 P=[1,2,3,4,5] 。 
因此，包含结果的数组为 [2,1,2,1] 。  
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>queries = [4,1,2,2], m = 4
<strong>输出：</strong>[3,1,2,0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>queries = [7,5,5,8,3], m = 8
<strong>输出：</strong>[6,5,0,7,5]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m &lt;= 10^3</code></li>
	<li><code>1 &lt;= queries.length &lt;= m</code></li>
	<li><code>1 &lt;= queries[i] &lt;= m</code></li>
</ul>


## 难度

Medium

## 标签

- 树状数组
- 数组
- 模拟

## 提示

1. Create the permutation P=[1,2,...,m], it could be a list for example.
2. For each i, find the position of queries[i] with a simple scan over P and then move this to the beginning.

## 示例

```
[3,1,2,1]
5
[4,1,2,2]
4
[7,5,5,8,3]
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> processQueries(vector<int>& queries, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] processQueries(int[] queries, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* processQueries(int* queries, int queriesSize, int m, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ProcessQueries(int[] queries, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} queries
 * @param {number} m
 * @return {number[]}
 */
var processQueries = function(queries, m) {
    
};
```

### TypeScript

```typescript
function processQueries(queries: number[], m: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $queries
     * @param Integer $m
     * @return Integer[]
     */
    function processQueries($queries, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func processQueries(_ queries: [Int], _ m: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun processQueries(queries: IntArray, m: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> processQueries(List<int> queries, int m) {
    
  }
}
```

### Go

```golang
func processQueries(queries []int, m int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} queries
# @param {Integer} m
# @return {Integer[]}
def process_queries(queries, m)
    
end
```

### Scala

```scala
object Solution {
    def processQueries(queries: Array[Int], m: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn process_queries(queries: Vec<i32>, m: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (process-queries queries m)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec process_queries(Queries :: [integer()], M :: integer()) -> [integer()].
process_queries(Queries, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec process_queries(queries :: [integer], m :: integer) :: [integer]
  def process_queries(queries, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func processQueries(queries: Array<Int64>, m: Int64): Array<Int64> {

    }
}
```

