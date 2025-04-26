# 2961. 双模幂运算

## 题目描述

<p>给你一个下标从 <strong>0 </strong>开始的二维数组 <code>variables</code> ，其中 <code>variables[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i,</sub> m<sub>i</sub>]</code>，以及一个整数 <code>target</code> 。</p>

<p>如果满足以下公式，则下标 <code>i</code> 是 <strong>好下标</strong>：</p>

<ul>
	<li><code>0 &lt;= i &lt; variables.length</code></li>
	<li><code>((a<sub>i</sub><sup>b<sub>i</sub></sup> % 10)<sup>c<sub>i</sub></sup>) % m<sub>i</sub> == target</code></li>
</ul>

<p>返回一个由<strong> 好下标 </strong>组成的数组，<strong>顺序不限</strong> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
<strong>输出：</strong>[0,2]
<strong>解释：</strong>对于 variables 数组中的每个下标 i ：
1) 对于下标 0 ，variables[0] = [2,3,3,10] ，(2<sup>3</sup> % 10)<sup>3</sup> % 10 = 2 。
2) 对于下标 1 ，variables[1] = [3,3,3,1] ，(3<sup>3</sup> % 10)<sup>3</sup> % 1 = 0 。
3) 对于下标 2 ，variables[2] = [6,1,1,4] ，(6<sup>1</sup> % 10)<sup>1</sup> % 4 = 2 。
因此，返回 [0,2] 作为答案。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>variables = [[39,3,1000,1000]], target = 17
<strong>输出：</strong>[]
<strong>解释：</strong>对于 variables 数组中的每个下标 i ：
1) 对于下标 0 ，variables[0] = [39,3,1000,1000] ，(39<sup>3</sup> % 10)<sup>1000</sup> % 1000 = 1 。
因此，返回 [] 作为答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= variables.length &lt;= 100</code></li>
	<li><code>variables[i] == [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub>]</code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub> &lt;= 10<sup>3</sup></code></li>
	<li><code><font face="monospace">0 &lt;= target &lt;= 10<sup>3</sup></font></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 模拟

## 示例

```
[[2,3,3,10],[3,3,3,1],[6,1,1,4]]
2
[[39,3,1000,1000]]
17
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getGoodIndices(vector<vector<int>>& variables, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> getGoodIndices(int[][] variables, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getGoodIndices(int** variables, int variablesSize, int* variablesColSize, int target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GetGoodIndices(int[][] variables, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} variables
 * @param {number} target
 * @return {number[]}
 */
var getGoodIndices = function(variables, target) {
    
};
```

### TypeScript

```typescript
function getGoodIndices(variables: number[][], target: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $variables
     * @param Integer $target
     * @return Integer[]
     */
    function getGoodIndices($variables, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getGoodIndices(_ variables: [[Int]], _ target: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getGoodIndices(variables: Array<IntArray>, target: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getGoodIndices(List<List<int>> variables, int target) {
    
  }
}
```

### Go

```golang
func getGoodIndices(variables [][]int, target int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} variables
# @param {Integer} target
# @return {Integer[]}
def get_good_indices(variables, target)
    
end
```

### Scala

```scala
object Solution {
    def getGoodIndices(variables: Array[Array[Int]], target: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_good_indices(variables: Vec<Vec<i32>>, target: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-good-indices variables target)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_good_indices(Variables :: [[integer()]], Target :: integer()) -> [integer()].
get_good_indices(Variables, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_good_indices(variables :: [[integer]], target :: integer) :: [integer]
  def get_good_indices(variables, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getGoodIndices(variables: Array<Array<Int64>>, target: Int64): ArrayList<Int64> {

    }
}
```

