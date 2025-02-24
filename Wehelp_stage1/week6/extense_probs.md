**我們開發的系統中，哪些路徑必須驗證使用者為已登入的狀態？**
我覺得是POST deleteMessage、POST createMessage、GET member，因為用戶有可能擬制各種請求，所以尤其是有對資料庫create,update,delete的路由方法，應該後端要認證其請求的合法性，當然合法性的定義可能與實際需求有關(可能只要會員即可又或者需要到更細部的member_id)
**我們開發的系統中，是否需要特別針對 GET /signin 做額外錯誤處理？理由是？**
我覺得需要，但是並不特別重要。
基本上就是好看，不要讓用戶陷入崩潰狀態，可以繼續開心地過好這一天。
**刪除留言的操作，如何限制只有留言的作者可以刪除自己的留言？**
每個人應有擅長的做法，不過請求須包含請求者的資訊且資料庫留言表也必須要有留言作者資訊，
接著就是後端要有辦法判斷請求者資訊與留言作者資訊是否相同。
**我們是否應該優化會員頁面一次抓取所有留言並顯示的操作，該如何優化？**
如果多併發的情況之下，如果一次抓取少一點，僅需較少的記憶體存放資料庫的資料，較少流量傳輸至前端，實作方式或許可以在template之中多一個頁面參數，會依此參數重新fetch內容
**請舉例說明什麼是 SQL Injection？如何防止？**
如果說member作為參數，傳入某一個路由以看只有username=member的訊息：
那如果有用戶將username輸入為member='' or 1=1
這樣原本寫這樣的人就會有sql注入的問題
sql="SELECT * FROM message WHERE username = '"+message+"'"
會變成
sql="SELECT * FROM message WHERE username = '' or 1=1
這樣也可以視為
sql="SELECT * FROM message WHERE 1=1
就可以看到所有訊息而非username=member的訊息