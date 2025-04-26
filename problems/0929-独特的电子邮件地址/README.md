# 929. 独特的电子邮件地址

## 题目描述

<p>每个 <strong>有效电子邮件地址</strong> 都由一个 <strong>本地名</strong> 和一个 <strong>域名</strong> 组成，以 <code>'@'</code> 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个&nbsp;<code>'.'</code> 或 <code>'+'</code> 。</p>

<ul>
	<li>例如，在&nbsp;<code>alice@leetcode.com</code>中，&nbsp;<code>alice</code>&nbsp;是 <strong>本地名</strong> ，而&nbsp;<code>leetcode.com</code>&nbsp;是 <strong>域名</strong> 。</li>
</ul>

<p>如果在电子邮件地址的<strong> 本地名 </strong>部分中的某些字符之间添加句点（<code>'.'</code>），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则 <strong>不适用于域名</strong> 。</p>

<ul>
	<li>例如，<code>"alice.z@leetcode.com”</code> 和 <code>“alicez@leetcode.com”</code>&nbsp;会转发到同一电子邮件地址。</li>
</ul>

<p>如果在<strong> 本地名 </strong>中添加加号（<code>'+'</code>），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则 <strong>不适用于域名</strong> 。</p>

<ul>
	<li>例如 <code>m.y+name@email.com</code> 将转发到 <code>my@email.com</code>。</li>
</ul>

<p>可以同时使用这两个规则。</p>

<p>给你一个字符串数组 <code>emails</code>，我们会向每个 <code>emails[i]</code> 发送一封电子邮件。返回实际收到邮件的不同地址数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
<strong>输出：</strong>2
<strong>解释：</strong>实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
<strong>输出：</strong>3
</pre>

<p><br />
<strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= emails.length &lt;= 100</code></li>
	<li><code>1 &lt;= emails[i].length&nbsp;&lt;= 100</code></li>
	<li><code>emails[i]</code> 由小写英文字母、<code>'+'</code>、<code>'.'</code> 和 <code>'@'</code> 组成</li>
	<li>每个 <code>emails[i]</code> 都包含有且仅有一个 <code>'@'</code> 字符</li>
	<li>所有本地名和域名都不为空</li>
	<li>本地名不会以 <code>'+'</code> 字符作为开头</li>
	<li>域名以&nbsp;<code>".com"</code> 后缀结尾。</li>
	<li>域名在&nbsp;<code>".com"</code> 后缀前至少包含一个字符</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        
    }
};
```

### Java

```java
class Solution {
    public int numUniqueEmails(String[] emails) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
```

### C

```c
int numUniqueEmails(char** emails, int emailsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumUniqueEmails(string[] emails) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    
};
```

### TypeScript

```typescript
function numUniqueEmails(emails: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $emails
     * @return Integer
     */
    function numUniqueEmails($emails) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numUniqueEmails(_ emails: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numUniqueEmails(List<String> emails) {
    
  }
}
```

### Go

```golang
func numUniqueEmails(emails []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} emails
# @return {Integer}
def num_unique_emails(emails)
    
end
```

### Scala

```scala
object Solution {
    def numUniqueEmails(emails: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-unique-emails emails)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_unique_emails(Emails :: [unicode:unicode_binary()]) -> integer().
num_unique_emails(Emails) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_unique_emails(emails :: [String.t]) :: integer
  def num_unique_emails(emails) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numUniqueEmails(emails: Array<String>): Int64 {

    }
}
```

