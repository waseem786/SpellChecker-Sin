      if format == 'JSON':
            output += '{ "spellcheck-result":<spellcheck-result>\n'
            for inputWord in corrections.keys():
                output += '"word":{<word>\n'
                result = {
                    True  : 'CORRECT',
                    False : 'INCORRECT'
                }[inputWord in corrections[inputWord].keys()]
                output += ' "source":{<source status=\" "status":' + result + ',\">"text:"' + inputWord + "</source>\n},"
                if result != 'CORRECT':
                    for correction in corrections[inputWord].keys():
                        output += '"correction":[{<correction module=\"  "module":' + corrections[inputWord][correction] + '\">"text":' + correction + "</correction>\n]}"
                output += '</word>\n}'
            output += '</spellcheck-result>}'
