# 2296. 设计一个文本编辑器

## 题目描述

<p>请你设计一个带光标的文本编辑器，它可以实现以下功能：</p>

<ul>
	<li><strong>添加：</strong>在光标所在处添加文本。</li>
	<li><strong>删除：</strong>在光标所在处删除文本（模拟键盘的删除键）。</li>
	<li><strong>移动：</strong>将光标往左或者往右移动。</li>
</ul>

<p>当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候&nbsp;<code>0 &lt;= cursor.position &lt;= currentText.length</code>&nbsp;都成立。</p>

<p>请你实现&nbsp;<code>TextEditor</code>&nbsp;类：</p>

<ul>
	<li><code>TextEditor()</code>&nbsp;用空文本初始化对象。</li>
	<li><code>void addText(string text)</code>&nbsp;将&nbsp;<code>text</code>&nbsp;添加到光标所在位置。添加完后光标在&nbsp;<code>text</code>&nbsp;的右边。</li>
	<li><code>int deleteText(int k)</code>&nbsp;删除光标左边&nbsp;<code>k</code>&nbsp;个字符。返回实际删除的字符数目。</li>
	<li><code>string cursorLeft(int k)</code> 将光标向左移动&nbsp;<code>k</code>&nbsp;次。返回移动后光标左边&nbsp;<code>min(10, len)</code>&nbsp;个字符，其中&nbsp;<code>len</code>&nbsp;是光标左边的字符数目。</li>
	<li><code>string cursorRight(int k)</code>&nbsp;将光标向右移动&nbsp;<code>k</code>&nbsp;次。返回移动后光标左边&nbsp;<code>min(10, len)</code>&nbsp;个字符，其中&nbsp;<code>len</code>&nbsp;是光标左边的字符数目。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
<strong>输出：</strong>
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

<strong>解释：</strong>
TextEditor textEditor = new TextEditor(); // 当前 text 为 "|" 。（'|' 字符表示光标）
textEditor.addText("leetcode"); // 当前文本为 "leetcode|" 。
textEditor.deleteText(4); // 返回 4
                          // 当前文本为 "leet|" 。
                          // 删除了 4 个字符。
textEditor.addText("practice"); // 当前文本为 "leetpractice|" 。
textEditor.cursorRight(3); // 返回 "etpractice"
                           // 当前文本为 "leetpractice|". 
                           // 光标无法移动到文本以外，所以无法移动。
                           // "etpractice" 是光标左边的 10 个字符。
textEditor.cursorLeft(8); // 返回 "leet"
                          // 当前文本为 "leet|practice" 。
                          // "leet" 是光标左边的 min(10, 4) = 4 个字符。
textEditor.deleteText(10); // 返回 4
                           // 当前文本为 "|practice" 。
                           // 只有 4 个字符被删除了。
textEditor.cursorLeft(2); // 返回 ""
                          // 当前文本为 "|practice" 。
                          // 光标无法移动到文本以外，所以无法移动。
                          // "" 是光标左边的 min(10, 0) = 0 个字符。
textEditor.cursorRight(6); // 返回 "practi"
                           // 当前文本为 "practi|ce" 。
                           // "practi" 是光标左边的 min(10, 6) = 6 个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length, k &lt;= 40</code></li>
	<li><code>text</code>&nbsp;只含有小写英文字母。</li>
	<li>调用 <code>addText</code>&nbsp;，<code>deleteText</code>&nbsp;，<code>cursorLeft</code> 和&nbsp;<code>cursorRight</code>&nbsp;的 <strong>总</strong> 次数不超过&nbsp;<code>2 * 10<sup>4</sup></code>&nbsp;次。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能设计并实现一个每次调用时间复杂度为 <code>O(k)</code> 的解决方案吗？</p>


## 难度

Hard

## 标签

- 栈
- 设计
- 链表
- 字符串
- 双向链表
- 模拟

## 提示

1. Making changes in the middle of some data structures is generally harder than changing the front/back of the same data structure.
2. Can you partition your data structure (text with cursor) into two parts, such that each part changes only near its ends?
3. Can you think of a data structure that supports efficient removals/additions to the front/back?
4. Try to solve the problem with two deques by maintaining the prefix and the suffix separately.

## 示例

```
["TextEditor","addText","deleteText","addText","cursorRight","cursorLeft","deleteText","cursorLeft","cursorRight"]
[[],["leetcode"],[4],["practice"],[3],[8],[10],[2],[6]]
```

## 示例代码

### C++

```cpp
class TextEditor {
public:
    TextEditor() {
        
    }
    
    void addText(string text) {
        
    }
    
    int deleteText(int k) {
        
    }
    
    string cursorLeft(int k) {
        
    }
    
    string cursorRight(int k) {
        
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
```

### Java

