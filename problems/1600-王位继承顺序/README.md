# 1600. 王位继承顺序

## 题目描述

<p>一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。</p>

<p>这个王国有一个明确规定的王位继承顺序，第一继承人总是国王自己。我们定义递归函数&nbsp;<code>Successor(x, curOrder)</code>&nbsp;，给定一个人&nbsp;<code>x</code>&nbsp;和当前的继承顺序，该函数返回 <code>x</code>&nbsp;的下一继承人。</p>

<pre>
Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子
</pre>

<p>比方说，假设王国由国王，他的孩子&nbsp;Alice 和 Bob （Alice 比 Bob&nbsp;年长）和 Alice 的孩子&nbsp;Jack 组成。</p>

<ol>
	<li>一开始，&nbsp;<code>curOrder</code>&nbsp;为&nbsp;<code>["king"]</code>.</li>
	<li>调用&nbsp;<code>Successor(king, curOrder)</code>&nbsp;，返回 Alice ，所以我们将 Alice 放入 <code>curOrder</code>&nbsp;中，得到&nbsp;<code>["king", "Alice"]</code>&nbsp;。</li>
	<li>调用&nbsp;<code>Successor(Alice, curOrder)</code>&nbsp;，返回 Jack ，所以我们将 Jack 放入&nbsp;<code>curOrder</code>&nbsp;中，得到&nbsp;<code>["king", "Alice", "Jack"]</code>&nbsp;。</li>
	<li>调用&nbsp;<code>Successor(Jack, curOrder)</code>&nbsp;，返回 Bob ，所以我们将 Bob 放入&nbsp;<code>curOrder</code>&nbsp;中，得到&nbsp;<code>["king", "Alice", "Jack", "Bob"]</code>&nbsp;。</li>
	<li>调用&nbsp;<code>Successor(Bob, curOrder)</code>&nbsp;，返回&nbsp;<code>null</code>&nbsp;。最终得到继承顺序为&nbsp;<code>["king", "Alice", "Jack", "Bob"]</code>&nbsp;。</li>
</ol>

<p>通过以上的函数，我们总是能得到一个唯一的继承顺序。</p>

<p>请你实现&nbsp;<code>ThroneInheritance</code>&nbsp;类：</p>

<ul>
	<li><code>ThroneInheritance(string kingName)</code> 初始化一个&nbsp;<code>ThroneInheritance</code>&nbsp;类的对象。国王的名字作为构造函数的参数传入。</li>
	<li><code>void birth(string parentName, string childName)</code>&nbsp;表示&nbsp;<code>parentName</code>&nbsp;新拥有了一个名为&nbsp;<code>childName</code>&nbsp;的孩子。</li>
	<li><code>void death(string name)</code>&nbsp;表示名为&nbsp;<code>name</code>&nbsp;的人死亡。一个人的死亡不会影响&nbsp;<code>Successor</code>&nbsp;函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。</li>
	<li><code>string[] getInheritanceOrder()</code>&nbsp;返回 <strong>除去</strong>&nbsp;死亡人员的当前继承顺序列表。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
<strong>输出：</strong>
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

<strong>解释：</strong>
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：<strong>king</strong>
t.birth("king", "andy"); // 继承顺序：king &gt; <strong>andy</strong>
t.birth("king", "bob"); // 继承顺序：king &gt; andy &gt; <strong>bob</strong>
t.birth("king", "catherine"); // 继承顺序：king &gt; andy &gt; bob &gt; <strong>catherine</strong>
t.birth("andy", "matthew"); // 继承顺序：king &gt; andy &gt; <strong>matthew</strong> &gt; bob &gt; catherine
t.birth("bob", "alex"); // 继承顺序：king &gt; andy &gt; matthew &gt; bob &gt; <strong>alex</strong> &gt; catherine
t.birth("bob", "asha"); // 继承顺序：king &gt; andy &gt; matthew &gt; bob &gt; alex &gt; <strong>asha</strong> &gt; catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king &gt; andy &gt; matthew &gt; <strong>bob（已经去世）</strong>&gt; alex &gt; asha &gt; catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= kingName.length, parentName.length, childName.length, name.length &lt;= 15</code></li>
	<li><code>kingName</code>，<code>parentName</code>，&nbsp;<code>childName</code>&nbsp;和&nbsp;<code>name</code>&nbsp;仅包含小写英文字母。</li>
	<li>所有的参数&nbsp;<code>childName</code> 和&nbsp;<code>kingName</code>&nbsp;<strong>互不相同</strong>。</li>
	<li>所有&nbsp;<code>death</code>&nbsp;函数中的死亡名字 <code>name</code>&nbsp;要么是国王，要么是已经出生了的人员名字。</li>
	<li>每次调用 <code>birth(parentName, childName)</code> 时，测试用例都保证 <code>parentName</code> 对应的人员是活着的。</li>
	<li>最多调用&nbsp;<code>10<sup>5</sup></code>&nbsp;次<code>birth</code> 和&nbsp;<code>death</code>&nbsp;。</li>
	<li>最多调用&nbsp;<code>10</code>&nbsp;次&nbsp;<code>getInheritanceOrder</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 树
