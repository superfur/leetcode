# 2007. 从双倍数组中还原原数组

## 题目描述

<p>一个整数数组&nbsp;<code>original</code>&nbsp;可以转变成一个 <strong>双倍</strong>&nbsp;数组&nbsp;<code>changed</code>&nbsp;，转变方式为将 <code>original</code>&nbsp;中每个元素 <strong>值乘以 2 </strong>加入数组中，然后将所有元素 <strong>随机打乱</strong>&nbsp;。</p>

<p>给你一个数组&nbsp;<code>changed</code>&nbsp;，如果&nbsp;<code>change</code>&nbsp;是&nbsp;<strong>双倍</strong>&nbsp;数组，那么请你返回&nbsp;<code>original</code>数组，否则请返回空数组。<code>original</code>&nbsp;的元素可以以&nbsp;<strong>任意</strong>&nbsp;顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>changed = [1,3,4,2,6,8]
<b>输出：</b>[1,3,4]
<b>解释：</b>一个可能的 original 数组为 [1,3,4] :
- 将 1 乘以 2 ，得到 1 * 2 = 2 。
- 将 3 乘以 2 ，得到 3 * 2 = 6 。
- 将 4 乘以 2 ，得到 4 * 2 = 8 。
其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>changed = [6,3,0,1]
<b>输出：</b>[]
<b>解释：</b>changed 不是一个双倍数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>changed = [1]
<b>输出：</b>[]
<b>解释：</b>changed 不是一个双倍数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= changed.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= changed[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 排序

## 提示

1. If changed is a doubled array, you should be able to delete elements and their doubled values until the array is empty.
2. Which element is guaranteed to not be a doubled value? It is the smallest element.
3. After removing the smallest element and its double from changed, is there another number that is guaranteed to not be a doubled value?

## 示例

```
[1,3,4,2,6,8]
[6,3,0,1]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findOriginalArray(int[] changed) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findOriginalArray(int* changed, int changedSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindOriginalArray(int[] changed) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} changed
 * @return {number[]}
 */
var findOriginalArray = function(changed) {
    
};
```

### TypeScript

```typescript
function findOriginalArray(changed: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $changed
     * @return Integer[]
     */
    function findOriginalArray($changed) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findOriginalArray(changed: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findOriginalArray(List<int> changed) {
    
  }
}
```

### Go

```golang
func findOriginalArray(changed []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} changed
# @return {Integer[]}
def find_original_array(changed)
    
end
```

### Scala

```scala
object Solution {
    def findOriginalArray(changed: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_original_array(changed: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-original-array changed)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_original_array(Changed :: [integer()]) -> [integer()].
find_original_array(Changed) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_original_array(changed :: [integer]) :: [integer]
  def find_original_array(changed) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findOriginalArray(changed: Array<Int64>): Array<Int64> {

    }
}
```

