# 1361. 验证二叉树

## 题目描述

<p>二叉树上有 <code>n</code>&nbsp;个节点，按从&nbsp;<code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;编号，其中节点&nbsp;<code>i</code>&nbsp;的两个子节点分别是&nbsp;<code>leftChild[i]</code>&nbsp;和&nbsp;<code>rightChild[i]</code>。</p>

<p>只有 <strong>所有</strong> 节点能够形成且 <strong>只</strong> 形成 <strong>一颗</strong>&nbsp;有效的二叉树时，返回&nbsp;<code>true</code>；否则返回 <code>false</code>。</p>

<p>如果节点&nbsp;<code>i</code>&nbsp;没有左子节点，那么&nbsp;<code>leftChild[i]</code>&nbsp;就等于&nbsp;<code>-1</code>。右子节点也符合该规则。</p>

<p>注意：节点没有值，本问题中仅仅使用节点编号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex1.png" style="height: 287px; width: 195px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex2.png" style="height: 272px; width: 183px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex3.png" style="height: 174px; width: 82px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 2, leftChild = [1,0], rightChild = [-1,-1]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == leftChild.length == rightChild.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-1 &lt;= leftChild[i], rightChild[i] &lt;= n - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 并查集
- 图
- 二叉树

## 提示

1. Find the parent of each node.
2. A valid tree must have nodes with only one parent and exactly one node with no parent.

## 示例

```
4
[1,-1,3,-1]
[2,-1,-1,-1]
4
[1,-1,3,-1]
[2,3,-1,-1]
2
[1,0]
[-1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
```

### C

```c
bool validateBinaryTreeNodes(int n, int* leftChild, int leftChildSize, int* rightChild, int rightChildSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} leftChild
 * @param {number[]} rightChild
 * @return {boolean}
 */
var validateBinaryTreeNodes = function(n, leftChild, rightChild) {
    
};
```

### TypeScript

```typescript
function validateBinaryTreeNodes(n: number, leftChild: number[], rightChild: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $leftChild
     * @param Integer[] $rightChild
     * @return Boolean
     */
    function validateBinaryTreeNodes($n, $leftChild, $rightChild) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validateBinaryTreeNodes(_ n: Int, _ leftChild: [Int], _ rightChild: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validateBinaryTreeNodes(n: Int, leftChild: IntArray, rightChild: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validateBinaryTreeNodes(int n, List<int> leftChild, List<int> rightChild) {
    
  }
}
```

### Go

```golang
func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} left_child
# @param {Integer[]} right_child
# @return {Boolean}
def validate_binary_tree_nodes(n, left_child, right_child)
    
end
```

### Scala

```scala
object Solution {
    def validateBinaryTreeNodes(n: Int, leftChild: Array[Int], rightChild: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (validate-binary-tree-nodes n leftChild rightChild)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec validate_binary_tree_nodes(N :: integer(), LeftChild :: [integer()], RightChild :: [integer()]) -> boolean().
validate_binary_tree_nodes(N, LeftChild, RightChild) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec validate_binary_tree_nodes(n :: integer, left_child :: [integer], right_child :: [integer]) :: boolean
  def validate_binary_tree_nodes(n, left_child, right_child) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validateBinaryTreeNodes(n: Int64, leftChild: Array<Int64>, rightChild: Array<Int64>): Bool {

    }
}
```

