# 1286. 字母组合迭代器

## 题目描述

<p>请你设计一个迭代器类&nbsp;<code>CombinationIterator</code>&nbsp;，包括以下内容：</p>

<ul>
	<li><code>CombinationIterator(string characters, int combinationLength)</code>&nbsp;一个构造函数，输入参数包括：用一个&nbsp;<strong>有序且字符唯一&nbsp;</strong>的字符串&nbsp;<code>characters</code>（该字符串只包含小写英文字母）和一个数字&nbsp;<code>combinationLength</code>&nbsp;。</li>
	<li>函数&nbsp;<em><code>next()</code>&nbsp;</em>，按&nbsp;<strong>字典序&nbsp;</strong>返回长度为&nbsp;<code>combinationLength</code> 的下一个字母组合。</li>
	<li>函数&nbsp;<em><code>hasNext()</code>&nbsp;</em>，只有存在长度为&nbsp;<code>combinationLength</code> 的下一个字母组合时，才返回&nbsp;<code>true</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong>
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
<strong>输出：</strong>
[null, "ab", true, "ac", true, "bc", false]
<strong>解释：
</strong>CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator
iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= combinationLength &lt;=&nbsp;characters.length &lt;= 15</code></li>
	<li>&nbsp;<code>characters</code>&nbsp;中每个字符都 <strong>不同</strong></li>
	<li>每组测试数据最多对&nbsp;<code>next</code>&nbsp;和&nbsp;<code>hasNext</code>&nbsp;调用&nbsp;<code>10<sup>4</sup></code>次</li>
	<li>题目保证每次调用函数&nbsp;<code>next</code>&nbsp;时都存在下一个字母组合。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 字符串
- 回溯
- 迭代器

## 提示

1. Generate all combinations as a preprocessing.
2. Use bit masking to generate all the combinations.

## 示例

```
["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]
[["abc",2],[],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class CombinationIterator {
public:
    CombinationIterator(string characters, int combinationLength) {
        
    }
    
    string next() {
        
    }
    
    bool hasNext() {
        
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```

### Java

```java
class CombinationIterator {

    public CombinationIterator(String characters, int combinationLength) {
        
    }
    
    public String next() {
        
    }
    
    public boolean hasNext() {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
```

### Python

```python
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        

    def next(self):
        """
        :rtype: str
        """
        

    def hasNext(self):
        """
        :rtype: bool
        """
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

### Python3

```python3
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        

    def next(self) -> str:
        

    def hasNext(self) -> bool:
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

### C

```c



typedef struct {
    
} CombinationIterator;


CombinationIterator* combinationIteratorCreate(char* characters, int combinationLength) {
    
}

char* combinationIteratorNext(CombinationIterator* obj) {
    
}

bool combinationIteratorHasNext(CombinationIterator* obj) {
    
}

void combinationIteratorFree(CombinationIterator* obj) {
    
}

/**
 * Your CombinationIterator struct will be instantiated and called as such:
 * CombinationIterator* obj = combinationIteratorCreate(characters, combinationLength);
 * char* param_1 = combinationIteratorNext(obj);
 
 * bool param_2 = combinationIteratorHasNext(obj);
 
 * combinationIteratorFree(obj);
*/
```

### C#

```csharp
public class CombinationIterator {

    public CombinationIterator(string characters, int combinationLength) {
        
    }
    
    public string Next() {
        
    }
    
    public bool HasNext() {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */
```

### JavaScript

```javascript
/**
 * @param {string} characters
 * @param {number} combinationLength
 */
var CombinationIterator = function(characters, combinationLength) {
    
};

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    
};

/** 
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = new CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

### TypeScript

```typescript
class CombinationIterator {
    constructor(characters: string, combinationLength: number) {
        
    }

    next(): string {
        
    }

