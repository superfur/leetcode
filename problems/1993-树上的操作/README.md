# 1993. 树上的操作

## 题目描述

<p>给你一棵&nbsp;<code>n</code>&nbsp;个节点的树，编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，以父节点数组&nbsp;<code>parent</code>&nbsp;的形式给出，其中&nbsp;<code>parent[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个节点的父节点。树的根节点为 <code>0</code>&nbsp;号节点，所以&nbsp;<code>parent[0] = -1</code>&nbsp;，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。</p>

<p>数据结构需要支持如下函数：</p>

<ul>
	<li><strong>Lock：</strong>指定用户给指定节点 <strong>上锁</strong>&nbsp;，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。</li>
	<li><strong>Unlock：</strong>指定用户给指定节点 <strong>解锁</strong>&nbsp;，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。</li>
	<li><b>Upgrade：</b>指定用户给指定节点&nbsp;<strong>上锁</strong>&nbsp;，并且将该节点的所有子孙节点&nbsp;<strong>解锁</strong>&nbsp;。只有如下 3 个条件 <strong>全部</strong> 满足时才能执行升级操作：
	<ul>
		<li>指定节点当前状态为未上锁。</li>
		<li>指定节点至少有一个上锁状态的子孙节点（可以是 <strong>任意</strong>&nbsp;用户上锁的）。</li>
		<li>指定节点没有任何上锁的祖先节点。</li>
	</ul>
	</li>
</ul>

<p>请你实现&nbsp;<code>LockingTree</code>&nbsp;类：</p>

<ul>
	<li><code>LockingTree(int[] parent)</code>&nbsp;用父节点数组初始化数据结构。</li>
	<li><code>lock(int num, int user)</code> 如果&nbsp;id 为&nbsp;<code>user</code>&nbsp;的用户可以给节点&nbsp;<code>num</code>&nbsp;上锁，那么返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。如果可以执行此操作，节点&nbsp;<code>num</code>&nbsp;会被 id 为 <code>user</code>&nbsp;的用户 <strong>上锁</strong>&nbsp;。</li>
	<li><code>unlock(int num, int user)</code>&nbsp;如果 id 为 <code>user</code>&nbsp;的用户可以给节点 <code>num</code>&nbsp;解锁，那么返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。如果可以执行此操作，节点 <code>num</code>&nbsp;变为 <strong>未上锁</strong>&nbsp;状态。</li>
	<li><code>upgrade(int num, int user)</code>&nbsp;如果 id 为 <code>user</code>&nbsp;的用户可以给节点 <code>num</code>&nbsp;升级，那么返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。如果可以执行此操作，节点 <code>num</code>&nbsp;会被&nbsp;<strong>升级 </strong>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/07/29/untitled.png" style="width: 375px; height: 246px;"></p>

<pre><strong>输入：</strong>
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
<strong>输出：</strong>
[null, true, false, true, true, true, false]

<strong>解释：</strong>
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // 返回 true ，因为节点 2 未上锁。
                           // 节点 2 被用户 2 上锁。
lockingTree.unlock(2, 3);  // 返回 false ，因为用户 3 无法解锁被用户 2 上锁的节点。
lockingTree.unlock(2, 2);  // 返回 true ，因为节点 2 之前被用户 2 上锁。
                           // 节点 2 现在变为未上锁状态。
lockingTree.lock(4, 5);    // 返回 true ，因为节点 4 未上锁。
                           // 节点 4 被用户 5 上锁。
lockingTree.upgrade(0, 1); // 返回 true ，因为节点 0 未上锁且至少有一个被上锁的子孙节点（节点 4）。
                           // 节点 0 被用户 1 上锁，节点 4 变为未上锁。
lockingTree.lock(0, 1);    // 返回 false ，因为节点 0 已经被上锁了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == parent.length</code></li>
	<li><code>2 &lt;= n &lt;= 2000</code></li>
	<li>对于&nbsp;<code>i != 0</code>&nbsp;，满足&nbsp;<code>0 &lt;= parent[i] &lt;= n - 1</code></li>
	<li><code>parent[0] == -1</code></li>
	<li><code>0 &lt;= num &lt;= n - 1</code></li>
	<li><code>1 &lt;= user &lt;= 10<sup>4</sup></code></li>
	<li><code>parent</code>&nbsp;表示一棵合法的树。</li>
	<li><code>lock</code>&nbsp;，<code>unlock</code>&nbsp;和&nbsp;<code>upgrade</code>&nbsp;的调用&nbsp;<strong>总共&nbsp;</strong>不超过&nbsp;<code>2000</code>&nbsp;次。</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 广度优先搜索
- 设计
- 数组
- 哈希表

## 提示

1. How can we use the small constraints to help us solve the problem?
2. How can we traverse the ancestors and descendants of a node?

## 示例

```
["LockingTree","lock","unlock","unlock","lock","upgrade","lock"]
[[[-1,0,0,1,1,2,2]],[2,2],[2,3],[2,2],[4,5],[0,1],[0,1]]
```

## 示例代码

### C++

```cpp
class LockingTree {
public:
    LockingTree(vector<int>& parent) {
        
    }
    
    bool lock(int num, int user) {
        
    }
    
    bool unlock(int num, int user) {
        
    }
    
    bool upgrade(int num, int user) {
        
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
```

### Java

```java
class LockingTree {

    public LockingTree(int[] parent) {
        
    }
    
    public boolean lock(int num, int user) {
        
    }
    
    public boolean unlock(int num, int user) {
        
    }
    
    public boolean upgrade(int num, int user) {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * boolean param_1 = obj.lock(num,user);
 * boolean param_2 = obj.unlock(num,user);
 * boolean param_3 = obj.upgrade(num,user);
 */
```

### Python

```python
class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
```

### Python3

```python3
class LockingTree:

    def __init__(self, parent: List[int]):
        

    def lock(self, num: int, user: int) -> bool:
        

    def unlock(self, num: int, user: int) -> bool:
        

    def upgrade(self, num: int, user: int) -> bool:
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
```

### C

```c



typedef struct {
    
} LockingTree;


LockingTree* lockingTreeCreate(int* parent, int parentSize) {
    
}

bool lockingTreeLock(LockingTree* obj, int num, int user) {
    
}

bool lockingTreeUnlock(LockingTree* obj, int num, int user) {
    
}

bool lockingTreeUpgrade(LockingTree* obj, int num, int user) {
    
}

void lockingTreeFree(LockingTree* obj) {
    
}

/**
 * Your LockingTree struct will be instantiated and called as such:
 * LockingTree* obj = lockingTreeCreate(parent, parentSize);
 * bool param_1 = lockingTreeLock(obj, num, user);
 
 * bool param_2 = lockingTreeUnlock(obj, num, user);
 
 * bool param_3 = lockingTreeUpgrade(obj, num, user);
 
 * lockingTreeFree(obj);
*/
```

### C#

```csharp
public class LockingTree {

    public LockingTree(int[] parent) {
        
    }
    
    public bool Lock(int num, int user) {
        
    }
    
    public bool Unlock(int num, int user) {
        
    }
    
    public bool Upgrade(int num, int user) {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * bool param_1 = obj.Lock(num,user);
 * bool param_2 = obj.Unlock(num,user);
 * bool param_3 = obj.Upgrade(num,user);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} parent
 */
var LockingTree = function(parent) {
    
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.lock = function(num, user) {
    
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.unlock = function(num, user) {
    
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.upgrade = function(num, user) {
    
};

/** 
 * Your LockingTree object will be instantiated and called as such:
 * var obj = new LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */
```

### TypeScript

```typescript
class LockingTree {
    constructor(parent: number[]) {
        
    }

    lock(num: number, user: number): boolean {
        
    }

    unlock(num: number, user: number): boolean {
        
    }

    upgrade(num: number, user: number): boolean {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * var obj = new LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */
```

### PHP

```php
class LockingTree {
    /**
     * @param Integer[] $parent
     */
    function __construct($parent) {
        
    }
  
    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function lock($num, $user) {
        
    }
  
    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function unlock($num, $user) {
        
    }
  
    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function upgrade($num, $user) {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * $obj = LockingTree($parent);
 * $ret_1 = $obj->lock($num, $user);
 * $ret_2 = $obj->unlock($num, $user);
 * $ret_3 = $obj->upgrade($num, $user);
 */
```

### Swift

```swift

class LockingTree {

    init(_ parent: [Int]) {
        
    }
    
    func lock(_ num: Int, _ user: Int) -> Bool {
        
    }
    
    func unlock(_ num: Int, _ user: Int) -> Bool {
        
    }
    
    func upgrade(_ num: Int, _ user: Int) -> Bool {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * let obj = LockingTree(parent)
 * let ret_1: Bool = obj.lock(num, user)
 * let ret_2: Bool = obj.unlock(num, user)
 * let ret_3: Bool = obj.upgrade(num, user)
 */
```

### Kotlin

```kotlin
class LockingTree(parent: IntArray) {

    fun lock(num: Int, user: Int): Boolean {
        
    }

    fun unlock(num: Int, user: Int): Boolean {
        
    }

    fun upgrade(num: Int, user: Int): Boolean {
        
    }

}

/**
 * Your LockingTree object will be instantiated and called as such:
 * var obj = LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */
```

### Dart

```dart
class LockingTree {

  LockingTree(List<int> parent) {
    
  }
  
  bool lock(int num, int user) {
    
  }
  
  bool unlock(int num, int user) {
    
  }
  
  bool upgrade(int num, int user) {
    
  }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = LockingTree(parent);
 * bool param1 = obj.lock(num,user);
 * bool param2 = obj.unlock(num,user);
 * bool param3 = obj.upgrade(num,user);
 */
```

### Go

```golang
type LockingTree struct {
    
}


func Constructor(parent []int) LockingTree {
    
}


func (this *LockingTree) Lock(num int, user int) bool {
    
}


func (this *LockingTree) Unlock(num int, user int) bool {
    
}


func (this *LockingTree) Upgrade(num int, user int) bool {
    
}


/**
 * Your LockingTree object will be instantiated and called as such:
 * obj := Constructor(parent);
 * param_1 := obj.Lock(num,user);
 * param_2 := obj.Unlock(num,user);
 * param_3 := obj.Upgrade(num,user);
 */
```

### Ruby

```ruby
class LockingTree

=begin
    :type parent: Integer[]
=end
    def initialize(parent)
        
    end


=begin
    :type num: Integer
    :type user: Integer
    :rtype: Boolean
=end
    def lock(num, user)
        
    end


=begin
    :type num: Integer
    :type user: Integer
    :rtype: Boolean
=end
    def unlock(num, user)
        
    end


=begin
    :type num: Integer
    :type user: Integer
    :rtype: Boolean
=end
    def upgrade(num, user)
        
    end


end

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree.new(parent)
# param_1 = obj.lock(num, user)
# param_2 = obj.unlock(num, user)
# param_3 = obj.upgrade(num, user)
```

### Scala

```scala
class LockingTree(_parent: Array[Int]) {

    def lock(num: Int, user: Int): Boolean = {
        
    }

    def unlock(num: Int, user: Int): Boolean = {
        
    }

    def upgrade(num: Int, user: Int): Boolean = {
        
    }

}

/**
 * Your LockingTree object will be instantiated and called as such:
 * val obj = new LockingTree(parent)
 * val param_1 = obj.lock(num,user)
 * val param_2 = obj.unlock(num,user)
 * val param_3 = obj.upgrade(num,user)
 */
```

### Rust

```rust
struct LockingTree {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LockingTree {

    fn new(parent: Vec<i32>) -> Self {
        
    }
    
    fn lock(&self, num: i32, user: i32) -> bool {
        
    }
    
    fn unlock(&self, num: i32, user: i32) -> bool {
        
    }
    
    fn upgrade(&self, num: i32, user: i32) -> bool {
        
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * let obj = LockingTree::new(parent);
 * let ret_1: bool = obj.lock(num, user);
 * let ret_2: bool = obj.unlock(num, user);
 * let ret_3: bool = obj.upgrade(num, user);
 */
```

### Racket

```racket
(define locking-tree%
  (class object%
    (super-new)
    
    ; parent : (listof exact-integer?)
    (init-field
      parent)
    
    ; lock : exact-integer? exact-integer? -> boolean?
    (define/public (lock num user)
      )
    ; unlock : exact-integer? exact-integer? -> boolean?
    (define/public (unlock num user)
      )
    ; upgrade : exact-integer? exact-integer? -> boolean?
    (define/public (upgrade num user)
      )))

;; Your locking-tree% object will be instantiated and called as such:
;; (define obj (new locking-tree% [parent parent]))
;; (define param_1 (send obj lock num user))
;; (define param_2 (send obj unlock num user))
;; (define param_3 (send obj upgrade num user))
```

### Erlang

```erlang
-spec locking_tree_init_(Parent :: [integer()]) -> any().
locking_tree_init_(Parent) ->
  .

-spec locking_tree_lock(Num :: integer(), User :: integer()) -> boolean().
locking_tree_lock(Num, User) ->
  .

-spec locking_tree_unlock(Num :: integer(), User :: integer()) -> boolean().
locking_tree_unlock(Num, User) ->
  .

-spec locking_tree_upgrade(Num :: integer(), User :: integer()) -> boolean().
locking_tree_upgrade(Num, User) ->
  .


%% Your functions will be called as such:
%% locking_tree_init_(Parent),
%% Param_1 = locking_tree_lock(Num, User),
%% Param_2 = locking_tree_unlock(Num, User),
%% Param_3 = locking_tree_upgrade(Num, User),

%% locking_tree_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule LockingTree do
  @spec init_(parent :: [integer]) :: any
  def init_(parent) do
    
  end

  @spec lock(num :: integer, user :: integer) :: boolean
  def lock(num, user) do
    
  end

  @spec unlock(num :: integer, user :: integer) :: boolean
  def unlock(num, user) do
    
  end

  @spec upgrade(num :: integer, user :: integer) :: boolean
  def upgrade(num, user) do
    
  end
end

# Your functions will be called as such:
# LockingTree.init_(parent)
# param_1 = LockingTree.lock(num, user)
# param_2 = LockingTree.unlock(num, user)
# param_3 = LockingTree.upgrade(num, user)

# LockingTree.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class LockingTree {
    init(parent: Array<Int64>) {

    }
    
    func lock(num: Int64, user: Int64): Bool {

    }
    
    func unlock(num: Int64, user: Int64): Bool {

    }
    
    func upgrade(num: Int64, user: Int64): Bool {

    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * let obj: LockingTree = LockingTree(parent)
 * let param_1 = obj.lock(num,user)
 * let param_2 = obj.unlock(num,user)
 * let param_3 = obj.upgrade(num,user)
 */
```

