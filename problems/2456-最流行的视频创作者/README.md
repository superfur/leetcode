# 2456. 最流行的视频创作者

## 题目描述

<p>给你两个字符串数组 <code>creators</code> 和 <code>ids</code> ，和一个整数数组 <code>views</code> ，所有数组的长度都是 <code>n</code> 。平台上第 <code>i</code> 个视频者是&nbsp;<code>creator[i]</code> ，视频分配的 id 是 <code>ids[i]</code> ，且播放量为 <code>views[i]</code> 。</p>

<p>视频创作者的 <strong>流行度</strong> 是该创作者的 <strong>所有</strong> 视频的播放量的 <strong>总和</strong> 。请找出流行度 <strong>最高</strong> 创作者以及该创作者播放量 <strong>最大</strong> 的视频的 id 。</p>

<ul>
	<li>如果存在多个创作者流行度都最高，则需要找出所有符合条件的创作者。</li>
	<li>如果某个创作者存在多个播放量最高的视频，则只需要找出字典序最小的 <code>id</code> 。</li>
</ul>

<p>返回一个二维字符串数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer[i] = [creator<sub>i</sub>, id<sub>i</sub>]</code><em> </em>表示<em> </em><code>creator<sub>i</sub></code> 的流行度 <strong>最高</strong> 且其最流行的视频 id 是<em> </em><code>id<sub>i</sub></code><em> </em>，可以按任何顺序返回该结果<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
<strong>输出：</strong>[["alice","one"],["bob","two"]]
<strong>解释：</strong>
alice 的流行度是 5 + 5 = 10 。
bob 的流行度是 10 。
chris 的流行度是 4 。
alice 和 bob 是流行度最高的创作者。
bob 播放量最高的视频 id 为 "two" 。
alice 播放量最高的视频 id 是 "one" 和 "three" 。由于 "one" 的字典序比 "three" 更小，所以结果中返回的 id 是 "one" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
<strong>输出：</strong>[["alice","b"]]
<strong>解释：</strong>
id 为 "b" 和 "c" 的视频都满足播放量最高的条件。
由于 "b" 的字典序比 "c" 更小，所以结果中返回的 id 是 "b" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == creators.length == ids.length == views.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= creators[i].length, ids[i].length &lt;= 5</code></li>
	<li><code>creators[i]</code> 和 <code>ids[i]</code> 仅由小写英文字母组成</li>
	<li><code>0 &lt;= views[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序
- 堆（优先队列）

## 提示

1. Use a hash table to store and categorize videos based on their creator.
2. For each creator, iterate through all their videos and use three variables to keep track of their popularity, their most popular video, and the id of their most popular video.

## 示例

```
["alice","bob","alice","chris"]
["one","two","three","four"]
[5,10,5,4]
["alice","alice","alice"]
["a","b","c"]
[1,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> mostPopularCreator(String[] creators, String[] ids, int[] views) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** mostPopularCreator(char** creators, int creatorsSize, char** ids, int idsSize, int* views, int viewsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> MostPopularCreator(string[] creators, string[] ids, int[] views) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} creators
 * @param {string[]} ids
 * @param {number[]} views
 * @return {string[][]}
 */
var mostPopularCreator = function(creators, ids, views) {
    
};
```

### TypeScript

```typescript
function mostPopularCreator(creators: string[], ids: string[], views: number[]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $creators
     * @param String[] $ids
     * @param Integer[] $views
     * @return String[][]
     */
    function mostPopularCreator($creators, $ids, $views) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostPopularCreator(_ creators: [String], _ ids: [String], _ views: [Int]) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostPopularCreator(creators: Array<String>, ids: Array<String>, views: IntArray): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> mostPopularCreator(List<String> creators, List<String> ids, List<int> views) {
    
  }
}
```

### Go

```golang
func mostPopularCreator(creators []string, ids []string, views []int) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[]} creators
# @param {String[]} ids
# @param {Integer[]} views
# @return {String[][]}
def most_popular_creator(creators, ids, views)
    
end
```

### Scala

```scala
object Solution {
    def mostPopularCreator(creators: Array[String], ids: Array[String], views: Array[Int]): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_popular_creator(creators: Vec<String>, ids: Vec<String>, views: Vec<i32>) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (most-popular-creator creators ids views)
  (-> (listof string?) (listof string?) (listof exact-integer?) (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec most_popular_creator(Creators :: [unicode:unicode_binary()], Ids :: [unicode:unicode_binary()], Views :: [integer()]) -> [[unicode:unicode_binary()]].
most_popular_creator(Creators, Ids, Views) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_popular_creator(creators :: [String.t], ids :: [String.t], views :: [integer]) :: [[String.t]]
  def most_popular_creator(creators, ids, views) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostPopularCreator(creators: Array<String>, ids: Array<String>, views: Array<Int64>): ArrayList<ArrayList<String>> {

    }
}
```

