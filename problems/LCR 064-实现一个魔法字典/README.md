# LCR 064. 实现一个魔法字典

## 题目描述

<p>设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 <strong>互不相同</strong> 。 如果给出一个单词，请判定能否只将这个单词中<strong>一个</strong>字母换成另一个字母，使得所形成的新单词存在于已构建的神奇字典中。</p>

<p>实现 <code>MagicDictionary</code> 类：</p>

<ul>
	<li><code>MagicDictionary()</code> 初始化对象</li>
	<li><code>void buildDict(String[]&nbsp;dictionary)</code> 使用字符串数组&nbsp;<code>dictionary</code> 设定该数据结构，<code>dictionary</code> 中的字符串互不相同</li>
	<li><code>bool search(String searchWord)</code> 给定一个字符串 <code>searchWord</code> ，判定能否只将字符串中<strong> 一个 </strong>字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>&nbsp;</p>

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
inputs = [&quot;MagicDictionary&quot;, &quot;buildDict&quot;, &quot;search&quot;, &quot;search&quot;, &quot;search&quot;, &quot;search&quot;]
inputs = [[], [[&quot;hello&quot;, &quot;leetcode&quot;]], [&quot;hello&quot;], [&quot;hhllo&quot;], [&quot;hell&quot;], [&quot;leetcoded&quot;]]
<strong>输出</strong>
[null, null, false, true, false, false]

<strong>解释</strong>
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict([&quot;hello&quot;, &quot;leetcode&quot;]);
magicDictionary.search(&quot;hello&quot;); // 返回 False
magicDictionary.search(&quot;hhllo&quot;); // 将第二个 &#39;h&#39; 替换为 &#39;e&#39; 可以匹配 &quot;hello&quot; ，所以返回 True
magicDictionary.search(&quot;hell&quot;); // 返回 False
magicDictionary.search(&quot;leetcoded&quot;); // 返回 False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;dictionary.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code> 仅由小写英文字母组成</li>
	<li><code>dictionary</code> 中的所有字符串 <strong>互不相同</strong></li>
	<li><code>1 &lt;=&nbsp;searchWord.length &lt;= 100</code></li>
	<li><code>searchWord</code> 仅由小写英文字母组成</li>
	<li><code>buildDict</code> 仅在 <code>search</code> 之前调用一次</li>
	<li>最多调用 <code>100</code> 次 <code>search</code></li>
</ul>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 676&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/implement-magic-dictionary/">https://leetcode-cn.com/problems/implement-magic-dictionary/</a></p>


## 难度

Medium

## 标签

- 深度优先搜索
- 设计
- 字典树
- 哈希表
- 字符串

## 示例

```
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
```

## 示例代码

### C++

```cpp
class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {

    }
    
    void buildDict(vector<string> dictionary) {

    }
    
    bool search(string searchWord) {

    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
 */
```

### Java

```java
class MagicDictionary {

    /** Initialize your data structure here. */
    public MagicDictionary() {

    }
    
    public void buildDict(String[] dictionary) {

    }
    
    public boolean search(String searchWord) {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */
```

### Python

```python
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """


    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
```

### Python3

```python3
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def buildDict(self, dictionary: List[str]) -> None:


    def search(self, searchWord: str) -> bool:



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
```

### C

```c



typedef struct {
    
} MagicDictionary;

/** Initialize your data structure here. */

MagicDictionary* magicDictionaryCreate() {
    
}

void magicDictionaryBuildDict(MagicDictionary* obj, char ** dictionary, int dictionarySize) {
  
}

bool magicDictionarySearch(MagicDictionary* obj, char * searchWord) {
  
}

void magicDictionaryFree(MagicDictionary* obj) {
    
}

/**
 * Your MagicDictionary struct will be instantiated and called as such:
 * MagicDictionary* obj = magicDictionaryCreate();
 * magicDictionaryBuildDict(obj, dictionary, dictionarySize);
 
 * bool param_2 = magicDictionarySearch(obj, searchWord);
 
 * magicDictionaryFree(obj);
*/
```

### C#

```csharp
public class MagicDictionary {

    /** Initialize your data structure here. */
    public MagicDictionary() {

    }
    
    public void BuildDict(string[] dictionary) {

    }
    
    public bool Search(string searchWord) {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.BuildDict(dictionary);
 * bool param_2 = obj.Search(searchWord);
 */
```

### JavaScript

