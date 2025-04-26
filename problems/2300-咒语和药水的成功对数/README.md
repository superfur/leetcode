# 2300. 咒语和药水的成功对数

## 题目描述

<p>给你两个正整数数组&nbsp;<code>spells</code> 和&nbsp;<code>potions</code>&nbsp;，长度分别为&nbsp;<code>n</code> 和&nbsp;<code>m</code>&nbsp;，其中&nbsp;<code>spells[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个咒语的能量强度，<code>potions[j]</code>&nbsp;表示第&nbsp;<code>j</code>&nbsp;瓶药水的能量强度。</p>

<p>同时给你一个整数&nbsp;<code>success</code>&nbsp;。一个咒语和药水的能量强度 <strong>相乘</strong> 如果&nbsp;<strong>大于等于</strong>&nbsp;<code>success</code>&nbsp;，那么它们视为一对&nbsp;<strong>成功</strong>&nbsp;的组合。</p>

<p>请你返回一个长度为 <code>n</code>&nbsp;的整数数组<em>&nbsp;</em><code>pairs</code>，其中<em>&nbsp;</em><code>pairs[i]</code>&nbsp;是能跟第 <code>i</code>&nbsp;个咒语成功组合的 <b>药水</b>&nbsp;数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>spells = [5,1,3], potions = [1,2,3,4,5], success = 7
<b>输出：</b>[4,0,3]
<strong>解释：</strong>
- 第 0 个咒语：5 * [1,2,3,4,5] = [5,<em><strong>10</strong></em>,<em><strong>15</strong></em>,<em><strong>20</strong></em>,<em><strong>25</strong></em>] 。总共 4 个成功组合。
- 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
- 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,<em><strong>9</strong></em>,<em><strong>12</strong></em>,<em><strong>15</strong></em>] 。总共 3 个成功组合。
所以返回 [4,0,3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>spells = [3,1,2], potions = [8,5,8], success = 16
<b>输出：</b>[2,0,2]
<strong>解释：</strong>
- 第 0 个咒语：3 * [8,5,8] = [<em><strong>24</strong></em>,15,<em><strong>24</strong></em>] 。总共 2 个成功组合。
- 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
- 第 2 个咒语：2 * [8,5,8] = [<em><strong>16</strong></em>,10,<em><strong>16</strong></em>] 。总共 2 个成功组合。
所以返回 [2,0,2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == spells.length</code></li>
	<li><code>m == potions.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= spells[i], potions[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= success &lt;= 10<sup>10</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
2. Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
3. We can efficiently do this by sorting the potions based on strength and using binary search.

## 示例

```
[5,1,3]
[1,2,3,4,5]
7
[3,1,2]
[8,5,8]
16
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        
    }
}
```

### Python

```python
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* successfulPairs(int* spells, int spellsSize, int* potions, int potionsSize, long long success, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    
};
```

### TypeScript

```typescript
function successfulPairs(spells: number[], potions: number[], success: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $spells
     * @param Integer[] $potions
     * @param Integer $success
     * @return Integer[]
     */
    function successfulPairs($spells, $potions, $success) {
        
    }
}
```

### Swift

```swift
class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> successfulPairs(List<int> spells, List<int> potions, int success) {
    
  }
}
```

### Go

```golang
func successfulPairs(spells []int, potions []int, success int64) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} spells
# @param {Integer[]} potions
# @param {Integer} success
# @return {Integer[]}
def successful_pairs(spells, potions, success)
    
end
```

### Scala

```scala
object Solution {
    def successfulPairs(spells: Array[Int], potions: Array[Int], success: Long): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (successful-pairs spells potions success)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec successful_pairs(Spells :: [integer()], Potions :: [integer()], Success :: integer()) -> [integer()].
successful_pairs(Spells, Potions, Success) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec successful_pairs(spells :: [integer], potions :: [integer], success :: integer) :: [integer]
  def successful_pairs(spells, potions, success) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func successfulPairs(spells: Array<Int64>, potions: Array<Int64>, success: Int64): Array<Int64> {

    }
}
```

