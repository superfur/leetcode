# 535. TinyURL 的加密与解密

## 题目描述

<p>TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL&nbsp;<code>https://leetcode.com/problems/design-tinyurl</code>&nbsp;时，它将返回一个简化的URL&nbsp;<code>http://tinyurl.com/4e9iAk</code> 。请你设计一个类来加密与解密 TinyURL 。</p>

<p>加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。</p>

<p>实现 <code>Solution</code> 类：</p>

<div class="original__bRMd">
<div>
<ul>
	<li><code>Solution()</code> 初始化 TinyURL 系统对象。</li>
	<li><code>String encode(String longUrl)</code> 返回 <code>longUrl</code> 对应的 TinyURL 。</li>
	<li><code>String decode(String shortUrl)</code> 返回 <code>shortUrl</code> 原本的 URL 。题目数据保证给定的 <code>shortUrl</code> 是由同一个系统对象加密的。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>url = "https://leetcode.com/problems/design-tinyurl"
<strong>输出：</strong>"https://leetcode.com/problems/design-tinyurl"

<strong>解释：</strong>
Solution obj = new Solution();
string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。
string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= url.length &lt;= 10<sup>4</sup></code></li>
	<li>题目数据保证 <code>url</code> 是一个有效的 URL</li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 字符串
- 哈希函数

## 示例

```
"https://leetcode.com/problems/design-tinyurl"
```

## 示例代码

### C++

```cpp
class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
```

### Java

```java
public class Codec {

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
```

### Python

```python
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

### Python3

```python3
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

### C

```c
/** Encodes a URL to a shortened URL. */
char* encode(char* longUrl) {
    
}

/** Decodes a shortened URL to its original URL. */
char* decode(char* shortUrl) {
    
}

// Your functions will be called as such:
// char* s = encode(s);
// decode(s);
```

### C#

```csharp
public class Codec {

    // Encodes a URL to a shortened URL
    public string encode(string longUrl) {
        
    }

    // Decodes a shortened URL to its original URL.
    public string decode(string shortUrl) {
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
```

### JavaScript

```javascript
/**
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */
```

### TypeScript

```typescript
/**
 * Encodes a URL to a shortened URL.
 */
function encode(longUrl: string): string {
	
};

/**
 * Decodes a shortened URL to its original URL.
 */
function decode(shortUrl: string): string {
	
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */
```

### PHP

```php
class Codec {
    /**
     * Encodes a URL to a shortened URL.
     * @param String $longUrl
     * @return String
     */
    function encode($longUrl) {
        
    }
    
    /**
     * Decodes a shortened URL to its original URL.
     * @param String $shortUrl
     * @return String
     */
    function decode($shortUrl) {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * $obj = Codec();
 * $s = $obj->encode($longUrl);
 * $ans = $obj->decode($s);
 */
```

### Swift

```swift
class Codec {
    // Encodes a URL to a shortened URL.
    func encode(_ longUrl: String) -> String {
        
    }
    
    // Decodes a shortened URL to its original URL.
    func decode(_ shortUrl: String) -> String {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec()
 * val s = obj.encode(longUrl)
 * let ans = obj.decode(s)
*/
```

### Kotlin

```kotlin
class Codec() {
    // Encodes a URL to a shortened URL.
    fun encode(longUrl: String): String {
        
    }

    // Decodes a shortened URL to its original URL.
    fun decode(shortUrl: String): String {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var obj = Codec()
 * var url = obj.encode(longUrl)
 * var ans = obj.decode(url)
 */
```

### Go

```golang
type Codec struct {
    
}


func Constructor() Codec {
    
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
    
}


/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
```

### Ruby

```ruby
# Encodes a URL to a shortened URL.
#
# @param {string} longUrl
# @return {string}
def encode(longUrl)
    
end

# Decodes a shortened URL to its original URL.
#
# @param {string} shortUrl
# @return {string}
def decode(shortUrl)
    
end


# Your functions will be called as such:
# decode(encode(url))
```

### Scala

```scala
class Codec {
    // Encodes a URL to a shortened URL.
    def encode(longURL: String): String = {
        
    }
    
    // Decodes a shortened URL to its original URL.
    def decode(shortURL: String): String = {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var obj = new Codec()
 * val s = obj.encode(longURL)
 * val ans = obj.decode(s)
 */
```

### Rust

```rust
struct Codec {
	
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        
    }
	
    // Encodes a URL to a shortened URL.
    fn encode(&self, longURL: String) -> String {
        
    }
	
    // Decodes a shortened URL to its original URL.
    fn decode(&self, shortURL: String) -> String {
        
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let s: String = obj.encode(strs);
 * let ans: VecVec<String> = obj.decode(s);
 */
```

