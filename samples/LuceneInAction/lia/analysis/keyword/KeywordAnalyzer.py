# ====================================================================
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ====================================================================

from lucene import Token, PythonAnalyzer, PythonTokenStream, JArray

#
# "Tokenizes" the entire stream as a single token.
#

class KeywordAnalyzer(PythonAnalyzer):
    
    def tokenStream(self, fieldName, reader):

        class _tokenStream(PythonTokenStream):

            def __init__(self):
                super(_tokenStream, self).__init__()
                self.done = False
      
            def next(self):
                if not self.done:
                    self.done = True
                    text = JArray('char')(1024)
                    size = reader.read(text, 0, 1024)
                    return Token(text, 0, size, 0, size)
                return None

        return _tokenStream()