```javascript
/**
 * Initialize your data structure here.
 */
var MagicDictionary = function() {

};

/** 
 * @param {string[]} dictionary
 * @return {void}
 */
MagicDictionary.prototype.buildDict = function(dictionary) {

};

/** 
 * @param {string} searchWord
 * @return {boolean}
 */
MagicDictionary.prototype.search = function(searchWord) {

};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

### TypeScript

```typescript
class MagicDictionary {
    constructor() {

    }

    buildDict(dictionary: string[]): void {

    }

    search(searchWord: string): boolean {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

### PHP

```php
class MagicDictionary {
    /**
     * Initialize your data structure here.
     */
    function __construct() {

    }

    /**
     * @param String[] $dictionary
     * @return NULL
     */
    function buildDict($dictionary) {

    }

    /**
     * @param String $searchWord
     * @return Boolean
     */
    function search($searchWord) {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * $obj = MagicDictionary();
 * $obj->buildDict($dictionary);
 * $ret_2 = $obj->search($searchWord);
 */
```

### Swift

```swift

class MagicDictionary {

    /** Initialize your data structure here. */
    init() {

    }
    
    func buildDict(_ dictionary: [String]) {

    }
    
    func search(_ searchWord: String) -> Bool {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary()
 * obj.buildDict(dictionary)
 * let ret_2: Bool = obj.search(searchWord)
 */
```

### Kotlin

```kotlin
class MagicDictionary() {

    /** Initialize your data structure here. */


    fun buildDict(dictionary: Array<String>) {

    }

    fun search(searchWord: String): Boolean {

    }

}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

### Go

```golang
type MagicDictionary struct {

}


/** Initialize your data structure here. */
func Constructor() MagicDictionary {

}


func (this *MagicDictionary) BuildDict(dictionary []string)  {

}


func (this *MagicDictionary) Search(searchWord string) bool {

}


/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
 */
```

### Ruby

```ruby
class MagicDictionary

=begin
    Initialize your data structure here.
=end
    def initialize()

    end


=begin
    :type dictionary: String[]
    :rtype: Void
=end
    def build_dict(dictionary)

    end


=begin
    :type search_word: String
    :rtype: Boolean
=end
    def search(search_word)

    end


end

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary.new()
# obj.build_dict(dictionary)
# param_2 = obj.search(search_word)
```

### Scala

```scala
class MagicDictionary() {

    /** Initialize your data structure here. */


    def buildDict(dictionary: Array[String]) {

    }

    def search(searchWord: String): Boolean = {

    }

}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

### Rust

```rust
struct MagicDictionary {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MagicDictionary {

    /** Initialize your data structure here. */
    fn new() -> Self {

    }
    
    fn build_dict(&self, dictionary: Vec<String>) {

    }
    
    fn search(&self, search_word: String) -> bool {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary::new();
 * obj.build_dict(dictionary);
 * let ret_2: bool = obj.search(searchWord);
 */
```

### Racket

```racket
(define magic-dictionary%
  (class object%
    (super-new)
    (init-field)
    
    ; build-dict : (listof string?) -> void?
    (define/public (build-dict dictionary)

      )
    ; search : string? -> boolean?
    (define/public (search searchWord)

      )))

;; Your magic-dictionary% object will be instantiated and called as such:
;; (define obj (new magic-dictionary%))
;; (send obj build-dict dictionary)
;; (define param_2 (send obj search search-word))
```

### Erlang

```erlang
-spec magic_dictionary_init_() -> any().
magic_dictionary_init_() ->
  .

-spec magic_dictionary_build_dict(Dictionary :: [unicode:unicode_binary()]) -> any().
magic_dictionary_build_dict(Dictionary) ->
  .

-spec magic_dictionary_search(SearchWord :: unicode:unicode_binary()) -> boolean().
magic_dictionary_search(SearchWord) ->
  .


%% Your functions will be called as such:
%% magic_dictionary_init_(),
%% magic_dictionary_build_dict(Dictionary),
%% Param_2 = magic_dictionary_search(SearchWord),

%% magic_dictionary_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MagicDictionary do
  @spec init_() :: any
  def init_() do

  end

  @spec build_dict(dictionary :: [String.t]) :: any
  def build_dict(dictionary) do

  end

  @spec search(search_word :: String.t) :: boolean
  def search(search_word) do

  end
end

# Your functions will be called as such:
# MagicDictionary.init_()
# MagicDictionary.build_dict(dictionary)
# param_2 = MagicDictionary.search(search_word)

# MagicDictionary.init_ will be called before every test case, in which you can do some necessary initializations.
```

