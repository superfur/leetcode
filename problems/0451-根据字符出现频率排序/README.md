# 451. 根据字符出现频率排序

## 题目描述

<p>给定一个字符串 <code>s</code> ，根据字符出现的 <strong>频率</strong> 对其进行 <strong>降序排序</strong> 。一个字符出现的 <strong>频率</strong> 是它出现在字符串中的次数。</p>

<p>返回 <em>已排序的字符串&nbsp;</em>。如果有多个答案，返回其中任何一个。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入: </strong>s = "tree"
<strong>输出: </strong>"eert"
<strong>解释: </strong>'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "cccaaa"
<strong>输出: </strong>"cccaaa"
<strong>解释: </strong>'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
</pre>

<p><strong class="example">示例 3:</strong></p>

<pre>
<strong>输入: </strong>s = "Aabb"
<strong>输出: </strong>"bbAa"
<strong>解释: </strong>此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;由大小写英文字母和数字组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 桶排序
- 计数
- 排序
- 堆（优先队列）

## 示例

```
"tree"
"cccaaa"
"Aabb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string frequencySort(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String frequencySort(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def frequencySort(self, s: str) -> str:
        
```

### C

```c
char* frequencySort(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string FrequencySort(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    
};
```

### TypeScript

```typescript
function frequencySort(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function frequencySort($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func frequencySort(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun frequencySort(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String frequencySort(String s) {
    
  }
}
```

### Go

```golang
func frequencySort(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def frequency_sort(s)
    
end
```

### Scala

```scala
object Solution {
    def frequencySort(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn frequency_sort(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (frequency-sort s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec frequency_sort(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
frequency_sort(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec frequency_sort(s :: String.t) :: String.t
  def frequency_sort(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func frequencySort(s: String): String {

    }
}
```

