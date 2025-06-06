# 385. 迷你语法分析器

## 题目描述

<p>给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果&nbsp;<code>NestedInteger</code> 。</p>

<p>列表中的每个元素只可能是整数或整数嵌套列表</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "324",
<strong>输出：</strong>324
<strong>解释：</strong>你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "[123,[456,[789]]]",
<strong>输出：</strong>[123,[456,[789]]]
<strong>解释：</strong>返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> 由数字、方括号&nbsp;<code>"[]"</code>、负号&nbsp;<code>'-'</code>&nbsp;、逗号&nbsp;<code>','</code>组成</li>
	<li>用例保证&nbsp;<code>s</code> 是可解析的&nbsp;<code>NestedInteger</code></li>
	<li>输入中的所有值的范围是&nbsp;<code>[-10<sup>6</sup>, 10<sup>6</sup>]</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 深度优先搜索
- 字符串

## 示例

```
"324"
"[123,[456,[789]]]"
```

## 示例代码

### C++

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        
    }
};
```

### Java

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        
    }
}
```

### Python

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        
```

### Python3

```python3
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        
```

### C

```c
/**
 * *********************************************************************
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * // Initializes an empty nested list and return a reference to the nested integer.
 * struct NestedInteger *NestedIntegerInit();
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * bool NestedIntegerIsInteger(struct NestedInteger *);
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * int NestedIntegerGetInteger(struct NestedInteger *);
 *
 * // Set this NestedInteger to hold a single integer.
 * void NestedIntegerSetInteger(struct NestedInteger *ni, int value);
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 * void NestedIntegerAdd(struct NestedInteger *ni, struct NestedInteger *elem);
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * struct NestedInteger **NestedIntegerGetList(struct NestedInteger *);
 *
 * // Return the nested list's size that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * int NestedIntegerGetListSize(struct NestedInteger *);
 * };
 */
struct NestedInteger* deserialize(char* s) {
    
}
```

### C#

```csharp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void SetInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void Add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
public class Solution {
    public NestedInteger Deserialize(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @param {string} s
 * @return {NestedInteger}
 */
var deserialize = function(s) {
    
};
```

### TypeScript

```typescript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

function deserialize(s: string): NestedInteger {
    
};
```

### PHP

```php
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {

 *     // if value is not specified, initializes an empty list.
 *     // Otherwise initializes a single integer equal to value.
 *     function __construct($value = null)

 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     function isInteger() : bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     function getInteger()
 *
 *     // Set this NestedInteger to hold a single integer.
 *     function setInteger($i) : void
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     function add($ni) : void
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     function getList() : array
 * }
 */
class Solution {

    /**
     * @param String $s
     * @return NestedInteger
     */
    function deserialize($s) {
        
    }
}
```

### Swift

```swift
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger() -> Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     public func getInteger() -> Int
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(value: Int)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(elem: NestedInteger)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     public func getList() -> [NestedInteger]
 * }
 */
class Solution {
    func deserialize(_ s: String) -> NestedInteger {
        
    }
}
```

### Kotlin

```kotlin
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     constructor()
 *
 *     // Constructor initializes a single integer.
 *     constructor(value: Int)
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     fun isInteger(): Boolean
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     fun getInteger(): Int?
 *
 *     // Set this NestedInteger to hold a single integer.
 *     fun setInteger(value: Int): Unit
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     fun add(ni: NestedInteger): Unit
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     fun getList(): List<NestedInteger>?
 * }
 */
class Solution {
    fun deserialize(s: String): NestedInteger {
        
    }
}
```

### Dart

```dart
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   // If [integer] is an int, constructor initializes a single integer.
 *   // Otherwise it initializes an empty nested list.
 *   NestedInteger([int? integer]);
 *
 *   // Returns true if this NestedInteger holds a single integer, rather than a nested list.
 *   bool isInteger();
 *
 *   // Returns the single integer that this NestedInteger holds, if it holds a single integer.
 *   // Returns null if this NestedInteger holds a nested list.
 *   int getInteger();
 *
 *   // Sets this NestedInteger to hold a single integer.
 *   void setInteger(int value);
 *
 *   // Sets this NestedInteger to hold a nested list and adds a nested integer to it.
 *   void add(NestedInteger ni);
 *
 *   // Returns the nested list that this NestedInteger holds, if it holds a nested list.
 *   // Returns empty list if this NestedInteger holds a single integer.
 *   List<NestedInteger> getList();
 * }
 */
class Solution {
  NestedInteger deserialize(String s) {
    
  }
}
```

### Go

```golang
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */
func deserialize(s string) *NestedInteger {
    
}
```

### Ruby

```ruby
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
#
#class NestedInteger
#    def is_integer()
#        """
#        Return true if this NestedInteger holds a single integer, rather than a nested list.
#        @return {Boolean}
#        """
#
#    def get_integer()
#        """
#        Return the single integer that this NestedInteger holds, if it holds a single integer
#        Return nil if this NestedInteger holds a nested list
#        @return {Integer}
#        """
#
#    def set_integer(value)
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        @return {Void}
#        """
#
#    def add(elem)
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        @return {Void}
#        """
#
#    def get_list()
#        """
#        Return the nested list that this NestedInteger holds, if it holds a nested list
#        Return nil if this NestedInteger holds a single integer
#        @return {NestedInteger[]}
#        """

# @param {String} s
# @return {NestedInteger}
def deserialize(s)
    
