# 2217. 找到指定长度的回文数

## 题目描述

<p>给你一个整数数组&nbsp;<code>queries</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>intLength</code>&nbsp;，请你返回一个数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code> 是长度为&nbsp;<code>intLength</code>&nbsp;的&nbsp;<strong>正回文数</strong> 中第<em>&nbsp;</em><code>queries[i]</code>&nbsp;小的数字，如果不存在这样的回文数，则为 <code>-1</code>&nbsp;。</p>

<p><strong>回文数</strong> 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>queries = [1,2,3,4,5,90], intLength = 3
<b>输出：</b>[101,111,121,131,141,999]
<strong>解释：</strong>
长度为 3 的最小回文数依次是：
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
第 90 个长度为 3 的回文数是 999 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>queries = [2,4,6], intLength = 4
<b>输出：</b>[1111,1331,1551]
<strong>解释：</strong>
长度为 4 的前 6 个回文数是：
1001, 1111, 1221, 1331, 1441 和 1551 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= intLength&nbsp;&lt;= 15</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. For any value of queries[i] and intLength, how can you check if there exists at least queries[i] palindromes of length intLength?
2. Since a palindrome reads the same forwards and backwards, consider how you can efficiently find the first half (ceil(intLength/2) digits) of the palindrome.

## 示例

```
[1,2,3,4,5,90]
3
[2,4,6]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> kthPalindrome(vector<int>& queries, int intLength) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] kthPalindrome(int[] queries, int intLength) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* kthPalindrome(int* queries, int queriesSize, int intLength, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] KthPalindrome(int[] queries, int intLength) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} queries
 * @param {number} intLength
 * @return {number[]}
 */
var kthPalindrome = function(queries, intLength) {
    
};
```

### TypeScript

```typescript
function kthPalindrome(queries: number[], intLength: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $queries
     * @param Integer $intLength
     * @return Integer[]
     */
    function kthPalindrome($queries, $intLength) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthPalindrome(_ queries: [Int], _ intLength: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthPalindrome(queries: IntArray, intLength: Int): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> kthPalindrome(List<int> queries, int intLength) {
    
  }
}
```

### Go

```golang
func kthPalindrome(queries []int, intLength int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} queries
# @param {Integer} int_length
# @return {Integer[]}
def kth_palindrome(queries, int_length)
    
end
```

### Scala

```scala
object Solution {
    def kthPalindrome(queries: Array[Int], intLength: Int): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_palindrome(queries: Vec<i32>, int_length: i32) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (kth-palindrome queries intLength)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec kth_palindrome(Queries :: [integer()], IntLength :: integer()) -> [integer()].
kth_palindrome(Queries, IntLength) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_palindrome(queries :: [integer], int_length :: integer) :: [integer]
  def kth_palindrome(queries, int_length) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthPalindrome(queries: Array<Int64>, intLength: Int64): Array<Int64> {

    }
}
```