- 深度优先搜索
- 设计
- 哈希表

## 提示

1. Create a tree structure of the family.
2. Without deaths, the order of inheritance is simply a pre-order traversal of the tree.
3. Mark the dead family members tree nodes and don't include them in the final order.

## 示例

```
["ThroneInheritance","birth","birth","birth","birth","birth","birth","getInheritanceOrder","death","getInheritanceOrder"]
[["king"],["king","andy"],["king","bob"],["king","catherine"],["andy","matthew"],["bob","alex"],["bob","asha"],[null],["bob"],[null]]
```

## 示例代码

### C++

```cpp
class ThroneInheritance {
public:
    ThroneInheritance(string kingName) {
        
    }
    
    void birth(string parentName, string childName) {
        
    }
    
    void death(string name) {
        
    }
    
    vector<string> getInheritanceOrder() {
        
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */
```

### Java

```java
class ThroneInheritance {

    public ThroneInheritance(String kingName) {
        
    }
    
    public void birth(String parentName, String childName) {
        
    }
    
    public void death(String name) {
        
    }
    
    public List<String> getInheritanceOrder() {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param_3 = obj.getInheritanceOrder();
 */
```

### Python

```python
class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
```

### Python3

```python3
class ThroneInheritance:

    def __init__(self, kingName: str):
        

    def birth(self, parentName: str, childName: str) -> None:
        

    def death(self, name: str) -> None:
        

    def getInheritanceOrder(self) -> List[str]:
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
```

### C

```c



typedef struct {
    
} ThroneInheritance;


ThroneInheritance* throneInheritanceCreate(char* kingName) {
    
}

void throneInheritanceBirth(ThroneInheritance* obj, char* parentName, char* childName) {
    
}

void throneInheritanceDeath(ThroneInheritance* obj, char* name) {
    
}

char** throneInheritanceGetInheritanceOrder(ThroneInheritance* obj, int* retSize) {
    
}

void throneInheritanceFree(ThroneInheritance* obj) {
    
}

/**
 * Your ThroneInheritance struct will be instantiated and called as such:
 * ThroneInheritance* obj = throneInheritanceCreate(kingName);
 * throneInheritanceBirth(obj, parentName, childName);
 
 * throneInheritanceDeath(obj, name);
 
 * char** param_3 = throneInheritanceGetInheritanceOrder(obj, retSize);
 
 * throneInheritanceFree(obj);
*/
```

### C#

```csharp
public class ThroneInheritance {

    public ThroneInheritance(string kingName) {
        
    }
    
    public void Birth(string parentName, string childName) {
        
    }
    
    public void Death(string name) {
        
    }
    
    public IList<string> GetInheritanceOrder() {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.Birth(parentName,childName);
 * obj.Death(name);
 * IList<string> param_3 = obj.GetInheritanceOrder();
 */
```

### JavaScript

```javascript
/**
 * @param {string} kingName
 */
var ThroneInheritance = function(kingName) {
    
};

/** 
 * @param {string} parentName 
 * @param {string} childName
 * @return {void}
 */
ThroneInheritance.prototype.birth = function(parentName, childName) {
    
};

/** 
 * @param {string} name
 * @return {void}
 */
ThroneInheritance.prototype.death = function(name) {
    
};

/**
 * @return {string[]}
 */
ThroneInheritance.prototype.getInheritanceOrder = function() {
    
};

/** 
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */
```

### TypeScript

```typescript
class ThroneInheritance {
    constructor(kingName: string) {
        
    }

    birth(parentName: string, childName: string): void {
        
    }

    death(name: string): void {
        
    }

    getInheritanceOrder(): string[] {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */
```

### PHP

```php
class ThroneInheritance {
    /**
     * @param String $kingName
     */
    function __construct($kingName) {
        
    }
  
    /**
     * @param String $parentName
     * @param String $childName
     * @return NULL
     */
    function birth($parentName, $childName) {
        
    }
  
    /**
     * @param String $name
     * @return NULL
     */
    function death($name) {
        
    }
  
    /**
     * @return String[]
     */
    function getInheritanceOrder() {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * $obj = ThroneInheritance($kingName);
 * $obj->birth($parentName, $childName);
 * $obj->death($name);
 * $ret_3 = $obj->getInheritanceOrder();
 */
```

### Swift

```swift

class ThroneInheritance {

    init(_ kingName: String) {
        
    }
    
    func birth(_ parentName: String, _ childName: String) {
        
    }
    
    func death(_ name: String) {
        
    }
    
    func getInheritanceOrder() -> [String] {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * let obj = ThroneInheritance(kingName)
 * obj.birth(parentName, childName)
 * obj.death(name)
 * let ret_3: [String] = obj.getInheritanceOrder()
 */
```

### Kotlin

```kotlin
class ThroneInheritance(kingName: String) {

    fun birth(parentName: String, childName: String) {
        
    }

    fun death(name: String) {
        
    }

    fun getInheritanceOrder(): List<String> {
        
    }

}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */
```

