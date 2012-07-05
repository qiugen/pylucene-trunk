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

from lucene import Document, IndexSearcher, PythonCollector, FieldCache, \
    BytesRef

#
# A Collector extension
#

class BookLinkCollector(PythonCollector):

    def __init__(self, searcher):
        super(BookLinkCollector, self).__init__()

        self.searcher = searcher
        self.documents = {}

    def acceptsDocsOutOfOrder(self):

        return True

    def setNextReader(self, context):

        self.docBase = context.docBase
        self.urls = FieldCache.DEFAULT.getTerms(context.reader, "url")
        self.titles = FieldCache.DEFAULT.getTerms(context.reader, "title2")

    def collect(self, docID, score):
        
        term = BytesRef()
        url = self.urls.getTerm(docID, term).utf8ToString()
        title = self.titles.getTerm(docID, term).utf8ToString()
        self.documents[url] = title

        print "%s: %s" %(title, score)

    def getLinks(self):

        return self.documents.copy()
