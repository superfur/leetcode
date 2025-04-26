# 2151. 基于陈述统计最多好人数

## 题目描述

<p>游戏中存在两种角色：</p>

<ul>
	<li><strong>好人</strong>：该角色只说真话。</li>
	<li><strong>坏人</strong>：该角色可能说真话，也可能说假话。</li>
</ul>

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>statements</code> ，大小为 <code>n x n</code> ，表示 <code>n</code> 个玩家对彼此角色的陈述。具体来说，<code>statements[i][j]</code> 可以是下述值之一：</p>

<ul>
	<li><code>0</code> 表示 <code>i</code> 的陈述认为 <code>j</code> 是 <strong>坏人</strong> 。</li>
	<li><code>1</code> 表示 <code>i</code> 的陈述认为 <code>j</code> 是 <strong>好人</strong> 。</li>
	<li><code>2</code> 表示 <code>i</code> 没有对 <code>j</code> 作出陈述。</li>
</ul>

<p>另外，玩家不会对自己进行陈述。形式上，对所有&nbsp;<code>0 &lt;= i &lt; n</code> ，都有 <code>statements[i][i] = 2</code> 。</p>

<p>根据这 <code>n</code> 个玩家的陈述，返回可以认为是 <strong>好人</strong> 的 <strong>最大</strong> 数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/15/logic1.jpg" style="width: 600px; height: 262px;">
<pre><strong>输入：</strong>statements = [[2,1,2],[1,2,2],[2,0,2]]
<strong>输出：</strong>2
<strong>解释：</strong>每个人都做一条陈述。
- 0 认为 1 是好人。
- 1 认为 0 是好人。
- 2 认为 1 是坏人。
以 2 为突破点。
- 假设 2 是一个好人：
    - 基于 2 的陈述，1 是坏人。
    - 那么可以确认 1 是坏人，2 是好人。
    - 基于 1 的陈述，由于 1 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下会出现矛盾，所以假设无效。
        - 说假话。在这种情况下，0 也是坏人并且在陈述时说假话。
    - <strong>在认为 2 是好人的情况下，这组玩家中只有一个好人。</strong>
- 假设 2 是一个坏人：
    - 基于 2 的陈述，由于 2 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下，0 和 1 都是坏人。
            - <strong>在认为 2 是坏人但说真话的情况下，这组玩家中没有一个好人。</strong>
        - 说假话。在这种情况下，1 是好人。
            - 由于 1 是好人，0 也是好人。
            - <strong>在认为 2 是坏人且说假话的情况下，这组玩家中有两个好人。</strong>
在最佳情况下，至多有两个好人，所以返回 2 。
注意，能得到此结论的方法不止一种。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/15/logic2.jpg" style="width: 600px; height: 262px;">
<pre><strong>输入：</strong>statements = [[2,0],[0,2]]
<strong>输出：</strong>1
<strong>解释：</strong>每个人都做一条陈述。
- 0 认为 1 是坏人。
- 1 认为 0 是坏人。
以 0 为突破点。
- 假设 0 是一个好人：
    - 基于与 0 的陈述，1 是坏人并说假话。
    - <strong>在认为 0 是好人的情况下，这组玩家中只有一个好人。</strong>
- 假设 0 是一个坏人：
    - 基于 0 的陈述，由于 0 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下，0 和 1 都是坏人。
            - <strong>在认为 0 是坏人但说真话的情况下，这组玩家中没有一个好人。</strong>
        - 说假话。在这种情况下，1 是好人。
            - <strong>在认为 0 是坏人且说假话的情况下，这组玩家中只有一个好人。</strong>
在最佳情况下，至多有一个好人，所以返回 1 。 
注意，能得到此结论的方法不止一种。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == statements.length == statements[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 15</code></li>
	<li><code>statements[i][j]</code> 的值为 <code>0</code>、<code>1</code> 或 <code>2</code></li>
	<li><code>statements[i][i] == 2</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 回溯
- 枚举

## 提示

1. You should test every possible assignment of good and bad people, using a bitmask.
2. In each bitmask, if the person i is good, then his statements should be consistent with the bitmask in order for the assignment to be valid.
3. If the assignment is valid, count how many people are good and keep track of the maximum.

## 示例

```
[[2,1,2],[1,2,2],[2,0,2]]
[[2,0],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumGood(vector<vector<int>>& statements) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumGood(int[][] statements) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        
```

### C

```c
int maximumGood(int** statements, int statementsSize, int* statementsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumGood(int[][] statements) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} statements
 * @return {number}
 */
var maximumGood = function(statements) {
    
};
```

### TypeScript

```typescript
function maximumGood(statements: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $statements
     * @return Integer
     */
    function maximumGood($statements) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumGood(_ statements: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumGood(statements: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumGood(List<List<int>> statements) {
    
  }
}
```

### Go

```golang
func maximumGood(statements [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} statements
# @return {Integer}
def maximum_good(statements)
    
end
```

### Scala

```scala
object Solution {
    def maximumGood(statements: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_good(statements: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-good statements)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_good(Statements :: [[integer()]]) -> integer().
maximum_good(Statements) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_good(statements :: [[integer]]) :: integer
  def maximum_good(statements) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumGood(statements: Array<Array<Int64>>): Int64 {

    }
}
```

