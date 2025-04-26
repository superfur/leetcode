# 1854. 人口最多的年份

## 题目描述

<p>给你一个二维整数数组 <code>logs</code> ，其中每个 <code>logs[i] = [birth<sub>i</sub>, death<sub>i</sub>]</code> 表示第 <code>i</code> 个人的出生和死亡年份。</p>

<p>年份 <code>x</code> 的 <strong>人口</strong> 定义为这一年期间活着的人的数目。第 <code>i</code> 个人被计入年份 <code>x</code> 的人口需要满足：<code>x</code> 在闭区间 <code>[birth<sub>i</sub>, death<sub>i</sub> - 1]</code> 内。注意，人不应当计入他们死亡当年的人口中。</p>

<p>返回 <strong>人口最多</strong> 且 <strong>最早</strong> 的年份。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>logs = [[1993,1999],[2000,2010]]
<strong>输出：</strong>1993
<strong>解释：</strong>人口最多为 1 ，而 1993 是人口为 1 的最早年份。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>logs = [[1950,1961],[1960,1971],[1970,1981]]
<strong>输出：</strong>1960
<strong>解释：</strong> 
人口最多为 2 ，分别出现在 1960 和 1970 。
其中最早年份是 1960 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 100</code></li>
	<li><code>1950 &lt;= birth<sub>i</sub> &lt; death<sub>i</sub> &lt;= 2050</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 计数
- 前缀和

## 提示

1. For each year find the number of people whose birth_i ≤ year and death_i > year.
2. Find the maximum value between all years.

## 示例

```
[[1993,1999],[2000,2010]]
[[1950,1961],[1960,1971],[1970,1981]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumPopulation(int[][] logs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
```

### C

```c
int maximumPopulation(int** logs, int logsSize, int* logsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumPopulation(int[][] logs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} logs
 * @return {number}
 */
var maximumPopulation = function(logs) {
    
};
```

### TypeScript

```typescript
function maximumPopulation(logs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $logs
     * @return Integer
     */
    function maximumPopulation($logs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumPopulation(_ logs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumPopulation(logs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumPopulation(List<List<int>> logs) {
    
  }
}
```

### Go

```golang
func maximumPopulation(logs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} logs
# @return {Integer}
def maximum_population(logs)
    
end
```

### Scala

```scala
object Solution {
    def maximumPopulation(logs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-population logs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_population(Logs :: [[integer()]]) -> integer().
maximum_population(Logs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_population(logs :: [[integer]]) :: integer
  def maximum_population(logs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumPopulation(logs: Array<Array<Int64>>): Int64 {

    }
}
```

