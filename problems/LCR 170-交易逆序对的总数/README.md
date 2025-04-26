# LCR 170. 交易逆序对的总数

## 题目描述

<p>在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 <code>record</code>，返回其中存在的「交易逆序对」总数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>record = [9, 7, 5, 4, 6]
<strong>输出：</strong>8
<strong>解释：</strong>交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<p><code>0 &lt;= record.length &lt;= 50000</code></p>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 示例

```
[7,5,6,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reversePairs(vector<int>& record) {
        
    }
};
```

### Java

```java
class Solution {
    public int reversePairs(int[] record) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reversePairs(self, record):
        """
        :type record: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        
```

### C

```c
int reversePairs(int* record, int recordSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReversePairs(int[] record) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} record
 * @return {number}
 */
var reversePairs = function(record) {
    
};
```

### TypeScript

```typescript
function reversePairs(record: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $record
     * @return Integer
     */
    function reversePairs($record) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reversePairs(_ record: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reversePairs(record: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reversePairs(List<int> record) {
    
  }
}
```

### Go

```golang
func reversePairs(record []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} record
# @return {Integer}
def reverse_pairs(record)
    
end
```

### Scala

```scala
object Solution {
    def reversePairs(record: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_pairs(record: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-pairs record)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec reverse_pairs(Record :: [integer()]) -> integer().
reverse_pairs(Record) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_pairs(record :: [integer]) :: integer
  def reverse_pairs(record) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reversePairs(record: Array<Int64>): Int64 {

    }
}
```