```java
class TextEditor {

    public TextEditor() {
        
    }
    
    public void addText(String text) {
        
    }
    
    public int deleteText(int k) {
        
    }
    
    public String cursorLeft(int k) {
        
    }
    
    public String cursorRight(int k) {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */
```

### Python

```python
class TextEditor(object):

    def __init__(self):
        

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
```

### Python3

```python3
class TextEditor:

    def __init__(self):
        

    def addText(self, text: str) -> None:
        

    def deleteText(self, k: int) -> int:
        

    def cursorLeft(self, k: int) -> str:
        

    def cursorRight(self, k: int) -> str:
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
```

### C

```c



typedef struct {
    
} TextEditor;


TextEditor* textEditorCreate() {
    
}

void textEditorAddText(TextEditor* obj, char* text) {
    
}

int textEditorDeleteText(TextEditor* obj, int k) {
    
}

char* textEditorCursorLeft(TextEditor* obj, int k) {
    
}

char* textEditorCursorRight(TextEditor* obj, int k) {
    
}

void textEditorFree(TextEditor* obj) {
    
}

/**
 * Your TextEditor struct will be instantiated and called as such:
 * TextEditor* obj = textEditorCreate();
 * textEditorAddText(obj, text);
 
 * int param_2 = textEditorDeleteText(obj, k);
 
 * char* param_3 = textEditorCursorLeft(obj, k);
 
 * char* param_4 = textEditorCursorRight(obj, k);
 
 * textEditorFree(obj);
*/
```

### C#

```csharp
public class TextEditor {

    public TextEditor() {
        
    }
    
    public void AddText(string text) {
        
    }
    
    public int DeleteText(int k) {
        
    }
    
    public string CursorLeft(int k) {
        
    }
    
    public string CursorRight(int k) {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.AddText(text);
 * int param_2 = obj.DeleteText(k);
 * string param_3 = obj.CursorLeft(k);
 * string param_4 = obj.CursorRight(k);
 */
```

### JavaScript

```javascript

var TextEditor = function() {
    
};

/** 
 * @param {string} text
 * @return {void}
 */
TextEditor.prototype.addText = function(text) {
    
};

/** 
 * @param {number} k
 * @return {number}
 */
TextEditor.prototype.deleteText = function(k) {
    
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorLeft = function(k) {
    
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorRight = function(k) {
    
};

/** 
 * Your TextEditor object will be instantiated and called as such:
 * var obj = new TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */
```

### TypeScript

```typescript
class TextEditor {
    constructor() {
        
    }

    addText(text: string): void {
        
    }

    deleteText(k: number): number {
        
    }

    cursorLeft(k: number): string {
        
    }

    cursorRight(k: number): string {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * var obj = new TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */
```

### PHP

```php
class TextEditor {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $text
     * @return NULL
     */
    function addText($text) {
        
    }
  
    /**
     * @param Integer $k
     * @return Integer
     */
    function deleteText($k) {
        
    }
  
    /**
     * @param Integer $k
     * @return String
     */
    function cursorLeft($k) {
        
    }
  
    /**
     * @param Integer $k
     * @return String
     */
    function cursorRight($k) {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * $obj = TextEditor();
 * $obj->addText($text);
 * $ret_2 = $obj->deleteText($k);
 * $ret_3 = $obj->cursorLeft($k);
 * $ret_4 = $obj->cursorRight($k);
 */
```

### Swift

```swift

class TextEditor {

    init() {
        
    }
    
    func addText(_ text: String) {
        
    }
    
    func deleteText(_ k: Int) -> Int {
        
    }
    
    func cursorLeft(_ k: Int) -> String {
        
    }
    
    func cursorRight(_ k: Int) -> String {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * let obj = TextEditor()
 * obj.addText(text)
 * let ret_2: Int = obj.deleteText(k)
 * let ret_3: String = obj.cursorLeft(k)
 * let ret_4: String = obj.cursorRight(k)
 */
```

### Kotlin

```kotlin
class TextEditor() {

    fun addText(text: String) {
        
    }

    fun deleteText(k: Int): Int {
        
    }

    fun cursorLeft(k: Int): String {
        
    }

    fun cursorRight(k: Int): String {
        
    }

}

/**
 * Your TextEditor object will be instantiated and called as such:
 * var obj = TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */
```

### Dart

```dart
class TextEditor {

  TextEditor() {
    
  }
  
  void addText(String text) {
    
  }
  
  int deleteText(int k) {
    
  }
  
  String cursorLeft(int k) {
    
  }
  
  String cursorRight(int k) {
    
  }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = TextEditor();
 * obj.addText(text);
 * int param2 = obj.deleteText(k);
 * String param3 = obj.cursorLeft(k);
 * String param4 = obj.cursorRight(k);
 */
```

### Go

