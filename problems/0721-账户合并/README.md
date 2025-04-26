# 721. 账户合并

## 题目描述

<p>给定一个列表 <code>accounts</code>，每个元素 <code>accounts[i]</code>&nbsp;是一个字符串列表，其中第一个元素 <code>accounts[i][0]</code>&nbsp;是&nbsp;<em>名称 (name)</em>，其余元素是 <em><strong>emails</strong> </em>表示该账户的邮箱地址。</p>

<p>现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。</p>

<p>合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 <strong>按字符 ASCII 顺序排列</strong> 的邮箱地址。账户本身可以以 <strong>任意顺序</strong> 返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
<b>输出：</b>[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
<b>解释：</b>
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
<strong>输出：</strong>[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= accounts.length &lt;= 1000</code></li>
	<li><code>2 &lt;= accounts[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= accounts[i][j].length &lt;= 30</code></li>
	<li><code>accounts[i][0]</code> 由英文字母组成</li>
	<li><code>accounts[i][j] (for j &gt; 0)</code> 是有效的邮箱地址</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. For every pair of emails in the same account, draw an edge between those emails.  The problem is about enumerating the connected components of this graph.

## 示例

```
[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** accountsMerge(char*** accounts, int accountsSize, int* accountsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> AccountsMerge(IList<IList<string>> accounts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function(accounts) {
    
};
```

### TypeScript

```typescript
function accountsMerge(accounts: string[][]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $accounts
     * @return String[][]
     */
    function accountsMerge($accounts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func accountsMerge(_ accounts: [[String]]) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> accountsMerge(List<List<String>> accounts) {
    
  }
}
```

### Go

```golang
func accountsMerge(accounts [][]string) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[][]} accounts
# @return {String[][]}
def accounts_merge(accounts)
    
end
```

### Scala

```scala
object Solution {
    def accountsMerge(accounts: List[List[String]]): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (accounts-merge accounts)
  (-> (listof (listof string?)) (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec accounts_merge(Accounts :: [[unicode:unicode_binary()]]) -> [[unicode:unicode_binary()]].
accounts_merge(Accounts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec accounts_merge(accounts :: [[String.t]]) :: [[String.t]]
  def accounts_merge(accounts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func accountsMerge(accounts: ArrayList<ArrayList<String>>): ArrayList<ArrayList<String>> {

    }
}
```

