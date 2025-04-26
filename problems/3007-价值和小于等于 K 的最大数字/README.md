# 3007. 价值和小于等于 K 的最大数字

## 题目描述

<p>给你一个整数&nbsp;<code>k</code>&nbsp;和一个整数&nbsp;<code>x</code>&nbsp;。整数&nbsp;<code>num</code>&nbsp;的价值是它的二进制表示中在&nbsp;<code>x</code>，<code>2x</code>，<code>3x</code>&nbsp;等位置处&nbsp;<strong><span data-keyword="set-bit">设置位</span></strong>&nbsp;的数目（从最低有效位开始）。下面的表格包含了如何计算价值的例子。</p>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
		</tr>
		<tr>
			<td>1</td>
			<td>13</td>
			<td><u>0</u><u>0</u><u>0</u><u>0</u><u>0</u><strong><u>1</u></strong><strong><u>1</u></strong><u>0</u><strong><u>1</u></strong></td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>13</td>
			<td>0<u>0</u>0<u>0</u>0<strong><u>1</u></strong>1<u>0</u>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>233</td>
			<td>0<strong><u>1</u></strong>1<strong><u>1</u></strong>0<strong><u>1</u></strong>0<u>0</u>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>3</td>
			<td>13</td>
			<td><u>0</u>00<u>0</u>01<strong><u>1</u></strong>01</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>362</td>
			<td><strong><u>1</u></strong>01<strong><u>1</u></strong>01<u>0</u>10</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><code>num</code>&nbsp;的 <strong>累加价值</strong> 是从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>num</code>&nbsp;的数字的 <strong>总</strong> 价值。如果&nbsp;<code>num</code>&nbsp;的累加价值小于或等于&nbsp;<code>k</code>&nbsp;则被认为是 <strong>廉价</strong> 的。</p>

<p>请你返回<strong>&nbsp;最大</strong>&nbsp;的廉价数字。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>k = 9, x = 1
<b>输出：</b>6
<b>解释：</b>由下表所示，6 是最大的廉价数字。
</pre>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
			<th>Accumulated Price</th>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td><u>0</u><u>0</u><strong><u>1</u></strong></td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>2</td>
			<td><u>0</u><strong><u>1</u></strong><u>0</u></td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>1</td>
			<td>3</td>
			<td><u>0</u><strong><u>1</u></strong><strong><u>1</u></strong></td>
			<td>2</td>
			<td>4</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td><strong><u>1</u></strong><u>0</u><u>0</u></td>
			<td>1</td>
			<td>5</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td><strong><u>1</u></strong><u>0</u><strong><u>1</u></strong></td>
			<td>2</td>
			<td>7</td>
		</tr>
		<tr>
			<td>1</td>
			<td>6</td>
			<td><strong><u>1</u></strong><strong><u>1</u></strong><u>0</u></td>
			<td>2</td>
			<td>9</td>
		</tr>
		<tr>
			<td>1</td>
			<td>7</td>
			<td><strong><u>1</u></strong><strong><u>1</u></strong><strong><u>1</u></strong></td>
			<td>3</td>
			<td>12</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>k = 7, x = 2
<b>输出：</b>9
<b>解释：</b>由下表所示，9 是最大的廉价数字。
</pre>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
			<th>Accumulated Price</th>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td><u>0</u>0<u>0</u>1</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>2</td>
			<td>2</td>
			<td><u>0</u>0<strong><u>1</u></strong>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td><u>0</u>0<strong><u>1</u></strong>1</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td><u>0</u>1<u>0</u>0</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>5</td>
			<td><u>0</u>1<u>0</u>1</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>6</td>
			<td><u>0</u>1<strong><u>1</u></strong>0</td>
			<td>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>7</td>
			<td><u>0</u>1<strong><u>1</u></strong>1</td>
			<td>1</td>
			<td>4</td>
		</tr>
		<tr>
			<td>2</td>
			<td>8</td>
			<td><strong><u>1</u></strong>0<u>0</u>0</td>
			<td>1</td>
			<td>5</td>
		</tr>
		<tr>
			<td>2</td>
			<td>9</td>
			<td><strong><u>1</u></strong>0<u>0</u>1</td>
			<td>1</td>
			<td>6</td>
		</tr>
		<tr>
			<td>2</td>
			<td>10</td>
			<td><strong><u>1</u></strong>0<strong><u>1</u></strong>0</td>
			<td>2</td>
			<td>8</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= x &lt;= 8</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 二分查找
- 动态规划

## 提示

1. Binary search the answer.
2. In each step of the binary search you should calculate the number of the set bits in the <code>i<sup>th</sup></code> position. Then calculate the sum of them.

## 示例

```
9
1
7
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findMaximumNumber(long long k, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public long findMaximumNumber(long k, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaximumNumber(self, k, x):
        """
        :type k: int
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        
```

### C

```c
long long findMaximumNumber(long long k, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindMaximumNumber(long k, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} x
 * @return {number}
 */
var findMaximumNumber = function(k, x) {
    
};
```

### TypeScript

```typescript
function findMaximumNumber(k: number, x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $x
     * @return Integer
     */
    function findMaximumNumber($k, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaximumNumber(_ k: Int, _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximumNumber(k: Long, x: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaximumNumber(int k, int x) {
    
  }
}
```

### Go

```golang
func findMaximumNumber(k int64, x int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} x
# @return {Integer}
def find_maximum_number(k, x)
    
end
```

### Scala

```scala
object Solution {
    def findMaximumNumber(k: Long, x: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-maximum-number k x)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_maximum_number(K :: integer(), X :: integer()) -> integer().
find_maximum_number(K, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximum_number(k :: integer, x :: integer) :: integer
  def find_maximum_number(k, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaximumNumber(k: Int64, x: Int64): Int64 {

    }
}
```

