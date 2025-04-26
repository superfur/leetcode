# 1376. 通知所有员工所需的时间

## 题目描述

<p>公司里有 <code>n</code> 名员工，每个员工的 ID 都是独一无二的，编号从 <code>0</code> 到 <code>n - 1</code>。公司的总负责人通过 <code>headID</code> 进行标识。</p>

<p>在 <code>manager</code> 数组中，每个员工都有一个直属负责人，其中 <code>manager[i]</code> 是第 <code>i</code> 名员工的直属负责人。对于总负责人，<code>manager[headID] = -1</code>。题目保证从属关系可以用树结构显示。</p>

<p>公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。</p>

<p>第 <code>i</code> 名员工需要 <code>informTime[i]</code> 分钟来通知它的所有直属下属（也就是说在 <code>informTime[i]</code> 分钟后，他的所有直属下属都可以开始传播这一消息）。</p>

<p>返回通知所有员工这一紧急消息所需要的 <strong>分钟数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1, headID = 0, manager = [-1], informTime = [0]
<strong>输出：</strong>0
<strong>解释：</strong>公司总负责人是该公司的唯一一名员工。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/graph.png" style="height: 174px; width: 404px;" /></p>

<pre>
<strong>输入：</strong>n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
<strong>输出：</strong>1
<strong>解释：</strong>id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>0 &lt;= headID &lt; n</code></li>
	<li><code>manager.length == n</code></li>
	<li><code>0 &lt;= manager[i] &lt; n</code></li>
	<li><code>manager[headID] == -1</code></li>
	<li><code>informTime.length&nbsp;== n</code></li>
	<li><code>0 &lt;= informTime[i] &lt;= 1000</code></li>
	<li>如果员工 <code>i</code> 没有下属，<code>informTime[i] == 0</code> 。</li>
	<li>题目 <strong>保证</strong> 所有员工都可以收到通知。</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索

## 提示

1. The company can be represented as a tree, headID is always the root.
2. Store for each node the time needed to be informed of the news.
3. Answer is the max time a leaf node needs to be informed.

## 示例

```
1
0
[-1]
[0]
6
2
[2,2,-1,2,2,2]
[0,0,1,0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
```

### C

```c
int numOfMinutes(int n, int headID, int* manager, int managerSize, int* informTime, int informTimeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} headID
 * @param {number[]} manager
 * @param {number[]} informTime
 * @return {number}
 */
var numOfMinutes = function(n, headID, manager, informTime) {
    
};
```

### TypeScript

```typescript
function numOfMinutes(n: number, headID: number, manager: number[], informTime: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $headID
     * @param Integer[] $manager
     * @param Integer[] $informTime
     * @return Integer
     */
    function numOfMinutes($n, $headID, $manager, $informTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfMinutes(_ n: Int, _ headID: Int, _ manager: [Int], _ informTime: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfMinutes(n: Int, headID: Int, manager: IntArray, informTime: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfMinutes(int n, int headID, List<int> manager, List<int> informTime) {
    
  }
}
```

### Go

```golang
func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} head_id
# @param {Integer[]} manager
# @param {Integer[]} inform_time
# @return {Integer}
def num_of_minutes(n, head_id, manager, inform_time)
    
end
```

### Scala

```scala
object Solution {
    def numOfMinutes(n: Int, headID: Int, manager: Array[Int], informTime: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-minutes n headID manager informTime)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_minutes(N :: integer(), HeadID :: integer(), Manager :: [integer()], InformTime :: [integer()]) -> integer().
num_of_minutes(N, HeadID, Manager, InformTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_minutes(n :: integer, head_id :: integer, manager :: [integer], inform_time :: [integer]) :: integer
  def num_of_minutes(n, head_id, manager, inform_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfMinutes(n: Int64, headID: Int64, manager: Array<Int64>, informTime: Array<Int64>): Int64 {

    }
}
```

