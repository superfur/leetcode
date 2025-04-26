# 2227. 加密解密字符串

## 题目描述

<p>给你一个字符数组 <code>keys</code> ，由若干 <strong>互不相同</strong> 的字符组成。还有一个字符串数组 <code>values</code> ，内含若干长度为 2 的字符串。另给你一个字符串数组 <code>dictionary</code> ，包含解密后所有允许的原字符串。请你设计并实现一个支持加密及解密下标从 <strong>0</strong> 开始字符串的数据结构。</p>

<p>字符串 <strong>加密</strong> 按下述步骤进行：</p>

<ol>
	<li>对字符串中的每个字符 <code>c</code> ，先从 <code>keys</code> 中找出满足 <code>keys[i] == c</code> 的下标 <code>i</code> 。</li>
	<li>在字符串中，用&nbsp;<code>values[i]</code> 替换字符 <code>c</code> 。</li>
</ol>

<p>请注意，如果&nbsp;<code>keys</code> 中不存在字符串中的字符，则无法执行加密过程，返回空字符串 <code>""</code>。</p>

<p>字符串 <strong>解密</strong> 按下述步骤进行：</p>

<ol>
	<li>将字符串每相邻 2 个字符划分为一个子字符串，对于每个子字符串 <code>s</code> ，找出满足 <code>values[i] == s</code> 的一个下标 <code>i</code> 。如果存在多个有效的 <code>i</code> ，从中选择 <strong>任意</strong> 一个。这意味着一个字符串解密可能得到多个解密字符串。</li>
	<li>在字符串中，用 <code>keys[i]</code> 替换 <code>s</code> 。</li>
</ol>

<p>实现 <code>Encrypter</code> 类：</p>

<ul>
	<li><code>Encrypter(char[] keys, String[] values, String[] dictionary)</code> 用 <code>keys</code>、<code>values</code> 和 <code>dictionary</code> 初始化 <code>Encrypter</code> 类。</li>
	<li><code>String encrypt(String word1)</code> 按上述加密过程完成对 <code>word1</code> 的加密，并返回加密后的字符串。</li>
	<li><code>int decrypt(String word2)</code> 统计并返回可以由 <code>word2</code> 解密得到且出现在 <code>dictionary</code> 中的字符串数目。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
<strong>输出：</strong>
[null, "eizfeiam", 2]

<strong>解释：</strong>
Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // 返回 "eizfeiam"。 
&nbsp;                          // 'a' 映射为 "ei"，'b' 映射为 "zf"，'c' 映射为 "ei"，'d' 映射为 "am"。
encrypter.decrypt("eizfeiam"); // return 2. 
                              // "ei" 可以映射为 'a' 或 'c'，"zf" 映射为 'b'，"am" 映射为 'd'。 
                              // 因此，解密后可以得到的字符串是 "abad"，"cbad"，"abcd" 和 "cbcd"。 
                              // 其中 2 个字符串，"abad" 和 "abcd"，在 dictionary 中出现，所以答案是 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= keys.length == values.length &lt;= 26</code></li>
	<li><code>values[i].length == 2</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 100</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li>所有 <code>keys[i]</code> 和 <code>dictionary[i]</code> <strong>互不相同</strong></li>
	<li><code>1 &lt;= word1.length &lt;= 2000</code></li>
	<li><code>1 &lt;= word2.length &lt;= 200</code></li>
	<li>所有 <code>word1[i]</code> 都出现在 <code>keys</code> 中</li>
	<li><code>word2.length</code> 是偶数</li>
	<li><code>keys</code>、<code>values[i]</code>、<code>dictionary[i]</code>、<code>word1</code> 和 <code>word2</code> 只含小写英文字母</li>
	<li>至多调用 <code>encrypt</code> 和 <code>decrypt</code> <strong>总计</strong> <code>200</code> 次</li>
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

1. For encryption, use hashmap to map each char of word1 to its value.
2. For decryption, use trie to prune when necessary.

## 示例

```
["Encrypter","encrypt","decrypt"]
[[["a","b","c","d"],["ei","zf","ei","am"],["abcd","acbd","adbc","badc","dacb","cadb","cbda","abad"]],["abcd"],["eizfeiam"]]
```

## 示例代码

### C++

```cpp
class Encrypter {
public:
    Encrypter(vector<char>& keys, vector<string>& values, vector<string>& dictionary) {
        
    }
    
    string encrypt(string word1) {
        
    }
    
    int decrypt(string word2) {
        
    }
};

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter* obj = new Encrypter(keys, values, dictionary);
 * string param_1 = obj->encrypt(word1);
 * int param_2 = obj->decrypt(word2);
 */
```

