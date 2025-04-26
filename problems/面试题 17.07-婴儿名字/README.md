# 面试题 17.07. 婴儿名字

## 题目描述

<p>每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。</p>

<p>在结果列表中，选择<strong> 字典序最小 </strong>的名字作为真实名字。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
<strong>输出：</strong>["John(27)","Chris(36)"]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>names.length <= 100000</code></li>
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
- 计数

## 提示

1. 讨论一下简单方法:当它们是同义词时将名称合并到一起。你如何确定传递关系?A == B, A == C, C == D 表示 A == D == B == C。
2. 该问题的核心是将名字分组成不同的拼写。基于此，计算出频率就相对容易了。
3. 你要尝试的一件事是维护每个名称到其“真正”拼写的映射。你还需要从真正的拼写映射到所有同义词。有时，你可能要合并两组不同的名称。运行一下这个算法，看看你能否让它工作。然后看看是否能简化/优化它。
4. 使用上述方法的一种简单方式是将每个名称映射到一个备选拼写列表。当一个组中的一个名称设置为等于另一个组中的名称时会发生什么?
5. 如果每个名称都映射到其替代拼写的列表，那么在将 X 和 Y 设置为同义词时，你可能需要更新许多列表。如果 X 是{A, B, C}的同义词，而 Y 是{D, E, F}的同义词，那么你需要将{Y, D, E, F}添加到 A 的同义词列表、B 的同义词列表、C 的同义词列表和 X 的同义词列表中。{Y, D, E, F}同理。有更快的方法么?
6. 相反，X、A、B 和 C 应该映射到同一个集合{X, A, B, C}。Y、D、E 和 F 应该映射到同一个集合{Y, D, E, F}。当我们将 X 和 Y 设置为同义词时，可以将其中一个集合复制到另一个集合中(例如，将{Y, D, E, F}添加到{X, A, B, C}中)。散列表还需进行其他更改么?
7. 另一种方法是把它看作一幅图。应该怎么做?
8. 可以把将 X, Y 记为同义词看作是在 X 节点和 Y 节点之间添加一条边。那么如何算一组同义词有哪些呢?
9. 每个连通子图表示一组同义词。要找到每个组，可以重复广度优先(或深度优先)搜索。

## 示例

```
["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"]
["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> trulyMostPopular(vector<string>& names, vector<string>& synonyms) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] trulyMostPopular(String[] names, String[] synonyms) {
        
    }
}
```

### Python

```python
class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** trulyMostPopular(char** names, int namesSize, char** synonyms, int synonymsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] TrulyMostPopular(string[] names, string[] synonyms) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} names
 * @param {string[]} synonyms
 * @return {string[]}
 */
var trulyMostPopular = function(names, synonyms) {
    
};
```

### TypeScript

```typescript
function trulyMostPopular(names: string[], synonyms: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $names
     * @param String[] $synonyms
     * @return String[]
     */
    function trulyMostPopular($names, $synonyms) {
        
    }
}
```

### Swift

```swift
class Solution {
    func trulyMostPopular(_ names: [String], _ synonyms: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trulyMostPopular(names: Array<String>, synonyms: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> trulyMostPopular(List<String> names, List<String> synonyms) {
    
  }
}
```

### Go

```golang
func trulyMostPopular(names []string, synonyms []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} names
# @param {String[]} synonyms
# @return {String[]}
def truly_most_popular(names, synonyms)
    
end
```

### Scala

```scala
object Solution {
    def trulyMostPopular(names: Array[String], synonyms: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn truly_most_popular(names: Vec<String>, synonyms: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (truly-most-popular names synonyms)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec truly_most_popular(Names :: [unicode:unicode_binary()], Synonyms :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
truly_most_popular(Names, Synonyms) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec truly_most_popular(names :: [String.t], synonyms :: [String.t]) :: [String.t]
  def truly_most_popular(names, synonyms) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func trulyMostPopular(names: Array<String>, synonyms: Array<String>): Array<String> {

    }
}
```

