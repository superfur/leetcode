# 3361. 两个字符串的切换距离

## 题目描述

<p>给你两个长度相同的字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;，以及两个整数数组&nbsp;<code>nextCost</code> 和&nbsp;<code>previousCost</code>&nbsp;。</p>

<p>一次操作中，你可以选择 <code>s</code>&nbsp;中的一个下标 <code>i</code>&nbsp;，执行以下操作 <strong>之一</strong>&nbsp;：</p>

<ul>
	<li>将&nbsp;<code>s[i]</code>&nbsp;切换为字母表中的下一个字母，如果&nbsp;<code>s[i] == 'z'</code>&nbsp;，切换后得到&nbsp;<code>'a'</code>&nbsp;。操作的代价为&nbsp;<code>nextCost[j]</code>&nbsp;，其中&nbsp;<code>j</code>&nbsp;表示&nbsp;<code>s[i]</code>&nbsp;在字母表中的下标。</li>
	<li>将&nbsp;<code>s[i]</code>&nbsp;切换为字母表中的上一个字母，如果&nbsp;<code>s[i] == 'a'</code>&nbsp;，切换后得到&nbsp;<code>'z'</code>&nbsp;。操作的代价为&nbsp;<code>previousCost[j]</code>&nbsp;，其中&nbsp;<code>j</code> 是&nbsp;<code>s[i]</code>&nbsp;在字母表中的下标。</li>
</ul>

<p><strong>切换距离</strong>&nbsp;指的是将字符串 <code>s</code>&nbsp;变为字符串 <code>t</code>&nbsp;的 <strong>最少</strong>&nbsp;操作代价总和。</p>

<p>请你返回从 <code>s</code>&nbsp;到 <code>t</code>&nbsp;的 <strong>切换距离</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<ul>
	<li>选择下标&nbsp;<code>i = 0</code>&nbsp;并将&nbsp;<code>s[0]</code>&nbsp;向前切换 25 次，总代价为 1 。</li>
	<li>选择下标&nbsp;<code>i = 1</code>&nbsp;并将&nbsp;<code>s[1]</code>&nbsp;向后切换 25 次，总代价为 0 。</li>
	<li>选择下标&nbsp;<code>i = 2</code>&nbsp;并将&nbsp;<code>s[2]</code>&nbsp;向前切换 25 次，总代价为 1 。</li>
	<li>选择下标&nbsp;<code>i = 3</code>&nbsp;并将&nbsp;<code>s[3]</code>&nbsp;向后切换 25 次，总代价为 0 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>31</span></p>

<p><b>解释：</b></p>

<ul>
	<li>选择下标&nbsp;<code>i = 0</code>&nbsp;并将&nbsp;<code>s[0]</code>&nbsp;向前切换 9 次，总代价为 9 。</li>
	<li>选择下标&nbsp;<code>i = 1</code>&nbsp;并将&nbsp;<code>s[1]</code>&nbsp;向后切换 10 次，总代价为 10 。</li>
	<li>选择下标&nbsp;<code>i = 2</code> 并将&nbsp;<code>s[2]</code>&nbsp;向前切换 1 次，总代价为 1 。</li>
	<li>选择下标 <code>i = 3</code> 并将&nbsp;<code>s[3]</code>&nbsp;向后切换 11 次，总代价为 11 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length == t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只包含小写英文字母。</li>
	<li><code>nextCost.length == previousCost.length == 26</code></li>
	<li><code>0 &lt;= nextCost[i], previousCost[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 前缀和

## 提示

1. - For every unordered pair of characters <code>(a, b)</code>, the cost of turning <code>a</code> into <code>b</code> is equal to the minimum between: 
<ul>
<li>If <code>i < j</code>, <code>nextCost[i] + nextCost[i + 1] + … + nextCost[j - 1]</code>, and <code>nextCost[i] + nextCost[i + 1] + … + nextCost[25] + nextCost[0] + … + nextCost[j - 1]</code> otherwise.</li>
    
    <li>If <code>i < j</code>, <code>prevCost[i] + prevCost[i - 1] + … + prevCost[0] + prevCost[25] + … + prevCost[j + 1]</code>, and <code>prevCost[i] + prevCost[i - 1] + … + prevCost[j + 1]</code> otherwise.</li>
    </ul>
    Where <code>i</code> and <code>j</code> are the indices of <code>a</code> and <code>b</code> in the alphabet.
2. The shift distance is the sum of costs of turning <code>s[i]</code> into <code>t[i]</code>.

## 示例

```
"abab"
"baba"
[100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
"leet"
"code"
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& previousCost) {
        
    }
};
```

### Java

```java
class Solution {
    public long shiftDistance(String s, String t, int[] nextCost, int[] previousCost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shiftDistance(self, s, t, nextCost, previousCost):
        """
        :type s: str
        :type t: str
        :type nextCost: List[int]
        :type previousCost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        
```

### C

```c
long long shiftDistance(char* s, char* t, int* nextCost, int nextCostSize, int* previousCost, int previousCostSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long ShiftDistance(string s, string t, int[] nextCost, int[] previousCost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number[]} nextCost
 * @param {number[]} previousCost
 * @return {number}
 */
var shiftDistance = function(s, t, nextCost, previousCost) {
    
};
```

### TypeScript

```typescript
function shiftDistance(s: string, t: string, nextCost: number[], previousCost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer[] $nextCost
     * @param Integer[] $previousCost
     * @return Integer
     */
    function shiftDistance($s, $t, $nextCost, $previousCost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shiftDistance(_ s: String, _ t: String, _ nextCost: [Int], _ previousCost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shiftDistance(s: String, t: String, nextCost: IntArray, previousCost: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int shiftDistance(String s, String t, List<int> nextCost, List<int> previousCost) {
    
  }
}
```

### Go

```golang
func shiftDistance(s string, t string, nextCost []int, previousCost []int) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @param {Integer[]} next_cost
# @param {Integer[]} previous_cost
# @return {Integer}
def shift_distance(s, t, next_cost, previous_cost)
    
end
```

### Scala

```scala
object Solution {
    def shiftDistance(s: String, t: String, nextCost: Array[Int], previousCost: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shift_distance(s: String, t: String, next_cost: Vec<i32>, previous_cost: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (shift-distance s t nextCost previousCost)
  (-> string? string? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec shift_distance(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), NextCost :: [integer()], PreviousCost :: [integer()]) -> integer().
shift_distance(S, T, NextCost, PreviousCost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shift_distance(s :: String.t, t :: String.t, next_cost :: [integer], previous_cost :: [integer]) :: integer
  def shift_distance(s, t, next_cost, previous_cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shiftDistance(s: String, t: String, nextCost: Array<Int64>, previousCost: Array<Int64>): Int64 {

    }
}
```

