# 1894. 找到需要补充粉笔的学生编号

## 题目描述

<p>一个班级里有&nbsp;<code>n</code>&nbsp;个学生，编号为 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;。每个学生会依次回答问题，编号为 <code>0</code>&nbsp;的学生先回答，然后是编号为 <code>1</code>&nbsp;的学生，以此类推，直到编号为 <code>n - 1</code>&nbsp;的学生，然后老师会重复这个过程，重新从编号为 <code>0</code>&nbsp;的学生开始回答问题。</p>

<p>给你一个长度为 <code>n</code>&nbsp;且下标从 <code>0</code>&nbsp;开始的整数数组&nbsp;<code>chalk</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。一开始粉笔盒里总共有&nbsp;<code>k</code>&nbsp;支粉笔。当编号为&nbsp;<code>i</code>&nbsp;的学生回答问题时，他会消耗 <code>chalk[i]</code>&nbsp;支粉笔。如果剩余粉笔数量 <strong>严格小于</strong>&nbsp;<code>chalk[i]</code>&nbsp;，那么学生 <code>i</code>&nbsp;需要 <strong>补充</strong>&nbsp;粉笔。</p>

<p>请你返回需要 <strong>补充</strong>&nbsp;粉笔的学生 <strong>编号</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>chalk = [5,1,5], k = 22
<b>输出：</b>0
<strong>解释：</strong>学生消耗粉笔情况如下：
- 编号为 0 的学生使用 5 支粉笔，然后 k = 17 。
- 编号为 1 的学生使用 1 支粉笔，然后 k = 16 。
- 编号为 2 的学生使用 5 支粉笔，然后 k = 11 。
- 编号为 0 的学生使用 5 支粉笔，然后 k = 6 。
- 编号为 1 的学生使用 1 支粉笔，然后 k = 5 。
- 编号为 2 的学生使用 5 支粉笔，然后 k = 0 。
编号为 0 的学生没有足够的粉笔，所以他需要补充粉笔。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>chalk = [3,4,1,2], k = 25
<b>输出：</b>1
<b>解释：</b>学生消耗粉笔情况如下：
- 编号为 0 的学生使用 3 支粉笔，然后 k = 22 。
- 编号为 1 的学生使用 4 支粉笔，然后 k = 18 。
- 编号为 2 的学生使用 1 支粉笔，然后 k = 17 。
- 编号为 3 的学生使用 2 支粉笔，然后 k = 15 。
- 编号为 0 的学生使用 3 支粉笔，然后 k = 12 。
- 编号为 1 的学生使用 4 支粉笔，然后 k = 8 。
- 编号为 2 的学生使用 1 支粉笔，然后 k = 7 。
- 编号为 3 的学生使用 2 支粉笔，然后 k = 5 。
- 编号为 0 的学生使用 3 支粉笔，然后 k = 2 。
编号为 1 的学生没有足够的粉笔，所以他需要补充粉笔。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>chalk.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= chalk[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和
- 模拟

## 提示

1. Subtract the sum of chalk from k until k is less than the sum of chalk.
2. Now iterate over the array. If chalk[i] is less than k, this is the answer. Otherwise, subtract chalk[i] from k and continue.

## 示例

```
[5,1,5]
22
[3,4,1,2]
25
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
```

### C

```c
int chalkReplacer(int* chalk, int chalkSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ChalkReplacer(int[] chalk, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} chalk
 * @param {number} k
 * @return {number}
 */
var chalkReplacer = function(chalk, k) {
    
};
```

### TypeScript

```typescript
function chalkReplacer(chalk: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $chalk
     * @param Integer $k
     * @return Integer
     */
    function chalkReplacer($chalk, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func chalkReplacer(_ chalk: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun chalkReplacer(chalk: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int chalkReplacer(List<int> chalk, int k) {
    
  }
}
```

### Go

```golang
func chalkReplacer(chalk []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} chalk
# @param {Integer} k
# @return {Integer}
def chalk_replacer(chalk, k)
    
end
```

### Scala

```scala
object Solution {
    def chalkReplacer(chalk: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (chalk-replacer chalk k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec chalk_replacer(Chalk :: [integer()], K :: integer()) -> integer().
chalk_replacer(Chalk, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec chalk_replacer(chalk :: [integer], k :: integer) :: integer
  def chalk_replacer(chalk, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func chalkReplacer(chalk: Array<Int64>, k: Int64): Int64 {

    }
}
```

