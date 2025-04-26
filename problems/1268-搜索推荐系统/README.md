# 1268. 搜索推荐系统

## 题目描述

<p>给你一个产品数组&nbsp;<code>products</code>&nbsp;和一个字符串&nbsp;<code>searchWord</code>&nbsp;，<code>products</code>&nbsp; 数组中每个产品都是一个字符串。</p>

<p>请你设计一个推荐系统，在依次输入单词&nbsp;<code>searchWord</code> 的每一个字母后，推荐&nbsp;<code>products</code> 数组中前缀与&nbsp;<code>searchWord</code> 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。</p>

<p>请你以二维列表的形式，返回在输入&nbsp;<code>searchWord</code>&nbsp;每个字母后相应的推荐产品的列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>products = [&quot;mobile&quot;,&quot;mouse&quot;,&quot;moneypot&quot;,&quot;monitor&quot;,&quot;mousepad&quot;], searchWord = &quot;mouse&quot;
<strong>输出：</strong>[
[&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;],
[&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;]
]
<strong>解释：</strong>按字典序排序后的产品列表是 [&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;,&quot;mouse&quot;,&quot;mousepad&quot;]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 [&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;]
输入 mou， mous 和 mouse 后系统都返回 [&quot;mouse&quot;,&quot;mousepad&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>products = [&quot;havana&quot;], searchWord = &quot;havana&quot;
<strong>输出：</strong>[[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;]]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>products = [&quot;bags&quot;,&quot;baggage&quot;,&quot;banner&quot;,&quot;box&quot;,&quot;cloths&quot;], searchWord = &quot;bags&quot;
<strong>输出：</strong>[[&quot;baggage&quot;,&quot;bags&quot;,&quot;banner&quot;],[&quot;baggage&quot;,&quot;bags&quot;,&quot;banner&quot;],[&quot;baggage&quot;,&quot;bags&quot;],[&quot;bags&quot;]]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>products = [&quot;havana&quot;], searchWord = &quot;tatiana&quot;
<strong>输出：</strong>[[],[],[],[],[],[],[]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= products.length &lt;= 1000</code></li>
	<li><code>1 &lt;= &Sigma; products[i].length &lt;= 2 * 10^4</code></li>
	<li><code>products[i]</code>&nbsp;中所有的字符都是小写英文字母。</li>
	<li><code>1 &lt;= searchWord.length &lt;= 1000</code></li>
	<li><code>searchWord</code>&nbsp;中所有字符都是小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 字符串
- 二分查找
- 排序
- 堆（优先队列）

## 提示

1. Brute force is a good choice because length of the string is ≤ 1000.
2. Binary search the answer.
3. Use Trie data structure to store the best three matching. Traverse the Trie.

## 示例

```
["mobile","mouse","moneypot","monitor","mousepad"]
"mouse"
["havana"]
"havana"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        
    }
}
```

### Python

```python
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** suggestedProducts(char** products, int productsSize, char* searchWord, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function(products, searchWord) {
    
};
```

### TypeScript

```typescript
function suggestedProducts(products: string[], searchWord: string): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $products
     * @param String $searchWord
     * @return String[][]
     */
    function suggestedProducts($products, $searchWord) {
        
    }
}
```

### Swift

```swift
class Solution {
    func suggestedProducts(_ products: [String], _ searchWord: String) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun suggestedProducts(products: Array<String>, searchWord: String): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> suggestedProducts(List<String> products, String searchWord) {
    
  }
}
```

### Go

```golang
func suggestedProducts(products []string, searchWord string) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[]} products
# @param {String} search_word
# @return {String[][]}
def suggested_products(products, search_word)
    
end
```

### Scala

```scala
object Solution {
    def suggestedProducts(products: Array[String], searchWord: String): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn suggested_products(products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (suggested-products products searchWord)
  (-> (listof string?) string? (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec suggested_products(Products :: [unicode:unicode_binary()], SearchWord :: unicode:unicode_binary()) -> [[unicode:unicode_binary()]].
suggested_products(Products, SearchWord) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec suggested_products(products :: [String.t], search_word :: String.t) :: [[String.t]]
  def suggested_products(products, search_word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func suggestedProducts(products: Array<String>, searchWord: String): ArrayList<ArrayList<String>> {

    }
}
```