    hasNext(): boolean {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = new CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

### PHP

```php
class CombinationIterator {
    /**
     * @param String $characters
     * @param Integer $combinationLength
     */
    function __construct($characters, $combinationLength) {
        
    }
  
    /**
     * @return String
     */
    function next() {
        
    }
  
    /**
     * @return Boolean
     */
    function hasNext() {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * $obj = CombinationIterator($characters, $combinationLength);
 * $ret_1 = $obj->next();
 * $ret_2 = $obj->hasNext();
 */
```

### Swift

```swift

class CombinationIterator {

    init(_ characters: String, _ combinationLength: Int) {
        
    }
    
    func next() -> String {
        
    }
    
    func hasNext() -> Bool {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj = CombinationIterator(characters, combinationLength)
 * let ret_1: String = obj.next()
 * let ret_2: Bool = obj.hasNext()
 */
```

### Kotlin

```kotlin
class CombinationIterator(characters: String, combinationLength: Int) {

    fun next(): String {
        
    }

    fun hasNext(): Boolean {
        
    }

}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

### Dart

```dart
class CombinationIterator {

  CombinationIterator(String characters, int combinationLength) {
    
  }
  
  String next() {
    
  }
  
  bool hasNext() {
    
  }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = CombinationIterator(characters, combinationLength);
 * String param1 = obj.next();
 * bool param2 = obj.hasNext();
 */
```

### Go

```golang
type CombinationIterator struct {
    
}


func Constructor(characters string, combinationLength int) CombinationIterator {
    
}


func (this *CombinationIterator) Next() string {
    
}


func (this *CombinationIterator) HasNext() bool {
    
}


/**
 * Your CombinationIterator object will be instantiated and called as such:
 * obj := Constructor(characters, combinationLength);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
```

### Ruby

```ruby
class CombinationIterator

=begin
    :type characters: String
    :type combination_length: Integer
=end
    def initialize(characters, combination_length)
        
    end


=begin
    :rtype: String
=end
    def next()
        
    end


=begin
    :rtype: Boolean
=end
    def has_next()
        
    end


end

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator.new(characters, combination_length)
# param_1 = obj.next()
# param_2 = obj.has_next()
```

### Scala

```scala
class CombinationIterator(_characters: String, _combinationLength: Int) {

    def next(): String = {
        
    }

    def hasNext(): Boolean = {
        
    }

}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * val obj = new CombinationIterator(characters, combinationLength)
 * val param_1 = obj.next()
 * val param_2 = obj.hasNext()
 */
```

### Rust

```rust
struct CombinationIterator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CombinationIterator {

    fn new(characters: String, combinationLength: i32) -> Self {
        
    }
    
    fn next(&self) -> String {
        
    }
    
    fn has_next(&self) -> bool {
        
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj = CombinationIterator::new(characters, combinationLength);
 * let ret_1: String = obj.next();
 * let ret_2: bool = obj.has_next();
 */
```

### Racket

```racket
(define combination-iterator%
  (class object%
    (super-new)
    
    ; characters : string?
    ; combination-length : exact-integer?
    (init-field
      characters
      combination-length)
    
    ; next : -> string?
    (define/public (next)
      )
    ; has-next : -> boolean?
    (define/public (has-next)
      )))

;; Your combination-iterator% object will be instantiated and called as such:
;; (define obj (new combination-iterator% [characters characters] [combination-length combination-length]))
;; (define param_1 (send obj next))
;; (define param_2 (send obj has-next))
```

### Erlang

```erlang
-spec combination_iterator_init_(Characters :: unicode:unicode_binary(), CombinationLength :: integer()) -> any().
combination_iterator_init_(Characters, CombinationLength) ->
  .

-spec combination_iterator_next() -> unicode:unicode_binary().
combination_iterator_next() ->
  .

-spec combination_iterator_has_next() -> boolean().
combination_iterator_has_next() ->
  .


%% Your functions will be called as such:
%% combination_iterator_init_(Characters, CombinationLength),
%% Param_1 = combination_iterator_next(),
%% Param_2 = combination_iterator_has_next(),

%% combination_iterator_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule CombinationIterator do
  @spec init_(characters :: String.t, combination_length :: integer) :: any
  def init_(characters, combination_length) do
    
  end

  @spec next() :: String.t
  def next() do
    
  end

  @spec has_next() :: boolean
  def has_next() do
    
  end
end

# Your functions will be called as such:
# CombinationIterator.init_(characters, combination_length)
# param_1 = CombinationIterator.next()
# param_2 = CombinationIterator.has_next()

# CombinationIterator.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class CombinationIterator {
    init(characters: String, combinationLength: Int64) {

    }
    
    func next(): String {

    }
    
    func hasNext(): Bool {

    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj: CombinationIterator = CombinationIterator(characters, combinationLength)
 * let param_1 = obj.next()
 * let param_2 = obj.hasNext()
 */
```

