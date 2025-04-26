# 811. 子域名访问计数

## 题目描述

<p>网站域名 <code>"discuss.leetcode.com"</code> 由多个子域名组成。顶级域名为 <code>"com"</code> ，二级域名为 <code>"leetcode.com"</code> ，最低一级为 <code>"discuss.leetcode.com"</code> 。当访问域名 <code>"discuss.leetcode.com"</code> 时，同时也会隐式访问其父域名 <code>"leetcode.com" </code>以及 <code>"com"</code> 。</p>

<p><strong>计数配对域名</strong> 是遵循 <code>"rep d1.d2.d3"</code> 或 <code>"rep d1.d2"</code> 格式的一个域名表示，其中 <code>rep</code> 表示访问域名的次数，<code>d1.d2.d3</code> 为域名本身。</p>

<ul>
	<li>例如，<code>"9001 discuss.leetcode.com"</code> 就是一个 <strong>计数配对域名</strong> ，表示 <code>discuss.leetcode.com</code> 被访问了 <code>9001</code> 次。</li>
</ul>

<p>给你一个<strong> 计数配对域名 </strong>组成的数组 <code>cpdomains</code> ，解析得到输入中每个子域名对应的&nbsp;<strong>计数配对域名</strong> ，并以数组形式返回。可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cpdomains = ["9001 discuss.leetcode.com"]
<strong>输出：</strong>["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
<strong>解释：</strong>例子中仅包含一个网站域名："discuss.leetcode.com"。
按照前文描述，子域名 "leetcode.com" 和 "com" 都会被访问，所以它们都被访问了 9001 次。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
<strong>输出：</strong>["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
<strong>解释：</strong>按照前文描述，会访问 "google.mail.com" 900 次，"yahoo.com" 50 次，"intel.mail.com" 1 次，"wiki.org" 5 次。
而对于父域名，会访问 "mail.com" 900 + 1 = 901 次，"com" 900 + 50 + 1 = 951 次，和 "org" 5 次。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cpdomain.length &lt;= 100</code></li>
	<li><code>1 &lt;= cpdomain[i].length &lt;= 100</code></li>
	<li><code>cpdomain[i]</code> 会遵循 <code>"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>.d3<sub>i</sub>"</code> 或 <code>"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>"</code> 格式</li>
	<li><code>rep<sub>i</sub></code> 是范围 <code>[1, 10<sup>4</sup>]</code> 内的一个整数</li>
	<li><code>d1<sub>i</sub></code>、<code>d2<sub>i</sub></code> 和 <code>d3<sub>i</sub></code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 示例

```
["9001 discuss.leetcode.com"]
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** subdomainVisits(char** cpdomains, int cpdomainsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> SubdomainVisits(string[] cpdomains) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    
};
```

### TypeScript

```typescript
function subdomainVisits(cpdomains: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $cpdomains
     * @return String[]
     */
    function subdomainVisits($cpdomains) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subdomainVisits(_ cpdomains: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subdomainVisits(cpdomains: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> subdomainVisits(List<String> cpdomains) {
    
  }
}
```

### Go

```golang
func subdomainVisits(cpdomains []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} cpdomains
# @return {String[]}
def subdomain_visits(cpdomains)
    
end
```

### Scala

```scala
object Solution {
    def subdomainVisits(cpdomains: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subdomain_visits(cpdomains: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (subdomain-visits cpdomains)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec subdomain_visits(Cpdomains :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
subdomain_visits(Cpdomains) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subdomain_visits(cpdomains :: [String.t]) :: [String.t]
  def subdomain_visits(cpdomains) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subdomainVisits(cpdomains: Array<String>): ArrayList<String> {

    }
}
```

