# 1773. 统计匹配检索规则的物品数量

## 题目描述

<p>给你一个数组 <code>items</code> ，其中 <code>items[i] = [type<sub>i</sub>, color<sub>i</sub>, name<sub>i</sub>]</code> ，描述第 <code>i</code> 件物品的类型、颜色以及名称。</p>

<p>另给你一条由两个字符串 <code>ruleKey</code> 和 <code>ruleValue</code> 表示的检索规则。</p>

<p>如果第 <code>i</code> 件物品能满足下述条件之一，则认为该物品与给定的检索规则 <strong>匹配</strong> ：</p>

<ul>
	<li><code>ruleKey == "type"</code> 且 <code>ruleValue == type<sub>i</sub></code> 。</li>
	<li><code>ruleKey == "color"</code> 且 <code>ruleValue == color<sub>i</sub></code> 。</li>
	<li><code>ruleKey == "name"</code> 且 <code>ruleValue == name<sub>i</sub></code> 。</li>
</ul>

<p>统计并返回 <strong>匹配检索规则的物品数量</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
<strong>输出：</strong>1
<strong>解释：</strong>只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
<strong>输出：</strong>2
<strong>解释：</strong>只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"] 。注意，["computer","silver","phone"] 未匹配检索规则。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= items.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= type<sub>i</sub>.length, color<sub>i</sub>.length, name<sub>i</sub>.length, ruleValue.length <= 10</code></li>
	<li><code>ruleKey</code> 等于 <code>"type"</code>、<code>"color"</code> 或 <code>"name"</code></li>
	<li>所有字符串仅由小写字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Iterate on each item, and check if each one matches the rule according to the statement.

## 示例

```
[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
"color"
"silver"
[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
"type"
"phone"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        
    }
};
```

### Java

```java
class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
```

### C

```c
int countMatches(char*** items, int itemsSize, int* itemsColSize, char* ruleKey, char* ruleValue) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    
};
```

### TypeScript

```typescript
function countMatches(items: string[][], ruleKey: string, ruleValue: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $items
     * @param String $ruleKey
     * @param String $ruleValue
     * @return Integer
     */
    function countMatches($items, $ruleKey, $ruleValue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countMatches(_ items: [[String]], _ ruleKey: String, _ ruleValue: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countMatches(items: List<List<String>>, ruleKey: String, ruleValue: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
    
  }
}
```

### Go

```golang
func countMatches(items [][]string, ruleKey string, ruleValue string) int {
    
}
```

### Ruby

```ruby
# @param {String[][]} items
# @param {String} rule_key
# @param {String} rule_value
# @return {Integer}
def count_matches(items, rule_key, rule_value)
    
end
```

### Scala

```scala
object Solution {
    def countMatches(items: List[List[String]], ruleKey: String, ruleValue: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-matches items ruleKey ruleValue)
  (-> (listof (listof string?)) string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_matches(Items :: [[unicode:unicode_binary()]], RuleKey :: unicode:unicode_binary(), RuleValue :: unicode:unicode_binary()) -> integer().
count_matches(Items, RuleKey, RuleValue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_matches(items :: [[String.t]], rule_key :: String.t, rule_value :: String.t) :: integer
  def count_matches(items, rule_key, rule_value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countMatches(items: ArrayList<ArrayList<String>>, ruleKey: String, ruleValue: String): Int64 {

    }
}
```

