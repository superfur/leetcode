# 2100. 适合野炊的日子

## 题目描述

<p>你和朋友们准备去野炊。给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>security</code>&nbsp;，其中&nbsp;<code>security[i]</code>&nbsp;是第 <code>i</code>&nbsp;天的建议出行指数。日子从 <code>0</code>&nbsp;开始编号。同时给你一个整数&nbsp;<code>time</code>&nbsp;。</p>

<p>如果第 <code>i</code>&nbsp;天满足以下所有条件，我们称它为一个适合野炊的日子：</p>

<ul>
	<li>第 <code>i</code>&nbsp;天前和后都分别至少有 <code>time</code>&nbsp;天。</li>
	<li>第 <code>i</code>&nbsp;天前连续 <code>time</code>&nbsp;天建议出行指数都是非递增的。</li>
	<li>第 <code>i</code>&nbsp;天后连续 <code>time</code>&nbsp;天建议出行指数都是非递减的。</li>
</ul>

<p>更正式的，第 <code>i</code> 天是一个适合野炊的日子当且仅当：<code>security[i - time] &gt;= security[i - time + 1] &gt;= ... &gt;= security[i] &lt;= ... &lt;= security[i + time - 1] &lt;= security[i + time]</code>.</p>

<p>请你返回一个数组，包含 <strong>所有</strong> 适合野炊的日子（下标从 <strong>0</strong>&nbsp;开始）。返回的日子可以 <strong>任意</strong>&nbsp;顺序排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>security = [5,3,3,3,5,6,2], time = 2
<b>输出：</b>[2,3]
<strong>解释：</strong>
第 2 天，我们有 security[0] &gt;= security[1] &gt;= security[2] &lt;= security[3] &lt;= security[4] 。
第 3 天，我们有 security[1] &gt;= security[2] &gt;= security[3] &lt;= security[4] &lt;= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合野炊的日子。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>security = [1,1,1,1,1], time = 0
<b>输出：</b>[0,1,2,3,4]
<strong>解释：</strong>
因为 time 等于 0 ，所以每一天都是适合野炊的日子，所以返回每一天。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>security = [1,2,3,4,5,6], time = 2
<b>输出：</b>[]
<strong>解释：</strong>
没有任何一天的前 2 天建议出行指数是非递增的。
所以没有适合野炊的日子，返回空数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= security.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= security[i], time &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 前缀和

## 提示

1. The trivial solution is to check the time days before and after each day. There are a lot of repeated operations using this solution. How could we optimize this solution?
2. We can use precomputation to make the solution faster.
3. Use an array to store the number of days before the i<sup>th</sup> day that is non-increasing, and another array to store the number of days after the i<sup>th</sup> day that is non-decreasing.

## 示例

```
[5,3,3,3,5,6,2]
2
[1,1,1,1,1]
0
[1,2,3,4,5,6]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodDaysToRobBank(int* security, int securitySize, int time, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GoodDaysToRobBank(int[] security, int time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} security
 * @param {number} time
 * @return {number[]}
 */
var goodDaysToRobBank = function(security, time) {
    
};
```

### TypeScript

```typescript
function goodDaysToRobBank(security: number[], time: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $security
     * @param Integer $time
     * @return Integer[]
     */
    function goodDaysToRobBank($security, $time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func goodDaysToRobBank(_ security: [Int], _ time: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun goodDaysToRobBank(security: IntArray, time: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> goodDaysToRobBank(List<int> security, int time) {
    
  }
}
```

### Go

```golang
func goodDaysToRobBank(security []int, time int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} security
# @param {Integer} time
# @return {Integer[]}
def good_days_to_rob_bank(security, time)
    
end
```

### Scala

```scala
object Solution {
    def goodDaysToRobBank(security: Array[Int], time: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn good_days_to_rob_bank(security: Vec<i32>, time: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (good-days-to-rob-bank security time)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec good_days_to_rob_bank(Security :: [integer()], Time :: integer()) -> [integer()].
good_days_to_rob_bank(Security, Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec good_days_to_rob_bank(security :: [integer], time :: integer) :: [integer]
  def good_days_to_rob_bank(security, time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func goodDaysToRobBank(security: Array<Int64>, time: Int64): ArrayList<Int64> {

    }
}
```

