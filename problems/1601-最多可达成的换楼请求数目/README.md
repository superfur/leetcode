# 1601. 最多可达成的换楼请求数目

## 题目描述

<p>我们有&nbsp;<code>n</code>&nbsp;栋楼，编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。</p>

<p>给你一个数组 <code>requests</code>&nbsp;，其中&nbsp;<code>requests[i] = [from<sub>i</sub>, to<sub>i</sub>]</code>&nbsp;，表示一个员工请求从编号为&nbsp;<code>from<sub>i</sub></code>&nbsp;的楼搬到编号为&nbsp;<code>to<sub>i</sub></code><sub>&nbsp;</sub>的楼。</p>

<p>一开始&nbsp;<strong>所有楼都是满的</strong>，所以从请求列表中选出的若干个请求是可行的需要满足 <strong>每栋楼员工净变化为 0&nbsp;</strong>。意思是每栋楼 <strong>离开</strong>&nbsp;的员工数目 <strong>等于</strong>&nbsp;该楼 <strong>搬入</strong>&nbsp;的员工数数目。比方说&nbsp;<code>n = 3</code>&nbsp;且两个员工要离开楼&nbsp;<code>0</code>&nbsp;，一个员工要离开楼&nbsp;<code>1</code>&nbsp;，一个员工要离开楼 <code>2</code>&nbsp;，如果该请求列表可行，应该要有两个员工搬入楼&nbsp;<code>0</code>&nbsp;，一个员工搬入楼&nbsp;<code>1</code>&nbsp;，一个员工搬入楼&nbsp;<code>2</code>&nbsp;。</p>

<p>请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/move1.jpg" style="height: 406px; width: 600px;"></p>

<pre><strong>输入：</strong>n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
<strong>输出：</strong>5
<strong>解释：</strong>请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/move2.jpg" style="height: 327px; width: 450px;"></p>

<pre><strong>输入：</strong>n = 3, requests = [[0,0],[1,2],[2,1]]
<strong>输出：</strong>3
<strong>解释：</strong>请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= requests.length &lt;= 16</code></li>
	<li><code>requests[i].length == 2</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; n</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 回溯
- 枚举

## 提示

1. Think brute force
2. When is a subset of requests okay?

## 示例

```
5
[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
3
[[0,0],[1,2],[2,1]]
4
[[0,3],[3,1],[1,2],[2,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumRequests(int n, vector<vector<int>>& requests) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
```

### C

```c
int maximumRequests(int n, int** requests, int requestsSize, int* requestsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumRequests(int n, int[][] requests) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} requests
 * @return {number}
 */
var maximumRequests = function(n, requests) {
    
};
```

### TypeScript

```typescript
function maximumRequests(n: number, requests: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $requests
     * @return Integer
     */
    function maximumRequests($n, $requests) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumRequests(_ n: Int, _ requests: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumRequests(n: Int, requests: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumRequests(int n, List<List<int>> requests) {
    
  }
}
```

### Go

```golang
func maximumRequests(n int, requests [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} requests
# @return {Integer}
def maximum_requests(n, requests)
    
end
```

### Scala

```scala
object Solution {
    def maximumRequests(n: Int, requests: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_requests(n: i32, requests: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-requests n requests)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_requests(N :: integer(), Requests :: [[integer()]]) -> integer().
maximum_requests(N, Requests) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_requests(n :: integer, requests :: [[integer]]) :: integer
  def maximum_requests(n, requests) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumRequests(n: Int64, requests: Array<Array<Int64>>): Int64 {

    }
}
```

