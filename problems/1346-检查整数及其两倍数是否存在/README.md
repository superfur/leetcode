# 1346. 检查整数及其两倍数是否存在

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>，请你检查是否存在两个整数&nbsp;<code>N</code> 和 <code>M</code>，满足&nbsp;<code>N</code>&nbsp;是&nbsp;<code>M</code>&nbsp;的两倍（即，<code>N = 2 * M</code>）。</p>

<p>更正式地，检查是否存在两个下标&nbsp;<code>i</code> 和 <code>j</code> 满足：</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [10,2,5,3]
<strong>输出：</strong>true
<strong>解释：</strong>N<code> = 10</code> 是 M<code> = 5 的两倍</code>，即 <code>10 = 2 * 5 。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [7,1,14,11]
<strong>输出：</strong>true
<strong>解释：</strong>N<code> = 14</code> 是 M<code> = 7 的两倍</code>，即 <code>14 = 2 * 7 </code>。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [3,1,7,11]
<strong>输出：</strong>false
<strong>解释：</strong>在该情况下不存在 N 和 M 满足 N = 2 * M 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10^3 &lt;= arr[i] &lt;= 10^3</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 双指针
- 二分查找
- 排序

## 提示

1. Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
2. On each step of the loop check if we have seen the element <code>2 * arr[i]</code> so far.
3. Also check if we have seen <code>arr[i] / 2</code> in case <code>arr[i] % 2 == 0</code>.

## 示例

```
[10,2,5,3]
[3,1,7,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkIfExist(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
```

### C

```c
bool checkIfExist(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckIfExist(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    
};
```

### TypeScript

```typescript
function checkIfExist(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function checkIfExist($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkIfExist(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkIfExist(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkIfExist(List<int> arr) {
    
  }
}
```

### Go

```golang
func checkIfExist(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def check_if_exist(arr)
    
end
```

### Scala

```scala
object Solution {
    def checkIfExist(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_if_exist(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-if-exist arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec check_if_exist(Arr :: [integer()]) -> boolean().
check_if_exist(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_if_exist(arr :: [integer]) :: boolean
  def check_if_exist(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkIfExist(arr: Array<Int64>): Bool {

    }
}
```

