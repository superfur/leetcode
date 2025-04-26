# 2836. 在传球游戏中最大化函数值

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>receiver</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>总共有&nbsp;<code>n</code>&nbsp;名玩家，玩家 <strong>编号</strong>&nbsp;互不相同，且为&nbsp;<code>[0, n - 1]</code>&nbsp;中的整数。这些玩家玩一个传球游戏，<code>receiver[i]</code>&nbsp;表示编号为 <code>i</code>&nbsp;的玩家会传球给编号为 <code>receiver[i]</code>&nbsp;的玩家。玩家可以传球给自己，也就是说&nbsp;<code>receiver[i]</code>&nbsp;可能等于&nbsp;<code>i</code>&nbsp;。</p>

<p>你需要从 <code>n</code>&nbsp;名玩家中选择一名玩家作为游戏开始时唯一手中有球的玩家，球会被传 <strong>恰好</strong>&nbsp;<code>k</code>&nbsp;次。</p>

<p>如果选择编号为 <code>x</code>&nbsp;的玩家作为开始玩家，定义函数&nbsp;<code>f(x)</code>&nbsp;表示从编号为&nbsp;<code>x</code>&nbsp;的玩家开始，<code>k</code>&nbsp;次传球内所有接触过球玩家的编号之&nbsp;<strong>和</strong>&nbsp;，如果有玩家多次触球，则 <strong>累加多次</strong>&nbsp;。换句话说，&nbsp;<code>f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver<sup>(k)</sup>[x]</code>&nbsp;。</p>

<p>你的任务时选择开始玩家 <code>x</code>&nbsp;，目的是<strong>&nbsp;最大化</strong>&nbsp;<code>f(x)</code>&nbsp;。</p>

<p>请你返回函数的 <strong>最大值</strong>&nbsp;。</p>

<p><strong>注意：</strong><code>receiver</code>&nbsp;可能含有重复元素。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<th style="padding: 5px; border: 1px solid black;">传递次数</th>
			<th style="padding: 5px; border: 1px solid black;">传球者编号</th>
			<th style="padding: 5px; border: 1px solid black;">接球者编号</th>
			<th style="padding: 5px; border: 1px solid black;">x + 所有接球者编号</th>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">0</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">0</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">4</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<pre>
<b>输入：</b>receiver = [2,0,1], k = 4
<b>输出：</b>6
<b>解释：</b>上表展示了从编号为 x = 2 开始的游戏过程。
从表中可知，f(2) 等于 6 。
6 是能得到最大的函数值。
所以输出为 6 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<th style="padding: 5px; border: 1px solid black;">传递次数</th>
			<th style="padding: 5px; border: 1px solid black;">传球者编号</th>
			<th style="padding: 5px; border: 1px solid black;">接球者编号</th>
			<th style="padding: 5px; border: 1px solid black;">x + 所有接球者编号</th>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">4</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">7</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">9</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">10</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<pre>
<b>输入：</b>receiver = [1,1,1,2,3], k = 3
<b>输出：</b>10
<b>解释：</b>上表展示了从编号为 x = 4 开始的游戏过程。
从表中可知，f(4) 等于 10 。
10 是能得到最大的函数值。
所以输出为 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= receiver.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= receiver[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>10</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划

## 提示

1. <div class="_1l1MA">We can solve the problem using binary lifting.</div>
2. <div class="_1l1MA">For each player with id <code>x</code> and for every <code>i</code> in the range <code>[0, ceil(log<sub>2</sub>k)]</code>, we can determine the last receiver's id and compute the sum of player ids who receive the ball after <code>2<sup>i</sup></code> passes, starting from <code>x</code>.</div>
3. <div class="_1l1MA">Let <code>last_receiver[x][i] =</code> the last receiver's id after <code>2<sup>i</sup></code> passes, and <code>sum[x][i] =</code> the sum of player ids who receive the ball after <code>2<sup>i</sup></code> passes. For all <code>x</code> in the range <code>[0, n - 1]</code>, <code>last_receiver[x][0] = receiver[x]</code>, and <code>sum[x][0] = receiver[x]</code>.</div>
4. <div class="_1l1MA">Then for <code>i</code> in range <code>[1, ceil(log<sub>2</sub>k)]</code>, <code>last_receiver[x][i] = last_receiver[last_receiver[x][i - 1]][i - 1]</code> and <code>sum[x][i] = sum[x][i - 1] + sum[last_receiver[x][i - 1]][i - 1]</code>, for all <code>x</code> in the range <code>[0, n - 1]</code>.</div>
5. <div class="_1l1MA">Starting from each player id <code>x</code>, we can now go through the powers of <code>2</code> in the binary representation of <code>k</code> and make jumps corresponding to each power, using the pre-computed values, to compute <code>f(x)</code>.</div>
6. <div class="_1l1MA">The answer is the maximum <code>f(x)</code> from each player id.</div>

## 示例

```
[2,0,1]
4
[1,1,1,2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long getMaxFunctionValue(vector<int>& receiver, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public long getMaxFunctionValue(List<Integer> receiver, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        
```

### C

```c
long long getMaxFunctionValue(int* receiver, int receiverSize, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public long GetMaxFunctionValue(IList<int> receiver, long k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} receiver
 * @param {number} k
 * @return {number}
 */
var getMaxFunctionValue = function(receiver, k) {
    
};
```

### TypeScript

```typescript
function getMaxFunctionValue(receiver: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $receiver
     * @param Integer $k
     * @return Integer
     */
    function getMaxFunctionValue($receiver, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaxFunctionValue(_ receiver: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaxFunctionValue(receiver: List<Int>, k: Long): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaxFunctionValue(List<int> receiver, int k) {
    
  }
}
```

### Go

```golang
func getMaxFunctionValue(receiver []int, k int64) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} receiver
# @param {Integer} k
# @return {Integer}
def get_max_function_value(receiver, k)
    
end
```

### Scala

```scala
object Solution {
    def getMaxFunctionValue(receiver: List[Int], k: Long): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_max_function_value(receiver: Vec<i32>, k: i64) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (get-max-function-value receiver k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_max_function_value(Receiver :: [integer()], K :: integer()) -> integer().
get_max_function_value(Receiver, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_max_function_value(receiver :: [integer], k :: integer) :: integer
  def get_max_function_value(receiver, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaxFunctionValue(receiver: ArrayList<Int64>, k: Int64): Int64 {

    }
}
```

