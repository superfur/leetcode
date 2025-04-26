# 1311. 获取你好友已观看的视频

## 题目描述

<p>有&nbsp;<code>n</code> 个人，每个人都有一个&nbsp; <code>0</code>&nbsp;到&nbsp;<code>n-1</code>&nbsp;的唯一&nbsp;<em>id</em>&nbsp;。</p>

<p>给你数组 <code>watchedVideos</code>&nbsp; 和&nbsp;<code>friends</code>&nbsp;，其中&nbsp;<code>watchedVideos[i]</code>&nbsp; 和&nbsp;<code>friends[i]</code>&nbsp;分别表示&nbsp;<code>id = i</code>&nbsp;的人观看过的视频列表和他的好友列表。</p>

<p>Level&nbsp;<strong>1</strong>&nbsp;的视频包含所有你好友观看过的视频，level&nbsp;<strong>2</strong>&nbsp;的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 <strong>k</strong>&nbsp;的视频包含所有从你出发，最短距离为&nbsp;<strong>k</strong>&nbsp;的好友观看过的视频。</p>

<p>给定你的&nbsp;<code>id</code>&nbsp; 和一个&nbsp;<code>level</code>&nbsp;值，请你找出所有指定 <code>level</code> 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_1.png" style="height: 179px; width: 129px;"></strong></p>

<pre><strong>输入：</strong>watchedVideos = [[&quot;A&quot;,&quot;B&quot;],[&quot;C&quot;],[&quot;B&quot;,&quot;C&quot;],[&quot;D&quot;]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
<strong>输出：</strong>[&quot;B&quot;,&quot;C&quot;] 
<strong>解释：</strong>
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -&gt; watchedVideos = [&quot;C&quot;]&nbsp;
id 为 2 -&gt; watchedVideos = [&quot;B&quot;,&quot;C&quot;]&nbsp;
你朋友观看过视频的频率为：
B -&gt; 1&nbsp;
C -&gt; 2
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_2.png" style="height: 179px; width: 129px;"></strong></p>

<pre><strong>输入：</strong>watchedVideos = [[&quot;A&quot;,&quot;B&quot;],[&quot;C&quot;],[&quot;B&quot;,&quot;C&quot;],[&quot;D&quot;]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
<strong>输出：</strong>[&quot;D&quot;]
<strong>解释：</strong>
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == watchedVideos.length ==&nbsp;friends.length</code></li>
	<li><code>2 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;watchedVideos[i].length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;watchedVideos[i][j].length &lt;= 8</code></li>
	<li><code>0 &lt;= friends[i].length &lt; n</code></li>
	<li><code>0 &lt;= friends[i][j]&nbsp;&lt; n</code></li>
	<li><code>0 &lt;= id &lt; n</code></li>
	<li><code>1 &lt;= level &lt; n</code></li>
	<li>如果&nbsp;<code>friends[i]</code> 包含&nbsp;<code>j</code>&nbsp;，那么&nbsp;<code>friends[j]</code> 包含&nbsp;<code>i</code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 图
- 数组
- 哈希表
- 排序

## 提示

1. Do BFS to find the kth level friends.
2. Then collect movies saw by kth level friends and sort them accordingly.

## 示例

```
[["A","B"],["C"],["B","C"],["D"]]
[[1,2],[0,3],[0,3],[1,2]]
0
1
[["A","B"],["C"],["B","C"],["D"]]
[[1,2],[0,3],[0,3],[1,2]]
0
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        
    }
}
```

### Python

```python
class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** watchedVideosByFriends(char*** watchedVideos, int watchedVideosSize, int* watchedVideosColSize, int** friends, int friendsSize, int* friendsColSize, int id, int level, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> WatchedVideosByFriends(IList<IList<string>> watchedVideos, int[][] friends, int id, int level) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} watchedVideos
 * @param {number[][]} friends
 * @param {number} id
 * @param {number} level
 * @return {string[]}
 */
var watchedVideosByFriends = function(watchedVideos, friends, id, level) {
    
};
```

### TypeScript

```typescript
function watchedVideosByFriends(watchedVideos: string[][], friends: number[][], id: number, level: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $watchedVideos
     * @param Integer[][] $friends
     * @param Integer $id
     * @param Integer $level
     * @return String[]
     */
    function watchedVideosByFriends($watchedVideos, $friends, $id, $level) {
        
    }
}
```

### Swift

```swift
class Solution {
    func watchedVideosByFriends(_ watchedVideos: [[String]], _ friends: [[Int]], _ id: Int, _ level: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun watchedVideosByFriends(watchedVideos: List<List<String>>, friends: Array<IntArray>, id: Int, level: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> watchedVideosByFriends(List<List<String>> watchedVideos, List<List<int>> friends, int id, int level) {
    
  }
}
```

### Go

```golang
func watchedVideosByFriends(watchedVideos [][]string, friends [][]int, id int, level int) []string {
    
}
```

### Ruby

```ruby
# @param {String[][]} watched_videos
# @param {Integer[][]} friends
# @param {Integer} id
# @param {Integer} level
# @return {String[]}
def watched_videos_by_friends(watched_videos, friends, id, level)
    
end
```

### Scala

```scala
object Solution {
    def watchedVideosByFriends(watchedVideos: List[List[String]], friends: Array[Array[Int]], id: Int, level: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn watched_videos_by_friends(watched_videos: Vec<Vec<String>>, friends: Vec<Vec<i32>>, id: i32, level: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (watched-videos-by-friends watchedVideos friends id level)
  (-> (listof (listof string?)) (listof (listof exact-integer?)) exact-integer? exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec watched_videos_by_friends(WatchedVideos :: [[unicode:unicode_binary()]], Friends :: [[integer()]], Id :: integer(), Level :: integer()) -> [unicode:unicode_binary()].
watched_videos_by_friends(WatchedVideos, Friends, Id, Level) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec watched_videos_by_friends(watched_videos :: [[String.t]], friends :: [[integer]], id :: integer, level :: integer) :: [String.t]
  def watched_videos_by_friends(watched_videos, friends, id, level) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func watchedVideosByFriends(watchedVideos: ArrayList<ArrayList<String>>, friends: Array<Array<Int64>>, id: Int64, level: Int64): ArrayList<String> {

    }
}
```

