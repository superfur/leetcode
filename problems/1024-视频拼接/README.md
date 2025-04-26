# 1024. 视频拼接

## 题目描述

<p>你将会获得一系列视频片段，这些片段来自于一项持续时长为&nbsp;<code>time</code>&nbsp;秒的体育赛事。这些片段可能有所重叠，也可能长度不一。</p>

<p>使用数组&nbsp;<code>clips</code> 描述所有的视频片段，其中 <code>clips[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示：某个视频片段开始于&nbsp;<code>start<sub>i</sub></code>&nbsp;并于&nbsp;<code>end<sub>i</sub></code>&nbsp;结束。</p>

<p>甚至可以对这些片段自由地再剪辑：</p>

<ul>
	<li>例如，片段&nbsp;<code>[0, 7]</code>&nbsp;可以剪切成&nbsp;<code>[0, 1] +&nbsp;[1, 3] + [3, 7]</code>&nbsp;三部分。</li>
</ul>

<p>我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（<code>[0, time]</code>）。返回所需片段的最小数目，如果无法完成该任务，则返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
<strong>输出：</strong>3
<strong>解释：</strong>
选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在手上的片段为 [0,2] + [2,8] + [8,10]，而这些覆盖了整场比赛 [0, 10]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,1],[1,2]], time = 5
<strong>输出：</strong>-1
<strong>解释：</strong>
无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
<strong>输出：</strong>3
<strong>解释： </strong>
选取片段 [0,4], [4,7] 和 [6,9] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= clips.length &lt;= 100</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 100</code></li>
	<li><code>1 &lt;= time &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. What if we sort the intervals?  Considering the sorted intervals, how can we solve the problem with dynamic programming?
2. Let's consider a DP(pos, limit) where pos represents the position of the current interval we are gonna take the decision and limit is the current covered area from [0 - limit]. This DP returns the minimum number of taken intervals or infinite if it's not possible to cover the [0 - T] section.

## 示例

```
[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
10
[[0,1],[1,2]]
5
[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int time) {
        
    }
};
```

### Java

```java
class Solution {
    public int videoStitching(int[][] clips, int time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
```

### C

```c
int videoStitching(int** clips, int clipsSize, int* clipsColSize, int time) {
    
}
```

### C#

```csharp
public class Solution {
    public int VideoStitching(int[][] clips, int time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} clips
 * @param {number} time
 * @return {number}
 */
var videoStitching = function(clips, time) {
    
};
```

### TypeScript

```typescript
function videoStitching(clips: number[][], time: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $clips
     * @param Integer $time
     * @return Integer
     */
    function videoStitching($clips, $time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func videoStitching(_ clips: [[Int]], _ time: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun videoStitching(clips: Array<IntArray>, time: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int videoStitching(List<List<int>> clips, int time) {
    
  }
}
```

### Go

```golang
func videoStitching(clips [][]int, time int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} clips
# @param {Integer} time
# @return {Integer}
def video_stitching(clips, time)
    
end
```

### Scala

```scala
object Solution {
    def videoStitching(clips: Array[Array[Int]], time: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn video_stitching(clips: Vec<Vec<i32>>, time: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (video-stitching clips time)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec video_stitching(Clips :: [[integer()]], Time :: integer()) -> integer().
video_stitching(Clips, Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec video_stitching(clips :: [[integer]], time :: integer) :: integer
  def video_stitching(clips, time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func videoStitching(clips: Array<Array<Int64>>, time: Int64): Int64 {

    }
}
```

