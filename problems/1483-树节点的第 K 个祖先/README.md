# 1483. 树节点的第 K 个祖先

## 题目描述

<p>给你一棵树，树上有 <code>n</code> 个节点，按从 <code>0</code> 到 <code>n-1</code> 编号。树以父节点数组的形式给出，其中 <code>parent[i]</code> 是节点 <code>i</code> 的父节点。树的根节点是编号为 <code>0</code> 的节点。</p>

<p>树节点的第 <em><code>k</code> </em>个祖先节点是从该节点到根节点路径上的第 <code>k</code> 个节点。</p>

<p>实现 <code>TreeAncestor</code> 类：</p>

<ul>
	<li><code>TreeAncestor（int n， int[] parent）</code> 对树和父数组中的节点数初始化对象。</li>
	<li><code>getKthAncestor</code><code>(int node, int k)</code> 返回节点 <code>node</code> 的第 <code>k</code> 个祖先节点。如果不存在这样的祖先节点，返回 <code>-1</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/14/1528_ex1.png" /></strong></p>

<pre>
<strong>输入：</strong>
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

<strong>输出：</strong>
[null,1,0,-1]

<strong>解释：</strong>
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>parent[0] == -1</code> 表示编号为 <code>0</code> 的节点是根节点。</li>
	<li>对于所有的 <code>0 &lt;&nbsp;i &lt; n</code> ，<code>0 &lt;= parent[i] &lt; n</code> 总成立</li>
	<li><code>0 &lt;= node &lt; n</code></li>
	<li>至多查询&nbsp;<code>5 * 10<sup>4</sup></code> 次</li>
</ul>


## 难度

Hard

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 设计
- 二分查找
- 动态规划

## 提示

1. The queries must be answered efficiently to avoid time limit exceeded verdict.
2. Use sparse table (dynamic programming application) to travel the tree upwards in a fast way.

## 示例

```
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
```

## 示例代码

### C++

```cpp
class TreeAncestor {
public:
    TreeAncestor(int n, vector<int>& parent) {
        
    }
    
    int getKthAncestor(int node, int k) {
        
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */
```

### Java

```java
class TreeAncestor {

    public TreeAncestor(int n, int[] parent) {
        
    }
    
    public int getKthAncestor(int node, int k) {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.getKthAncestor(node,k);
 */
```

### Python

```python
class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
```

### Python3

```python3
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        

    def getKthAncestor(self, node: int, k: int) -> int:
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
```

### C

```c



typedef struct {
    
} TreeAncestor;


TreeAncestor* treeAncestorCreate(int n, int* parent, int parentSize) {
    
}

int treeAncestorGetKthAncestor(TreeAncestor* obj, int node, int k) {
    
}

void treeAncestorFree(TreeAncestor* obj) {
    
}

/**
 * Your TreeAncestor struct will be instantiated and called as such:
 * TreeAncestor* obj = treeAncestorCreate(n, parent, parentSize);
 * int param_1 = treeAncestorGetKthAncestor(obj, node, k);
 
 * treeAncestorFree(obj);
*/
```

### C#

```csharp
public class TreeAncestor {

    public TreeAncestor(int n, int[] parent) {
        
    }
    
    public int GetKthAncestor(int node, int k) {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.GetKthAncestor(node,k);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} parent
 */
var TreeAncestor = function(n, parent) {
    
};

/** 
 * @param {number} node 
 * @param {number} k
 * @return {number}
 */
TreeAncestor.prototype.getKthAncestor = function(node, k) {
    
};

/** 
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = new TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
```

### TypeScript

```typescript
class TreeAncestor {
    constructor(n: number, parent: number[]) {
        
    }

    getKthAncestor(node: number, k: number): number {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = new TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
```

### PHP

```php
class TreeAncestor {
    /**
     * @param Integer $n
     * @param Integer[] $parent
     */
    function __construct($n, $parent) {
        
    }
  
    /**
     * @param Integer $node
     * @param Integer $k
     * @return Integer
     */
    function getKthAncestor($node, $k) {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * $obj = TreeAncestor($n, $parent);
 * $ret_1 = $obj->getKthAncestor($node, $k);
 */
```

