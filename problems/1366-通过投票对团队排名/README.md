# 1366. 通过投票对团队排名

## 题目描述

<p>现在有一个特殊的排名系统，依据参赛团队在投票人心中的次序进行排名，每个投票者都需要按从高到低的顺序对参与排名的所有团队进行排位。</p>

<p>排名规则如下：</p>

<ul>
	<li>参赛团队的排名次序依照其所获「排位第一」的票的多少决定。如果存在多个团队并列的情况，将继续考虑其「排位第二」的票的数量。以此类推，直到不再存在并列的情况。</li>
	<li>如果在考虑完所有投票情况后仍然出现并列现象，则根据团队字母的字母顺序进行排名。</li>
</ul>

<p>给你一个字符串数组&nbsp;<code>votes</code> 代表全体投票者给出的排位情况，请你根据上述排名规则对所有参赛团队进行排名。</p>

<p>请你返回能表示按排名系统 <strong>排序后</strong> 的所有团队排名的字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>votes = ["ABC","ACB","ABC","ACB","ACB"]
<strong>输出：</strong>"ACB"
<strong>解释：</strong>
A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
B 队获得两票「排位第二」，三票「排位第三」。
C 队获得三票「排位第二」，两票「排位第三」。
由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>votes = ["WXYZ","XYZW"]
<strong>输出：</strong>"XWYZ"
<strong>解释：</strong>
X 队在并列僵局打破后成为排名第一的团队。X 队和 W 队的「排位第一」票数一样，但是 X 队有一票「排位第二」，而 W 没有获得「排位第二」。 
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
<strong>输出：</strong>"ZMNAGUEDSJYLBOPHRQICWFXTVK"
<strong>解释：</strong>只有一个投票者，所以排名完全按照他的意愿。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= votes.length &lt;= 1000</code></li>
	<li><code>1 &lt;= votes[i].length &lt;= 26</code></li>
	<li><code>votes[i].length ==&nbsp;votes[j].length</code> for&nbsp;<code>0 &lt;= i, j &lt; votes.length</code></li>
	<li><code>votes[i][j]</code>&nbsp;是英文 <strong>大写</strong> 字母</li>
	<li><code>votes[i]</code>&nbsp;中的所有字母都是唯一的</li>
	<li><code>votes[0]</code>&nbsp;中出现的所有字母 <strong>同样也</strong> 出现在&nbsp;<code>votes[j]</code>&nbsp;中，其中&nbsp;<code>1 &lt;= j &lt; votes.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 计数
- 排序

## 提示

1. Build array rank where rank[i][j] is the number of votes for team i to be the j-th rank.
2. Sort the teams by rank array. if rank array is the same for two or more teams, sort them by the ID in ascending order.

## 示例

```
["ABC","ACB","ABC","ACB","ACB"]
["WXYZ","XYZW"]
["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string rankTeams(vector<string>& votes) {
        
    }
};
```

### Java

```java
class Solution {
    public String rankTeams(String[] votes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
```

### C

```c
char* rankTeams(char** votes, int votesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string RankTeams(string[] votes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} votes
 * @return {string}
 */
var rankTeams = function(votes) {
    
};
```

### TypeScript

```typescript
function rankTeams(votes: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $votes
     * @return String
     */
    function rankTeams($votes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rankTeams(_ votes: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rankTeams(votes: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String rankTeams(List<String> votes) {
    
  }
}
```

### Go

```golang
func rankTeams(votes []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} votes
# @return {String}
def rank_teams(votes)
    
end
```

### Scala

```scala
object Solution {
    def rankTeams(votes: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (rank-teams votes)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec rank_teams(Votes :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
rank_teams(Votes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rank_teams(votes :: [String.t]) :: String.t
  def rank_teams(votes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rankTeams(votes: Array<String>): String {

    }
}
```

