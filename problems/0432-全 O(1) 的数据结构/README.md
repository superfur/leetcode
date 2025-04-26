# 432. 全 O(1) 的数据结构

## 题目描述

<p>请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。</p>

<p>实现 <code>AllOne</code> 类：</p>

<ul>
	<li><code>AllOne()</code> 初始化数据结构的对象。</li>
	<li><code>inc(String key)</code> 字符串 <code>key</code> 的计数增加 <code>1</code> 。如果数据结构中尚不存在 <code>key</code> ，那么插入计数为 <code>1</code> 的 <code>key</code> 。</li>
	<li><code>dec(String key)</code> 字符串 <code>key</code> 的计数减少 <code>1</code> 。如果 <code>key</code> 的计数在减少后为 <code>0</code> ，那么需要将这个 <code>key</code> 从数据结构中删除。测试用例保证：在减少计数前，<code>key</code> 存在于数据结构中。</li>
	<li><code>getMaxKey()</code> 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 <code>""</code> 。</li>
	<li><code>getMinKey()</code> 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 <code>""</code> 。</li>
</ul>

<p><strong>注意：</strong>每个函数都应当满足 <code>O(1)</code> 平均时间复杂度。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
<strong>输出</strong>
[null, null, null, "hello", "hello", null, "hello", "leet"]

<strong>解释</strong>
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= key.length &lt;= 10</code></li>
	<li><code>key</code> 由小写英文字母组成</li>
	<li>测试用例保证：在每次调用 <code>dec</code> 时，数据结构中总存在 <code>key</code></li>
	<li>最多调用 <code>inc</code>、<code>dec</code>、<code>getMaxKey</code> 和 <code>getMinKey</code> 方法 <code>5 * 10<sup>4</sup></code> 次</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 哈希表
- 链表
- 双向链表

## 示例

```
["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
[[],["hello"],["hello"],[],[],["leet"],[],[]]
```

## 示例代码

### C++

```cpp
class AllOne {
public:
    AllOne() {
        
    }
    
    void inc(string key) {
        
    }
    
    void dec(string key) {
        
    }
    
    string getMaxKey() {
        
    }
    
    string getMinKey() {
        
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```

### Java

```java
class AllOne {

    public AllOne() {
        
    }
    
    public void inc(String key) {
        
    }
    
    public void dec(String key) {
        
    }
    
    public String getMaxKey() {
        
    }
    
    public String getMinKey() {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
```

### Python

```python
class AllOne(object):

    def __init__(self):
        

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        

    def getMaxKey(self):
        """
        :rtype: str
        """
        

    def getMinKey(self):
        """
        :rtype: str
        """
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```

### Python3

```python3
class AllOne:

    def __init__(self):
        

    def inc(self, key: str) -> None:
        

    def dec(self, key: str) -> None:
        

    def getMaxKey(self) -> str:
        

    def getMinKey(self) -> str:
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
```

### C

```c



typedef struct {
    
} AllOne;


AllOne* allOneCreate() {
    
}

void allOneInc(AllOne* obj, char* key) {
    
}

void allOneDec(AllOne* obj, char* key) {
    
}

char* allOneGetMaxKey(AllOne* obj) {
    
}

char* allOneGetMinKey(AllOne* obj) {
    
}

void allOneFree(AllOne* obj) {
    
}

/**
 * Your AllOne struct will be instantiated and called as such:
 * AllOne* obj = allOneCreate();
 * allOneInc(obj, key);
 
 * allOneDec(obj, key);
 
 * char* param_3 = allOneGetMaxKey(obj);
 
 * char* param_4 = allOneGetMinKey(obj);
 
 * allOneFree(obj);
*/
```

### C#

```csharp
public class AllOne {

    public AllOne() {
        
    }
    
    public void Inc(string key) {
        
    }
    
    public void Dec(string key) {
        
    }
    
    public string GetMaxKey() {
        
    }
    
    public string GetMinKey() {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.Inc(key);
 * obj.Dec(key);
 * string param_3 = obj.GetMaxKey();
 * string param_4 = obj.GetMinKey();
 */
```

### JavaScript

```javascript

var AllOne = function() {
    
};

/** 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.inc = function(key) {
    
};

/** 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.dec = function(key) {
    
};

/**
 * @return {string}
 */
AllOne.prototype.getMaxKey = function() {
    
};

/**
 * @return {string}
 */
AllOne.prototype.getMinKey = function() {
    
};

/** 
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
```

### TypeScript

```typescript
class AllOne {
    constructor() {
        
    }

    inc(key: string): void {
        
    }

    dec(key: string): void {
        
    }

    getMaxKey(): string {
        
    }

    getMinKey(): string {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
```

### PHP

```php
class AllOne {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $key
     * @return NULL
     */
    function inc($key) {
        
    }
  
    /**
     * @param String $key
     * @return NULL
     */
    function dec($key) {
        
    }
  
    /**
     * @return String
     */
    function getMaxKey() {
        
    }
  
    /**
     * @return String
     */
    function getMinKey() {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * $obj = AllOne();
 * $obj->inc($key);
 * $obj->dec($key);
 * $ret_3 = $obj->getMaxKey();
 * $ret_4 = $obj->getMinKey();
 */
```

