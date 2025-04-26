# 1125. 最小的必要团队

## 题目描述

<p>作为项目经理，你规划了一份需求的技能清单 <code>req_skills</code>，并打算从备选人员名单 <code>people</code> 中选出些人组成一个「必要团队」（ 编号为 <code>i</code> 的备选人员 <code>people[i]</code> 含有一份该备选人员掌握的技能列表）。</p>

<p>所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 <code>req_skills</code> 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：</p>

<ul>
	<li>例如，团队 <code>team = [0, 1, 3]</code> 表示掌握技能分别为 <code>people[0]</code>，<code>people[1]</code>，和 <code>people[3]</code> 的备选人员。</li>
</ul>

<p>请你返回 <strong>任一</strong> 规模最小的必要团队，团队成员用人员编号表示。你可以按 <strong>任意顺序</strong> 返回答案，题目数据保证答案存在。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
<strong>输出：</strong>[0,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
<strong>输出：</strong>[1,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= req_skills.length <= 16</code></li>
	<li><code>1 <= req_skills[i].length <= 16</code></li>
	<li><code>req_skills[i]</code> 由小写英文字母组成</li>
	<li><code>req_skills</code> 中的所有字符串 <strong>互不相同</strong></li>
	<li><code>1 <= people.length <= 60</code></li>
	<li><code>0 <= people[i].length <= 16</code></li>
	<li><code>1 <= people[i][j].length <= 16</code></li>
	<li><code>people[i][j]</code> 由小写英文字母组成</li>
	<li><code>people[i]</code> 中的所有字符串 <strong>互不相同</strong></li>
	<li><code>people[i]</code> 中的每个技能是 <code>req_skills</code> 中的技能</li>
	<li>题目数据保证「必要团队」一定存在</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. Do a bitmask DP.
2. For each person, for each set of skills, we can update our understanding of a minimum set of people needed to perform this set of skills.

## 示例

```
["java","nodejs","reactjs"]
[["java"],["nodejs"],["nodejs","reactjs"]]
["algorithms","math","java","reactjs","csharp","aws"]
[["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& people) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestSufficientTeam(char** req_skills, int req_skillsSize, char*** people, int peopleSize, int* peopleColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SmallestSufficientTeam(string[] req_skills, IList<IList<string>> people) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} req_skills
 * @param {string[][]} people
 * @return {number[]}
 */
var smallestSufficientTeam = function(req_skills, people) {
    
};
```

### TypeScript

```typescript
function smallestSufficientTeam(req_skills: string[], people: string[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $req_skills
     * @param String[][] $people
     * @return Integer[]
     */
    function smallestSufficientTeam($req_skills, $people) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestSufficientTeam(_ req_skills: [String], _ people: [[String]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestSufficientTeam(req_skills: Array<String>, people: List<List<String>>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> smallestSufficientTeam(List<String> req_skills, List<List<String>> people) {
    
  }
}
```

### Go

```golang
func smallestSufficientTeam(req_skills []string, people [][]string) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} req_skills
# @param {String[][]} people
# @return {Integer[]}
def smallest_sufficient_team(req_skills, people)
    
end
```

### Scala

```scala
object Solution {
    def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_sufficient_team(req_skills: Vec<String>, people: Vec<Vec<String>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-sufficient-team req_skills people)
  (-> (listof string?) (listof (listof string?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec smallest_sufficient_team(Req_skills :: [unicode:unicode_binary()], People :: [[unicode:unicode_binary()]]) -> [integer()].
smallest_sufficient_team(Req_skills, People) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_sufficient_team(req_skills :: [String.t], people :: [[String.t]]) :: [integer]
  def smallest_sufficient_team(req_skills, people) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestSufficientTeam(req_skills: Array<String>, people: ArrayList<ArrayList<String>>): Array<Int64> {

    }
}
```

