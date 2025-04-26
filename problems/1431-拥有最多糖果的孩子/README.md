# 1431. 拥有最多糖果的孩子

## 题目描述

<p>有&nbsp;<code>n</code>&nbsp;个有糖果的孩子。给你一个数组&nbsp;<code>candies</code>，其中&nbsp;<code>candies[i]</code>&nbsp;代表第 <code>i</code> 个孩子拥有的糖果数目，和一个整数&nbsp;<code>extraCandies</code>&nbsp;表示你所有的额外糖果的数量。</p>

<p>返回一个长度为&nbsp;<code>n</code>&nbsp;的布尔数组 <code>result</code>，如果把所有的&nbsp;<code>extraCandies</code>&nbsp;给第&nbsp;<code>i</code>&nbsp;个孩子之后，他会拥有所有孩子中&nbsp;<strong>最多&nbsp;</strong>的糖果，那么&nbsp;<code>result[i]</code>&nbsp;为&nbsp;<code>true</code>，否则为 <code>false</code>。</p>

<p>注意，允许有多个孩子同时拥有 <strong>最多</strong>&nbsp;的糖果数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>candies = [2,3,5,1,3], extraCandies = 3
<strong>输出：</strong>[true,true,true,false,true] 
<strong>解释：</strong>如果你把额外的糖果全部给：
孩子 1，将有 2 + 3 = 5 个糖果，是孩子中最多的。
孩子 2，将有 3 + 3 = 6 个糖果，是孩子中最多的。
孩子 3，将有 5 + 3 = 8 个糖果，是孩子中最多的。
孩子 4，将有 1 + 3 = 4 个糖果，不是孩子中最多的。
孩子 5，将有 3 + 3 = 6 个糖果，是孩子中最多的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>candies = [4,2,1,1,2], extraCandies = 1
<strong>输出：</strong>[true,false,false,false,false] 
<strong>解释：</strong>只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>candies = [12,1,12], extraCandies = 10
<strong>输出：</strong>[true,false,true]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == candies.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= candies[i] &lt;= 100</code></li>
	<li><code>1 &lt;= extraCandies &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i].

## 示例

```
[2,3,5,1,3]
3
[4,2,1,1,2]
1
[12,1,12]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    
};
```

### TypeScript

```typescript
function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies($candies, $extraCandies) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    
  }
}
```

### Go

```golang
func kidsWithCandies(candies []int, extraCandies int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} candies
# @param {Integer} extra_candies
# @return {Boolean[]}
def kids_with_candies(candies, extra_candies)
    
end
```

### Scala

```scala
object Solution {
    def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (kids-with-candies candies extraCandies)
  (-> (listof exact-integer?) exact-integer? (listof boolean?))
  )
```

### Erlang

```erlang
-spec kids_with_candies(Candies :: [integer()], ExtraCandies :: integer()) -> [boolean()].
kids_with_candies(Candies, ExtraCandies) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kids_with_candies(candies :: [integer], extra_candies :: integer) :: [boolean]
  def kids_with_candies(candies, extra_candies) do
    
  end
end
```

