# 2127. 参加会议的最多员工数

## 题目描述

<p>一个公司准备组织一场会议，邀请名单上有&nbsp;<code>n</code>&nbsp;位员工。公司准备了一张 <strong>圆形</strong>&nbsp;的桌子，可以坐下 <strong>任意数目</strong>&nbsp;的员工。</p>

<p>员工编号为 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;。每位员工都有一位 <strong>喜欢</strong>&nbsp;的员工，每位员工&nbsp;<strong>当且仅当</strong>&nbsp;他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 <strong>不会</strong>&nbsp;是他自己。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>favorite</code>&nbsp;，其中&nbsp;<code>favorite[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;位员工喜欢的员工。请你返回参加会议的&nbsp;<strong>最多员工数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/14/ex1.png" style="width: 236px; height: 195px;" /></p>

<pre>
<b>输入：</b>favorite = [2,2,1,2]
<b>输出：</b>3
<strong>解释：</strong>
上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
注意，公司也可以邀请员工 1，2 和 3 参加会议。
所以最多参加会议的员工数目为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>favorite = [1,2,0]
<b>输出：</b>3
<b>解释：</b>
每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
座位安排同图 1 所示：
- 员工 0 坐在员工 2 和 1 之间。
- 员工 1 坐在员工 0 和 2 之间。
- 员工 2 坐在员工 1 和 0 之间。
参与会议的最多员工数目为 3 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/14/ex2.png" style="width: 219px; height: 220px;" /></p>

<pre>
<b>输入：</b>favorite = [3,0,1,4,1]
<b>输出：</b>4
<b>解释：</b>
上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
员工 2 无法参加，因为他喜欢的员工 1 旁边的座位已经被占领了。
所以公司只能不邀请员工 2 。
参加会议的最多员工数目为 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == favorite.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= favorite[i] &lt;=&nbsp;n - 1</code></li>
	<li><code>favorite[i] != i</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 图
- 拓扑排序

## 提示

1. From the given array favorite, create a graph where for every index i, there is a directed edge from favorite[i] to i. The graph will be a combination of cycles and chains of acyclic edges. Now, what are the ways in which we can choose employees to sit at the table?
2. The first way by which we can choose employees is by selecting a cycle of the graph. It can be proven that in this case, the employees that do not lie in the cycle can never be seated at the table (unless the cycle has a length of 2).
3. The second way is by combining acyclic chains. At most two chains can be combined by a cycle of length 2, where each chain ends on one of the employees in the cycle.

## 示例

```
[2,2,1,2]
[1,2,0]
[3,0,1,4,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumInvitations(int[] favorite) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        
```

### C

```c
int maximumInvitations(int* favorite, int favoriteSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumInvitations(int[] favorite) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} favorite
 * @return {number}
 */
var maximumInvitations = function(favorite) {
    
};
```

### TypeScript

```typescript
function maximumInvitations(favorite: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $favorite
     * @return Integer
     */
    function maximumInvitations($favorite) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumInvitations(_ favorite: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumInvitations(favorite: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumInvitations(List<int> favorite) {
    
  }
}
```

### Go

```golang
func maximumInvitations(favorite []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} favorite
# @return {Integer}
def maximum_invitations(favorite)
    
end
```

### Scala

```scala
object Solution {
    def maximumInvitations(favorite: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-invitations favorite)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_invitations(Favorite :: [integer()]) -> integer().
maximum_invitations(Favorite) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_invitations(favorite :: [integer]) :: integer
  def maximum_invitations(favorite) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumInvitations(favorite: Array<Int64>): Int64 {

    }
}
```