```golang
type TextEditor struct {
    
}


func Constructor() TextEditor {
    
}


func (this *TextEditor) AddText(text string)  {
    
}


func (this *TextEditor) DeleteText(k int) int {
    
}


func (this *TextEditor) CursorLeft(k int) string {
    
}


func (this *TextEditor) CursorRight(k int) string {
    
}


/**
 * Your TextEditor object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddText(text);
 * param_2 := obj.DeleteText(k);
 * param_3 := obj.CursorLeft(k);
 * param_4 := obj.CursorRight(k);
 */
```

### Ruby

```ruby
class TextEditor
    def initialize()
        
    end


=begin
    :type text: String
    :rtype: Void
=end
    def add_text(text)
        
    end


=begin
    :type k: Integer
    :rtype: Integer
=end
    def delete_text(k)
        
    end


=begin
    :type k: Integer
    :rtype: String
=end
    def cursor_left(k)
        
    end


=begin
    :type k: Integer
    :rtype: String
=end
    def cursor_right(k)
        
    end


end

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor.new()
# obj.add_text(text)
# param_2 = obj.delete_text(k)
# param_3 = obj.cursor_left(k)
# param_4 = obj.cursor_right(k)
```

### Scala

```scala
class TextEditor() {

    def addText(text: String): Unit = {
        
    }

    def deleteText(k: Int): Int = {
        
    }

    def cursorLeft(k: Int): String = {
        
    }

    def cursorRight(k: Int): String = {
        
    }

}

/**
 * Your TextEditor object will be instantiated and called as such:
 * val obj = new TextEditor()
 * obj.addText(text)
 * val param_2 = obj.deleteText(k)
 * val param_3 = obj.cursorLeft(k)
 * val param_4 = obj.cursorRight(k)
 */
```

### Rust

```rust
struct TextEditor {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TextEditor {

    fn new() -> Self {
        
    }
    
    fn add_text(&self, text: String) {
        
    }
    
    fn delete_text(&self, k: i32) -> i32 {
        
    }
    
    fn cursor_left(&self, k: i32) -> String {
        
    }
    
    fn cursor_right(&self, k: i32) -> String {
        
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * let obj = TextEditor::new();
 * obj.add_text(text);
 * let ret_2: i32 = obj.delete_text(k);
 * let ret_3: String = obj.cursor_left(k);
 * let ret_4: String = obj.cursor_right(k);
 */
```

### Racket

```racket
(define text-editor%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add-text : string? -> void?
    (define/public (add-text text)
      )
    ; delete-text : exact-integer? -> exact-integer?
    (define/public (delete-text k)
      )
    ; cursor-left : exact-integer? -> string?
    (define/public (cursor-left k)
      )
    ; cursor-right : exact-integer? -> string?
    (define/public (cursor-right k)
      )))

;; Your text-editor% object will be instantiated and called as such:
;; (define obj (new text-editor%))
;; (send obj add-text text)
;; (define param_2 (send obj delete-text k))
;; (define param_3 (send obj cursor-left k))
;; (define param_4 (send obj cursor-right k))
```

### Erlang

```erlang
-spec text_editor_init_() -> any().
text_editor_init_() ->
  .

-spec text_editor_add_text(Text :: unicode:unicode_binary()) -> any().
text_editor_add_text(Text) ->
  .

-spec text_editor_delete_text(K :: integer()) -> integer().
text_editor_delete_text(K) ->
  .

-spec text_editor_cursor_left(K :: integer()) -> unicode:unicode_binary().
text_editor_cursor_left(K) ->
  .

-spec text_editor_cursor_right(K :: integer()) -> unicode:unicode_binary().
text_editor_cursor_right(K) ->
  .


%% Your functions will be called as such:
%% text_editor_init_(),
%% text_editor_add_text(Text),
%% Param_2 = text_editor_delete_text(K),
%% Param_3 = text_editor_cursor_left(K),
%% Param_4 = text_editor_cursor_right(K),

%% text_editor_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TextEditor do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add_text(text :: String.t) :: any
  def add_text(text) do
    
  end

  @spec delete_text(k :: integer) :: integer
  def delete_text(k) do
    
  end

  @spec cursor_left(k :: integer) :: String.t
  def cursor_left(k) do
    
  end

  @spec cursor_right(k :: integer) :: String.t
  def cursor_right(k) do
    
  end
end

# Your functions will be called as such:
# TextEditor.init_()
# TextEditor.add_text(text)
# param_2 = TextEditor.delete_text(k)
# param_3 = TextEditor.cursor_left(k)
# param_4 = TextEditor.cursor_right(k)

# TextEditor.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TextEditor {
    init() {

    }
    
    func addText(text: String): Unit {

    }
    
    func deleteText(k: Int64): Int64 {

    }
    
    func cursorLeft(k: Int64): String {

    }
    
    func cursorRight(k: Int64): String {

    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * let obj: TextEditor = TextEditor()
 * obj.addText(text)
 * let param_2 = obj.deleteText(k)
 * let param_3 = obj.cursorLeft(k)
 * let param_4 = obj.cursorRight(k)
 */
```

