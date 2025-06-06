# 1032. 字符流

## 题目描述

<p>设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 <code>words</code> 中的一个字符串。</p>

<p>例如，<code>words = ["abc", "xyz"]</code> 且字符流中逐个依次加入 4 个字符 <code>'a'</code>、<code>'x'</code>、<code>'y'</code> 和 <code>'z'</code> ，你所设计的算法应当可以检测到&nbsp;<code>"axyz"</code> 的后缀 <code>"xyz"</code> 与&nbsp;<code>words</code> 中的字符串 <code>"xyz"</code> 匹配。</p>

<p>按下述要求实现 <code>StreamChecker</code> 类：</p>

<ul>
	<li><code>StreamChecker(String[] words)</code> ：构造函数，用字符串数组&nbsp;<code>words</code> 初始化数据结构。</li>
	<li><code>boolean query(char letter)</code>：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 <code>words</code> 中的某一字符串，返回 <code>true</code> ；否则，返回 <code>false</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
<strong>输出：</strong>
[null, false, false, false, true, false, true, false, false, false, false, false, true]

<strong>解释：</strong>
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // 返回 False
streamChecker.query("b"); // 返回 False
streamChecker.query("c"); // 返回n False
streamChecker.query("d"); // 返回 True ，因为 'cd' 在 words 中
streamChecker.query("e"); // 返回 False
streamChecker.query("f"); // 返回 True ，因为 'f' 在 words 中
streamChecker.query("g"); // 返回 False
streamChecker.query("h"); // 返回 False
streamChecker.query("i"); // 返回 False
streamChecker.query("j"); // 返回 False
streamChecker.query("k"); // 返回 False
streamChecker.query("l"); // 返回 True ，因为 'kl' 在 words 中
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 2000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 200</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
	<li><code>letter</code> 是一个小写英文字母</li>
	<li>最多调用查询 <code>4 * 10<sup>4</sup></code> 次</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 字典树
- 数组
- 字符串
- 数据流

## 提示

1. Put the words into a trie, and manage a set of pointers within that trie.

## 示例

```
["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]
[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]
```

## 示例代码

### C++

```cpp
class StreamChecker {
public:
    StreamChecker(vector<string>& words) {
        
    }
    
    bool query(char letter) {
        
    }
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */
```

### Java

```java
class StreamChecker {

    public StreamChecker(String[] words) {
        
    }
    
    public boolean query(char letter) {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * boolean param_1 = obj.query(letter);
 */
```

### Python

```python
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```

### Python3

```python3
class StreamChecker:

    def __init__(self, words: List[str]):
        

    def query(self, letter: str) -> bool:
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```

### C

```c



typedef struct {
    
} StreamChecker;


StreamChecker* streamCheckerCreate(char** words, int wordsSize) {
    
}

bool streamCheckerQuery(StreamChecker* obj, char letter) {
    
}

void streamCheckerFree(StreamChecker* obj) {
    
}

/**
 * Your StreamChecker struct will be instantiated and called as such:
 * StreamChecker* obj = streamCheckerCreate(words, wordsSize);
 * bool param_1 = streamCheckerQuery(obj, letter);
 
 * streamCheckerFree(obj);
*/
```

### C#

```csharp
public class StreamChecker {

    public StreamChecker(string[] words) {
        
    }
    
    public bool Query(char letter) {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * bool param_1 = obj.Query(letter);
 */
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 */
var StreamChecker = function(words) {
    
};

/** 
 * @param {character} letter
 * @return {boolean}
 */
StreamChecker.prototype.query = function(letter) {
    
};

/** 
 * Your StreamChecker object will be instantiated and called as such:
 * var obj = new StreamChecker(words)
 * var param_1 = obj.query(letter)
 */
```

### TypeScript

```typescript
class StreamChecker {
    constructor(words: string[]) {
        
    }

    query(letter: string): boolean {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * var obj = new StreamChecker(words)
 * var param_1 = obj.query(letter)
 */
```

### PHP

```php
class StreamChecker {
    /**
     * @param String[] $words
     */
    function __construct($words) {
        
    }
  
    /**
     * @param String $letter
     * @return Boolean
     */
    function query($letter) {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * $obj = StreamChecker($words);
 * $ret_1 = $obj->query($letter);
 */
```

### Swift

```swift

class StreamChecker {

    init(_ words: [String]) {
        
    }
    
    func query(_ letter: Character) -> Bool {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj = StreamChecker(words)
 * let ret_1: Bool = obj.query(letter)
 */
```

### Kotlin

```kotlin
class StreamChecker(words: Array<String>) {

    fun query(letter: Char): Boolean {
        
    }

}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * var obj = StreamChecker(words)
 * var param_1 = obj.query(letter)
 */
```

### Dart

```dart
class StreamChecker {

  StreamChecker(List<String> words) {
    
  }
  
  bool query(String letter) {
    
  }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = StreamChecker(words);
 * bool param1 = obj.query(letter);
 */
```

### Go

```golang
type StreamChecker struct {
    
}


func Constructor(words []string) StreamChecker {
    
}


func (this *StreamChecker) Query(letter byte) bool {
    
}


/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */
```

### Ruby

```ruby
class StreamChecker

=begin
    :type words: String[]
=end
    def initialize(words)
        
    end


=begin
    :type letter: Character
    :rtype: Boolean
=end
    def query(letter)
        
    end


end

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker.new(words)
# param_1 = obj.query(letter)
```

### Scala

```scala
class StreamChecker(_words: Array[String]) {

    def query(letter: Char): Boolean = {
        
    }

}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * val obj = new StreamChecker(words)
 * val param_1 = obj.query(letter)
 */
```

### Rust

```rust
struct StreamChecker {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StreamChecker {

    fn new(words: Vec<String>) -> Self {
        
    }
    
    fn query(&self, letter: char) -> bool {
        
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj = StreamChecker::new(words);
 * let ret_1: bool = obj.query(letter);
 */
```

### Racket

```racket
(define stream-checker%
  (class object%
    (super-new)
    
    ; words : (listof string?)
    (init-field
      words)
    
    ; query : char? -> boolean?
    (define/public (query letter)
      )))

;; Your stream-checker% object will be instantiated and called as such:
;; (define obj (new stream-checker% [words words]))
;; (define param_1 (send obj query letter))
```

### Erlang

```erlang
-spec stream_checker_init_(Words :: [unicode:unicode_binary()]) -> any().
stream_checker_init_(Words) ->
  .

-spec stream_checker_query(Letter :: char()) -> boolean().
stream_checker_query(Letter) ->
  .


%% Your functions will be called as such:
%% stream_checker_init_(Words),
%% Param_1 = stream_checker_query(Letter),

%% stream_checker_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule StreamChecker do
  @spec init_(words :: [String.t]) :: any
  def init_(words) do
    
  end

  @spec query(letter :: char) :: boolean
  def query(letter) do
    
  end
end

# Your functions will be called as such:
# StreamChecker.init_(words)
# param_1 = StreamChecker.query(letter)

# StreamChecker.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class StreamChecker {
    init(words: Array<String>) {

    }
    
    func query(letter: Rune): Bool {

    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj: StreamChecker = StreamChecker(words)
 * let param_1 = obj.query(letter)
 */
```

