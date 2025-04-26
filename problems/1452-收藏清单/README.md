# 1452. 收藏清单

## 题目描述

<p>给你一个数组 <code>favoriteCompanies</code> ，其中 <code>favoriteCompanies[i]</code> 是第 <code>i</code> 名用户收藏的公司清单（<strong>下标从 0 开始</strong>）。</p>

<p>请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标<em>。</em>下标需要按升序排列<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>favoriteCompanies = [[&quot;leetcode&quot;,&quot;google&quot;,&quot;facebook&quot;],[&quot;google&quot;,&quot;microsoft&quot;],[&quot;google&quot;,&quot;facebook&quot;],[&quot;google&quot;],[&quot;amazon&quot;]]
<strong>输出：</strong>[0,1,4] 
<strong>解释：</strong>
favoriteCompanies[2]=[&quot;google&quot;,&quot;facebook&quot;] 是 favoriteCompanies[0]=[&quot;leetcode&quot;,&quot;google&quot;,&quot;facebook&quot;] 的子集。
favoriteCompanies[3]=[&quot;google&quot;] 是 favoriteCompanies[0]=[&quot;leetcode&quot;,&quot;google&quot;,&quot;facebook&quot;] 和 favoriteCompanies[1]=[&quot;google&quot;,&quot;microsoft&quot;] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>favoriteCompanies = [[&quot;leetcode&quot;,&quot;google&quot;,&quot;facebook&quot;],[&quot;leetcode&quot;,&quot;amazon&quot;],[&quot;facebook&quot;,&quot;google&quot;]]
<strong>输出：</strong>[0,1] 
<strong>解释：</strong>favoriteCompanies[2]=[&quot;facebook&quot;,&quot;google&quot;] 是 favoriteCompanies[0]=[&quot;leetcode&quot;,&quot;google&quot;,&quot;facebook&quot;] 的子集，因此，答案为 [0,1] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>favoriteCompanies = [[&quot;leetcode&quot;],[&quot;google&quot;],[&quot;facebook&quot;],[&quot;amazon&quot;]]
<strong>输出：</strong>[0,1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;favoriteCompanies.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;favoriteCompanies[i].length &lt;= 500</code></li>
	<li><code>1 &lt;=&nbsp;favoriteCompanies[i][j].length &lt;= 20</code></li>
	<li><code>favoriteCompanies[i]</code> 中的所有字符串 <strong>各不相同</strong> 。</li>
	<li>用户收藏的公司清单也 <strong>各不相同</strong> ，也就是说，即便我们按字母顺序排序每个清单， <code>favoriteCompanies[i] != favoriteCompanies[j] </code>仍然成立。</li>
	<li>所有字符串仅包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Use hashing to convert company names in numbers and then for each list check if this is a subset of any other list.
2. In order to check if a list is a subset of another list, use two pointers technique to get a linear solution for this task. The total complexity will be O(n^2 * m) where n is the number of lists and m is the maximum number of elements in a list.

## 示例

```
[["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
[["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
[["leetcode"],["google"],["facebook"],["amazon"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> peopleIndexes(vector<vector<string>>& favoriteCompanies) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        
    }
}
```

### Python

```python
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* peopleIndexes(char*** favoriteCompanies, int favoriteCompaniesSize, int* favoriteCompaniesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> PeopleIndexes(IList<IList<string>> favoriteCompanies) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} favoriteCompanies
 * @return {number[]}
 */
var peopleIndexes = function(favoriteCompanies) {
    
};
```

### TypeScript

```typescript
function peopleIndexes(favoriteCompanies: string[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $favoriteCompanies
     * @return Integer[]
     */
    function peopleIndexes($favoriteCompanies) {
        
    }
}
```

### Swift

```swift
class Solution {
    func peopleIndexes(_ favoriteCompanies: [[String]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun peopleIndexes(favoriteCompanies: List<List<String>>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> peopleIndexes(List<List<String>> favoriteCompanies) {
    
  }
}
```

### Go

```golang
func peopleIndexes(favoriteCompanies [][]string) []int {
    
}
```

### Ruby

```ruby
# @param {String[][]} favorite_companies
# @return {Integer[]}
def people_indexes(favorite_companies)
    
end
```

### Scala

```scala
object Solution {
    def peopleIndexes(favoriteCompanies: List[List[String]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn people_indexes(favorite_companies: Vec<Vec<String>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (people-indexes favoriteCompanies)
  (-> (listof (listof string?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec people_indexes(FavoriteCompanies :: [[unicode:unicode_binary()]]) -> [integer()].
people_indexes(FavoriteCompanies) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec people_indexes(favorite_companies :: [[String.t]]) :: [integer]
  def people_indexes(favorite_companies) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func peopleIndexes(favoriteCompanies: ArrayList<ArrayList<String>>): ArrayList<Int64> {

    }
}
```

