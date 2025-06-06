# 274. H 指数

## 题目描述

<p>给你一个整数数组 <code>citations</code> ，其中 <code>citations[i]</code> 表示研究者的第 <code>i</code> 篇论文被引用的次数。计算并返回该研究者的 <strong><code>h</code><em>&nbsp;</em>指数</strong>。</p>

<p>根据维基百科上&nbsp;<a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：<code>h</code> 代表“高引用次数” ，一名科研人员的 <code>h</code><strong> 指数 </strong>是指他（她）至少发表了 <code>h</code> 篇论文，并且&nbsp;<strong>至少&nbsp;</strong>有 <code>h</code> 篇论文被引用次数大于等于 <code>h</code> 。如果 <code>h</code><em> </em>有多种可能的值，<strong><code>h</code> 指数 </strong>是其中最大的那个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>citations = [3,0,6,1,5]</code>
<strong>输出：</strong>3 
<strong>解释：</strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 <code>3, 0, 6, 1, 5</code> 次。
&nbsp;    由于研究者有 <code>3 </code>篇论文每篇 <strong>至少 </strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用 <strong>不多于</strong> <code>3</code> 次，所以她的 <em>h </em>指数是 <code>3</code>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>citations = [1,3,1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == citations.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= citations[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 计数排序
- 排序

## 提示

1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.

## 示例

```
[3,0,6,1,5]
[1,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        
    }
};
```

### Java

```java
class Solution {
    public int hIndex(int[] citations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
```

### C

```c
int hIndex(int* citations, int citationsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int HIndex(int[] citations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    
};
```

### TypeScript

```typescript
function hIndex(citations: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $citations
     * @return Integer
     */
    function hIndex($citations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hIndex(citations: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int hIndex(List<int> citations) {
    
  }
}
```

### Go

```golang
func hIndex(citations []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
    
end
```

### Scala

```scala
object Solution {
    def hIndex(citations: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (h-index citations)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec h_index(Citations :: [integer()]) -> integer().
h_index(Citations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hIndex(citations: Array<Int64>): Int64 {

    }
}
```

