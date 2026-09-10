(comment) @comment
(string) @string

(directive) @keyword
(macro_keyword) @keyword
(mnemonic) @function
(register) @variable.special
(label_definition name: (identifier) @type)
(label_reference) @variable
(macro_argument name: (identifier) @variable.parameter)

(number) @number
[(operator) (operator_plus)] @operator
(comma) @punctuation.delimiter
":" @punctuation.delimiter
"[" @punctuation.bracket
"]" @punctuation.bracket
"(" @punctuation.bracket
")" @punctuation.bracket