end
```

### Scala

```scala
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * trait NestedInteger {
 *
 *   // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *   def isInteger: Boolean
 *
 *   // Return the single integer that this NestedInteger holds, if it holds a single integer.
 *   def getInteger: Int
 *
 *   // Set this NestedInteger to hold a single integer.
 *   def setInteger(i: Int): Unit
 *
 *   // Return the nested list that this NestedInteger holds, if it holds a nested list.
 *   def getList: Array[NestedInteger]
 *
 *   // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *   def add(ni: NestedInteger): Unit
 * }
 */
object Solution {
    def deserialize(s: String): NestedInteger = {
        
    }
}
```

### Rust

```rust
// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//   Int(i32),
//   List(Vec<NestedInteger>)
// }
impl Solution {
    pub fn deserialize(s: String) -> NestedInteger {
        
    }
}
```

### Racket

```racket
;; This is the interface that allows for creating nested lists.
;; You should not implement it, or speculate about its implementation

#|

(define nested-integer%
  (class object%
    ...

    ; Return true if this nested-integer% holds a single integer, rather than a nested list.
    ; -> boolean?
    (define/public (is-integer)
      ...)

    ; Return the single integer that this nested-integer% holds, if it holds a single integer,
    ; or #f if this nested-integer% holds a nested list.
    ; -> integer?
    (define/public (get-integer)
      ...)

    ; Set this nested-integer% to hold a single integer equal to value.
    ; -> integer? void?
    (define/public (set-integer i)
      ...)

    ; Set this nested-integer% to hold a nested list and adds a nested integer elem to it.
    ; -> (is-a?/c nested-integer%) void?
    (define/public (add ni)
      ...)

    ; Return the nested list that this nested-integer% holds,
    ; or an empty list if this nested-integer% holds a single integer.
    ; -> gvector?
    (define/public (get-list)
      ...)))

|#

(define/contract (deserialize s)
  (-> string? (is-a?/c nested-integer%))
  )
```

### Erlang

```erlang
%% % This is the interface that allows for creating nested lists.
%% % You should not implement it, or speculate about its implementation
%%
%% % Create an empty nested list.
%% nested_integer:new() -> nested_integer().
%%
%% % Create a single integer.
%% nested_integer:new(Val :: integer()) -> nested_integer().
%%
%% % Return true if argument NestedInteger holds a single integer, rather than a nested list.
%% nested_integer:is_integer(NestedInteger :: nested_integer()) -> boolean().
%%
%% % Return the single integer that NestedInteger holds, if it holds a single integer.
%% % The result is undefined if it holds a nested list.
%% nested_integer:get_integer(NestedInteger :: nested_integer()) -> integer().
%%
%% % Return a copy of argument NestedInteger with it set to hold a single integer Val.
%% nested_integer:set_integer(NestedInteger :: nested_integer(), Val :: integer()) -> nested_integer().
%%
%% % Return a copy of argument NestedInteger with it set to hold a nested list and adds a nested_integer Elem to it.
%% nested_integer:add(NestedInteger :: nested_integer(), Elem :: nested_integer()) -> nested_integer().
%%
%% % Return the nested list that NestedInteger holds, if it holds a nested list.
%% % The result is undefined if it holds a single integer.
%% nested_integer:get_list(NestedInteger :: nested_integer()) -> array:array(nested_integer()).

-spec deserialize(S :: unicode:unicode_binary()) -> nested_integer:nested_integer().
deserialize(S) ->
  .
```

### Elixir

```elixir
# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
#
# # Create an empty nested list.
# :nested_integer.new() :: :nested_integer.nested_integer
#
# # Create a single integer.
# :nested_integer.new(val :: integer) :: :nested_integer.nested_integer
#
# # Return true if argument nested_integer holds a single integer, rather than a nested list.
# :nested_integer.is_integer(nested_integer :: :nested_integer.nested_integer) :: boolean
#
# # Return the single integer that nested_integer holds, if it holds a single integer
# # The result is undefined if it holds a nested list.
# :nested_integer.get_integer(nested_integer :: :nested_integer.nested_integer) :: integer
#
# # Return a copy of argument nested_integer with it set to hold a single integer val.
# :nested_integer.set_integer(nested_integer :: :nested_integer.nested_integer, val :: integer) :: :nested_integer.nested_integer
#
# # Return a copy of argument nested_integer with it set to hold a nested list and adds a nested_integer elem to it.
# :nested_integer.add(nested_integer :: :nested_integer.nested_integer, elem :: :nested_integer.nested_integer) :: :nested_integer.nested_integer
#
# # Return the nested list that nested_integer holds, if it holds a nested list.
# # The result is undefined if it holds a single integer.
# :nested_integer.get_list(nested_integer :: :nested_integer.nested_integer) :: :array.array(:nested_integer.nested_integer)

defmodule Solution do
  @spec deserialize(s :: String.t) :: :nested_integer.nested_integer
  def deserialize(s) do
    
  end
end
```

### Cangjie

```cangjie
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation.
 * public class NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public init()
 *
 *     // Constructor initializes a single integer.
 *     public init(val: Int64)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger(): Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list.
 *     public func getInteger(): Int64
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(i: Int64): Unit
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer.
 *     public func getList(): ArrayList<NestedInteger>
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(ni: NestedInteger): Unit
 * }
 */

class Solution {
    func deserialize(s: String): NestedInteger {

    }
}
```

