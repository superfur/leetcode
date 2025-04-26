# 1562. 查找大小为 M 的最新分组

## 题目描述

<p>给你一个数组 <code>arr</code> ，该数组表示一个从 <code>1</code> 到 <code>n</code> 的数字排列。有一个长度为 <code>n</code> 的二进制字符串，该字符串上的所有位最初都设置为 <code>0</code> 。</p>

<p>在从 <code>1</code> 到 <code>n</code> 的每个步骤 <code>i</code> 中（假设二进制字符串和 <code>arr</code> 都是从 <code>1</code> 开始索引的情况下），二进制字符串上位于位置 <code>arr[i]</code> 的位将会设为 <code>1</code> 。</p>

<p>给你一个整数 <code>m</code> ，请你找出二进制字符串上存在长度为 <code>m</code> 的一组 <code>1</code> 的最后步骤。一组 <code>1</code> 是一个连续的、由 <code>1</code> 组成的子串，且左右两边不再有可以延伸的 <code>1</code> 。</p>

<p>返回存在长度 <strong>恰好</strong> 为 <code>m</code> 的 <strong>一组 <code>1</code>&nbsp;</strong> 的最后步骤。如果不存在这样的步骤，请返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [3,5,1,2,4], m = 1
<strong>输出：</strong>4
<strong>解释：
</strong>步骤 1：&quot;00<strong>1</strong>00&quot;，由 1 构成的组：[&quot;1&quot;]
步骤 2：&quot;0010<strong>1</strong>&quot;，由 1 构成的组：[&quot;1&quot;, &quot;1&quot;]
步骤 3：&quot;<strong>1</strong>0101&quot;，由 1 构成的组：[&quot;1&quot;, &quot;1&quot;, &quot;1&quot;]
步骤 4：&quot;1<strong>1</strong>101&quot;，由 1 构成的组：[&quot;111&quot;, &quot;1&quot;]
步骤 5：&quot;111<strong>1</strong>1&quot;，由 1 构成的组：[&quot;11111&quot;]
存在长度为 1 的一组 1 的最后步骤是步骤 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [3,1,5,4,2], m = 2
<strong>输出：</strong>-1
<strong>解释：
</strong>步骤 1：&quot;00<strong>1</strong>00&quot;，由 1 构成的组：[&quot;1&quot;]
步骤 2：&quot;<strong>1</strong>0100&quot;，由 1 构成的组：[&quot;1&quot;, &quot;1&quot;]
步骤 3：&quot;1010<strong>1</strong>&quot;，由 1 构成的组：[&quot;1&quot;, &quot;1&quot;, &quot;1&quot;]
步骤 4：&quot;101<strong>1</strong>1&quot;，由 1 构成的组：[&quot;1&quot;, &quot;111&quot;]
步骤 5：&quot;1<strong>1</strong>111&quot;，由 1 构成的组：[&quot;11111&quot;]
不管是哪一步骤都无法形成长度为 2 的一组 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1], m = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [2,1], m = 2
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == arr.length</code></li>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= n</code></li>
	<li><code>arr</code> 中的所有整数 <strong>互不相同</strong></li>
	<li><code>1 &lt;= m&nbsp;&lt;= arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找
- 模拟

## 提示

1. Since the problem asks for the latest step, can you start the searching from the end of arr?
2. Use a map to store the current “1” groups.
3. At each step (going backwards) you need to split one group and update the map.

## 示例

```
[3,5,1,2,4]
1
[3,1,5,4,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLatestStep(vector<int>& arr, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLatestStep(int[] arr, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
```

### C

```c
int findLatestStep(int* arr, int arrSize, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLatestStep(int[] arr, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} m
 * @return {number}
 */
var findLatestStep = function(arr, m) {
    
};
```

### TypeScript

```typescript
function findLatestStep(arr: number[], m: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @return Integer
     */
    function findLatestStep($arr, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLatestStep(_ arr: [Int], _ m: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLatestStep(arr: IntArray, m: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLatestStep(List<int> arr, int m) {
    
  }
}
```

### Go

```golang
func findLatestStep(arr []int, m int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} m
# @return {Integer}
def find_latest_step(arr, m)
    
end
```

### Scala

```scala
object Solution {
    def findLatestStep(arr: Array[Int], m: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_latest_step(arr: Vec<i32>, m: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-latest-step arr m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_latest_step(Arr :: [integer()], M :: integer()) -> integer().
find_latest_step(Arr, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_latest_step(arr :: [integer], m :: integer) :: integer
  def find_latest_step(arr, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLatestStep(arr: Array<Int64>, m: Int64): Int64 {

    }
}
```