### Swift

```swift

class AllOne {

    init() {
        
    }
    
    func inc(_ key: String) {
        
    }
    
    func dec(_ key: String) {
        
    }
    
    func getMaxKey() -> String {
        
    }
    
    func getMinKey() -> String {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * let ret_3: String = obj.getMaxKey()
 * let ret_4: String = obj.getMinKey()
 */
```

### Kotlin

```kotlin
class AllOne() {

    fun inc(key: String) {
        
    }

    fun dec(key: String) {
        
    }

    fun getMaxKey(): String {
        
    }

    fun getMinKey(): String {
        
    }

}

/**
 * Your AllOne object will be instantiated and called as such:
 * var obj = AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
```

### Dart

```dart
class AllOne {

  AllOne() {
    
  }
  
  void inc(String key) {
    
  }
  
  void dec(String key) {
    
  }
  
  String getMaxKey() {
    
  }
  
  String getMinKey() {
    
  }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param3 = obj.getMaxKey();
 * String param4 = obj.getMinKey();
 */
```

### Go

```golang
type AllOne struct {
    
}


func Constructor() AllOne {
    
}


func (this *AllOne) Inc(key string)  {
    
}


func (this *AllOne) Dec(key string)  {
    
}


func (this *AllOne) GetMaxKey() string {
    
}


func (this *AllOne) GetMinKey() string {
    
}


/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */
```

### Ruby

```ruby
class AllOne
    def initialize()
        
    end


=begin
    :type key: String
    :rtype: Void
=end
    def inc(key)
        
    end


=begin
    :type key: String
    :rtype: Void
=end
    def dec(key)
        
    end


=begin
    :rtype: String
=end
    def get_max_key()
        
    end


=begin
    :rtype: String
=end
    def get_min_key()
        
    end


end

# Your AllOne object will be instantiated and called as such:
# obj = AllOne.new()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.get_max_key()
# param_4 = obj.get_min_key()
```

### Scala

```scala
class AllOne() {

    def inc(key: String): Unit = {
        
    }

    def dec(key: String): Unit = {
        
    }

    def getMaxKey(): String = {
        
    }

    def getMinKey(): String = {
        
    }

}

/**
 * Your AllOne object will be instantiated and called as such:
 * val obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * val param_3 = obj.getMaxKey()
 * val param_4 = obj.getMinKey()
 */
```

### Rust

```rust
struct AllOne {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {

    fn new() -> Self {
        
    }
    
    fn inc(&self, key: String) {
        
    }
    
    fn dec(&self, key: String) {
        
    }
    
    fn get_max_key(&self) -> String {
        
    }
    
    fn get_min_key(&self) -> String {
        
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne::new();
 * obj.inc(key);
 * obj.dec(key);
 * let ret_3: String = obj.get_max_key();
 * let ret_4: String = obj.get_min_key();
 */
```

### Racket

```racket
(define all-one%
  (class object%
    (super-new)
    
    (init-field)
    
    ; inc : string? -> void?
    (define/public (inc key)
      )
    ; dec : string? -> void?
    (define/public (dec key)
      )
    ; get-max-key : -> string?
    (define/public (get-max-key)
      )
    ; get-min-key : -> string?
    (define/public (get-min-key)
      )))

;; Your all-one% object will be instantiated and called as such:
;; (define obj (new all-one%))
;; (send obj inc key)
;; (send obj dec key)
;; (define param_3 (send obj get-max-key))
;; (define param_4 (send obj get-min-key))
```

### Erlang

```erlang
-spec all_one_init_() -> any().
all_one_init_() ->
  .

-spec all_one_inc(Key :: unicode:unicode_binary()) -> any().
all_one_inc(Key) ->
  .

-spec all_one_dec(Key :: unicode:unicode_binary()) -> any().
all_one_dec(Key) ->
  .

-spec all_one_get_max_key() -> unicode:unicode_binary().
all_one_get_max_key() ->
  .

-spec all_one_get_min_key() -> unicode:unicode_binary().
all_one_get_min_key() ->
  .


%% Your functions will be called as such:
%% all_one_init_(),
%% all_one_inc(Key),
%% all_one_dec(Key),
%% Param_3 = all_one_get_max_key(),
%% Param_4 = all_one_get_min_key(),

%% all_one_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule AllOne do
  @spec init_() :: any
  def init_() do
    
  end

  @spec inc(key :: String.t) :: any
  def inc(key) do
    
  end

  @spec dec(key :: String.t) :: any
  def dec(key) do
    
  end

  @spec get_max_key() :: String.t
  def get_max_key() do
    
  end

  @spec get_min_key() :: String.t
  def get_min_key() do
    
  end
end

# Your functions will be called as such:
# AllOne.init_()
# AllOne.inc(key)
# AllOne.dec(key)
# param_3 = AllOne.get_max_key()
# param_4 = AllOne.get_min_key()

# AllOne.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class AllOne {
    init() {

    }
    
    func inc(key: String): Unit {

    }
    
    func dec(key: String): Unit {

    }
    
    func getMaxKey(): String {

    }
    
    func getMinKey(): String {

    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj: AllOne = AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * let param_3 = obj.getMaxKey()
 * let param_4 = obj.getMinKey()
 */
```

