# 面试题 17.05.  字母与数字

## 题目描述

<p>给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。</p>

<p>返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

<strong>输出：</strong>["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>["A","A"]

<strong>输出：</strong>[]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>array.length &lt;= 100000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. 是哪个字母或数字并不重要。你可以把该问题简化为只包含 A 和 B 的数组。然后寻找具有相同数量的 A 和 B 的最长子数组。
2. 从蛮力解法开始。
3. 如果你从一开始就计算 A 的个数和 B 的个数会怎样(试着构建数组构成的表并保存到目前为止 A 和 B 的数量)?
4. 当表中 A 和 B 的个数相等时，整个子数组(从索引 0 开始)的 A 和 B 的个数相等。如何使用该表来查找不以索引 0 开始的、符合条件的子数组?
5. 假设在这个表中，索引 i 满足 count(A, 0->i) = 3 和 count(B, 0->i) = 7。这意味着 B 比 A 多 4 个。如果你发现后面的某点 j 具有相同的差值(count(B, 0->j) - count(a, 0->j))，那么这表示子数组中有相同数量的 A 和 B。

## 示例

```
["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
["A","A"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findLongestSubarray(vector<string>& array) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] findLongestSubarray(String[] array) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findLongestSubarray(char** array, int arraySize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] FindLongestSubarray(string[] array) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} array
 * @return {string[]}
 */
var findLongestSubarray = function(array) {
    
};
```

### TypeScript

```typescript
function findLongestSubarray(array: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $array
     * @return String[]
     */
    function findLongestSubarray($array) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLongestSubarray(_ array: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLongestSubarray(array: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findLongestSubarray(List<String> array) {
    
  }
}
```

### Go

```golang
func findLongestSubarray(array []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} array
# @return {String[]}
def find_longest_subarray(array)
    
end
```

### Scala

```scala
object Solution {
    def findLongestSubarray(array: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_longest_subarray(array: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-longest-subarray array)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_longest_subarray(Array :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_longest_subarray(Array) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_longest_subarray(array :: [String.t]) :: [String.t]
  def find_longest_subarray(array) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLongestSubarray(array: Array<String>): Array<String> {

    }
}
```

