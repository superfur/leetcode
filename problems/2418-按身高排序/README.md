# 2418. 按身高排序

## 题目描述

<p>给你一个字符串数组 <code>names</code> ，和一个由 <strong>互不相同</strong> 的正整数组成的数组 <code>heights</code> 。两个数组的长度均为 <code>n</code> 。</p>

<p>对于每个下标 <code>i</code>，<code>names[i]</code> 和 <code>heights[i]</code> 表示第 <code>i</code> 个人的名字和身高。</p>

<p>请按身高 <strong>降序</strong> 顺序返回对应的名字数组 <code>names</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>names = ["Mary","John","Emma"], heights = [180,165,170]
<strong>输出：</strong>["Mary","Emma","John"]
<strong>解释：</strong>Mary 最高，接着是 Emma 和 John 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>names = ["Alice","Bob","Bob"], heights = [155,185,150]
<strong>输出：</strong>["Bob","Alice","Bob"]
<strong>解释：</strong>第一个 Bob 最高，然后是 Alice 和第二个 Bob 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == names.length == heights.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= names[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>names[i]</code> 由大小写英文字母组成</li>
	<li><code>heights</code> 中的所有值互不相同</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Find the tallest person and swap with the first person, then find the second tallest person and swap with the second person, etc. Repeat until you fix all n people.

## 示例

```
["Mary","John","Emma"]
[180,165,170]
["Alice","Bob","Bob"]
[155,185,150]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] SortPeople(string[] names, int[] heights) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    
};
```

### TypeScript

```typescript
function sortPeople(names: string[], heights: number[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $names
     * @param Integer[] $heights
     * @return String[]
     */
    function sortPeople($names, $heights) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortPeople(_ names: [String], _ heights: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortPeople(names: Array<String>, heights: IntArray): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> sortPeople(List<String> names, List<int> heights) {
    
  }
}
```

### Go

```golang
func sortPeople(names []string, heights []int) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} names
# @param {Integer[]} heights
# @return {String[]}
def sort_people(names, heights)
    
end
```

### Scala

```scala
object Solution {
    def sortPeople(names: Array[String], heights: Array[Int]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (sort-people names heights)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec sort_people(Names :: [unicode:unicode_binary()], Heights :: [integer()]) -> [unicode:unicode_binary()].
sort_people(Names, Heights) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_people(names :: [String.t], heights :: [integer]) :: [String.t]
  def sort_people(names, heights) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortPeople(names: Array<String>, heights: Array<Int64>): Array<String> {

    }
}
```