### Swift

```swift

class TreeAncestor {

    init(_ n: Int, _ parent: [Int]) {
        
    }
    
    func getKthAncestor(_ node: Int, _ k: Int) -> Int {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * let obj = TreeAncestor(n, parent)
 * let ret_1: Int = obj.getKthAncestor(node, k)
 */
```

### Kotlin

```kotlin
class TreeAncestor(n: Int, parent: IntArray) {

    fun getKthAncestor(node: Int, k: Int): Int {
        
    }

}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * var obj = TreeAncestor(n, parent)
 * var param_1 = obj.getKthAncestor(node,k)
 */
```

### Dart

```dart
class TreeAncestor {

  TreeAncestor(int n, List<int> parent) {
    
  }
  
  int getKthAncestor(int node, int k) {
    
  }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = TreeAncestor(n, parent);
 * int param1 = obj.getKthAncestor(node,k);
 */
```

### Go

```golang
type TreeAncestor struct {
    
}


func Constructor(n int, parent []int) TreeAncestor {
    
}


func (this *TreeAncestor) GetKthAncestor(node int, k int) int {
    
}


/**
 * Your TreeAncestor object will be instantiated and called as such:
 * obj := Constructor(n, parent);
 * param_1 := obj.GetKthAncestor(node,k);
 */
```

### Ruby

```ruby
class TreeAncestor

=begin
    :type n: Integer
    :type parent: Integer[]
=end
    def initialize(n, parent)
        
    end


=begin
    :type node: Integer
    :type k: Integer
    :rtype: Integer
=end
    def get_kth_ancestor(node, k)
        
    end


end

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor.new(n, parent)
# param_1 = obj.get_kth_ancestor(node, k)
```

### Scala

```scala
class TreeAncestor(_n: Int, _parent: Array[Int]) {

    def getKthAncestor(node: Int, k: Int): Int = {
        
    }

}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * val obj = new TreeAncestor(n, parent)
 * val param_1 = obj.getKthAncestor(node,k)
 */
```

### Rust

```rust
struct TreeAncestor {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TreeAncestor {

    fn new(n: i32, parent: Vec<i32>) -> Self {
        
    }
    
    fn get_kth_ancestor(&self, node: i32, k: i32) -> i32 {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * let obj = TreeAncestor::new(n, parent);
 * let ret_1: i32 = obj.get_kth_ancestor(node, k);
 */
```

### Racket

```racket
(define tree-ancestor%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; parent : (listof exact-integer?)
    (init-field
      n
      parent)
    
    ; get-kth-ancestor : exact-integer? exact-integer? -> exact-integer?
    (define/public (get-kth-ancestor node k)
      )))

;; Your tree-ancestor% object will be instantiated and called as such:
;; (define obj (new tree-ancestor% [n n] [parent parent]))
;; (define param_1 (send obj get-kth-ancestor node k))
```

### Erlang

```erlang
-spec tree_ancestor_init_(N :: integer(), Parent :: [integer()]) -> any().
tree_ancestor_init_(N, Parent) ->
  .

-spec tree_ancestor_get_kth_ancestor(Node :: integer(), K :: integer()) -> integer().
tree_ancestor_get_kth_ancestor(Node, K) ->
  .


%% Your functions will be called as such:
%% tree_ancestor_init_(N, Parent),
%% Param_1 = tree_ancestor_get_kth_ancestor(Node, K),

%% tree_ancestor_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TreeAncestor do
  @spec init_(n :: integer, parent :: [integer]) :: any
  def init_(n, parent) do
    
  end

  @spec get_kth_ancestor(node :: integer, k :: integer) :: integer
  def get_kth_ancestor(node, k) do
    
  end
end

# Your functions will be called as such:
# TreeAncestor.init_(n, parent)
# param_1 = TreeAncestor.get_kth_ancestor(node, k)

# TreeAncestor.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TreeAncestor {
    init(n: Int64, parent: Array<Int64>) {

    }
    
    func getKthAncestor(node: Int64, k: Int64): Int64 {

    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * let obj: TreeAncestor = TreeAncestor(n, parent)
 * let param_1 = obj.getKthAncestor(node,k)
 */
```

