# 1170. 比较字符串最小字母出现频次

## 题目描述

<p>定义一个函数 <code>f(s)</code>，统计 <code>s</code>  中<strong>（按字典序比较）最小字母的出现频次</strong> ，其中 <code>s</code> 是一个非空字符串。</p>

<p>例如，若 <code>s = "dcce"</code>，那么 <code>f(s) = 2</code>，因为字典序最小字母是 <code>"c"</code>，它出现了 2 次。</p>

<p>现在，给你两个字符串数组待查表 <code>queries</code> 和词汇表 <code>words</code> 。对于每次查询 <code>queries[i]</code> ，需统计 <code>words</code> 中满足 <code>f(queries[i])</code> < <code>f(W)</code> 的<strong> 词的数目</strong> ，<code>W</code> 表示词汇表 <code>words</code> 中的每个词。</p>

<p>请你返回一个整数数组 <code>answer</code> 作为答案，其中每个 <code>answer[i]</code> 是第 <code>i</code> 次查询的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>queries = ["cbd"], words = ["zaaaz"]
<strong>输出：</strong>[1]
<strong>解释：</strong>查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= queries.length <= 2000</code></li>
	<li><code>1 <= words.length <= 2000</code></li>
	<li><code>1 <= queries[i].length, words[i].length <= 10</code></li>
	<li><code>queries[i][j]</code>、<code>words[i][j]</code> 都由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 二分查找
- 排序

## 提示

1. For each string from words calculate the leading count and store it in an array, then sort the integer array.
2. For each string from queries calculate the leading count "p" and in base of the sorted array calculated on the step 1 do a binary search to count the number of items greater than "p".

## 示例

```
["cbd"]
["zaaaz"]
["bbb","cc"]
["a","aa","aaa","aaaa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numSmallerByFrequency(char** queries, int queriesSize, char** words, int wordsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumSmallerByFrequency(string[] queries, string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} queries
 * @param {string[]} words
 * @return {number[]}
 */
var numSmallerByFrequency = function(queries, words) {
    
};
```

### TypeScript

```typescript
function numSmallerByFrequency(queries: string[], words: string[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String[] $words
     * @return Integer[]
     */
    function numSmallerByFrequency($queries, $words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSmallerByFrequency(_ queries: [String], _ words: [String]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSmallerByFrequency(queries: Array<String>, words: Array<String>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numSmallerByFrequency(List<String> queries, List<String> words) {
    
  }
}
```

### Go

```golang
func numSmallerByFrequency(queries []string, words []string) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} queries
# @param {String[]} words
# @return {Integer[]}
def num_smaller_by_frequency(queries, words)
    
end
```

### Scala

```scala
object Solution {
    def numSmallerByFrequency(queries: Array[String], words: Array[String]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_smaller_by_frequency(queries: Vec<String>, words: Vec<String>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (num-smaller-by-frequency queries words)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec num_smaller_by_frequency(Queries :: [unicode:unicode_binary()], Words :: [unicode:unicode_binary()]) -> [integer()].
num_smaller_by_frequency(Queries, Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_smaller_by_frequency(queries :: [String.t], words :: [String.t]) :: [integer]
  def num_smaller_by_frequency(queries, words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSmallerByFrequency(queries: Array<String>, words: Array<String>): Array<Int64> {

    }
}
```