### Dart

```dart
class ThroneInheritance {

  ThroneInheritance(String kingName) {
    
  }
  
  void birth(String parentName, String childName) {
    
  }
  
  void death(String name) {
    
  }
  
  List<String> getInheritanceOrder() {
    
  }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param3 = obj.getInheritanceOrder();
 */
```

### Go

```golang
type ThroneInheritance struct {
    
}


func Constructor(kingName string) ThroneInheritance {
    
}


func (this *ThroneInheritance) Birth(parentName string, childName string)  {
    
}


func (this *ThroneInheritance) Death(name string)  {
    
}


func (this *ThroneInheritance) GetInheritanceOrder() []string {
    
}


/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * obj := Constructor(kingName);
 * obj.Birth(parentName,childName);
 * obj.Death(name);
 * param_3 := obj.GetInheritanceOrder();
 */
```

### Ruby

```ruby
class ThroneInheritance

=begin
    :type king_name: String
=end
    def initialize(king_name)
        
    end


=begin
    :type parent_name: String
    :type child_name: String
    :rtype: Void
=end
    def birth(parent_name, child_name)
        
    end


=begin
    :type name: String
    :rtype: Void
=end
    def death(name)
        
    end


=begin
    :rtype: String[]
=end
    def get_inheritance_order()
        
    end


end

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance.new(king_name)
# obj.birth(parent_name, child_name)
# obj.death(name)
# param_3 = obj.get_inheritance_order()
```

### Scala

```scala
class ThroneInheritance(_kingName: String) {

    def birth(parentName: String, childName: String): Unit = {
        
    }

    def death(name: String): Unit = {
        
    }

    def getInheritanceOrder(): List[String] = {
        
    }

}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * val obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * val param_3 = obj.getInheritanceOrder()
 */
```

### Rust

```rust
struct ThroneInheritance {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ThroneInheritance {

    fn new(kingName: String) -> Self {
        
    }
    
    fn birth(&self, parent_name: String, child_name: String) {
        
    }
    
    fn death(&self, name: String) {
        
    }
    
    fn get_inheritance_order(&self) -> Vec<String> {
        
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * let obj = ThroneInheritance::new(kingName);
 * obj.birth(parentName, childName);
 * obj.death(name);
 * let ret_3: Vec<String> = obj.get_inheritance_order();
 */
```

### Racket

```racket
(define throne-inheritance%
  (class object%
    (super-new)
    
    ; king-name : string?
    (init-field
      king-name)
    
    ; birth : string? string? -> void?
    (define/public (birth parent-name child-name)
      )
    ; death : string? -> void?
    (define/public (death name)
      )
    ; get-inheritance-order : -> (listof string?)
    (define/public (get-inheritance-order)
      )))

;; Your throne-inheritance% object will be instantiated and called as such:
;; (define obj (new throne-inheritance% [king-name king-name]))
;; (send obj birth parent-name child-name)
;; (send obj death name)
;; (define param_3 (send obj get-inheritance-order))
```

### Erlang

```erlang
-spec throne_inheritance_init_(KingName :: unicode:unicode_binary()) -> any().
throne_inheritance_init_(KingName) ->
  .

-spec throne_inheritance_birth(ParentName :: unicode:unicode_binary(), ChildName :: unicode:unicode_binary()) -> any().
throne_inheritance_birth(ParentName, ChildName) ->
  .

-spec throne_inheritance_death(Name :: unicode:unicode_binary()) -> any().
throne_inheritance_death(Name) ->
  .

-spec throne_inheritance_get_inheritance_order() -> [unicode:unicode_binary()].
throne_inheritance_get_inheritance_order() ->
  .


%% Your functions will be called as such:
%% throne_inheritance_init_(KingName),
%% throne_inheritance_birth(ParentName, ChildName),
%% throne_inheritance_death(Name),
%% Param_3 = throne_inheritance_get_inheritance_order(),

%% throne_inheritance_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule ThroneInheritance do
  @spec init_(king_name :: String.t) :: any
  def init_(king_name) do
    
  end

  @spec birth(parent_name :: String.t, child_name :: String.t) :: any
  def birth(parent_name, child_name) do
    
  end

  @spec death(name :: String.t) :: any
  def death(name) do
    
  end

  @spec get_inheritance_order() :: [String.t]
  def get_inheritance_order() do
    
  end
end

# Your functions will be called as such:
# ThroneInheritance.init_(king_name)
# ThroneInheritance.birth(parent_name, child_name)
# ThroneInheritance.death(name)
# param_3 = ThroneInheritance.get_inheritance_order()

# ThroneInheritance.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class ThroneInheritance {
    init(kingName: String) {

    }
    
    func birth(parentName: String, childName: String): Unit {

    }
    
    func death(name: String): Unit {

    }
    
    func getInheritanceOrder(): ArrayList<String> {

    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * let obj: ThroneInheritance = ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * let param_3 = obj.getInheritanceOrder()
 */
```

