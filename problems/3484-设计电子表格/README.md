# 3484. 设计电子表格

## 题目描述

<p>电子表格是一个网格，它有 26 列（从 <code>'A'</code> 到 <code>'Z'</code>）和指定数量的 <code>rows</code>。每个单元格可以存储一个 0 到 10<sup>5</sup>&nbsp;之间的整数值。</p>

<p>请你实现一个&nbsp;<code>Spreadsheet</code> 类：</p>

<ul>
	<li><code>Spreadsheet(int rows)</code> 初始化一个具有 26 列（从 <code>'A'</code> 到 <code>'Z'</code>）和指定行数的电子表格。所有单元格最初的值都为 0 。</li>
	<li><code>void setCell(String cell, int value)</code> 设置指定单元格的值。单元格引用以 <code>"AX"</code> 的格式提供（例如，<code>"A1"</code>，<code>"B10"</code>），其中字母表示列（从 <code>'A'</code> 到 <code>'Z'</code>），数字表示从<strong>&nbsp;</strong><strong>1</strong>&nbsp;开始的行号。</li>
	<li><code>void resetCell(String cell)</code> 重置指定单元格的值为 0 。</li>
	<li><code>int getValue(String formula)</code> 计算一个公式的值，格式为 <code>"=X+Y"</code>，其中 <code>X</code> 和 <code>Y</code>&nbsp;<strong>要么</strong> 是单元格引用，要么非负整数，返回计算的和。</li>
</ul>

<p><strong>注意：</strong> 如果 <code>getValue</code> 引用一个未通过 <code>setCell</code> 明确设置的单元格，则该单元格的值默认为 0 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]<br />
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]</span></p>

<p><strong>输出：</strong><br />
<span class="example-io">[null, 12, null, 16, null, 25, null, 15] </span></p>

<p><strong>解释</strong></p>
Spreadsheet spreadsheet = new Spreadsheet(3); // 初始化一个具有 3 行和 26 列的电子表格<br data-end="321" data-start="318" />
spreadsheet.getValue("=5+7"); // 返回 12 (5+7)<br data-end="373" data-start="370" />
spreadsheet.setCell("A1", 10); // 设置 A1 为 10<br data-end="423" data-start="420" />
spreadsheet.getValue("=A1+6"); // 返回 16 (10+6)<br data-end="477" data-start="474" />
spreadsheet.setCell("B2", 15); // 设置 B2 为 15<br data-end="527" data-start="524" />
spreadsheet.getValue("=A1+B2"); // 返回 25 (10+15)<br data-end="583" data-start="580" />
spreadsheet.resetCell("A1"); // 重置 A1 为 0<br data-end="634" data-start="631" />
spreadsheet.getValue("=A1+B2"); // 返回 15 (0+15)</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rows &lt;= 10<sup>3</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>公式保证采用 <code>"=X+Y"</code> 格式，其中 <code>X</code> 和 <code>Y</code> 要么是有效的单元格引用，要么是小于等于 <code>10<sup>5</sup></code> 的 <strong>非负</strong> 整数。</li>
	<li>每个单元格引用由一个大写字母 <code>'A'</code> 到 <code>'Z'</code> 和一个介于 <code>1</code> 和 <code>rows</code> 之间的行号组成。</li>
	<li><strong>总共</strong> 最多会对 <code>setCell</code>、<code>resetCell</code> 和 <code>getValue</code> 调用 <code>10<sup>4</sup></code> 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 字符串
- 矩阵

## 提示

1. Use a hashmap to represent the cells, where the key is the cell reference (e.g., <code>"A1"</code>) and the value is the integer stored in the cell.
2. For <code>setCell</code>, simply assign the given value to the specified cell in the hashmap.
3. For <code>resetCell</code>, set the value of the specified cell to <code>0</code> in the hashmap.
4. For <code>getValue</code>, find the values of the operands from the hashmap and return their sum.

## 示例

```
["Spreadsheet","getValue","setCell","getValue","setCell","getValue","resetCell","getValue"]
[[3],["=5+7"],["A1",10],["=A1+6"],["B2",15],["=A1+B2"],["A1"],["=A1+B2"]]
```

## 示例代码

### C++

```cpp
class Spreadsheet {
public:
    Spreadsheet(int rows) {
        
    }
    
    void setCell(string cell, int value) {
        
    }
    
    void resetCell(string cell) {
        
    }
    
    int getValue(string formula) {
        
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */
```

