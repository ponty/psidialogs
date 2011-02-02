
##[[[cog
##   import apigen
##   apigen.commonApiFunctionList()
##]]]
_dict={ 'askDate': (['message', 'default', 'title'],
             'str',
             ["'Select date.'", "''", "''"]),
 'askFileForOpen': (['message', 'default', 'title'],
                    'str',
                    ["'Select file for open.'", "''", "''"]),
 'askFileForSave': (['message', 'default', 'title'],
                    'str',
                    ["'Select file for save.'", "''", "''"]),
 'askFilesForOpen': (['message', 'default', 'title'],
                     '[str]',
                     ["'Select files for open.'", "''", "''"]),
 'askFolder': (['message', 'default', 'ok', 'cancel', 'title'],
               'str',
               ["'Select folder.'", "''", "'OK'", "'Cancel'", "''"]),
 'askOkCancel': (['message', 'default', 'title'], 'bool', ["''", '0', "''"]),
 'askPassword': (['message', 'default', 'ok', 'cancel', 'title'],
                 'str',
                 ["'Enter password.'", "''", "'OK'", "'Cancel'", "''"]),
 'askString': (['message', 'default', 'ok', 'cancel', 'title'],
               'str',
               ["'Enter something.'", "''", "'OK'", "'Cancel'", "''"]),
 'askYesNo': (['message', 'default', 'title'], 'bool', ["''", '0', "''"]),
 'buttonChoice': (['choices', 'message', 'default', 'title'],
                  'str',
                  ['[]', "'Select a button.'", '0', "''"]),
 'choice': (['choices', 'message', 'default', 'title'],
            'str',
            ['[]', "'Pick something.'", 'None', "''"]),
 'error': (['message', 'ok', 'title'], '', ["'Error!'", "'OK'", "''"]),
 'message': (['message', 'ok', 'title'], '', ["'Hello!'", "'OK'", "''"]),
 'multiChoice': (['choices', 'message', 'default', 'title'],
                 '[str]',
                 ['[]', "'Pick as many items as you like.'", 'None', "''"]),
 'text': (['text', 'message', 'title'], '', ["''", "''", "''"]),
 'warning': (['message', 'ok', 'title'], '', ["'Warning!'", "'OK'", "''"])}
##[[[end]]] 
    
def functions():
##    global _dict
    return _dict.keys()
    
def argnames(func):
   args,typ,d = _dict[func]
   return args
   
def returntype(func):
   args,typ,d = _dict[func]
   return typ
   
def defaults(func):
   args,typ,d = _dict[func]
   return d
