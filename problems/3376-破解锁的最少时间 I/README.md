# 3376. 破解锁的最少时间 I

## 题目描述

<p>Bob 被困在了一个地窖里，他需要破解 <code>n</code>&nbsp;个锁才能逃出地窖，每一个锁都需要一定的 <strong>能量</strong>&nbsp;才能打开。每一个锁需要的能量存放在一个数组&nbsp;<code>strength</code>&nbsp;里，其中&nbsp;<code>strength[i]</code>&nbsp;表示打开第 <code>i</code>&nbsp;个锁需要的能量。</p>

<p>Bob 有一把剑，它具备以下的特征：</p>

<ul>
	<li>一开始剑的能量为 0 。</li>
	<li>剑的能量增加因子&nbsp;<code><font face="monospace">X</font></code>&nbsp;一开始的值为 1 。</li>
	<li>每分钟，剑的能量都会增加当前的&nbsp;<code>X</code>&nbsp;值。</li>
	<li>打开第 <code>i</code>&nbsp;把锁，剑的能量需要到达 <strong>至少</strong>&nbsp;<code>strength[i]</code>&nbsp;。</li>
	<li>打开一把锁以后，剑的能量会变回 0 ，<code>X</code>&nbsp;的值会增加一个给定的值 <code>K</code>&nbsp;。</li>
</ul>

<p>你的任务是打开所有 <code>n</code>&nbsp;把锁并逃出地窖，请你求出需要的 <strong>最少</strong>&nbsp;分钟数。</p>

<p>请你返回 Bob<strong>&nbsp;</strong>打开所有 <code>n</code>&nbsp;把锁需要的 <strong>最少</strong>&nbsp;时间。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>strength = [3,4,1], K = 1</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><b>解释：</b></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">时间</th>
			<th style="border: 1px solid black;">能量</th>
			<th style="border: 1px solid black;">X</th>
			<th style="border: 1px solid black;">操作</th>
			<th style="border: 1px solid black;">更新后的 X</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">什么也不做</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">打开第 3&nbsp;把锁</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">什么也不做</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">打开第 2 把锁</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">打开第 1 把锁</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

<p>无法用少于 4 分钟打开所有的锁，所以答案为 4 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>strength = [2,5,4], K = 2</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">时间</th>
			<th style="border: 1px solid black;">能量</th>
			<th style="border: 1px solid black;">X</th>
			<th style="border: 1px solid black;">操作</th>
			<th style="border: 1px solid black;">更新后的 X</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">什么也不做</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">什么也不做</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">打开第 1 把锁</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">什么也不做</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">打开第 2 把锁</td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">打开第 3 把锁</td>
			<td style="border: 1px solid black;">7</td>
		</tr>
	</tbody>
</table>

<p>无法用少于 5 分钟打开所有的锁，所以答案为 5 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == strength.length</code></li>
	<li><code>1 &lt;= n &lt;= 8</code></li>
	<li><code>1 &lt;= K &lt;= 10</code></li>
	<li><code>1 &lt;= strength[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 深度优先搜索
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. Try all <code>n!</code> permutation ways of breaking the locks.

## 示例

```
[3,4,1]
1
[2,5,4]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinimumTime(vector<int>& strength, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinimumTime(List<Integer> strength, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinimumTime(self, strength, k):
        """
        :type strength: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        
```

### C

```c
int findMinimumTime(int* strength, int strengthSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinimumTime(IList<int> strength, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} strength
 * @param {number} k
 * @return {number}
 */
var findMinimumTime = function(strength, k) {
    
};
```

### TypeScript

```typescript
function findMinimumTime(strength: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $strength
     * @param Integer $k
     * @return Integer
     */
    function findMinimumTime($strength, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinimumTime(_ strength: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinimumTime(strength: List<Int>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinimumTime(List<int> strength, int k) {
    
  }
}
```

### Go

```golang
func findMinimumTime(strength []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} strength
# @param {Integer} k
# @return {Integer}
def find_minimum_time(strength, k)
    
end
```

### Scala

```scala
object Solution {
    def findMinimumTime(strength: List[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_minimum_time(strength: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-minimum-time strength k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_minimum_time(Strength :: [integer()], K :: integer()) -> integer().
find_minimum_time(Strength, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_minimum_time(strength :: [integer], k :: integer) :: integer
  def find_minimum_time(strength, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinimumTime(strength: ArrayList<Int64>, k: Int64): Int64 {

    }
}
```

