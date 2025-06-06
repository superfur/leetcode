# 649. Dota2 参议院

## 题目描述

<p>Dota2 的世界里有两个阵营：<code>Radiant</code>（天辉）和&nbsp;<code>Dire</code>（夜魇）</p>

<p>Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的 <strong>一 </strong>项：</p>

<ul>
	<li><strong>禁止一名参议员的权利</strong>：参议员可以让另一位参议员在这一轮和随后的几轮中丧失<strong> 所有的权利 </strong>。</li>
	<li><strong>宣布胜利</strong>：如果参议员发现有权利投票的参议员都是 <strong>同一个阵营的</strong> ，他可以宣布胜利并决定在游戏中的有关变化。</li>
</ul>

<p>给你一个字符串&nbsp;<code>senate</code> 代表每个参议员的阵营。字母 <code>'R'</code> 和 <code>'D'</code>分别代表了&nbsp;<code>Radiant</code>（天辉）和&nbsp;<code>Dire</code>（夜魇）。然后，如果有 <code>n</code> 个参议员，给定字符串的大小将是&nbsp;<code>n</code>。</p>

<p>以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。</p>

<p>假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是&nbsp;<code>"Radiant"</code> 或 <code>"Dire"</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>senate = "RD"
<strong>输出：</strong>"Radiant"
<strong>解释：
</strong><code>第 1 轮时，第一个参议员来自 Radiant 阵营，他可以使用第一项权利让第二个参议员失去所有权利。
这一轮中，第二个参议员将会被跳过，因为他的权利被禁止了。
第 2 轮时，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人</code>。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>senate = "RDD"
<strong>输出：</strong>"Dire"
<strong>解释：</strong>
第 1 轮时，第一个<code>来自 Radiant 阵营的</code>参议员可以使用第一项权利禁止第二个参议员的权利。
<code>这一轮中，</code>第二个<code>来自 Dire 阵营的</code>参议员会将被跳过，因为他的权利被禁止了。
<code>这一轮中，</code>第三个<code>来自 Dire 阵营的</code>参议员可以使用他的第一项权利禁止第一个参议员的权利。
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == senate.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>senate[i]</code> 为 <code>'R'</code> 或 <code>'D'</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 队列
- 字符串

## 示例

```
"RD"
"RDD"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string predictPartyVictory(string senate) {
        
    }
};
```

### Java

```java
class Solution {
    public String predictPartyVictory(String senate) {
        
    }
}
```

### Python

```python
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
```

### C

```c
char* predictPartyVictory(char* senate) {
    
}
```

### C#

```csharp
public class Solution {
    public string PredictPartyVictory(string senate) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} senate
 * @return {string}
 */
var predictPartyVictory = function(senate) {
    
};
```

### TypeScript

```typescript
function predictPartyVictory(senate: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $senate
     * @return String
     */
    function predictPartyVictory($senate) {
        
    }
}
```

### Swift

```swift
class Solution {
    func predictPartyVictory(_ senate: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun predictPartyVictory(senate: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String predictPartyVictory(String senate) {
    
  }
}
```

### Go

```golang
func predictPartyVictory(senate string) string {
    
}
```

### Ruby

```ruby
# @param {String} senate
# @return {String}
def predict_party_victory(senate)
    
end
```

### Scala

```scala
object Solution {
    def predictPartyVictory(senate: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (predict-party-victory senate)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec predict_party_victory(Senate :: unicode:unicode_binary()) -> unicode:unicode_binary().
predict_party_victory(Senate) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec predict_party_victory(senate :: String.t) :: String.t
  def predict_party_victory(senate) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func predictPartyVictory(senate: String): String {

    }
}
```

