# 745. 前缀和后缀搜索

## 题目描述

<p>设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。</p>

<p>实现 <code>WordFilter</code> 类：</p>

<ul>
	<li><code>WordFilter(string[] words)</code> 使用词典中的单词 <code>words</code> 初始化对象。</li>
	<li><code>f(string pref, string suff)</code> 返回词典中具有前缀&nbsp;<code>pref</code>&nbsp;和后缀 <code>suff</code>&nbsp;的单词的下标。如果存在不止一个满足要求的下标，返回其中 <strong>最大的下标</strong> 。如果不存在这样的单词，返回 <code>-1</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong>输出</strong>
[null, 0]
<strong>解释</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suffix = "e" 。
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 7</code></li>
	<li><code>1 &lt;= pref.length, suff.length &lt;= 7</code></li>
	<li><code>words[i]</code>、<code>pref</code> 和 <code>suff</code> 仅由小写英文字母组成</li>
	<li>最多对函数 <code>f</code> 执行 <code>10<sup>4</sup></code> 次调用</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. Take "apple" as an example, we will insert add "apple{apple", "pple{apple", "ple{apple", "le{apple", "e{apple", "{apple" into the Trie Tree.
2. If the query is: prefix = "app", suffix = "le", we can find it by querying our trie for
"le { app".
3. We use '{' because in ASCii Table, '{' is next to 'z', so we just need to create new TrieNode[27] instead of 26. Also, compared with traditional Trie, we add the attribute weight in class TrieNode.
You can still choose any different character.

## 示例

```
["WordFilter","f"]
[[["apple"]],["a","e"]]
```

## 示例代码

### C++

```cpp
class WordFilter {
public:
    WordFilter(vector<string>& words) {
        
    }
    
    int f(string pref, string suff) {
        
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(pref,suff);
 */
```

### Java

```java
class WordFilter {

    public WordFilter(String[] words) {
        
    }
    
    public int f(String pref, String suff) {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(pref,suff);
 */
```

### Python

```python
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
```

### Python3

```python3
class WordFilter:

    def __init__(self, words: List[str]):
        

    def f(self, pref: str, suff: str) -> int:
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
```

### C

```c



typedef struct {
    
} WordFilter;


WordFilter* wordFilterCreate(char** words, int wordsSize) {
    
}

int wordFilterF(WordFilter* obj, char* pref, char* suff) {
    
}

void wordFilterFree(WordFilter* obj) {
    
}

/**
 * Your WordFilter struct will be instantiated and called as such:
 * WordFilter* obj = wordFilterCreate(words, wordsSize);
 * int param_1 = wordFilterF(obj, pref, suff);
 
 * wordFilterFree(obj);
*/
```

### C#

```csharp
public class WordFilter {

    public WordFilter(string[] words) {
        
    }
    
    public int F(string pref, string suff) {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.F(pref,suff);
 */
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 */
var WordFilter = function(words) {
    
};

/** 
 * @param {string} pref 
 * @param {string} suff
 * @return {number}
 */
WordFilter.prototype.f = function(pref, suff) {
    
};

/** 
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```

### TypeScript

```typescript
class WordFilter {
    constructor(words: string[]) {
        
    }

    f(pref: string, suff: string): number {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```

### PHP

```php
class WordFilter {
    /**
     * @param String[] $words
     */
    function __construct($words) {
        
    }
  
    /**
     * @param String $pref
     * @param String $suff
     * @return Integer
     */
    function f($pref, $suff) {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * $obj = WordFilter($words);
 * $ret_1 = $obj->f($pref, $suff);
 */
```

### Swift

```swift

class WordFilter {

    init(_ words: [String]) {
        
    }
    
    func f(_ pref: String, _ suff: String) -> Int {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter(words)
 * let ret_1: Int = obj.f(pref, suff)
 */
```

### Kotlin

```kotlin
class WordFilter(words: Array<String>) {

    fun f(pref: String, suff: String): Int {
        
    }

}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```

### Dart

```dart
class WordFilter {

  WordFilter(List<String> words) {
    
  }
  
  int f(String pref, String suff) {
    
  }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = WordFilter(words);
 * int param1 = obj.f(pref,suff);
 */
```

### Go

```golang
type WordFilter struct {
    
}


func Constructor(words []string) WordFilter {
    
}


func (this *WordFilter) F(pref string, suff string) int {
    
}


/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(pref,suff);
 */
```

### Ruby

```ruby
class WordFilter

=begin
    :type words: String[]
=end
    def initialize(words)
        
    end


=begin
    :type pref: String
    :type suff: String
    :rtype: Integer
=end
    def f(pref, suff)
        
    end


end

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter.new(words)
# param_1 = obj.f(pref, suff)
```

### Scala

```scala
class WordFilter(_words: Array[String]) {

    def f(pref: String, suff: String): Int = {
        
    }

}

/**
 * Your WordFilter object will be instantiated and called as such:
 * val obj = new WordFilter(words)
 * val param_1 = obj.f(pref,suff)
 */
```

### Rust

```rust
struct WordFilter {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordFilter {

    fn new(words: Vec<String>) -> Self {
        
    }
    
    fn f(&self, pref: String, suff: String) -> i32 {
        
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter::new(words);
 * let ret_1: i32 = obj.f(pref, suff);
 */
```

### Racket

```racket
(define word-filter%
  (class object%
    (super-new)
    
    ; words : (listof string?)
    (init-field
      words)
    
    ; f : string? string? -> exact-integer?
    (define/public (f pref suff)
      )))

;; Your word-filter% object will be instantiated and called as such:
;; (define obj (new word-filter% [words words]))
;; (define param_1 (send obj f pref suff))
```

### Erlang

```erlang
-spec word_filter_init_(Words :: [unicode:unicode_binary()]) -> any().
word_filter_init_(Words) ->
  .

-spec word_filter_f(Pref :: unicode:unicode_binary(), Suff :: unicode:unicode_binary()) -> integer().
word_filter_f(Pref, Suff) ->
  .


%% Your functions will be called as such:
%% word_filter_init_(Words),
%% Param_1 = word_filter_f(Pref, Suff),

%% word_filter_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule WordFilter do
  @spec init_(words :: [String.t]) :: any
  def init_(words) do
    
  end

  @spec f(pref :: String.t, suff :: String.t) :: integer
  def f(pref, suff) do
    
  end
end

# Your functions will be called as such:
# WordFilter.init_(words)
# param_1 = WordFilter.f(pref, suff)

# WordFilter.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class WordFilter {
    init(words: Array<String>) {

    }
    
    func f(pref: String, suff: String): Int64 {

    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj: WordFilter = WordFilter(words)
 * let param_1 = obj.f(pref,suff)
 */
```

