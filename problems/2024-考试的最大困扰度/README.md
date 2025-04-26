# 2024. 考试的最大困扰度

## 题目描述

<p>一位老师正在出一场由 <code>n</code>&nbsp;道判断题构成的考试，每道题的答案为 true （用 <code><span style="">'T'</span></code> 表示）或者 false （用 <code>'F'</code>&nbsp;表示）。老师想增加学生对自己做出答案的不确定性，方法是&nbsp;<strong>最大化&nbsp;</strong>有 <strong>连续相同</strong>&nbsp;结果的题数。（也就是连续出现 true 或者连续出现 false）。</p>

<p>给你一个字符串&nbsp;<code>answerKey</code>&nbsp;，其中&nbsp;<code>answerKey[i]</code>&nbsp;是第 <code>i</code>&nbsp;个问题的正确结果。除此以外，还给你一个整数 <code>k</code>&nbsp;，表示你能进行以下操作的最多次数：</p>

<ul>
	<li>每次操作中，将问题的正确答案改为&nbsp;<code>'T'</code> 或者&nbsp;<code>'F'</code>&nbsp;（也就是将 <code>answerKey[i]</code> 改为&nbsp;<code>'T'</code>&nbsp;或者&nbsp;<code>'F'</code>&nbsp;）。</li>
</ul>

<p>请你返回在不超过 <code>k</code>&nbsp;次操作的情况下，<strong>最大</strong>&nbsp;连续 <code>'T'</code>&nbsp;或者 <code>'F'</code>&nbsp;的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>answerKey = "TTFF", k = 2
<b>输出：</b>4
<b>解释：</b>我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "<em><strong>TTTT</strong></em>" 。
总共有四个连续的 'T' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>answerKey = "TFFT", k = 1
<b>输出：</b>3
<b>解释：</b>我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "<em><strong>FFF</strong></em>T" 。
或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "T<em><strong>FFF</strong></em>" 。
两种情况下，都有三个连续的 'F' 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>answerKey = "TTFTTFTT", k = 1
<b>输出：</b>5
<b>解释：</b>我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "<em><strong>TTTTT</strong></em>FTT" 。
或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTF<em><strong>TTTTT</strong></em>" 。
两种情况下，都有五个连续的 'T' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == answerKey.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>answerKey[i]</code>&nbsp;要么是&nbsp;<code>'T'</code> ，要么是&nbsp;<code>'F'</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. Can we use the maximum length at the previous position to help us find the answer for the current position?
2. Can we use binary search to find the maximum consecutive same answer at every position?

## 示例

```
"TTFF"
2
"TFFT"
1
"TTFTTFTT"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
```

### C

```c
int maxConsecutiveAnswers(char* answerKey, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxConsecutiveAnswers(string answerKey, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} answerKey
 * @param {number} k
 * @return {number}
 */
var maxConsecutiveAnswers = function(answerKey, k) {
    
};
```

### TypeScript

```typescript
function maxConsecutiveAnswers(answerKey: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $answerKey
     * @param Integer $k
     * @return Integer
     */
    function maxConsecutiveAnswers($answerKey, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxConsecutiveAnswers(_ answerKey: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxConsecutiveAnswers(answerKey: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxConsecutiveAnswers(String answerKey, int k) {
    
  }
}
```

### Go

```golang
func maxConsecutiveAnswers(answerKey string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} answer_key
# @param {Integer} k
# @return {Integer}
def max_consecutive_answers(answer_key, k)
    
end
```

### Scala

```scala
object Solution {
    def maxConsecutiveAnswers(answerKey: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-consecutive-answers answerKey k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_consecutive_answers(AnswerKey :: unicode:unicode_binary(), K :: integer()) -> integer().
max_consecutive_answers(AnswerKey, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_consecutive_answers(answer_key :: String.t, k :: integer) :: integer
  def max_consecutive_answers(answer_key, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxConsecutiveAnswers(answerKey: String, k: Int64): Int64 {

    }
}
```