### Java

```java
class Spreadsheet {

    public Spreadsheet(int rows) {
        
    }
    
    public void setCell(String cell, int value) {
        
    }
    
    public void resetCell(String cell) {
        
    }
    
    public int getValue(String formula) {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */
```

### Python

```python
class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
```

### Python3

```python3
class Spreadsheet:

    def __init__(self, rows: int):
        

    def setCell(self, cell: str, value: int) -> None:
        

    def resetCell(self, cell: str) -> None:
        

    def getValue(self, formula: str) -> int:
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
```

### C

```c



typedef struct {
    
} Spreadsheet;


Spreadsheet* spreadsheetCreate(int rows) {
    
}

void spreadsheetSetCell(Spreadsheet* obj, char* cell, int value) {
    
}

void spreadsheetResetCell(Spreadsheet* obj, char* cell) {
    
}

int spreadsheetGetValue(Spreadsheet* obj, char* formula) {
    
}

void spreadsheetFree(Spreadsheet* obj) {
    
}

/**
 * Your Spreadsheet struct will be instantiated and called as such:
 * Spreadsheet* obj = spreadsheetCreate(rows);
 * spreadsheetSetCell(obj, cell, value);
 
 * spreadsheetResetCell(obj, cell);
 
 * int param_3 = spreadsheetGetValue(obj, formula);
 
 * spreadsheetFree(obj);
*/
```

### C#

```csharp
public class Spreadsheet {

    public Spreadsheet(int rows) {
        
    }
    
    public void SetCell(string cell, int value) {
        
    }
    
    public void ResetCell(string cell) {
        
    }
    
    public int GetValue(string formula) {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * int param_3 = obj.GetValue(formula);
 */
```

### JavaScript

```javascript
/**
 * @param {number} rows
 */
var Spreadsheet = function(rows) {
    
};

/** 
 * @param {string} cell 
 * @param {number} value
 * @return {void}
 */
Spreadsheet.prototype.setCell = function(cell, value) {
    
};

/** 
 * @param {string} cell
 * @return {void}
 */
Spreadsheet.prototype.resetCell = function(cell) {
    
};

/** 
 * @param {string} formula
 * @return {number}
 */
Spreadsheet.prototype.getValue = function(formula) {
    
};

/** 
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */
```

### TypeScript

```typescript
class Spreadsheet {
    constructor(rows: number) {
        
    }

    setCell(cell: string, value: number): void {
        
    }

    resetCell(cell: string): void {
        
    }

    getValue(formula: string): number {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */
```

### PHP

```php
class Spreadsheet {
    /**
     * @param Integer $rows
     */
    function __construct($rows) {
        
    }
  
    /**
     * @param String $cell
     * @param Integer $value
     * @return NULL
     */
    function setCell($cell, $value) {
        
    }
  
    /**
     * @param String $cell
     * @return NULL
     */
    function resetCell($cell) {
        
    }
  
    /**
     * @param String $formula
     * @return Integer
     */
    function getValue($formula) {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * $obj = Spreadsheet($rows);
 * $obj->setCell($cell, $value);
 * $obj->resetCell($cell);
 * $ret_3 = $obj->getValue($formula);
 */
```

### Swift

```swift

class Spreadsheet {

    init(_ rows: Int) {
        
    }
    
    func setCell(_ cell: String, _ value: Int) {
        
    }
    
    func resetCell(_ cell: String) {
        
    }
    
    func getValue(_ formula: String) -> Int {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet(rows)
 * obj.setCell(cell, value)
 * obj.resetCell(cell)
 * let ret_3: Int = obj.getValue(formula)
 */
```

### Kotlin

```kotlin
class Spreadsheet(rows: Int) {

    fun setCell(cell: String, value: Int) {
        
    }

    fun resetCell(cell: String) {
        
    }

    fun getValue(formula: String): Int {
        
    }

}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */
```

### Dart

```dart
class Spreadsheet {

  Spreadsheet(int rows) {
    
  }
  
  void setCell(String cell, int value) {
    
  }
  
  void resetCell(String cell) {
    
  }
  
  int getValue(String formula) {
    
  }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param3 = obj.getValue(formula);
 */
```

### Go

