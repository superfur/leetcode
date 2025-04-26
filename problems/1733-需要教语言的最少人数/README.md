# 1733. 需要教语言的最少人数

## 题目描述

<p>在一个由 <code>m</code> 个用户组成的社交网络里，我们获取到一些用户之间的好友关系。两个用户之间可以相互沟通的条件是他们都掌握同一门语言。</p>

<p>给你一个整数 <code>n</code> ，数组 <code>languages</code> 和数组 <code>friendships</code> ，它们的含义如下：</p>

<ul>
	<li>总共有 <code>n</code> 种语言，编号从 <code>1</code> 到 <code>n</code> 。</li>
	<li><code>languages[i]</code> 是第 <code>i</code> 位用户掌握的语言集合。</li>
	<li><code>friendships[i] = [u<sub>​​​​​​i</sub>​​​, v<sub>​​​​​​i</sub>]</code> 表示 <code>u<sup>​​​​​</sup><sub>​​​​​​i</sub></code>​​​​​ 和 <code>v<sub>i</sub></code> 为好友关系。</li>
</ul>

<p>你可以选择 <strong>一门</strong> 语言并教会一些用户，使得所有好友之间都可以相互沟通。请返回你 <strong>最少</strong> 需要教会多少名用户。</p>
请注意，好友关系没有传递性，也就是说如果 <code>x</code> 和 <code>y</code> 是好友，且 <code>y</code> 和 <code>z</code> 是好友， <code>x</code> 和 <code>z</code> 不一定是好友。

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
<b>输出：</b>1
<b>解释：</b>你可以选择教用户 1 第二门语言，也可以选择教用户 2 第一门语言。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
<b>输出：</b>2
<b>解释：</b>教用户 1 和用户 3 第三门语言，需要教 2 名用户。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 500</code></li>
	<li><code>languages.length == m</code></li>
	<li><code>1 <= m <= 500</code></li>
	<li><code>1 <= languages[i].length <= n</code></li>
	<li><code>1 <= languages[i][j] <= n</code></li>
	<li><code>1 <= u<sub>​​​​​​i</sub> < v<sub>​​​​​​i</sub> <= languages.length</code></li>
	<li><code>1 <= friendships.length <= 500</code></li>
	<li>所有的好友关系 <code>(u<sub>​​​​​i, </sub>v<sub>​​​​​​i</sub>)</code> 都是唯一的。</li>
	<li><code>languages[i]</code> 中包含的值互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. You can just use brute force and find out for each language the number of users you need to teach
2. Note that a user can appear in multiple friendships but you need to teach that user only once

## 示例

```
2
[[1],[2],[1,2]]
[[1,2],[1,3],[2,3]]
3
[[2],[1,3],[1,2],[3]]
[[1,4],[1,2],[3,4],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
```

### C

```c
int minimumTeachings(int n, int** languages, int languagesSize, int* languagesColSize, int** friendships, int friendshipsSize, int* friendshipsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTeachings(int n, int[][] languages, int[][] friendships) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function(n, languages, friendships) {
    
};
```

### TypeScript

```typescript
function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $languages
     * @param Integer[][] $friendships
     * @return Integer
     */
    function minimumTeachings($n, $languages, $friendships) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTeachings(_ n: Int, _ languages: [[Int]], _ friendships: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTeachings(n: Int, languages: Array<IntArray>, friendships: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTeachings(int n, List<List<int>> languages, List<List<int>> friendships) {
    
  }
}
```

### Go

```golang
func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} languages
# @param {Integer[][]} friendships
# @return {Integer}
def minimum_teachings(n, languages, friendships)
    
end
```

### Scala

```scala
object Solution {
    def minimumTeachings(n: Int, languages: Array[Array[Int]], friendships: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_teachings(n: i32, languages: Vec<Vec<i32>>, friendships: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-teachings n languages friendships)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_teachings(N :: integer(), Languages :: [[integer()]], Friendships :: [[integer()]]) -> integer().
minimum_teachings(N, Languages, Friendships) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_teachings(n :: integer, languages :: [[integer]], friendships :: [[integer]]) :: integer
  def minimum_teachings(n, languages, friendships) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTeachings(n: Int64, languages: Array<Array<Int64>>, friendships: Array<Array<Int64>>): Int64 {

    }
}
```

