# 1169. 查询无效交易

## 题目描述

<p>如果出现下述两种情况，交易 <strong>可能无效</strong>：</p>

<ul>
	<li>交易金额超过<meta charset="UTF-8" />&nbsp;<code>$1000</code></li>
	<li>或者，它和&nbsp;<strong>另一个城市</strong>&nbsp;中 <strong>同名</strong> 的另一笔交易相隔不超过 <code>60</code> 分钟（包含 60 分钟整）</li>
</ul>

<p>给定字符串数组交易清单<meta charset="UTF-8" />&nbsp;<code>transaction</code>&nbsp;。每个交易字符串&nbsp;<code>transactions[i]</code>&nbsp;由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。</p>

<p>返回&nbsp;<code>transactions</code>，返回可能无效的交易列表。你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
<strong>输出：</strong>["alice,20,800,mtv","alice,50,100,beijing"]
<strong>解释：</strong>第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
<strong>输出：</strong>["alice,50,1200,mtv"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
<strong>输出：</strong>["bob,50,1200,mtv"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>transactions.length &lt;= 1000</code></li>
	<li>每笔交易&nbsp;<code>transactions[i]</code>&nbsp;按&nbsp;<code>"{name},{time},{amount},{city}"</code>&nbsp;的格式进行记录</li>
	<li>每个交易名称&nbsp;<code>{name}</code>&nbsp;和城市&nbsp;<code>{city}</code>&nbsp;都由小写英文字母组成，长度在&nbsp;<code>1</code>&nbsp;到&nbsp;<code>10</code>&nbsp;之间</li>
	<li>每个交易时间&nbsp;<code>{time}</code>&nbsp;由一些数字组成，表示一个&nbsp;<code>0</code>&nbsp;到&nbsp;<code>1000</code>&nbsp;之间的整数</li>
	<li>每笔交易金额&nbsp;<code>{amount}</code>&nbsp;由一些数字组成，表示一个&nbsp;<code>0</code> 到&nbsp;<code>2000</code>&nbsp;之间的整数</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Split each string into four arrays.
2. For each transaction check if it's invalid, you can do this with just a loop with help of the four arrays generated on step 1.
3. At the end you perform O(N ^ 2) operations.

## 示例

```
["alice,20,800,mtv","alice,50,100,beijing"]
["alice,20,800,mtv","alice,50,1200,mtv"]
["alice,20,800,mtv","bob,50,1200,mtv"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> invalidTransactions(vector<string>& transactions) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** invalidTransactions(char** transactions, int transactionsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> InvalidTransactions(string[] transactions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} transactions
 * @return {string[]}
 */
var invalidTransactions = function(transactions) {
    
};
```

### TypeScript

```typescript
function invalidTransactions(transactions: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $transactions
     * @return String[]
     */
    function invalidTransactions($transactions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func invalidTransactions(_ transactions: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun invalidTransactions(transactions: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> invalidTransactions(List<String> transactions) {
    
  }
}
```

### Go

```golang
func invalidTransactions(transactions []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} transactions
# @return {String[]}
def invalid_transactions(transactions)
    
end
```

### Scala

```scala
object Solution {
    def invalidTransactions(transactions: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn invalid_transactions(transactions: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (invalid-transactions transactions)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec invalid_transactions(Transactions :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
invalid_transactions(Transactions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec invalid_transactions(transactions :: [String.t]) :: [String.t]
  def invalid_transactions(transactions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func invalidTransactions(transactions: Array<String>): ArrayList<String> {

    }
}
```