### Java

```java
class Encrypter {

    public Encrypter(char[] keys, String[] values, String[] dictionary) {
        
    }
    
    public String encrypt(String word1) {
        
    }
    
    public int decrypt(String word2) {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = new Encrypter(keys, values, dictionary);
 * String param_1 = obj.encrypt(word1);
 * int param_2 = obj.decrypt(word2);
 */
```

### Python

```python
class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
```

### Python3

```python3
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        

    def encrypt(self, word1: str) -> str:
        

    def decrypt(self, word2: str) -> int:
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
```

### C

```c



typedef struct {
    
} Encrypter;


Encrypter* encrypterCreate(char* keys, int keysSize, char** values, int valuesSize, char** dictionary, int dictionarySize) {
    
}

char* encrypterEncrypt(Encrypter* obj, char* word1) {
    
}

int encrypterDecrypt(Encrypter* obj, char* word2) {
    
}

void encrypterFree(Encrypter* obj) {
    
}

/**
 * Your Encrypter struct will be instantiated and called as such:
 * Encrypter* obj = encrypterCreate(keys, keysSize, values, valuesSize, dictionary, dictionarySize);
 * char* param_1 = encrypterEncrypt(obj, word1);
 
 * int param_2 = encrypterDecrypt(obj, word2);
 
 * encrypterFree(obj);
*/
```

### C#

```csharp
public class Encrypter {

    public Encrypter(char[] keys, string[] values, string[] dictionary) {
        
    }
    
    public string Encrypt(string word1) {
        
    }
    
    public int Decrypt(string word2) {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = new Encrypter(keys, values, dictionary);
 * string param_1 = obj.Encrypt(word1);
 * int param_2 = obj.Decrypt(word2);
 */
```

### JavaScript

```javascript
/**
 * @param {character[]} keys
 * @param {string[]} values
 * @param {string[]} dictionary
 */
var Encrypter = function(keys, values, dictionary) {
    
};

/** 
 * @param {string} word1
 * @return {string}
 */
Encrypter.prototype.encrypt = function(word1) {
    
};

/** 
 * @param {string} word2
 * @return {number}
 */
Encrypter.prototype.decrypt = function(word2) {
    
};

/** 
 * Your Encrypter object will be instantiated and called as such:
 * var obj = new Encrypter(keys, values, dictionary)
 * var param_1 = obj.encrypt(word1)
 * var param_2 = obj.decrypt(word2)
 */
```

### TypeScript

```typescript
class Encrypter {
    constructor(keys: string[], values: string[], dictionary: string[]) {
        
    }

    encrypt(word1: string): string {
        
    }

    decrypt(word2: string): number {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * var obj = new Encrypter(keys, values, dictionary)
 * var param_1 = obj.encrypt(word1)
 * var param_2 = obj.decrypt(word2)
 */
```

### PHP

```php
class Encrypter {
    /**
     * @param String[] $keys
     * @param String[] $values
     * @param String[] $dictionary
     */
    function __construct($keys, $values, $dictionary) {
        
    }
  
    /**
     * @param String $word1
     * @return String
     */
    function encrypt($word1) {
        
    }
  
    /**
     * @param String $word2
     * @return Integer
     */
    function decrypt($word2) {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * $obj = Encrypter($keys, $values, $dictionary);
 * $ret_1 = $obj->encrypt($word1);
 * $ret_2 = $obj->decrypt($word2);
 */
```

### Swift

```swift

class Encrypter {

    init(_ keys: [Character], _ values: [String], _ dictionary: [String]) {
        
    }
    
    func encrypt(_ word1: String) -> String {
        
    }
    
    func decrypt(_ word2: String) -> Int {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * let obj = Encrypter(keys, values, dictionary)
 * let ret_1: String = obj.encrypt(word1)
 * let ret_2: Int = obj.decrypt(word2)
 */
```

### Kotlin

```kotlin
class Encrypter(keys: CharArray, values: Array<String>, dictionary: Array<String>) {

    fun encrypt(word1: String): String {
        
    }

    fun decrypt(word2: String): Int {
        
    }

}

/**
 * Your Encrypter object will be instantiated and called as such:
 * var obj = Encrypter(keys, values, dictionary)
 * var param_1 = obj.encrypt(word1)
 * var param_2 = obj.decrypt(word2)
 */
```

### Dart

