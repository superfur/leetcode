# 1104. 二叉树寻路

## 题目描述

<p>在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 <strong>逐行</strong> 依次按&nbsp;&ldquo;之&rdquo; 字形进行标记。</p>

<p>如下图所示，在奇数行（即，第一行、第三行、第五行&hellip;&hellip;）中，按从左到右的顺序进行标记；</p>

<p>而偶数行（即，第二行、第四行、第六行&hellip;&hellip;）中，按从右到左的顺序进行标记。</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/28/tree.png" style="height: 138px; width: 300px;"></p>

<p>给你树上某一个节点的标号 <code>label</code>，请你返回从根节点到该标号为 <code>label</code> 节点的路径，该路径是由途经的节点标号所组成的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>label = 14
<strong>输出：</strong>[1,3,4,14]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>label = 26
<strong>输出：</strong>[1,2,6,10,26]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= label &lt;= 10^6</code></li>
</ul>


## 难度

Medium

## 标签

- 树
- 数学
- 二叉树

## 提示

1. Based on the label of the current node, find what the label must be for the parent of that node.

## 示例

```
14
26
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathInZigZagTree(int label, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> PathInZigZagTree(int label) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} label
 * @return {number[]}
 */
var pathInZigZagTree = function(label) {
    
};
```

### TypeScript

```typescript
function pathInZigZagTree(label: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $label
     * @return Integer[]
     */
    function pathInZigZagTree($label) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pathInZigZagTree(_ label: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pathInZigZagTree(label: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> pathInZigZagTree(int label) {
    
  }
}
```

### Go

```golang
func pathInZigZagTree(label int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} label
# @return {Integer[]}
def path_in_zig_zag_tree(label)
    
end
```

### Scala

```scala
object Solution {
    def pathInZigZagTree(label: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn path_in_zig_zag_tree(label: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (path-in-zig-zag-tree label)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec path_in_zig_zag_tree(Label :: integer()) -> [integer()].
path_in_zig_zag_tree(Label) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec path_in_zig_zag_tree(label :: integer) :: [integer]
  def path_in_zig_zag_tree(label) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pathInZigZagTree(label: Int64): ArrayList<Int64> {

    }
}
```