```golang
type Spreadsheet struct {
    
}


func Constructor(rows int) Spreadsheet {
    
}


func (this *Spreadsheet) SetCell(cell string, value int)  {
    
}


func (this *Spreadsheet) ResetCell(cell string)  {
    
}


func (this *Spreadsheet) GetValue(formula string) int {
    
}


/**
 * Your Spreadsheet object will be instantiated and called as such:
 * obj := Constructor(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * param_3 := obj.GetValue(formula);
 */
```

### Ruby

```ruby
class Spreadsheet

=begin
    :type rows: Integer
=end
    def initialize(rows)
        
    end


=begin
    :type cell: String
    :type value: Integer
    :rtype: Void
=end
    def set_cell(cell, value)
        
    end


=begin
    :type cell: String
    :rtype: Void
=end
    def reset_cell(cell)
        
    end


=begin
    :type formula: String
    :rtype: Integer
=end
    def get_value(formula)
        
    end


end

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet.new(rows)
# obj.set_cell(cell, value)
# obj.reset_cell(cell)
# param_3 = obj.get_value(formula)
```

### Scala

```scala
class Spreadsheet(_rows: Int) {

    def setCell(cell: String, value: Int): Unit = {
        
    }

    def resetCell(cell: String): Unit = {
        
    }

    def getValue(formula: String): Int = {
        
    }

}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * val obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * val param_3 = obj.getValue(formula)
 */
```

### Rust

```rust
struct Spreadsheet {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Spreadsheet {

    fn new(rows: i32) -> Self {
        
    }
    
    fn set_cell(&self, cell: String, value: i32) {
        
    }
    
    fn reset_cell(&self, cell: String) {
        
    }
    
    fn get_value(&self, formula: String) -> i32 {
        
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet::new(rows);
 * obj.set_cell(cell, value);
 * obj.reset_cell(cell);
 * let ret_3: i32 = obj.get_value(formula);
 */
```

### Racket

```racket
(define spreadsheet%
  (class object%
    (super-new)
    
    ; rows : exact-integer?
    (init-field
      rows)
    
    ; set-cell : string? exact-integer? -> void?
    (define/public (set-cell cell value)
      )
    ; reset-cell : string? -> void?
    (define/public (reset-cell cell)
      )
    ; get-value : string? -> exact-integer?
    (define/public (get-value formula)
      )))

;; Your spreadsheet% object will be instantiated and called as such:
;; (define obj (new spreadsheet% [rows rows]))
;; (send obj set-cell cell value)
;; (send obj reset-cell cell)
;; (define param_3 (send obj get-value formula))
```

### Erlang

```erlang
-spec spreadsheet_init_(Rows :: integer()) -> any().
spreadsheet_init_(Rows) ->
  .

-spec spreadsheet_set_cell(Cell :: unicode:unicode_binary(), Value :: integer()) -> any().
spreadsheet_set_cell(Cell, Value) ->
  .

-spec spreadsheet_reset_cell(Cell :: unicode:unicode_binary()) -> any().
spreadsheet_reset_cell(Cell) ->
  .

-spec spreadsheet_get_value(Formula :: unicode:unicode_binary()) -> integer().
spreadsheet_get_value(Formula) ->
  .


%% Your functions will be called as such:
%% spreadsheet_init_(Rows),
%% spreadsheet_set_cell(Cell, Value),
%% spreadsheet_reset_cell(Cell),
%% Param_3 = spreadsheet_get_value(Formula),

%% spreadsheet_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Spreadsheet do
  @spec init_(rows :: integer) :: any
  def init_(rows) do
    
  end

  @spec set_cell(cell :: String.t, value :: integer) :: any
  def set_cell(cell, value) do
    
  end

  @spec reset_cell(cell :: String.t) :: any
  def reset_cell(cell) do
    
  end

  @spec get_value(formula :: String.t) :: integer
  def get_value(formula) do
    
  end
end

# Your functions will be called as such:
# Spreadsheet.init_(rows)
# Spreadsheet.set_cell(cell, value)
# Spreadsheet.reset_cell(cell)
# param_3 = Spreadsheet.get_value(formula)

# Spreadsheet.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Spreadsheet {
    init(rows: Int64) {

    }
    
    func setCell(cell: String, value: Int64): Unit {

    }
    
    func resetCell(cell: String): Unit {

    }
    
    func getValue(formula: String): Int64 {

    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj: Spreadsheet = Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * let param_3 = obj.getValue(formula)
 */
```

