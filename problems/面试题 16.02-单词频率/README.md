# 面试题 16.02. 单词频率

## 题目描述

<p>设计一个方法，找出任意指定单词在一本书中的出现频率。</p>

<p>你的实现应该支持如下操作：</p>

<ul>
	<li><code>WordsFrequency(book)</code>构造函数，参数为字符串数组构成的一本书</li>
	<li><code>get(word)</code>查询指定单词在书中出现的频率</li>
</ul>

<p><strong>示例：</strong></p>

<pre>WordsFrequency wordsFrequency = new WordsFrequency({&quot;i&quot;, &quot;have&quot;, &quot;an&quot;, &quot;apple&quot;, &quot;he&quot;, &quot;have&quot;, &quot;a&quot;, &quot;pen&quot;});
wordsFrequency.get(&quot;you&quot;); //返回0，&quot;you&quot;没有出现过
wordsFrequency.get(&quot;have&quot;); //返回2，&quot;have&quot;出现2次
wordsFrequency.get(&quot;an&quot;); //返回1
wordsFrequency.get(&quot;apple&quot;); //返回1
wordsFrequency.get(&quot;pen&quot;); //返回1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>book[i]</code>中只包含小写字母</li>
	<li><code>1 &lt;= book.length &lt;= 100000</code></li>
	<li><code>1 &lt;= book[i].length &lt;= 10</code></li>
	<li><code>get</code>函数的调用次数不会超过100000</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. 想想这个问题的最佳运行时间是多少。如果你的解法匹配最理想的运行时间，那么你可能无法做的更好了。
2. 可以使用散列表来优化重复的情况吗？

## 示例

```
["WordsFrequency","get","get","get","get","get"]
[[["i","have","an","apple","he","have","a","pen"]],["you"],["have"],["an"],["apple"],["pen"]]
```

## 示例代码

### C++

```cpp
class WordsFrequency {
public:
    WordsFrequency(vector<string>& book) {
        
    }
    
    int get(string word) {
        
    }
};

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency* obj = new WordsFrequency(book);
 * int param_1 = obj->get(word);
 */
```

### Java

```java
class WordsFrequency {

    public WordsFrequency(String[] book) {
        
    }
    
    public int get(String word) {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = new WordsFrequency(book);
 * int param_1 = obj.get(word);
 */
```

### Python

```python
class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        

    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
```

### Python3

```python3
class WordsFrequency:

    def __init__(self, book: List[str]):
        

    def get(self, word: str) -> int:
        


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
```

### C

```c



typedef struct {
    
} WordsFrequency;


WordsFrequency* wordsFrequencyCreate(char** book, int bookSize) {
    
}

int wordsFrequencyGet(WordsFrequency* obj, char* word) {
    
}

void wordsFrequencyFree(WordsFrequency* obj) {
    
}

/**
 * Your WordsFrequency struct will be instantiated and called as such:
 * WordsFrequency* obj = wordsFrequencyCreate(book, bookSize);
 * int param_1 = wordsFrequencyGet(obj, word);
 
 * wordsFrequencyFree(obj);
*/
```

### C#

```csharp
public class WordsFrequency {

    public WordsFrequency(string[] book) {
        
    }
    
    public int Get(string word) {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = new WordsFrequency(book);
 * int param_1 = obj.Get(word);
 */
```

### JavaScript

```javascript
/**
 * @param {string[]} book
 */
var WordsFrequency = function(book) {
    
};

/** 
 * @param {string} word
 * @return {number}
 */
WordsFrequency.prototype.get = function(word) {
    
};

/** 
 * Your WordsFrequency object will be instantiated and called as such:
 * var obj = new WordsFrequency(book)
 * var param_1 = obj.get(word)
 */
```

### TypeScript

```typescript
class WordsFrequency {
    constructor(book: string[]) {
        
    }

    get(word: string): number {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * var obj = new WordsFrequency(book)
 * var param_1 = obj.get(word)
 */
```

### PHP

```php
class WordsFrequency {
    /**
     * @param String[] $book
     */
    function __construct($book) {
        
    }
  
    /**
     * @param String $word
     * @return Integer
     */
    function get($word) {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * $obj = WordsFrequency($book);
 * $ret_1 = $obj->get($word);
 */
```

### Swift

```swift

class WordsFrequency {

    init(_ book: [String]) {
        
    }
    
    func get(_ word: String) -> Int {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * let obj = WordsFrequency(book)
 * let ret_1: Int = obj.get(word)
 */
```

### Kotlin

```kotlin
class WordsFrequency(book: Array<String>) {

    fun get(word: String): Int {
        
    }

}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * var obj = WordsFrequency(book)
 * var param_1 = obj.get(word)
 */
```

### Dart

```dart
class WordsFrequency {

  WordsFrequency(List<String> book) {
    
  }
  
  int get(String word) {
    
  }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = WordsFrequency(book);
 * int param1 = obj.get(word);
 */
```

### Go

```golang
type WordsFrequency struct {
    
}


func Constructor(book []string) WordsFrequency {
    
}


func (this *WordsFrequency) Get(word string) int {
    
}


/**
 * Your WordsFrequency object will be instantiated and called as such:
 * obj := Constructor(book);
 * param_1 := obj.Get(word);
 */
```

### Ruby

```ruby
class WordsFrequency

=begin
    :type book: String[]
=end
    def initialize(book)
        
    end


=begin
    :type word: String
    :rtype: Integer
=end
    def get(word)
        
    end


end

# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency.new(book)
# param_1 = obj.get(word)
```

### Scala

```scala
class WordsFrequency(_book: Array[String]) {

    def get(word: String): Int = {
        
    }

}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * val obj = new WordsFrequency(book)
 * val param_1 = obj.get(word)
 */
```

### Rust

```rust
struct WordsFrequency {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordsFrequency {

    fn new(book: Vec<String>) -> Self {
        
    }
    
    fn get(&self, word: String) -> i32 {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * let obj = WordsFrequency::new(book);
 * let ret_1: i32 = obj.get(word);
 */
```

### Racket

```racket
(define words-frequency%
  (class object%
    (super-new)
    
    ; book : (listof string?)
    (init-field
      book)
    
    ; get : string? -> exact-integer?
    (define/public (get word)
      )))

;; Your words-frequency% object will be instantiated and called as such:
;; (define obj (new words-frequency% [book book]))
;; (define param_1 (send obj get word))
```

### Erlang

```erlang
-spec words_frequency_init_(Book :: [unicode:unicode_binary()]) -> any().
words_frequency_init_(Book) ->
  .

-spec words_frequency_get(Word :: unicode:unicode_binary()) -> integer().
words_frequency_get(Word) ->
  .


%% Your functions will be called as such:
%% words_frequency_init_(Book),
%% Param_1 = words_frequency_get(Word),

%% words_frequency_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule WordsFrequency do
  @spec init_(book :: [String.t]) :: any
  def init_(book) do
    
  end

  @spec get(word :: String.t) :: integer
  def get(word) do
    
  end
end

# Your functions will be called as such:
# WordsFrequency.init_(book)
# param_1 = WordsFrequency.get(word)

# WordsFrequency.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class WordsFrequency {
    init(book: Array<String>) {

    }
    
    func get(word: String): Int64 {

    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * let obj: WordsFrequency = WordsFrequency(book)
 * let param_1 = obj.get(word)
 */
```

