# 3043. 最长公共前缀的长度

## 题目描述

<p>给你两个 <strong>正整数 </strong>数组 <code>arr1</code> 和 <code>arr2</code> 。</p>

<p>正整数的 <strong>前缀 </strong>是其 <strong>最左边 </strong>的一位或多位数字组成的整数。例如，<code>123</code> 是整数 <code>12345</code> 的前缀，而 <code>234</code><strong> 不是 </strong>。</p>

<p>设若整数 <code>c</code> 是整数 <code>a</code> 和 <code>b</code> 的<strong> 公共前缀 </strong>，那么 <code>c</code> 需要同时是 <code>a</code> 和 <code>b</code> 的前缀。例如，<code>5655359</code> 和 <code>56554</code> 有公共前缀 <code>565</code>&nbsp;和 <code>5655</code>，而 <code>1223</code> 和 <code>43456</code><strong> 没有 </strong>公共前缀。</p>

<p>你需要找出属于 <code>arr1</code> 的整数 <code>x</code> 和属于 <code>arr2</code> 的整数 <code>y</code> 组成的所有数对 <code>(x, y)</code> 之中最长的公共前缀的长度。</p>

<p>返回所有数对之中最长公共前缀的长度。如果它们之间不存在公共前缀，则返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,10,100], arr2 = [1000]
<strong>输出：</strong>3
<strong>解释：</strong>存在 3 个数对 (arr1[i], arr2[j]) ：
- (1, 1000) 的最长公共前缀是 1 。
- (10, 1000) 的最长公共前缀是 10 。
- (100, 1000) 的最长公共前缀是 100 。
最长的公共前缀是 100 ，长度为 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,2,3], arr2 = [4,4,4]
<strong>输出：</strong>0
<strong>解释：</strong>任何数对 (arr1[i], arr2[j]) 之中都不存在公共前缀，因此返回 0 。
请注意，同一个数组内元素之间的公共前缀不在考虑范围内。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr1[i], arr2[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. Put all the possible prefixes of each element in <code>arr1</code> into a HashSet.
2. For all the possible prefixes of each element in <code>arr2</code>, check if it exists in the HashSet.

## 示例

```
[1,10,100]
[1000]
[1,2,3]
[4,4,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
```

### C

```c
int longestCommonPrefix(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestCommonPrefix(int[] arr1, int[] arr2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var longestCommonPrefix = function(arr1, arr2) {
    
};
```

### TypeScript

```typescript
function longestCommonPrefix(arr1: number[], arr2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function longestCommonPrefix($arr1, $arr2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestCommonPrefix(_ arr1: [Int], _ arr2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestCommonPrefix(arr1: IntArray, arr2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestCommonPrefix(List<int> arr1, List<int> arr2) {
    
  }
}
```

### Go

```golang
func longestCommonPrefix(arr1 []int, arr2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def longest_common_prefix(arr1, arr2)
    
end
```

### Scala

```scala
object Solution {
    def longestCommonPrefix(arr1: Array[Int], arr2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-common-prefix arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_common_prefix(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
longest_common_prefix(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(arr1 :: [integer], arr2 :: [integer]) :: integer
  def longest_common_prefix(arr1, arr2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestCommonPrefix(arr1: Array<Int64>, arr2: Array<Int64>): Int64 {

    }
}
```

