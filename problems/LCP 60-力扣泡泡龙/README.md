# LCP 60. 力扣泡泡龙

## 题目描述

欢迎各位勇者来到力扣城，本次试炼主题为「力扣泡泡龙」。

游戏初始状态的泡泡形如二叉树 `root`，每个节点值对应了该泡泡的分值。勇者最多可以击破一个节点泡泡，要求满足：
- 被击破的节点泡泡 **至多** 只有一个子节点泡泡
- 当被击破的节点泡泡有子节点泡泡时，则子节点泡泡将取代被击破泡泡的位置
    > 注：即整棵子树泡泡上移

请问在击破一个节点泡泡操作或无击破操作后，二叉泡泡树的最大「层和」是多少。

**注意：**
- 「层和」为同一高度的所有节点的分值之和

**示例 1：**
> 输入：`root = [6,0,3,null,8]`
>
> 输出：`11`
>
> 解释：勇者的最佳方案如图所示
>![image.png](https://pic.leetcode-cn.com/1648180809-XSWPLu-image.png){:height="100px"}



**示例 2：**
> 输入：`root = [5,6,2,4,null,null,1,3,5]`
>
> 输出：`9`
>
> 解释：勇者击破 6 节点，此时「层和」最大为 3+5+1 = 9
>![image.png](https://pic.leetcode-cn.com/1648180769-TLpYop-image.png){:height="200px"}



**示例 3：**
> 输入：`root = [-5,1,7]`
>
> 输出：`8`
>
> 解释：勇者不击破节点，「层和」最大为 1+7 = 8


**提示**：
- `2 <= 树中节点个数 <= 10^5`
- `-10000 <= 树中节点的值 <= 10000`


## 难度

Hard

## 标签

- 树
- 动态规划
- 二叉树

## 示例

```
[6,0,3,null,8]
[5,6,2,4,null,null,1,3,5]
[-5,1,7]
```

## 示例代码

### C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int getMaxLayerSum(TreeNode* root) {

    }
};
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getMaxLayerSum(TreeNode root) {

    }
}
```

### Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def getMaxLayerSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
```

### Python3

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getMaxLayerSum(self, root: Optional[TreeNode]) -> int:
```

### C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int getMaxLayerSum(struct TreeNode* root){

}
```

### C#

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int GetMaxLayerSum(TreeNode root) {

    }
}
```

### JavaScript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getMaxLayerSum = function(root) {

};
```

### TypeScript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function getMaxLayerSum(root: TreeNode | null): number {

};
```

### PHP

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function getMaxLayerSum($root) {

    }
}
```

### Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func getMaxLayerSum(_ root: TreeNode?) -> Int {

    }
}
```

### Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun getMaxLayerSum(root: TreeNode?): Int {

    }
}
```

### Go

```golang
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getMaxLayerSum(root *TreeNode) int {

}
```

### Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def get_max_layer_sum(root)

end
```

### Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */
object Solution {
    def getMaxLayerSum(root: TreeNode): Int = {

    }
}
```

### Rust

```rust
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn get_max_layer_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {

    }
}
```

### Racket

```racket
; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (get-max-layer-sum root)
  (-> (or/c tree-node? #f) exact-integer?)

  )
```

### Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec get_max_layer_sum(Root :: #tree_node{} | null) -> integer().
get_max_layer_sum(Root) ->
  .
```

### Elixir

```elixir
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec get_max_layer_sum(root :: TreeNode.t | nil) :: integer
  def get_max_layer_sum(root) do

  end
end
```

