# 211. 添加与搜索单词 - 数据结构设计

## 题目描述

<p>请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。</p>

<p>实现词典类 <code>WordDictionary</code> ：</p>

<ul>
	<li><code>WordDictionary()</code> 初始化词典对象</li>
	<li><code>void addWord(word)</code> 将 <code>word</code> 添加到数据结构中，之后可以对它进行匹配</li>
	<li><code>bool search(word)</code> 如果数据结构中存在字符串与&nbsp;<code>word</code> 匹配，则返回 <code>true</code> ；否则，返回&nbsp; <code>false</code> 。<code>word</code> 中可能包含一些 <code>'.'</code> ，每个&nbsp;<code>.</code> 都可以表示任何一个字母。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
<strong>输出：</strong>
[null,null,null,null,false,true,true,true]

<strong>解释：</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // 返回 False
wordDictionary.search("bad"); // 返回 True
wordDictionary.search(".ad"); // 返回 True
wordDictionary.search("b.."); // 返回 True
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 25</code></li>
	<li><code>addWord</code> 中的 <code>word</code> 由小写英文字母组成</li>
	<li><code>search</code> 中的 <code>word</code> 由 '.' 或小写英文字母组成</li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>addWord</code> 和 <code>search</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 设计
- 字典树
- 字符串

## 提示

1. You should be familiar with how a Trie works. If not, please work on this problem: <a href="https://leetcode.com/problems/implement-trie-prefix-tree/">Implement Trie (Prefix Tree)</a> first.

## 示例

```
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
```

## 示例代码

### C++

```cpp
class WordDictionary {
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        
    }
    
    bool search(string word) {
        
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

### Java

```java
class WordDictionary {

    public WordDictionary() {
        
    }
    
    public void addWord(String word) {
        
    }
    
    public boolean search(String word) {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
```

### Python

```python
class WordDictionary(object):

    def __init__(self):
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

### Python3

```python3
class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

### C

```c



typedef struct {
    
} WordDictionary;


WordDictionary* wordDictionaryCreate() {
    
}

void wordDictionaryAddWord(WordDictionary* obj, char* word) {
    
}

bool wordDictionarySearch(WordDictionary* obj, char* word) {
    
}

void wordDictionaryFree(WordDictionary* obj) {
    
}

/**
 * Your WordDictionary struct will be instantiated and called as such:
 * WordDictionary* obj = wordDictionaryCreate();
 * wordDictionaryAddWord(obj, word);
 
 * bool param_2 = wordDictionarySearch(obj, word);
 
 * wordDictionaryFree(obj);
*/
```

### C#

```csharp
public class WordDictionary {

    public WordDictionary() {
        
    }
    
    public void AddWord(string word) {
        
    }
    
    public bool Search(string word) {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.AddWord(word);
 * bool param_2 = obj.Search(word);
 */
```

### JavaScript

```javascript

var WordDictionary = function() {
    
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

### TypeScript

```typescript
class WordDictionary {
    constructor() {
        
    }

    addWord(word: string): void {
        
    }

    search(word: string): boolean {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

### PHP

```php
class WordDictionary {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $word
     * @return NULL
     */
    function addWord($word) {
        
    }
  
    /**
     * @param String $word
     * @return Boolean
     */
    function search($word) {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * $obj = WordDictionary();
 * $obj->addWord($word);
 * $ret_2 = $obj->search($word);
 */
```

### Swift

```swift

class WordDictionary {

    init() {
        
    }
    
    func addWord(_ word: String) {
        
    }
    
    func search(_ word: String) -> Bool {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary()
 * obj.addWord(word)
 * let ret_2: Bool = obj.search(word)
 */
```

### Kotlin

```kotlin
class WordDictionary() {

    fun addWord(word: String) {
        
    }

    fun search(word: String): Boolean {
        
    }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

### Dart

```dart
class WordDictionary {

  WordDictionary() {
    
  }
  
  void addWord(String word) {
    
  }
  
  bool search(String word) {
    
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = WordDictionary();
 * obj.addWord(word);
 * bool param2 = obj.search(word);
 */
```

### Go

```golang
type WordDictionary struct {
    
}


func Constructor() WordDictionary {
    
}


func (this *WordDictionary) AddWord(word string)  {
    
}


func (this *WordDictionary) Search(word string) bool {
    
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
```

### Ruby

```ruby
class WordDictionary
    def initialize()
        
    end


=begin
    :type word: String
    :rtype: Void
=end
    def add_word(word)
        
    end


=begin
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        
    end


end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary.new()
# obj.add_word(word)
# param_2 = obj.search(word)
```

### Scala

```scala
class WordDictionary() {

    def addWord(word: String): Unit = {
        
    }

    def search(word: String): Boolean = {
        
    }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * val obj = new WordDictionary()
 * obj.addWord(word)
 * val param_2 = obj.search(word)
 */
```

### Rust

```rust
struct WordDictionary {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    fn new() -> Self {
        
    }
    
    fn add_word(&self, word: String) {
        
    }
    
    fn search(&self, word: String) -> bool {
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */
```

### Racket

```racket
(define word-dictionary%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add-word : string? -> void?
    (define/public (add-word word)
      )
    ; search : string? -> boolean?
    (define/public (search word)
      )))

;; Your word-dictionary% object will be instantiated and called as such:
;; (define obj (new word-dictionary%))
;; (send obj add-word word)
;; (define param_2 (send obj search word))
```

### Erlang

```erlang
-spec word_dictionary_init_() -> any().
word_dictionary_init_() ->
  .

-spec word_dictionary_add_word(Word :: unicode:unicode_binary()) -> any().
word_dictionary_add_word(Word) ->
  .

-spec word_dictionary_search(Word :: unicode:unicode_binary()) -> boolean().
word_dictionary_search(Word) ->
  .


%% Your functions will be called as such:
%% word_dictionary_init_(),
%% word_dictionary_add_word(Word),
%% Param_2 = word_dictionary_search(Word),

%% word_dictionary_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule WordDictionary do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add_word(word :: String.t) :: any
  def add_word(word) do
    
  end

  @spec search(word :: String.t) :: boolean
  def search(word) do
    
  end
end

# Your functions will be called as such:
# WordDictionary.init_()
# WordDictionary.add_word(word)
# param_2 = WordDictionary.search(word)

# WordDictionary.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class WordDictionary {
    init() {

    }
    
    func addWord(word: String): Unit {

    }
    
    func search(word: String): Bool {

    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj: WordDictionary = WordDictionary()
 * obj.addWord(word)
 * let param_2 = obj.search(word)
 */
```

