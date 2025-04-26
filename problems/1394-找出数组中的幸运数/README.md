# 1394. 找出数组中的幸运数

## 题目描述

<p>在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。</p>

<p>给你一个整数数组 <code>arr</code>，请你从中找出并返回一个幸运数。</p>

<ul>
	<li>如果数组中存在多个幸运数，只需返回 <strong>最大</strong> 的那个。</li>
	<li>如果数组中不含幸运数，则返回 <strong>-1 </strong>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [2,2,3,4]
<strong>输出：</strong>2
<strong>解释：</strong>数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,2,3,3,3]
<strong>输出：</strong>3
<strong>解释：</strong>1、2 以及 3 都是幸运数，只需要返回其中最大的 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [2,2,2,3,3]
<strong>输出：</strong>-1
<strong>解释：</strong>数组中不存在幸运数。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [5]
<strong>输出：</strong>-1
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [7,7,7,7,7,7,7]
<strong>输出：</strong>7
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 500</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Count the frequency of each integer in the array.
2. Get all lucky numbers and return the largest of them.

## 示例

```
[2,2,3,4]
[1,2,2,3,3,3]
[2,2,2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLucky(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLucky(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
```

### C

```c
int findLucky(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLucky(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    
};
```

### TypeScript

```typescript
function findLucky(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLucky($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLucky(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLucky(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLucky(List<int> arr) {
    
  }
}
```

### Go

```golang
func findLucky(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def find_lucky(arr)
    
end
```

### Scala

```scala
object Solution {
    def findLucky(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-lucky arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_lucky(Arr :: [integer()]) -> integer().
find_lucky(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lucky(arr :: [integer]) :: integer
  def find_lucky(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLucky(arr: Array<Int64>): Int64 {

    }
}
```

