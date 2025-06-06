# 面试题 17.26. 稀疏相似度

## 题目描述

<p>两个(具有不同单词的)文档的交集(intersection)中元素的个数除以并集(union)中元素的个数，就是这两个文档的相似度。例如，{1, 5, 3} 和 {1, 7, 2, 3} 的相似度是 0.4，其中，交集的元素有 2 个，并集的元素有 5 个。给定一系列的长篇文档，每个文档元素各不相同，并与一个 ID 相关联。它们的相似度非常&ldquo;稀疏&rdquo;，也就是说任选 2 个文档，相似度都很接近 0。请设计一个算法返回每对文档的 ID 及其相似度。只需输出相似度大于 0 的组合。请忽略空文档。为简单起见，可以假定每个文档由一个含有不同整数的数组表示。</p>

<p>输入为一个二维数组 <code>docs</code>，<code>docs[i]</code>&nbsp;表示&nbsp;id 为 <code>i</code> 的文档。返回一个数组，其中每个元素是一个字符串，代表每对相似度大于 0 的文档，其格式为 <code>{id1},{id2}: {similarity}</code>，其中 <code>id1</code> 为两个文档中较小的 id，<code>similarity</code> 为相似度，精确到小数点后 4 位。以任意顺序返回数组均可。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 
<code>[
&nbsp; [14, 15, 100, 9, 3],
&nbsp; [32, 1, 9, 3, 5],
&nbsp; [15, 29, 2, 6, 8, 7],
&nbsp; [7, 10]
]</code>
<strong>输出:</strong>
[
&nbsp; &quot;0,1: 0.2500&quot;,
&nbsp; &quot;0,2: 0.1000&quot;,
&nbsp; &quot;2,3: 0.1429&quot;
]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>docs.length &lt;= 500</code></li>
	<li><code>docs[i].length &lt;= 500</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. 解法1：从一个简单的算法开始，将每个文档依次与其他文档进行比较。你如何尽快计算两个文档的相似度？
2. 解法1：要计算两个文档的相似性，可以尝试用某种方式重新组织数据。排序？使用其他的数据结构?
3. 解法1：你应该能够得到一个O(A+B) 的算法来计算两个文档的相似性。
4. 解法1：交集和并集之间是什么关系？你能用一个计算出另一个吗？
5. 解法1：要理解两个集合的交集和并集的关系，考虑用Venn图（一个圆与另一个圆重叠的图）。
6. 解法2：人们很容易想到一些小的优化——例如，在每个数组中跟踪最小和最大元素。然后，在特定情况下，你可以快速计算出两个数组是否不重叠。这样做（以及其他类似的优化）的问题是，仍然需要将所有文档与其他文档进行比较。它没有利用相似度是“稀疏”的这一事实。考虑到我们有很多文档，真的不需要将所有文档与其他文档进行比较（即使比较运算速度很快）。所有这类解复杂度都是O(D²)，其中D是文档的数量。我们不应该将所有的文档与其他文档进行比较。
7. 解法2：如果我们不能将所有文档与其他文档进行比较，那么就需要进一步比较其元素。考虑一个简单的解决方案，看看是否可以将其扩展到多个文档。
8. 解法2：思考这个问题的一种方法是，我们需要能够非常快速地找到与特定文档有某一相似值的所有文档的列表（同样地，我们不应该“查看所有文档并快速消除不具备某相似值的文档”。那样的话时间复杂度至少是O(D²)）。
9. 解法2：根据前面的提示，我们可以思考是什么构成了与特定文档（类似于{13, 16, 21, 3}文档）有指定相似度的文档。这个列表有哪些属性？我们如何收集所有的那样的文档？
10. 解法2：与{13, 16, 21, 3}相似的文档列表包括所有包含3、16、21和3的文档。如何才能有效地找到这个列表？记住，我们将对许多文档做此计算，所以一些预处理是必要的。
11. 解法2：尝试构建一个散列表，使其从每个单词映射到包含此单词的文档。这将允许我们轻松地找到所有与{13, 16, 21, 3}有特定相似值的文档。
12. 解法2：一旦有了一种方法可以容易地找到与特定文档有某一相似值的所有文档，你就可以通过一个简单的算法进行计算。你能让算法更快一些吗？具体来说，可以直接从散列表计算相似度吗？
13. 解法2：假设你正在通过查找一个从单词映射到文档的散列表来查找与{1, 4, 6}相似的文档。执行此查找时，同一文档ID会出现多次。这说明了什么？
14. 解法3：有另一种解决方案。考虑从所有的文档中提取所有的单词，将它们放入一个巨大的列表中，并对这个列表进行排序。假设你仍然知道每个单词来自哪个文档。如何跟踪相似的文档?

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> computeSimilarities(vector<vector<int>>& docs) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> computeSimilarities(int[][] docs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def computeSimilarities(self, docs):
        """
        :type docs: List[List[int]]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** computeSimilarities(int** docs, int docsSize, int* docsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> ComputeSimilarities(int[][] docs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} docs
 * @return {string[]}
 */
var computeSimilarities = function(docs) {
    
};
```

### TypeScript

```typescript
function computeSimilarities(docs: number[][]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $docs
     * @return String[]
     */
    function computeSimilarities($docs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func computeSimilarities(_ docs: [[Int]]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun computeSimilarities(docs: Array<IntArray>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> computeSimilarities(List<List<int>> docs) {
    
  }
}
```

### Go

```golang
func computeSimilarities(docs [][]int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} docs
# @return {String[]}
def compute_similarities(docs)
    
end
```

### Scala

```scala
object Solution {
    def computeSimilarities(docs: Array[Array[Int]]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn compute_similarities(docs: Vec<Vec<i32>>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (compute-similarities docs)
  (-> (listof (listof exact-integer?)) (listof string?))
  )
```

### Erlang

```erlang
-spec compute_similarities(Docs :: [[integer()]]) -> [unicode:unicode_binary()].
compute_similarities(Docs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec compute_similarities(docs :: [[integer]]) :: [String.t]
  def compute_similarities(docs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func computeSimilarities(docs: Array<Array<Int64>>): ArrayList<String> {

    }
}
```

