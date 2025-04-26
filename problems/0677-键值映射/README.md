# 677. 键值映射

## 题目描述

<p>设计一个 map ，满足以下几点:</p>

<ul>
	<li>字符串表示键，整数表示值</li>
	<li>返回具有前缀等于给定字符串的键的值的总和</li>
</ul>

<p>实现一个 <code>MapSum</code> 类：</p>

<ul>
	<li><code>MapSum()</code> 初始化 <code>MapSum</code> 对象</li>
	<li><code>void insert(String key, int val)</code> 插入 <code>key-val</code> 键值对，字符串表示键 <code>key</code> ，整数表示值 <code>val</code> 。如果键 <code>key</code> 已经存在，那么原来的键值对&nbsp;<code>key-value</code>&nbsp;将被替代成新的键值对。</li>
	<li><code>int sum(string prefix)</code> 返回所有以该前缀 <code>prefix</code> 开头的键 <code>key</code> 的值的总和。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
<strong>输出：</strong>
[null, null, 3, null, 5]

<strong>解释：</strong>
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // 返回 3 (<u>ap</u>ple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // 返回 5 (<u>ap</u>ple + <u>ap</u>p = 3 + 2 = 5)
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= key.length, prefix.length &lt;= 50</code></li>
	<li><code>key</code> 和 <code>prefix</code> 仅由小写英文字母组成</li>
	<li><code>1 &lt;= val &lt;= 1000</code></li>
	<li>最多调用 <code>50</code> 次 <code>insert</code> 和 <code>sum</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 字典树
- 哈希表
- 字符串

## 示例

```
["MapSum","insert","sum","insert","sum"]
[[],["apple",3],["ap"],["app",2],["ap"]]
```

## 示例代码

### C++

```cpp
class MapSum {
public:
    MapSum() {
        
    }
    
    void insert(string key, int val) {
        
    }
    
    int sum(string prefix) {
        
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```

### Java

```java
class MapSum {

    public MapSum() {
        
    }
    
    public void insert(String key, int val) {
        
    }
    
    public int sum(String prefix) {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```

### Python

```python
class MapSum(object):

    def __init__(self):
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

### Python3

```python3
class MapSum:

    def __init__(self):
        

    def insert(self, key: str, val: int) -> None:
        

    def sum(self, prefix: str) -> int:
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

### C

```c



typedef struct {
    
} MapSum;


MapSum* mapSumCreate() {
    
}

void mapSumInsert(MapSum* obj, char* key, int val) {
    
}

int mapSumSum(MapSum* obj, char* prefix) {
    
}

void mapSumFree(MapSum* obj) {
    
}

/**
 * Your MapSum struct will be instantiated and called as such:
 * MapSum* obj = mapSumCreate();
 * mapSumInsert(obj, key, val);
 
 * int param_2 = mapSumSum(obj, prefix);
 
 * mapSumFree(obj);
*/
```

### C#

```csharp
public class MapSum {

    public MapSum() {
        
    }
    
    public void Insert(string key, int val) {
        
    }
    
    public int Sum(string prefix) {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.Insert(key,val);
 * int param_2 = obj.Sum(prefix);
 */
```

### JavaScript

```javascript

var MapSum = function() {
    
};

/** 
 * @param {string} key 
 * @param {number} val
 * @return {void}
 */
MapSum.prototype.insert = function(key, val) {
    
};

/** 
 * @param {string} prefix
 * @return {number}
 */
MapSum.prototype.sum = function(prefix) {
    
};

/** 
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
```

### TypeScript

```typescript
class MapSum {
    constructor() {
        
    }

    insert(key: string, val: number): void {
        
    }

    sum(prefix: string): number {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
```

### PHP

```php
class MapSum {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $key
     * @param Integer $val
     * @return NULL
     */
    function insert($key, $val) {
        
    }
  
    /**
     * @param String $prefix
     * @return Integer
     */
    function sum($prefix) {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * $obj = MapSum();
 * $obj->insert($key, $val);
 * $ret_2 = $obj->sum($prefix);
 */
```

