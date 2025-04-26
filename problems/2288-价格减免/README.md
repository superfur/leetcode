# 2288. 价格减免

## 题目描述

<p><strong>句子</strong> 是由若干个单词组成的字符串，单词之间用单个空格分隔，其中每个单词可以包含数字、小写字母、和美元符号 <code>'$'</code> 。如果单词的形式为美元符号后跟着一个非负实数，那么这个单词就表示一个 <strong>价格</strong> 。</p>

<ul>
	<li>例如 <code>"$100"</code>、<code>"$23"</code> 和 <code>"$6"</code> 表示价格，而 <code>"100"</code>、<code>"$"</code> 和 <code>"$1e5</code> 不是。</li>
</ul>

<p>给你一个字符串 <code>sentence</code> 表示一个句子和一个整数 <code>discount</code> 。对于每个表示价格的单词，都在价格的基础上减免 <code>discount%</code> ，并 <strong>更新</strong> 该单词到句子中。所有更新后的价格应该表示为一个 <strong>恰好保留小数点后两位</strong> 的数字。</p>

<p>返回表示修改后句子的字符串。</p>

<p>注意：所有价格 <strong>最多</strong> 为&nbsp;<code>10</code> 位数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50
<strong>输出：</strong>"there are $0.50 $1.00 and 5$ candies in the shop"
<strong>解释：</strong>
表示价格的单词是 "$1" 和 "$2" 。 
- "$1" 减免 50% 为 "$0.50" ，所以 "$1" 替换为 "$0.50" 。
- "$2" 减免 50% 为 "$1" ，所以 "$2" 替换为 "$1.00" 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100
<strong>输出：</strong>"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
<strong>解释：</strong>
任何价格减免 100% 都会得到 0 。
表示价格的单词分别是 "$3"、"$5"、"$6" 和 "$9"。
每个单词都替换为 "$0.00"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 10<sup>5</sup></code></li>
	<li><code>sentence</code> 由小写英文字母、数字、<code>' '</code> 和&nbsp;<code>'$'</code> 组成</li>
	<li><code>sentence</code> 不含前导和尾随空格</li>
	<li><code>sentence</code> 的所有单词都用单个空格分隔</li>
	<li>所有价格都是 <strong>正</strong> 整数且不含前导零</li>
	<li>所有价格 <strong>最多</strong> 为&nbsp; <code>10</code> 位数字</li>
	<li><code>0 &lt;= discount &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 提示

1. Extract each word from the sentence and check if it represents a price.
2. For each price, apply the given discount to it and update it.

## 示例

```
"there are $1 $2 and 5$ candies in the shop"
50
"1 2 $3 4 $5 $6 7 8$ $9 $10$"
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string discountPrices(string sentence, int discount) {
        
    }
};
```

### Java

```java
class Solution {
    public String discountPrices(String sentence, int discount) {
        
    }
}
```

### Python

```python
class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
```

### C

```c
char* discountPrices(char* sentence, int discount) {
    
}
```

### C#

```csharp
public class Solution {
    public string DiscountPrices(string sentence, int discount) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} sentence
 * @param {number} discount
 * @return {string}
 */
var discountPrices = function(sentence, discount) {
    
};
```

### TypeScript

```typescript
function discountPrices(sentence: string, discount: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $sentence
     * @param Integer $discount
     * @return String
     */
    function discountPrices($sentence, $discount) {
        
    }
}
```

### Swift

```swift
class Solution {
    func discountPrices(_ sentence: String, _ discount: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun discountPrices(sentence: String, discount: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String discountPrices(String sentence, int discount) {
    
  }
}
```

### Go

```golang
func discountPrices(sentence string, discount int) string {
    
}
```

### Ruby

```ruby
# @param {String} sentence
# @param {Integer} discount
# @return {String}
def discount_prices(sentence, discount)
    
end
```

### Scala

```scala
object Solution {
    def discountPrices(sentence: String, discount: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn discount_prices(sentence: String, discount: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (discount-prices sentence discount)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec discount_prices(Sentence :: unicode:unicode_binary(), Discount :: integer()) -> unicode:unicode_binary().
discount_prices(Sentence, Discount) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec discount_prices(sentence :: String.t, discount :: integer) :: String.t
  def discount_prices(sentence, discount) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func discountPrices(sentence: String, discount: Int64): String {

    }
}
```

