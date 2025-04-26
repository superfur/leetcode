# 989. 数组形式的整数加法

## 题目描述

<p>整数的 <strong>数组形式</strong> &nbsp;<code>num</code>&nbsp;是按照从左到右的顺序表示其数字的数组。</p>

<ul>
	<li>例如，对于 <code>num = 1321</code> ，数组形式是 <code>[1,3,2,1]</code> 。</li>
</ul>

<p>给定 <code>num</code> ，整数的 <strong>数组形式</strong> ，和整数 <code>k</code> ，返回 <em>整数 <code>num + k</code> 的 <strong>数组形式</strong></em> 。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = [1,2,0,0], k = 34
<strong>输出：</strong>[1,2,3,4]
<strong>解释：</strong>1200 + 34 = 1234
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = [2,7,4], k = 181
<strong>输出：</strong>[4,5,5]
<strong>解释：</strong>274 + 181 = 455
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = [2,1,5], k = 806
<strong>输出：</strong>[1,0,2,1]
<strong>解释：</strong>215 + 806 = 1021
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= num[i] &lt;= 9</code></li>
	<li><code>num</code>&nbsp;不包含任何前导零，除了零本身</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 示例

```
[1,2,0,0]
34
[2,7,4]
181
[2,1,5]
806
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> AddToArrayForm(int[] num, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    
};
```

### TypeScript

```typescript
function addToArrayForm(num: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $num
     * @param Integer $k
     * @return Integer[]
     */
    function addToArrayForm($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addToArrayForm(_ num: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addToArrayForm(num: IntArray, k: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> addToArrayForm(List<int> num, int k) {
    
  }
}
```

### Go

```golang
func addToArrayForm(num []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} num
# @param {Integer} k
# @return {Integer[]}
def add_to_array_form(num, k)
    
end
```

### Scala

```scala
object Solution {
    def addToArrayForm(num: Array[Int], k: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_to_array_form(num: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (add-to-array-form num k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec add_to_array_form(Num :: [integer()], K :: integer()) -> [integer()].
add_to_array_form(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_to_array_form(num :: [integer], k :: integer) :: [integer]
  def add_to_array_form(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addToArrayForm(num: Array<Int64>, k: Int64): ArrayList<Int64> {

    }
}
```

