# 919. 完全二叉树插入器

## 题目描述

<p><strong>完全二叉树</strong> 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。</p>

<p>设计一种算法，将一个新节点插入到一棵完全二叉树中，并在插入后保持其完整。</p>

<p>实现 <code>CBTInserter</code> 类:</p>

<ul>
	<li><code>CBTInserter(TreeNode root)</code>&nbsp;使用头节点为&nbsp;<code>root</code>&nbsp;的给定树初始化该数据结构；</li>
	<li><code>CBTInserter.insert(int v)</code>&nbsp; 向树中插入一个值为&nbsp;<code>Node.val == val</code>的新节点&nbsp;<code>TreeNode</code>。使树保持完全二叉树的状态，<strong>并返回插入节点</strong>&nbsp;<code>TreeNode</code>&nbsp;<strong>的父节点的值</strong>；</li>
	<li><code>CBTInserter.get_root()</code> 将返回树的头节点。</li>
</ul>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg" style="height: 143px; width: 500px;" /></p>

<pre>
<strong>输入</strong>
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
<strong>输出</strong>
[null, 1, 2, [1, 2, 3, 4]]

<strong>解释</strong>
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数量范围为&nbsp;<code>[1, 1000]</code>&nbsp;</li>
	<li><code>0 &lt;= Node.val &lt;= 5000</code></li>
	<li><code>root</code>&nbsp;是完全二叉树</li>
	<li><code>0 &lt;= val &lt;= 5000</code>&nbsp;</li>
	<li>每个测试用例最多调用&nbsp;<code>insert</code>&nbsp;和&nbsp;<code>get_root</code>&nbsp;操作&nbsp;<code>10<sup>4</sup></code>&nbsp;次</li>
</ul>


## 难度

Medium

## 标签

- 树
- 广度优先搜索
- 设计
- 二叉树

## 示例

```
["CBTInserter","insert","insert","get_root"]
[[[1,2]],[3],[4],[]]
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
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class CBTInserter {
public:
    CBTInserter(TreeNode* root) {
        
    }
    
    int insert(int val) {
        
    }
    
    TreeNode* get_root() {
        
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(val);
 * TreeNode* param_2 = obj->get_root();
 */
```

### Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class CBTInserter {

    public CBTInserter(TreeNode root) {
        
    }
    
    public int insert(int val) {
        
    }
    
    public TreeNode get_root() {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(val);
 * TreeNode param_2 = obj.get_root();
 */
```

### Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
```

### Python3

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        

    def insert(self, val: int) -> int:
        

    def get_root(self) -> Optional[TreeNode]:
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
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



typedef struct {
    
} CBTInserter;


CBTInserter* cBTInserterCreate(struct TreeNode* root) {
    
}

int cBTInserterInsert(CBTInserter* obj, int val) {
    
}

struct TreeNode* cBTInserterGet_root(CBTInserter* obj) {
    
}

void cBTInserterFree(CBTInserter* obj) {
    
}

/**
 * Your CBTInserter struct will be instantiated and called as such:
 * CBTInserter* obj = cBTInserterCreate(root);
 * int param_1 = cBTInserterInsert(obj, val);
 
 * struct TreeNode* param_2 = cBTInserterGet_root(obj);
 
 * cBTInserterFree(obj);
*/
```

### C#

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class CBTInserter {

    public CBTInserter(TreeNode root) {
        
    }
    
    public int Insert(int val) {
        
    }
    
    public TreeNode Get_root() {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.Insert(val);
 * TreeNode param_2 = obj.Get_root();
 */
```

### JavaScript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 */
var CBTInserter = function(root) {
    
};

/** 
 * @param {number} val
 * @return {number}
 */
CBTInserter.prototype.insert = function(val) {
    
};

/**
 * @return {TreeNode}
 */
CBTInserter.prototype.get_root = function() {
    
};

/** 
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(val)
 * var param_2 = obj.get_root()
 */
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

class CBTInserter {
    constructor(root: TreeNode | null) {
        
    }

    insert(val: number): number {
        
    }

    get_root(): TreeNode | null {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(val)
 * var param_2 = obj.get_root()
 */
```

### PHP

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class CBTInserter {
    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        
    }
  
    /**
     * @param Integer $val
     * @return Integer
     */
    function insert($val) {
        
    }
  
    /**
     * @return TreeNode
     */
    function get_root() {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * $obj = CBTInserter($root);
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->get_root();
 */
```

### Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

class CBTInserter {

    init(_ root: TreeNode?) {
        
    }
    
    func insert(_ val: Int) -> Int {
        
    }
    
    func get_root() -> TreeNode? {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * let obj = CBTInserter(root)
 * let ret_1: Int = obj.insert(val)
 * let ret_2: TreeNode? = obj.get_root()
 */
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
class CBTInserter(root: TreeNode?) {

    fun insert(`val`: Int): Int {
        
    }

    fun get_root(): TreeNode? {
        
    }

}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = CBTInserter(root)
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.get_root()
 */
```

### Dart

```dart
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class CBTInserter {

  CBTInserter(TreeNode? root) {
    
  }
  
  int insert(int val) {
    
  }
  
  TreeNode? get_root() {
    
  }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = CBTInserter(root);
 * int param1 = obj.insert(val);
 * TreeNode? param2 = obj.get_root();
 */
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
type CBTInserter struct {
    
}


func Constructor(root *TreeNode) CBTInserter {
    
}


func (this *CBTInserter) Insert(val int) int {
    
}


func (this *CBTInserter) Get_root() *TreeNode {
    
}


/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(val);
 * param_2 := obj.Get_root();
 */
```

### Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
class CBTInserter

=begin
    :type root: TreeNode
=end
    def initialize(root)
        
    end


=begin
    :type val: Integer
    :rtype: Integer
=end
    def insert(val)
        
    end


=begin
    :rtype: TreeNode
=end
    def get_root()
        
    end


end

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter.new(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
```

### Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
class CBTInserter(_root: TreeNode) {

    def insert(`val`: Int): Int = {
        
    }

    def get_root(): TreeNode = {
        
    }

}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * val obj = new CBTInserter(root)
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.get_root()
 */
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
struct CBTInserter {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CBTInserter {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        
    }
    
    fn insert(&self, val: i32) -> i32 {
        
    }
    
    fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {
        
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * let obj = CBTInserter::new(root);
 * let ret_1: i32 = obj.insert(val);
 * let ret_2: Option<Rc<RefCell<TreeNode>>> = obj.get_root();
 */
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

(define cbt-inserter%
  (class object%
    (super-new)
    
    ; root : (or/c tree-node? #f)
    (init-field
      root)
    
    ; insert : exact-integer? -> exact-integer?
    (define/public (insert val)
      )
    ; get_root : -> (or/c tree-node? #f)
    (define/public (get_root)
      )))

;; Your cbt-inserter% object will be instantiated and called as such:
;; (define obj (new cbt-inserter% [root root]))
;; (define param_1 (send obj insert val))
;; (define param_2 (send obj get_root))
```

### Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec cbt_inserter_init_(Root :: #tree_node{} | null) -> any().
cbt_inserter_init_(Root) ->
  .

-spec cbt_inserter_insert(Val :: integer()) -> integer().
cbt_inserter_insert(Val) ->
  .

-spec cbt_inserter_get_root() -> #tree_node{} | null.
cbt_inserter_get_root() ->
  .


%% Your functions will be called as such:
%% cbt_inserter_init_(Root),
%% Param_1 = cbt_inserter_insert(Val),
%% Param_2 = cbt_inserter_get_root(),

%% cbt_inserter_init_ will be called before every test case, in which you can do some necessary initializations.
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

defmodule CBTInserter do
  @spec init_(root :: TreeNode.t | nil) :: any
  def init_(root) do
    
  end

  @spec insert(val :: integer) :: integer
  def insert(val) do
    
  end

  @spec get_root() :: TreeNode.t | nil
  def get_root() do
    
  end
end

# Your functions will be called as such:
# CBTInserter.init_(root)
# param_1 = CBTInserter.insert(val)
# param_2 = CBTInserter.get_root()

# CBTInserter.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
/**
 * Definition for a binary tree node.
 * public class BinaryTreeNode {
 *     public var val: Int64
 *     public var left: ?BinaryTreeNode
 *     public var right: ?BinaryTreeNode
 *     public init() {
 *         val = 0
 *         left = None
 *         right = None
 *     }
 *     public init(val: Int64) {
 *         this()
 *         this.val = val
 *     }
 * }
 */

class CBTInserter {
    init(root: ?BinaryTreeNode) {

    }
    
    func insert(val: Int64): Int64 {

    }
    
    func get_root(): ?BinaryTreeNode {

    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * let obj: CBTInserter = CBTInserter(root)
 * let param_1 = obj.insert(val)
 * let param_2 = obj.get_root()
 */
```

