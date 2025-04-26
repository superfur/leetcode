# LCR 035. 最小时间差

## 题目描述

<p>给定一个 24 小时制（小时:分钟 <strong>&quot;HH:MM&quot;</strong>）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>timePoints = [&quot;23:59&quot;,&quot;00:00&quot;]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>timePoints = [&quot;00:00&quot;,&quot;23:59&quot;,&quot;00:00&quot;]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= timePoints &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>timePoints[i]</code> 格式为 <strong>&quot;HH:MM&quot;</strong></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 539&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/minimum-time-difference/">https://leetcode-cn.com/problems/minimum-time-difference/</a></p>


## 难度

Medium

## 标签

- 数组
- 数学
- 字符串
- 排序

## 示例

```
["23:59","00:00"]
["00:00","23:59","00:00"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {

    }
};
```

### Java

```java
class Solution {
    public int findMinDifference(List<String> timePoints) {

    }
}
```

### Python

```python
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
```

### C

```c


int findMinDifference(char ** timePoints, int timePointsSize){

}
```

### C#

```csharp
public class Solution {
    public int FindMinDifference(IList<string> timePoints) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {

};
```

### TypeScript

```typescript
function findMinDifference(timePoints: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $timePoints
     * @return Integer
     */
    function findMinDifference($timePoints) {

    }
}
```

### Swift

```swift
class Solution {
    func findMinDifference(_ timePoints: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinDifference(timePoints: List<String>): Int {

    }
}
```

### Go

```golang
func findMinDifference(timePoints []string) int {

}
```

### Ruby

```ruby
# @param {String[]} time_points
# @return {Integer}
def find_min_difference(time_points)

end
```

### Scala

```scala
object Solution {
    def findMinDifference(timePoints: List[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (find-min-difference timePoints)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec find_min_difference(TimePoints :: [unicode:unicode_binary()]) -> integer().
find_min_difference(TimePoints) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_min_difference(time_points :: [String.t]) :: integer
  def find_min_difference(time_points) do

  end
end
```

