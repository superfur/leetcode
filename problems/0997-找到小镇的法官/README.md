# 997. 找到小镇的法官

## 题目描述

<p>小镇里有 <code>n</code> 个人，按从 <code>1</code> 到 <code>n</code> 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。</p>

<p>如果小镇法官真的存在，那么：</p>

<ol>
	<li>小镇法官不会信任任何人。</li>
	<li>每个人（除了小镇法官）都信任这位小镇法官。</li>
	<li>只有一个人同时满足属性 <strong>1</strong> 和属性 <strong>2</strong> 。</li>
</ol>

<p>给你一个数组 <code>trust</code> ，其中 <code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示编号为 <code>a<sub>i</sub></code> 的人信任编号为 <code>b<sub>i</sub></code> 的人。</p>

<p>如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2, trust = [[1,2]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, trust = [[1,3],[2,3]]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3, trust = [[1,3],[2,3],[3,1]]
<strong>输出：</strong>-1
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= trust.length &lt;= 10<sup>4</sup></code></li>
	<li><code>trust[i].length == 2</code></li>
	<li><code>trust</code> 中的所有<code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> <strong>互不相同</strong></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
</ul>


## 难度

Easy

## 标签

- 图
- 数组
- 哈希表

## 示例

```
2
[[1,2]]
3
[[1,3],[2,3]]
3
[[1,3],[2,3],[3,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        
    }
};
```

### Java

```java
class Solution {
    public int findJudge(int n, int[][] trust) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
```

### C

```c
int findJudge(int n, int** trust, int trustSize, int* trustColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindJudge(int n, int[][] trust) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    
};
```

### TypeScript

```typescript
function findJudge(n: number, trust: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge($n, $trust) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findJudge(_ n: Int, _ trust: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findJudge(n: Int, trust: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findJudge(int n, List<List<int>> trust) {
    
  }
}
```

### Go

```golang
func findJudge(n int, trust [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} trust
# @return {Integer}
def find_judge(n, trust)
    
end
```

### Scala

```scala
object Solution {
    def findJudge(n: Int, trust: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-judge n trust)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_judge(N :: integer(), Trust :: [[integer()]]) -> integer().
find_judge(N, Trust) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_judge(n :: integer, trust :: [[integer]]) :: integer
  def find_judge(n, trust) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findJudge(n: Int64, trust: Array<Array<Int64>>): Int64 {

    }
}
```

