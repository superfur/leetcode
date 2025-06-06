# 1672. 最富有客户的资产总量

## 题目描述

<p>给你一个 <code>m x n</code> 的整数网格 <code>accounts</code> ，其中 <code>accounts[i][j]</code> 是第 <code>i​​​​​<sup>​​​​​​</sup>​</code> 位客户在第 <code>j</code> 家银行托管的资产数量。返回最富有客户所拥有的 <strong>资产总量</strong> 。</p>

<p>客户的 <strong>资产总量</strong> 就是他们在各家银行托管的资产数量之和。最富有客户就是 <strong>资产总量</strong> 最大的客户。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>accounts = [[1,2,3],[3,2,1]]
<strong>输出：</strong>6
<strong>解释：</strong>
<code>第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
</code>两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>accounts = [[1,5],[7,3],[3,5]]
<strong>输出：</strong>10
<strong>解释：</strong>
<code>第 1 位客户的资产总量</code> = 6
<code>第 2 位客户的资产总量</code> = 10 
<code>第 3 位客户的资产总量</code> = 8
第 2 位客户是最富有的，资产总量是 10</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>accounts = [[2,8,7],[7,1,3],[1,9,5]]
<strong>输出：</strong>17
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == accounts.length</code></li>
	<li><code>n == accounts[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= accounts[i][j] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Calculate the wealth of each customer
2. Find the maximum element in array.

## 示例

```
[[1,2,3],[3,2,1]]
[[1,5],[7,3],[3,5]]
[[2,8,7],[7,1,3],[1,9,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumWealth(int[][] accounts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
```

### C

```c
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumWealth(int[][] accounts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    
};
```

### TypeScript

```typescript
function maximumWealth(accounts: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $accounts
     * @return Integer
     */
    function maximumWealth($accounts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumWealth(_ accounts: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumWealth(List<List<int>> accounts) {
    
  }
}
```

### Go

```golang
func maximumWealth(accounts [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} accounts
# @return {Integer}
def maximum_wealth(accounts)
    
end
```

### Scala

```scala
object Solution {
    def maximumWealth(accounts: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-wealth accounts)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_wealth(Accounts :: [[integer()]]) -> integer().
maximum_wealth(Accounts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_wealth(accounts :: [[integer]]) :: integer
  def maximum_wealth(accounts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumWealth(accounts: Array<Array<Int64>>): Int64 {

    }
}
```

