# 599. 两个列表的最小索引总和

## 题目描述

<p>假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。</p>

<p>你需要帮助他们用<strong>最少的索引和</strong>找出他们<strong>共同喜爱的餐厅</strong>。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
<strong>输出:</strong> ["Shogun"]
<strong>解释:</strong> 他们唯一共同喜爱的餐厅是“Shogun”。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong>list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"]
<strong>输出:</strong> ["Shogun"]
<strong>解释:</strong> 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= list1.length, list2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= list1[i].length, list2[i].length &lt;= 30</code>&nbsp;</li>
	<li><code>list1[i]</code> 和 <code>list2[i]</code> 由空格<meta charset="UTF-8" />&nbsp;<code>' '</code>&nbsp;和英文字母组成。</li>
	<li><code>list1</code> 的所有字符串都是 <strong>唯一</strong> 的。</li>
	<li><code>list2</code> 中的所有字符串都是 <strong>唯一</strong> 的。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["Shogun","Tapioca Express","Burger King","KFC"]
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
["Shogun","Tapioca Express","Burger King","KFC"]
["KFC","Shogun","Burger King"]
["happy","sad","good"]
["sad","happy","good"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    
};
```

### TypeScript

```typescript
function findRestaurant(list1: string[], list2: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $list1
     * @param String[] $list2
     * @return String[]
     */
    function findRestaurant($list1, $list2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRestaurant(_ list1: [String], _ list2: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRestaurant(list1: Array<String>, list2: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findRestaurant(List<String> list1, List<String> list2) {
    
  }
}
```

### Go

```golang
func findRestaurant(list1 []string, list2 []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} list1
# @param {String[]} list2
# @return {String[]}
def find_restaurant(list1, list2)
    
end
```

### Scala

```scala
object Solution {
    def findRestaurant(list1: Array[String], list2: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_restaurant(list1: Vec<String>, list2: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-restaurant list1 list2)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_restaurant(List1 :: [unicode:unicode_binary()], List2 :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_restaurant(List1, List2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_restaurant(list1 :: [String.t], list2 :: [String.t]) :: [String.t]
  def find_restaurant(list1, list2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRestaurant(list1: Array<String>, list2: Array<String>): Array<String> {

    }
}
```