```dart
class Encrypter {

  Encrypter(List<String> keys, List<String> values, List<String> dictionary) {
    
  }
  
  String encrypt(String word1) {
    
  }
  
  int decrypt(String word2) {
    
  }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = Encrypter(keys, values, dictionary);
 * String param1 = obj.encrypt(word1);
 * int param2 = obj.decrypt(word2);
 */
```

### Go

```golang
type Encrypter struct {
    
}


func Constructor(keys []byte, values []string, dictionary []string) Encrypter {
    
}


func (this *Encrypter) Encrypt(word1 string) string {
    
}


func (this *Encrypter) Decrypt(word2 string) int {
    
}


/**
 * Your Encrypter object will be instantiated and called as such:
 * obj := Constructor(keys, values, dictionary);
 * param_1 := obj.Encrypt(word1);
 * param_2 := obj.Decrypt(word2);
 */
```

### Ruby

```ruby
class Encrypter

=begin
    :type keys: Character[]
    :type values: String[]
    :type dictionary: String[]
=end
    def initialize(keys, values, dictionary)
        
    end


=begin
    :type word1: String
    :rtype: String
=end
    def encrypt(word1)
        
    end


=begin
    :type word2: String
    :rtype: Integer
=end
    def decrypt(word2)
        
    end


end

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter.new(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
```

### Scala

```scala
class Encrypter(_keys: Array[Char], _values: Array[String], _dictionary: Array[String]) {

    def encrypt(word1: String): String = {
        
    }

    def decrypt(word2: String): Int = {
        
    }

}

/**
 * Your Encrypter object will be instantiated and called as such:
 * val obj = new Encrypter(keys, values, dictionary)
 * val param_1 = obj.encrypt(word1)
 * val param_2 = obj.decrypt(word2)
 */
```

### Rust

```rust
struct Encrypter {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Encrypter {

    fn new(keys: Vec<char>, values: Vec<String>, dictionary: Vec<String>) -> Self {
        
    }
    
    fn encrypt(&self, word1: String) -> String {
        
    }
    
    fn decrypt(&self, word2: String) -> i32 {
        
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * let obj = Encrypter::new(keys, values, dictionary);
 * let ret_1: String = obj.encrypt(word1);
 * let ret_2: i32 = obj.decrypt(word2);
 */
```

### Racket

```racket
(define encrypter%
  (class object%
    (super-new)
    
    ; keys : (listof char?)
    ; values : (listof string?)
    ; dictionary : (listof string?)
    (init-field
      keys
      values
      dictionary)
    
    ; encrypt : string? -> string?
    (define/public (encrypt word1)
      )
    ; decrypt : string? -> exact-integer?
    (define/public (decrypt word2)
      )))

;; Your encrypter% object will be instantiated and called as such:
;; (define obj (new encrypter% [keys keys] [values values] [dictionary dictionary]))
;; (define param_1 (send obj encrypt word1))
;; (define param_2 (send obj decrypt word2))
```

### Erlang

```erlang
-spec encrypter_init_(Keys :: [char()], Values :: [unicode:unicode_binary()], Dictionary :: [unicode:unicode_binary()]) -> any().
encrypter_init_(Keys, Values, Dictionary) ->
  .

-spec encrypter_encrypt(Word1 :: unicode:unicode_binary()) -> unicode:unicode_binary().
encrypter_encrypt(Word1) ->
  .

-spec encrypter_decrypt(Word2 :: unicode:unicode_binary()) -> integer().
encrypter_decrypt(Word2) ->
  .


%% Your functions will be called as such:
%% encrypter_init_(Keys, Values, Dictionary),
%% Param_1 = encrypter_encrypt(Word1),
%% Param_2 = encrypter_decrypt(Word2),

%% encrypter_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Encrypter do
  @spec init_(keys :: [char], values :: [String.t], dictionary :: [String.t]) :: any
  def init_(keys, values, dictionary) do
    
  end

  @spec encrypt(word1 :: String.t) :: String.t
  def encrypt(word1) do
    
  end

  @spec decrypt(word2 :: String.t) :: integer
  def decrypt(word2) do
    
  end
end

# Your functions will be called as such:
# Encrypter.init_(keys, values, dictionary)
# param_1 = Encrypter.encrypt(word1)
# param_2 = Encrypter.decrypt(word2)

# Encrypter.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Encrypter {
    init(keys: Array<Rune>, values: Array<String>, dictionary: Array<String>) {

    }
    
    func encrypt(word1: String): String {

    }
    
    func decrypt(word2: String): Int64 {

    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * let obj: Encrypter = Encrypter(keys, values, dictionary)
 * let param_1 = obj.encrypt(word1)
 * let param_2 = obj.decrypt(word2)
 */
```

