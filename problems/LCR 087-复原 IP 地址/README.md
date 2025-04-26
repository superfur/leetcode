# LCR 087. 复原 IP 地址

## 题目描述

<p>给定一个只包含数字的字符串 <code>s</code> ，用以表示一个 IP 地址，返回所有可能从&nbsp;<code>s</code> 获得的 <strong>有效 IP 地址 </strong>。你可以按任何顺序返回答案。</p>

<p><strong>有效 IP 地址</strong> 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>&#39;.&#39;</code> 分隔。</p>

<p>例如：&quot;0.1.2.201&quot; 和 &quot;192.168.1.1&quot; 是 <strong>有效</strong> IP 地址，但是 &quot;0.011.255.245&quot;、&quot;192.168.1.312&quot; 和 &quot;192.168@1.1&quot; 是 <strong>无效</strong> IP 地址。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;25525511135&quot;
<strong>输出：</strong>[&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;0000&quot;
<strong>输出：</strong>[&quot;0.0.0.0&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;1111&quot;
<strong>输出：</strong>[&quot;1.1.1.1&quot;]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;010010&quot;
<strong>输出：</strong>[&quot;0.10.0.10&quot;,&quot;0.100.1.0&quot;]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;10203040&quot;
<strong>输出：</strong>[&quot;10.20.30.40&quot;,&quot;102.0.30.40&quot;,&quot;10.203.0.40&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 93&nbsp;题相同：<a href="https://leetcode-cn.com/problems/restore-ip-addresses/">https://leetcode-cn.com/problems/restore-ip-addresses/</a>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串
- 回溯

## 示例

```
"25525511135"
"0000"
"1111"
"010010"
"101023"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {

    }
};
```

### Java

```java
class Solution {
    public List<String> restoreIpAddresses(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
```

### Python3

```python3
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** restoreIpAddresses(char * s, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public IList<string> RestoreIpAddresses(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {

};
```

### TypeScript

```typescript
function restoreIpAddresses(s: string): string[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function restoreIpAddresses($s) {

    }
}
```

### Swift

```swift
class Solution {
    func restoreIpAddresses(_ s: String) -> [String] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun restoreIpAddresses(s: String): List<String> {

    }
}
```

### Go

```golang
func restoreIpAddresses(s string) []string {

}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def restore_ip_addresses(s)

end
```

### Scala

```scala
object Solution {
    def restoreIpAddresses(s: String): List[String] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn restore_ip_addresses(s: String) -> Vec<String> {

    }
}
```

### Racket

```racket
(define/contract (restore-ip-addresses s)
  (-> string? (listof string?))

  )
```

### Erlang

```erlang
-spec restore_ip_addresses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
restore_ip_addresses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec restore_ip_addresses(s :: String.t) :: [String.t]
  def restore_ip_addresses(s) do

  end
end
```

