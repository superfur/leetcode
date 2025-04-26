# 2433. 找出前缀异或的原始数组

## 题目描述

<p>给你一个长度为 <code>n</code> 的 <strong>整数</strong> 数组 <code>pref</code> 。找出并返回满足下述条件且长度为 <code>n</code> 的数组<em> </em><code>arr</code> ：</p>

<ul>
	<li><code>pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]</code>.</li>
</ul>

<p>注意 <code>^</code> 表示 <strong>按位异或</strong>（bitwise-xor）运算。</p>

<p>可以证明答案是 <strong>唯一</strong> 的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>pref = [5,2,0,3,1]
<strong>输出：</strong>[5,7,2,3,2]
<strong>解释：</strong>从数组 [5,7,2,3,2] 可以得到如下结果：
- pref[0] = 5
- pref[1] = 5 ^ 7 = 2
- pref[2] = 5 ^ 7 ^ 2 = 0
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>pref = [13]
<strong>输出：</strong>[13]
<strong>解释：</strong>pref[0] = arr[0] = 13
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pref.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= pref[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组

## 提示

1. Consider the following equation: x ^ a = b. How can you find x?
2. Notice that arr[i] ^ pref[i-1] = pref[i]. This is the same as the previous equation.

## 示例

```
[5,2,0,3,1]
[13]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findArray(int[] pref) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findArray(int* pref, int prefSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindArray(int[] pref) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} pref
 * @return {number[]}
 */
var findArray = function(pref) {
    
};
```

### TypeScript

```typescript
function findArray(pref: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $pref
     * @return Integer[]
     */
    function findArray($pref) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findArray(_ pref: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findArray(pref: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findArray(List<int> pref) {
    
  }
}
```

### Go

```golang
func findArray(pref []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} pref
# @return {Integer[]}
def find_array(pref)
    
end
```

### Scala

```scala
object Solution {
    def findArray(pref: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-array pref)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_array(Pref :: [integer()]) -> [integer()].
find_array(Pref) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_array(pref :: [integer]) :: [integer]
  def find_array(pref) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findArray(pref: Array<Int64>): Array<Int64> {

    }
}
```

