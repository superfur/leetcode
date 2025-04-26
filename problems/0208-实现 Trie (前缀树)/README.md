# 208. 实现 Trie (前缀树)

## 题目描述

<p><strong><a href="https://baike.baidu.com/item/字典树/9825209?fr=aladdin" target="_blank">Trie</a></strong>（发音类似 "try"）或者说 <strong>前缀树</strong> 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。</p>

<p>请你实现 Trie 类：</p>

<ul>
	<li><code>Trie()</code> 初始化前缀树对象。</li>
	<li><code>void insert(String word)</code> 向前缀树中插入字符串 <code>word</code> 。</li>
	<li><code>boolean search(String word)</code> 如果字符串 <code>word</code> 在前缀树中，返回 <code>true</code>（即，在检索之前已经插入）；否则，返回 <code>false</code> 。</li>
	<li><code>boolean startsWith(String prefix)</code> 如果之前已经插入的字符串&nbsp;<code>word</code> 的前缀之一为 <code>prefix</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>输出</strong>
[null, null, true, false, true, null, true]

<strong>解释</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length, prefix.length &lt;= 2000</code></li>
	<li><code>word</code> 和 <code>prefix</code> 仅由小写英文字母组成</li>
	<li><code>insert</code>、<code>search</code> 和 <code>startsWith</code> 调用次数 <strong>总计</strong> 不超过 <code>3 * 10<sup>4</sup></code> 次</li>
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
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
```

## 示例代码

### C++

```cpp
class Trie {
public:
    Trie() {
        
    }
    
    void insert(string word) {
        
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

### Java

```java
class Trie {

    public Trie() {
        
    }
    
    public void insert(String word) {
        
    }
    
    public boolean search(String word) {
        
    }
    
    public boolean startsWith(String prefix) {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

### Python

```python
class Trie(object):

    def __init__(self):
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

### Python3

```python3
class Trie:

    def __init__(self):
        

    def insert(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

### C

```c



typedef struct {
    
} Trie;


Trie* trieCreate() {
    
}

void trieInsert(Trie* obj, char* word) {
    
}

bool trieSearch(Trie* obj, char* word) {
    
}

bool trieStartsWith(Trie* obj, char* prefix) {
    
}

void trieFree(Trie* obj) {
    
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/
```

### C#

```csharp
public class Trie {

    public Trie() {
        
    }
    
    public void Insert(string word) {
        
    }
    
    public bool Search(string word) {
        
    }
    
    public bool StartsWith(string prefix) {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */
```

### JavaScript

```javascript

var Trie = function() {
    
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

### TypeScript

```typescript
class Trie {
    constructor() {
        
    }

    insert(word: string): void {
        
    }

    search(word: string): boolean {
        
    }

    startsWith(prefix: string): boolean {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

### PHP

```php
class Trie {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $word
     * @return NULL
     */
    function insert($word) {
        
    }
  
    /**
     * @param String $word
     * @return Boolean
     */
    function search($word) {
        
    }
  
    /**
     * @param String $prefix
     * @return Boolean
     */
    function startsWith($prefix) {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * $obj = Trie();
 * $obj->insert($word);
 * $ret_2 = $obj->search($word);
 * $ret_3 = $obj->startsWith($prefix);
 */
```

### Swift

```swift

class Trie {

    init() {
        
    }
    
    func insert(_ word: String) {
        
    }
    
    func search(_ word: String) -> Bool {
        
    }
    
    func startsWith(_ prefix: String) -> Bool {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie()
 * obj.insert(word)
 * let ret_2: Bool = obj.search(word)
 * let ret_3: Bool = obj.startsWith(prefix)
 */
```

### Kotlin

```kotlin
class Trie() {

    fun insert(word: String) {
        
    }

    fun search(word: String): Boolean {
        
    }

    fun startsWith(prefix: String): Boolean {
        
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

### Dart

```dart
class Trie {

  Trie() {
    
  }
  
  void insert(String word) {
    
  }
  
  bool search(String word) {
    
  }
  
  bool startsWith(String prefix) {
    
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = Trie();
 * obj.insert(word);
 * bool param2 = obj.search(word);
 * bool param3 = obj.startsWith(prefix);
 */
```

### Go

```golang
type Trie struct {
    
}


func Constructor() Trie {
    
}


func (this *Trie) Insert(word string)  {
    
}


func (this *Trie) Search(word string) bool {
    
}


func (this *Trie) StartsWith(prefix string) bool {
    
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
```

### Ruby

```ruby
class Trie
    def initialize()
        
    end


=begin
    :type word: String
    :rtype: Void
=end
    def insert(word)
        
    end


=begin
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        
    end


=begin
    :type prefix: String
    :rtype: Boolean
=end
    def starts_with(prefix)
        
    end


end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)
```

### Scala

```scala
class Trie() {

    def insert(word: String): Unit = {
        
    }

    def search(word: String): Boolean = {
        
    }

    def startsWith(prefix: String): Boolean = {
        
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * val obj = new Trie()
 * obj.insert(word)
 * val param_2 = obj.search(word)
 * val param_3 = obj.startsWith(prefix)
 */
```

### Rust

```rust
struct Trie {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    fn new() -> Self {
        
    }
    
    fn insert(&self, word: String) {
        
    }
    
    fn search(&self, word: String) -> bool {
        
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
```

### Racket

```racket
(define trie%
  (class object%
    (super-new)
    
    (init-field)
    
    ; insert : string? -> void?
    (define/public (insert word)
      )
    ; search : string? -> boolean?
    (define/public (search word)
      )
    ; starts-with : string? -> boolean?
    (define/public (starts-with prefix)
      )))

;; Your trie% object will be instantiated and called as such:
;; (define obj (new trie%))
;; (send obj insert word)
;; (define param_2 (send obj search word))
;; (define param_3 (send obj starts-with prefix))
```

### Erlang

```erlang
-spec trie_init_() -> any().
trie_init_() ->
  .

-spec trie_insert(Word :: unicode:unicode_binary()) -> any().
trie_insert(Word) ->
  .

-spec trie_search(Word :: unicode:unicode_binary()) -> boolean().
trie_search(Word) ->
  .

-spec trie_starts_with(Prefix :: unicode:unicode_binary()) -> boolean().
trie_starts_with(Prefix) ->
  .


%% Your functions will be called as such:
%% trie_init_(),
%% trie_insert(Word),
%% Param_2 = trie_search(Word),
%% Param_3 = trie_starts_with(Prefix),

%% trie_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Trie do
  @spec init_() :: any
  def init_() do
    
  end

  @spec insert(word :: String.t) :: any
  def insert(word) do
    
  end

  @spec search(word :: String.t) :: boolean
  def search(word) do
    
  end

  @spec starts_with(prefix :: String.t) :: boolean
  def starts_with(prefix) do
    
  end
end

# Your functions will be called as such:
# Trie.init_()
# Trie.insert(word)
# param_2 = Trie.search(word)
# param_3 = Trie.starts_with(prefix)

# Trie.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Trie {
    init() {

    }
    
    func insert(word: String): Unit {

    }
    
    func search(word: String): Bool {

    }
    
    func startsWith(prefix: String): Bool {

    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj: Trie = Trie()
 * obj.insert(word)
 * let param_2 = obj.search(word)
 * let param_3 = obj.startsWith(prefix)
 */
```

