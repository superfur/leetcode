# 1723. 完成所有工作的最短时间

## 题目描述

<p>给你一个整数数组 <code>jobs</code> ，其中 <code>jobs[i]</code> 是完成第 <code>i</code> 项工作要花费的时间。</p>

<p>请你将这些工作分配给 <code>k</code> 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 <strong>工作时间</strong> 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 <strong>最大工作时间</strong> 得以 <strong>最小化</strong> 。</p>

<p>返回分配方案中尽可能 <strong>最小</strong> 的 <strong>最大工作时间</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>jobs = [3,2,3], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>给每位工人分配一项工作，最大工作时间是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>jobs = [1,2,4,7,8], k = 2
<strong>输出：</strong>11
<strong>解释：</strong>按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= jobs.length <= 12</code></li>
	<li><code>1 <= jobs[i] <= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. We can select a subset of tasks and assign it to a worker then solve the subproblem on the remaining tasks

## 示例

```
[3,2,3]
3
[1,2,4,7,8]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTimeRequired(int[] jobs, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
```

### C

```c
int minimumTimeRequired(int* jobs, int jobsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTimeRequired(int[] jobs, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} jobs
 * @param {number} k
 * @return {number}
 */
var minimumTimeRequired = function(jobs, k) {
    
};
```

### TypeScript

```typescript
function minimumTimeRequired(jobs: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $jobs
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeRequired($jobs, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTimeRequired(_ jobs: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTimeRequired(jobs: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTimeRequired(List<int> jobs, int k) {
    
  }
}
```

### Go

```golang
func minimumTimeRequired(jobs []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} jobs
# @param {Integer} k
# @return {Integer}
def minimum_time_required(jobs, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumTimeRequired(jobs: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time_required(jobs: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time-required jobs k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time_required(Jobs :: [integer()], K :: integer()) -> integer().
minimum_time_required(Jobs, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time_required(jobs :: [integer], k :: integer) :: integer
  def minimum_time_required(jobs, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTimeRequired(jobs: Array<Int64>, k: Int64): Int64 {

    }
}
```