### Swift

```swift

class MapSum {

    init() {
        
    }
    
    func insert(_ key: String, _ val: Int) {
        
    }
    
    func sum(_ prefix: String) -> Int {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * let obj = MapSum()
 * obj.insert(key, val)
 * let ret_2: Int = obj.sum(prefix)
 */
```

### Kotlin

```kotlin
class MapSum() {

    fun insert(key: String, `val`: Int) {
        
    }

    fun sum(prefix: String): Int {
        
    }

}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = MapSum()
 * obj.insert(key,`val`)
 * var param_2 = obj.sum(prefix)
 */
```

### Dart

```dart
class MapSum {

  MapSum() {
    
  }
  
  void insert(String key, int val) {
    
  }
  
  int sum(String prefix) {
    
  }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = MapSum();
 * obj.insert(key,val);
 * int param2 = obj.sum(prefix);
 */
```

### Go

```golang
type MapSum struct {
    
}


func Constructor() MapSum {
    
}


func (this *MapSum) Insert(key string, val int)  {
    
}


func (this *MapSum) Sum(prefix string) int {
    
}


/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
```

### Ruby

```ruby
class MapSum
    def initialize()
        
    end


=begin
    :type key: String
    :type val: Integer
    :rtype: Void
=end
    def insert(key, val)
        
    end


=begin
    :type prefix: String
    :rtype: Integer
=end
    def sum(prefix)
        
    end


end

# Your MapSum object will be instantiated and called as such:
# obj = MapSum.new()
# obj.insert(key, val)
# param_2 = obj.sum(prefix)
```

### Scala

```scala
class MapSum() {

    def insert(key: String, `val`: Int): Unit = {
        
    }

    def sum(prefix: String): Int = {
        
    }

}

/**
 * Your MapSum object will be instantiated and called as such:
 * val obj = new MapSum()
 * obj.insert(key,`val`)
 * val param_2 = obj.sum(prefix)
 */
```

### Rust

```rust
struct MapSum {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MapSum {

    fn new() -> Self {
        
    }
    
    fn insert(&self, key: String, val: i32) {
        
    }
    
    fn sum(&self, prefix: String) -> i32 {
        
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * let obj = MapSum::new();
 * obj.insert(key, val);
 * let ret_2: i32 = obj.sum(prefix);
 */
```

### Racket

```racket
(define map-sum%
  (class object%
    (super-new)
    
    (init-field)
    
    ; insert : string? exact-integer? -> void?
    (define/public (insert key val)
      )
    ; sum : string? -> exact-integer?
    (define/public (sum prefix)
      )))

;; Your map-sum% object will be instantiated and called as such:
;; (define obj (new map-sum%))
;; (send obj insert key val)
;; (define param_2 (send obj sum prefix))
```

### Erlang

```erlang
-spec map_sum_init_() -> any().
map_sum_init_() ->
  .

-spec map_sum_insert(Key :: unicode:unicode_binary(), Val :: integer()) -> any().
map_sum_insert(Key, Val) ->
  .

-spec map_sum_sum(Prefix :: unicode:unicode_binary()) -> integer().
map_sum_sum(Prefix) ->
  .


%% Your functions will be called as such:
%% map_sum_init_(),
%% map_sum_insert(Key, Val),
%% Param_2 = map_sum_sum(Prefix),

%% map_sum_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MapSum do
  @spec init_() :: any
  def init_() do
    
  end

  @spec insert(key :: String.t, val :: integer) :: any
  def insert(key, val) do
    
  end

  @spec sum(prefix :: String.t) :: integer
  def sum(prefix) do
    
  end
end

# Your functions will be called as such:
# MapSum.init_()
# MapSum.insert(key, val)
# param_2 = MapSum.sum(prefix)

# MapSum.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MapSum {
    init() {

    }
    
    func insert(key: String, val: Int64): Unit {

    }
    
    func sum(prefix: String): Int64 {

    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * let obj: MapSum = MapSum()
 * obj.insert(key,val)
 * let param_2 = obj.sum(prefix)
 */
```

